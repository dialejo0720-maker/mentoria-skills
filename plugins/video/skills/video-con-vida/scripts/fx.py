"""
fx.py — motor de efectos de video-con-vida.

Todo trabaja con arrays numpy float32 en [0, 1]:
    rgb   = (H, W, 3)      alpha = (H, W)      rgba = (H, W, 4)

Orden de capas en cada fotograma:
    fondo (plate / video / color) → elementos detrás → persona (alpha) → elementos delante

Uso típico (un efecto = una función que recibe el contexto del fotograma):

    import sys; sys.path.insert(0, r"<carpeta base de video-con-vida>/scripts")
    from fx import *

    def efecto(c):                      # c.t, c.p, c.frame, c.alpha, c.plate, c.W, c.H
        bg = darken(c.frame, 0.3)
        return person_over(bg, c.frame, c.alpha)

    render("efecto_16.mp4", efecto, start=4.2, dur=1.3)
"""
import json
import math
import os
import subprocess
from pathlib import Path
from types import SimpleNamespace

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from scipy import ndimage

# ───────────────────────── conversión ─────────────────────────

def f32(a):
    """uint8 → float32 [0,1]. Si ya es float, lo deja igual."""
    a = np.asarray(a)
    return a.astype(np.float32) / 255.0 if a.dtype == np.uint8 else a.astype(np.float32)


def to_u8(a):
    a = np.asarray(a)
    if a.dtype == np.uint8:
        return a
    return np.clip(a * 255.0 + 0.5, 0, 255).astype(np.uint8)


def to_pil(a):
    a = to_u8(a)
    return Image.fromarray(a, "RGBA" if a.ndim == 3 and a.shape[2] == 4 else ("L" if a.ndim == 2 else "RGB"))


def from_pil(img):
    return f32(np.array(img))


def color(c):
    """'#F5F1E8' | (245,241,232) | (0.96,0.94,0.9) → tupla float."""
    if isinstance(c, str):
        c = c.lstrip("#")
        return tuple(int(c[i:i + 2], 16) / 255.0 for i in (0, 2, 4))
    c = tuple(c)
    return tuple(x / 255.0 for x in c[:3]) if max(c[:3]) > 1 else tuple(float(x) for x in c[:3])


def solid(W, H, c):
    return np.broadcast_to(np.array(color(c), np.float32), (H, W, 3)).copy()

# ───────────────────────── video in / out ─────────────────────────

def probe(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=width,height,r_frame_rate:stream_side_data=rotation:format=duration",
         "-of", "json", str(path)],
        capture_output=True, text=True, check=True).stdout
    j = json.loads(out)
    s = j["streams"][0]
    num, den = map(int, s["r_frame_rate"].split("/"))
    w, h = int(s["width"]), int(s["height"])
    rot = 0
    for sd in s.get("side_data_list", []) or []:
        rot = int(sd.get("rotation", 0) or 0)
    if abs(rot) in (90, 270):          # video de celular grabado girado: ffmpeg lo endereza al decodificar
        w, h = h, w
    return dict(w=w, h=h, fps=num / den, duration=float(j.get("format", {}).get("duration", 0) or 0))


def iter_frames(path, start=0.0, dur=None, size=None, gray=False, fps=None, cover=False, loop=False):
    """Genera fotogramas uint8 (H,W,3) o (H,W) si gray. size=(W,H) reescala.
    cover=True llena el tamaño recortando (sin deformar). loop=True repite el clip si es más corto."""
    info = probe(path)
    w, h = size or (info["w"], info["h"])
    if cover:
        vf = [f"scale={w}:{h}:force_original_aspect_ratio=increase:flags=lanczos", f"crop={w}:{h}"]
    else:
        vf = [f"scale={w}:{h}:flags=lanczos"]
    if fps:
        vf.append(f"fps={fps}")
    cmd = ["ffmpeg", "-v", "error"] + (["-stream_loop", "-1"] if loop else []) + ["-ss", f"{start:.4f}", "-i", str(path)]
    if dur:
        cmd += ["-t", f"{dur:.4f}"]
    cmd += ["-vf", ",".join(vf), "-f", "rawvideo", "-pix_fmt", "gray" if gray else "rgb24", "-"]
    # stderr a DEVNULL: si se deja de leer antes del final, ffmpeg se queja de "broken pipe" (inofensivo)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
    ch = 1 if gray else 3
    n = w * h * ch
    got = 0
    try:
        while True:
            buf = p.stdout.read(n)
            if len(buf) < n:
                break
            got += 1
            a = np.frombuffer(buf, np.uint8).reshape(h, w, ch)
            yield a[..., 0] if gray else a
    finally:
        if p.poll() is None:
            p.kill()
        p.stdout.close()
        p.wait()
    if got == 0:
        raise RuntimeError(f"ffmpeg no devolvió fotogramas de {path} en t={start}. ¿El tramo existe?")


def load_frames(path, start=0.0, dur=None, size=None, gray=False, fps=None, cover=False, loop=False):
    return list(iter_frames(path, start, dur, size, gray, fps, cover, loop))


def load_image(path, size=None):
    img = Image.open(path).convert("RGB")
    if size and img.size != tuple(size):
        img = img.resize(tuple(size), Image.LANCZOS)
    return from_pil(img)


class Writer:
    """Escribe fotogramas a mp4 (H.264, yuv420p). audio=ruta para copiar el audio de ese tramo."""

    def __init__(self, out, W, H, fps=30, audio=None, audio_start=0.0, crf=18):
        cmd = ["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
               "-s", f"{W}x{H}", "-r", f"{fps}", "-i", "-"]
        if audio:
            cmd += ["-ss", f"{audio_start:.4f}", "-i", str(audio), "-map", "0:v", "-map", "1:a?",
                    "-c:a", "aac", "-b:a", "192k", "-shortest"]
        cmd += ["-c:v", "libx264", "-preset", "medium", "-crf", str(crf), "-pix_fmt", "yuv420p",
                "-movflags", "+faststart", str(out)]
        self.p = subprocess.Popen(cmd, stdin=subprocess.PIPE)

    def write(self, rgb):
        self.p.stdin.write(np.ascontiguousarray(to_u8(rgb)[..., :3]).tobytes())

    def close(self):
        self.p.stdin.close()
        self.p.wait()

    def __enter__(self):
        return self

    def __exit__(self, *a):
        self.close()


def _base_dir(video):
    return Path(video).resolve().parent / "base"


def render(out, fn, video="video.mp4", start=0.0, dur=1.0, alpha=None, plate=None,
           fps=None, audio=True, qa=True, extra_tail=0.0):
    """
    Corre fn(c) por cada fotograma del tramo [start, start+dur] de `video` y guarda `out`.
    c tiene: i, n, t (s dentro del efecto), p (0→1), T (s absolutos en el video),
             frame (rgb), alpha (H,W) o None, plate (rgb) o None, W, H, fps, video.
    Si existe base/alpha.mp4 y base/plate.png junto al video, se cargan solos.
    qa=True guarda <out>_qa.jpg con 3 fotogramas (inicio, medio, final) para revisarlos.
    """
    info = probe(video)
    W, H = info["w"], info["h"]
    fps = fps or round(info["fps"])
    base = _base_dir(video)
    alpha = alpha if alpha is not None else (base / "alpha.mp4" if (base / "alpha.mp4").exists() else None)
    plate = plate if plate is not None else (base / "plate.png" if (base / "plate.png").exists() else None)
    a_off = 0.0
    meta = base / "meta.json"
    if meta.exists():
        a_off = json.loads(meta.read_text()).get("alpha_start", 0.0)

    plate_img = load_image(plate, (W, H)) if plate else None
    frames = iter_frames(video, start, dur, (W, H), fps=fps)
    alphas = iter_frames(alpha, max(0.0, start - a_off), dur, (W, H), gray=True, fps=fps) if alpha else None
    n = max(1, int(round(dur * fps)))
    picks = {0, n // 2, n - 1}
    shots = []
    with Writer(out, W, H, fps, audio=video if audio else None, audio_start=start) as w:
        for i in range(n):
            try:
                fr = next(frames)
            except StopIteration:
                break
            prev_al = al if i else None
            al = None
            if alphas is not None:
                try:
                    al = f32(next(alphas))
                except StopIteration:
                    al = prev_al  # el seek a veces entrega un cuadro de alpha menos: se repite el último
            t = i / fps
            c = SimpleNamespace(i=i, n=n, t=t, p=i / max(1, n - 1), T=start + t, frame=f32(fr),
                                alpha=al, plate=plate_img, W=W, H=H, fps=fps, video=video)
            img = fn(c)
            w.write(img)
            if qa and i in picks:
                shots.append(to_u8(img))
    if qa and shots:
        contact(shots, str(Path(out).with_suffix("")) + "_qa.jpg")
    return out

# ───────────────────────── tiempo y curvas ─────────────────────────
# Regla de oro: nada lineal. Entradas con ease_out_back (rebote 5–10 %), salidas con ease_in.

def clamp(x, a=0.0, b=1.0):
    return max(a, min(b, x))


def lerp(a, b, t):
    return a + (b - a) * t


def prog(t, t0, dur):
    """Progreso 0→1 de una animación que empieza en t0 y dura dur."""
    return clamp((t - t0) / dur) if dur > 0 else float(t >= t0)


def ease_out_cubic(t):
    return 1 - (1 - t) ** 3


def ease_in_cubic(t):
    return t ** 3


def ease_in_out_cubic(t):
    return 4 * t ** 3 if t < 0.5 else 1 - (-2 * t + 2) ** 3 / 2


def ease_out_expo(t):
    return 1.0 if t >= 1 else 1 - 2 ** (-10 * t)


def ease_in_expo(t):
    return 0.0 if t <= 0 else 2 ** (10 * t - 10)


def _back_raw(t, s):
    u = t - 1
    return 1 + (s + 1) * u ** 3 + s * u ** 2


_S_CACHE = {}


def _back_s(overshoot):
    """Constante s de easeOutBack que da exactamente ese rebote (0.10 → s≈1.70)."""
    key = round(overshoot, 4)
    if key not in _S_CACHE:
        ts = np.linspace(0, 1, 400)
        lo, hi = 0.0, 6.0
        for _ in range(40):
            mid = (lo + hi) / 2
            if _back_raw(ts, mid).max() - 1 < overshoot:
                lo = mid
            else:
                hi = mid
        _S_CACHE[key] = (lo + hi) / 2
    return _S_CACHE[key]


def ease_out_back(t, overshoot=0.08):
    """Acelera, se pasa del destino un `overshoot` (0.05–0.10) y regresa. La curva base de todo."""
    return _back_raw(clamp(t), _back_s(overshoot))


def bounce_pop(t, overshoot=0.15):
    """Para puntos/iconos que 'saltan' al aparecer (escala 0 → 1.15 → 1)."""
    return ease_out_back(t, overshoot)


def squash(t_since_land, amount=0.12, dur=0.28):
    """Aplastar-estirar al aterrizar. Devuelve (sx, sy): ancho crece cuando la altura baja."""
    if t_since_land < 0 or t_since_land > dur:
        return 1.0, 1.0
    k = amount * math.exp(-5 * t_since_land / dur) * math.cos(math.pi * 2.2 * t_since_land / dur)
    return 1 + k, 1 - k


def stagger(t, i, gap=0.10, start=0.0, dur=0.45):
    """Progreso 0→1 del elemento i en una entrada escalonada (80–120 ms entre elementos)."""
    return prog(t, start + i * gap, dur)

# micro-movimiento: la pantalla nunca queda quieta

def breathe(t, amp=0.012, period=2.8, phase=0.0):
    """Escala que 'respira': 1 ± amp."""
    return 1 + amp * math.sin(2 * math.pi * t / period + phase)


def float_y(t, px=6, period=3.2, phase=0.0):
    return px * math.sin(2 * math.pi * t / period + phase)


def sway(t, deg=1.5, period=4.0, phase=0.0):
    return deg * math.sin(2 * math.pi * t / period + phase)


def slow_zoom(t, dur, amount=0.03):
    """Zoom de cámara lento y constante (1 → 1+amount en dur segundos)."""
    return 1 + amount * ease_in_out_cubic(clamp(t / dur)) if dur > 0 else 1.0


def blink(t, every=3.5, length=0.12):
    """1 = ojo abierto, 0 = cerrado. Para mascotas/íconos con ojos."""
    ph = t % every
    return 0.0 if ph < length else 1.0

# ───────────────────────── composición ─────────────────────────

def person_over(bg, frame, alpha):
    """Pega a la persona (frame recortado por alpha) sobre bg."""
    a = alpha[..., None]
    return bg * (1 - a) + frame * a


def paste(dst, rgba, x, y, opacity=1.0):
    """Pega rgba con su esquina superior izquierda en (x, y). Modifica dst y lo devuelve."""
    H, W = dst.shape[:2]
    h, w = rgba.shape[:2]
    x, y = int(round(x)), int(round(y))
    x0, y0, x1, y1 = max(0, x), max(0, y), min(W, x + w), min(H, y + h)
    if x0 >= x1 or y0 >= y1:
        return dst
    src = rgba[y0 - y:y1 - y, x0 - x:x1 - x]
    a = src[..., 3:4] * opacity
    dst[y0:y1, x0:x1] = dst[y0:y1, x0:x1] * (1 - a) + src[..., :3] * a
    return dst


def paste_center(dst, rgba, cx, cy, opacity=1.0):
    h, w = rgba.shape[:2]
    return paste(dst, rgba, cx - w / 2, cy - h / 2, opacity)


def add(dst, rgba, x=0, y=0, strength=1.0):
    """Suma aditiva (para brillos y luces)."""
    tmp = np.zeros_like(dst)
    paste(tmp, np.dstack([rgba[..., :3] * rgba[..., 3:4], np.ones(rgba.shape[:2], np.float32)]), x, y)
    return np.clip(dst + tmp * strength, 0, 1)


def with_alpha(rgb, a):
    return np.dstack([rgb, a]).astype(np.float32)

# ───────────────────────── formas, tarjetas y texto ─────────────────────────

_FONT_DIRS = [Path("C:/Windows/Fonts"), Path.home() / "AppData/Local/Microsoft/Windows/Fonts"]
FONTS = {
    "black": ["seguibl.ttf", "ariblk.ttf"],          # titulares tipo reel (Segoe UI Black)
    "bold": ["segoeuib.ttf", "arialbd.ttf"],
    "regular": ["segoeui.ttf", "arial.ttf"],
    "serif": ["georgia.ttf", "times.ttf"],            # portada de revista
    "serif-bold": ["georgiab.ttf", "timesbd.ttf"],
    "serif-italic": ["georgiai.ttf", "timesi.ttf"],
    "mono": ["consola.ttf", "cour.ttf"],
    "script": ["segoesc.ttf"],
    "hand": ["segoepr.ttf", "segoesc.ttf"],           # letra a mano
    "impact": ["impact.ttf"],
}


def font(name="black", size=80):
    """name = clave de FONTS, nombre de archivo .ttf o ruta completa."""
    cands = FONTS.get(name, [name])
    for c in cands:
        p = Path(c)
        if p.is_file():
            return ImageFont.truetype(str(p), size)
        for d in _FONT_DIRS:
            if (d / c).is_file():
                return ImageFont.truetype(str(d / c), size)
    return ImageFont.load_default(size)


def text(txt, size=80, fnt="black", fill="#FFFFFF", stroke=0, stroke_fill="#000000",
         spacing=0.15, align="center", max_width=None, ss=2):
    """Texto como rgba (renderizado a 2x y reducido: bordes limpios). max_width parte líneas."""
    f = font(fnt, size * ss)
    lines = [txt] if not max_width else _wrap(txt, f, max_width * ss)
    tmp = ImageDraw.Draw(Image.new("L", (1, 1)))
    boxes = [tmp.textbbox((0, 0), ln, font=f, stroke_width=stroke * ss) for ln in lines]
    lh = int(size * ss * (1 + spacing))
    w = max(b[2] - b[0] for b in boxes) + 4 * ss
    h = lh * (len(lines) - 1) + (boxes[-1][3] - min(b[1] for b in boxes)) + 4 * ss
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    top = min(b[1] for b in boxes)
    for k, (ln, b) in enumerate(zip(lines, boxes)):
        lw = b[2] - b[0]
        x = {"left": 0, "right": w - lw, "center": (w - lw) // 2}[align] - b[0] + 2 * ss
        d.text((x, k * lh - top + 2 * ss), ln, font=f, fill=_rgba255(fill),
               stroke_width=stroke * ss, stroke_fill=_rgba255(stroke_fill))
    img = img.resize((max(1, w // ss), max(1, h // ss)), Image.LANCZOS)
    return from_pil(img)


def _wrap(txt, f, maxw):
    words, lines, cur = txt.split(), [], ""
    d = ImageDraw.Draw(Image.new("L", (1, 1)))
    for wd in words:
        test = (cur + " " + wd).strip()
        if d.textlength(test, font=f) <= maxw or not cur:
            cur = test
        else:
            lines.append(cur)
            cur = wd
    return lines + ([cur] if cur else [])


def _rgba255(c, a=1.0):
    r, g, b = color(c)
    return (int(r * 255), int(g * 255), int(b * 255), int(a * 255))


def rounded_rect(w, h, r=24, fill="#FFFFFF", border=0, border_fill="#FFFFFF", ss=2):
    img = Image.new("RGBA", (w * ss, h * ss), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, w * ss - 1, h * ss - 1], r * ss, fill=_rgba255(fill),
                        outline=_rgba255(border_fill) if border else None, width=border * ss)
    return from_pil(img.resize((w, h), Image.LANCZOS))


def round_corners(rgb_or_rgba, r=24, border=0, border_fill="#FFFFFF", ss=2):
    """Recorta un fotograma/imagen con esquinas redondas (y borde opcional)."""
    src = rgb_or_rgba if rgb_or_rgba.shape[2] == 4 else with_alpha(rgb_or_rgba, np.ones(rgb_or_rgba.shape[:2], np.float32))
    h, w = src.shape[:2]
    m = Image.new("L", (w * ss, h * ss), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, w * ss - 1, h * ss - 1], r * ss, fill=255)
    m = f32(np.array(m.resize((w, h), Image.LANCZOS)))
    out = src.copy()
    out[..., 3] *= m
    if border:
        ring = _ring_alpha(w, h, r, border, ss)
        out[..., :3] = out[..., :3] * (1 - ring[..., None]) + np.array(color(border_fill), np.float32) * ring[..., None]
        out[..., 3] = np.maximum(out[..., 3], ring)
    return out


def shadow(rgba, blur=24, opacity=0.45, offset=(0, 12), pad=None):
    """Devuelve (rgba_con_sombra, pad): la capa crece `pad` px por lado; centra igual que la original."""
    pad = pad if pad is not None else blur * 2 + max(abs(offset[0]), abs(offset[1]))
    h, w = rgba.shape[:2]
    out = np.zeros((h + 2 * pad, w + 2 * pad, 4), np.float32)
    sh = np.zeros((h + 2 * pad, w + 2 * pad), np.float32)
    sh[pad + offset[1]:pad + offset[1] + h, pad + offset[0]:pad + offset[0] + w] = rgba[..., 3]
    sh = ndimage.gaussian_filter(sh, blur / 2) * opacity
    out[..., 3] = sh
    paste_rgba(out, rgba, pad, pad)
    return out, pad


def hard_shadow(rgba, offset=(14, 14), opacity=0.9, fill="#000000"):
    """Sombra dura desplazada (estilo recorte de papel)."""
    h, w = rgba.shape[:2]
    ox, oy = offset
    out = np.zeros((h + abs(oy), w + abs(ox), 4), np.float32)
    sh = np.dstack([solid(w, h, fill), rgba[..., 3] * opacity])
    paste_rgba(out, sh, max(0, ox), max(0, oy))
    paste_rgba(out, rgba, max(0, -ox), max(0, -oy))
    return out


def paste_rgba(dst, src, x, y):
    """Alpha-over rgba sobre rgba (conserva transparencia)."""
    H, W = dst.shape[:2]
    h, w = src.shape[:2]
    x0, y0, x1, y1 = max(0, x), max(0, y), min(W, x + w), min(H, y + h)
    if x0 >= x1 or y0 >= y1:
        return dst
    s = src[y0 - y:y1 - y, x0 - x:x1 - x]
    d = dst[y0:y1, x0:x1]
    sa, da = s[..., 3:4], d[..., 3:4]
    oa = sa + da * (1 - sa)
    rgb = (s[..., :3] * sa + d[..., :3] * da * (1 - sa)) / np.maximum(oa, 1e-6)
    dst[y0:y1, x0:x1] = np.concatenate([rgb, oa], axis=2)
    return dst


def card(img, w=None, h=None, radius=12, border=2, border_fill="#FFFFFF", shadow_blur=20, shadow_opacity=0.5):
    """Tarjeta: imagen/fotograma reescalado, esquinas redondas, borde y sombra. Devuelve rgba (con margen de sombra)."""
    if w or h:
        hh, ww = img.shape[:2]
        w = w or int(ww * h / hh)
        h = h or int(hh * w / ww)
        img = from_pil(to_pil(img).resize((w, h), Image.LANCZOS))
    c = round_corners(img, radius, border, border_fill)
    out, _ = shadow(c, shadow_blur, shadow_opacity) if shadow_blur else (c, 0)
    return out


def _ring_alpha(w, h, r, b, ss=2):
    m = Image.new("L", (w * ss, h * ss), 0)
    d = ImageDraw.Draw(m)
    d.rounded_rectangle([0, 0, w * ss - 1, h * ss - 1], r * ss, outline=255, width=b * ss)
    return f32(np.array(m.resize((w, h), Image.LANCZOS)))

# ───────────────────────── transformaciones ─────────────────────────

def transform(rgba, scale=1.0, angle=0.0, sx=1.0, sy=1.0):
    """Escala (y aplasta-estira con sx/sy) y rota en grados. Devuelve rgba nuevo, centrado igual."""
    if rgba.shape[2] == 3:
        rgba = with_alpha(rgba, np.ones(rgba.shape[:2], np.float32))
    h, w = rgba.shape[:2]
    nw, nh = max(1, int(round(w * scale * sx))), max(1, int(round(h * scale * sy)))
    img = to_pil(rgba)
    if (nw, nh) != (w, h):
        img = img.resize((nw, nh), Image.BICUBIC)
    if abs(angle) > 0.01:
        img = img.rotate(angle, Image.BICUBIC, expand=True)
    return from_pil(img)


def _persp_coeffs(dst_quad, src_quad):
    A, B = [], []
    for (x, y), (u, v) in zip(dst_quad, src_quad):
        A += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]
        B += [u, v]
    return np.linalg.solve(np.array(A, float), np.array(B, float)).tolist()


def warp_to_quad(rgba, quad):
    """Deforma rgba para que sus 4 esquinas (sup-izq, sup-der, inf-der, inf-izq) caigan en quad (coords de pantalla).
    Devuelve (capa, x0, y0) para hacer paste(dst, capa, x0, y0)."""
    if rgba.shape[2] == 3:
        rgba = with_alpha(rgba, np.ones(rgba.shape[:2], np.float32))
    h, w = rgba.shape[:2]
    q = np.array(quad, float)
    x0, y0 = np.floor(q.min(0)).astype(int)
    x1, y1 = np.ceil(q.max(0)).astype(int)
    local = [(x - x0, y - y0) for x, y in q]
    co = _persp_coeffs(local, [(0, 0), (w, 0), (w, h), (0, h)])
    img = to_pil(rgba).transform((max(1, x1 - x0), max(1, y1 - y0)), Image.PERSPECTIVE, co, Image.BICUBIC)
    return from_pil(img), int(x0), int(y0)


def project(x, y, z, cx, cy, focal=1400):
    """Proyección en perspectiva: punto 3D (z>0 = más lejos) → (sx, sy, escala)."""
    s = focal / (focal + z)
    return cx + x * s, cy + y * s, s


def rotate_y_quad(w, h, yaw_deg, cx, cy, z=0.0, focal=1400, pitch_deg=0.0):
    """Esquinas de una tarjeta w×h centrada en (cx,cy,z) girada yaw en Y (y pitch en X), proyectadas."""
    ya, pa = math.radians(yaw_deg), math.radians(pitch_deg)
    pts = []
    for px, py in [(-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h / 2)]:
        x, zz = px * math.cos(ya), px * math.sin(ya)
        y, zz = py * math.cos(pa) - zz * math.sin(pa), py * math.sin(pa) + zz * math.cos(pa)
        sx, sy, _ = project(x, y, zz + z, 0, 0, focal)
        pts.append((cx + sx, cy + sy))
    return pts

# ───────────────────────── operaciones de imagen ─────────────────────────

def zoom(img, scale, cx=None, cy=None):
    """Zoom digital hacia (cx, cy) sin salirse del cuadro."""
    H, W = img.shape[:2]
    if scale <= 1.0001:
        return img
    cx = W / 2 if cx is None else cx
    cy = H / 2 if cy is None else cy
    cw, ch = W / scale, H / scale
    x0 = clamp(cx - cw / 2, 0, W - cw)
    y0 = clamp(cy - ch / 2, 0, H - ch)
    pil = to_pil(img).resize((W, H), Image.BICUBIC, box=(x0, y0, x0 + cw, y0 + ch))
    return from_pil(pil)


def scale_about(img, scale, cx, cy, fill=0.0):
    """Escala la imagen completa alrededor de (cx,cy); si scale<1 deja borde `fill`. Para zoom hacia atrás."""
    H, W = img.shape[:2]
    if scale >= 1:
        return zoom(img, scale, cx, cy)
    out = np.full_like(img, fill)
    w, h = max(1, int(W * scale)), max(1, int(H * scale))
    small = from_pil(to_pil(img).resize((w, h), Image.LANCZOS))
    return paste(out, with_alpha(small, np.ones((h, w), np.float32)), cx - w / 2, cy - h / 2)


def blur(img, r):
    if r <= 0:
        return img
    if img.ndim == 2:
        return ndimage.gaussian_filter(img, r / 2)
    return from_pil(to_pil(img).filter(ImageFilter.GaussianBlur(r)))


def darken(img, k):
    """Oscurece k (0.3 = 30 % más oscuro)."""
    return img * (1 - k)


def radial_blur(img, cx, cy, strength=0.15, n=10):
    """Desenfoque radial: promedia n copias escaladas hacia (cx,cy)."""
    acc = np.zeros_like(img)
    for k in range(n):
        acc += zoom(img, 1 + strength * k / max(1, n - 1), cx, cy)
    return acc / n


def edge_radial_blur(img, cx, cy, strength=0.06, n=8, inner=0.35):
    """Desenfoque radial solo en los bordes (centro nítido)."""
    H, W = img.shape[:2]
    yy, xx = np.mgrid[0:H, 0:W]
    d = np.sqrt(((xx - cx) / W) ** 2 + ((yy - cy) / H) ** 2) / 0.7
    m = np.clip((d - inner) / (1 - inner), 0, 1)[..., None].astype(np.float32)
    return img * (1 - m) + radial_blur(img, cx, cy, strength, n) * m


def glow_layer(rgba, radius=18):
    """Copia desenfocada de la capa: súmala con add() encima de la capa nítida."""
    pm = rgba[..., :3] * rgba[..., 3:4]
    b = np.dstack([ndimage.gaussian_filter(pm[..., k], radius / 2) for k in range(3)])
    a = ndimage.gaussian_filter(rgba[..., 3], radius / 2)
    return np.dstack([b / np.maximum(a[..., None], 1e-4), a]).astype(np.float32)


def color_match(fg, fg_alpha, bg, strength=0.35):
    """Corrige suave el color de la persona hacia el tono medio del nuevo fondo."""
    m = fg_alpha > 0.5
    if m.sum() < 100:
        return fg
    mu_f = fg[m].mean(0)
    mu_b = bg.reshape(-1, 3).mean(0)
    return np.clip(fg + (mu_b - mu_f) * strength, 0, 1)

# ───────────────────────── máscaras ─────────────────────────

def dilate(alpha, px):
    """Crece la máscara px píxeles (para bordes tipo sticker)."""
    d = ndimage.distance_transform_edt(alpha < 0.5)
    return np.clip(px + 1 - d, 0, 1).astype(np.float32)


def erode(alpha, px):
    d = ndimage.distance_transform_edt(alpha >= 0.5)
    return np.clip(d - px, 0, 1).astype(np.float32)


def feather(alpha, px=1):
    return ndimage.gaussian_filter(alpha, px).astype(np.float32)


def bbox(alpha, thr=0.5):
    ys, xs = np.where(alpha > thr)
    if len(xs) == 0:
        return None
    return int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())


def face_center(alpha):
    """Estimación del centro de la cara a partir del recorte (sin MediaPipe). Verifícala con un still."""
    H, W = alpha.shape
    b = bbox(alpha)
    if not b:
        return W / 2, H * 0.35
    top = b[1]
    band = alpha[top:top + int(H * 0.16)]
    xs = np.where(band > 0.5)[1]
    cx = float(xs.mean()) if len(xs) else W / 2
    return cx, top + H * 0.09


def chest_center(alpha):
    cx, cy = face_center(alpha)
    return cx, min(alpha.shape[0] * 0.92, cy + alpha.shape[0] * 0.2)


def head_shoulders(alpha, frac=0.30):
    """Máscara solo de cabeza y hombros (la parte de arriba del recorte)."""
    b = bbox(alpha)
    out = np.zeros_like(alpha)
    if not b:
        return out
    cut = b[1] + int(alpha.shape[0] * frac)
    out[:cut] = alpha[:cut]
    return feather(out, 2)


def contours(alpha, thr=0.5, step=6):
    """Contorno exterior principal como lista de puntos (x, y). Usa OpenCV si está; si no, un trazado propio."""
    m = (alpha > thr).astype(np.uint8)
    try:
        import cv2
        cs, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if not cs:
            return []
        c = max(cs, key=len)[:, 0, :]
        return [tuple(p) for p in c[::step]]
    except ImportError:
        pass
    # sin OpenCV: borde = máscara - erosión, ordenado por ángulo desde el centroide (suficiente para siluetas)
    edge = m & ~ndimage.binary_erosion(m, iterations=2)
    ys, xs = np.nonzero(edge)
    if len(xs) == 0:
        return []
    cx, cy = xs.mean(), ys.mean()
    ang = np.arctan2(ys - cy, xs - cx)
    o = np.argsort(ang)
    pts = list(zip(xs[o], ys[o]))
    return pts[::step]

# ───────────────────────── QA y montaje ─────────────────────────

def still(img, path, max_side=900):
    im = to_pil(img).convert("RGB")
    im.thumbnail((max_side, max_side))
    im.save(path, quality=88)
    return path


def contact(frames, out, height=640):
    ims = []
    for f in frames:
        im = to_pil(f).convert("RGB")
        im = im.resize((int(im.width * height / im.height), height), Image.LANCZOS)
        ims.append(im)
    sheet = Image.new("RGB", (sum(i.width for i in ims) + 10 * (len(ims) - 1), height), (20, 20, 20))
    x = 0
    for im in ims:
        sheet.paste(im, (x, 0))
        x += im.width + 10
    sheet.save(out, quality=88)
    return out


def concat(files, out, W=1080, H=1920, fps=30):
    """Une clips con corte seco (re-codifica para igualar tamaño/fps/audio)."""
    inputs, parts = [], []
    for k, f in enumerate(files):
        inputs += ["-i", str(f)]
        has_audio = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries",
                                    "stream=index", "-of", "csv=p=0", str(f)],
                                   capture_output=True, text=True).stdout.strip() != ""
        parts.append(f"[{k}:v]scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,"
                     f"fps={fps},setsar=1,format=yuv420p[v{k}];")
        if has_audio:
            parts.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=stereo[a{k}];")
        else:
            parts.append(f"anullsrc=r=48000:cl=stereo,atrim=0:{probe(f)['duration']:.3f}[a{k}];")
    chain = "".join(f"[v{k}][a{k}]" for k in range(len(files)))
    fc = "".join(parts) + f"{chain}concat=n={len(files)}:v=1:a=1[v][a]"
    subprocess.run(["ffmpeg", "-y", "-v", "error", *inputs, "-filter_complex", fc, "-map", "[v]", "-map", "[a]",
                    "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-c:a", "aac", "-b:a", "192k",
                    "-movflags", "+faststart", str(out)], check=True)
    return out
