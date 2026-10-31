"""
efectos.py — los 17 efectos de la guía (más el revelado con las manos), listos para usar.

  python efectos.py <NN|nombre> video.mp4 --start S [--dur D] [opciones]

Ejemplos:
  python efectos.py 05 video.mp4 --start 3.2                       # zoom digital (no necesita base/)
  python efectos.py orbita video.mp4 --start 6 --clips clips/
  python efectos.py 16 video.mp4 --start 9.4 --texto ESTUDIO
  python efectos.py 07 video.mp4 --start 12 --items "Suelta tus clips|Activa la skill|Publícalo|Repite"
  python efectos.py 12 video.mp4 --start 15 --fondo otra_toma.mp4
  python efectos.py 03 video.mp4 --start 2 --etiqueta "03/17|mundo app" --cabecera "17 efectos de video|que claude puede crear"

Opciones comunes:
  --out        archivo de salida (default efecto_NN.mp4)
  --texto      texto principal del efecto (03, 13, 16, 17, 18)
  --items      lista separada por | (07 checklist, 08 titulares, 11 panel)
  --clips      carpeta con clips/imágenes para tarjetas y muros (01, 02, 08); si no, usa tu mismo video
  --fondo      video de fondo (12 pantalla verde)
  --acento     color de acento (default naranja #FF8A1F)
  --etiqueta   "NN/17|nombre" abajo, entra con rebote
  --cabecera   "línea 1|línea 2" fija arriba
  --manos      "x1,y1,x2,y2" (0–1) posición final de las manos abiertas (18 portal)
  --sync-voz   (05) pone cada salto de zoom en una palabra detectada con faster-whisper

Necesitan base/alpha.mp4 (preparar.py): todos menos 05, 09 y 11. Necesitan base/plate.png: 15 (y lo mejora 01).
"""
import argparse
import datetime
import functools
import glob
import math
import random
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageOps
from scipy import ndimage

sys.path.insert(0, str(Path(__file__).parent))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from fx import *  # noqa: F401,F403,E402
from fx import _rgba255  # noqa: E402

ACENTO = "#FF8A1F"
AMARILLO = "#F7E36B"


@functools.lru_cache(maxsize=512)
def T(txt, size, fnt="black", fill="#FFFFFF", stroke=0, stroke_fill="#000000", max_width=None, align="center"):
    """text() con caché: el mismo texto no se vuelve a renderizar en cada fotograma."""
    return text(txt, size, fnt, fill, stroke, stroke_fill, max_width=max_width, align=align)


def need_alpha(c, nombre):
    if c.alpha is None:
        raise SystemExit(f"«{nombre}» necesita base/alpha.mp4. Corre primero: python preparar.py {c.video}")


def fuentes(o, n, w, h, c):
    """n listas de fotogramas (w×h) para tarjetas/muros: de --clips o del mismo video en otros momentos."""
    dur = c.n / c.fps + 0.1
    files = []
    if o.clips:
        for ext in ("mp4", "mov", "webm", "png", "jpg", "jpeg", "webp"):
            files += glob.glob(str(Path(o.clips) / f"*.{ext}"))
        files.sort()
    out = []
    D = probe(c.video)["duration"]
    for k in range(n):
        if files:
            f = files[k % len(files)]
            if f.lower().endswith(("png", "jpg", "jpeg", "webp")):
                fr = [f32(np.array(ImageOps.fit(Image.open(f).convert("RGB"), (w, h), Image.LANCZOS)))]
            else:
                fr = [f32(x) for x in load_frames(f, (k // len(files)) * 1.3, dur, (w, h), fps=c.fps, cover=True, loop=True)]
        else:
            t0 = (c.T + 1.9 * (k + 1)) % max(0.1, D - dur - 0.1)
            fr = [f32(x) for x in load_frames(c.video, t0, dur, (w, h), fps=c.fps, cover=True)]
        out.append(fr or [np.zeros((h, w, 3), np.float32)])
    return out


def draw_layer(W, H):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    return img, ImageDraw.Draw(img)


def check_icon(size, fill, done=True, ring="#8A8A8A"):
    img, d = draw_layer(size * 2, size * 2)
    if done:
        d.ellipse([0, 0, size * 2 - 1, size * 2 - 1], fill=_rgba255(fill))
        d.line([(size * 0.55, size * 1.05), (size * 0.88, size * 1.38), (size * 1.5, size * 0.68)],
               fill=(255, 255, 255, 255), width=max(2, size // 4), joint="curve")
    else:
        d.ellipse([2, 2, size * 2 - 3, size * 2 - 3], outline=_rgba255(ring), width=max(2, size // 6))
    return from_pil(img.resize((size, size), Image.LANCZOS))

# ───────────────────────── 01 órbita ─────────────────────────

def e01(c, o, st):
    need_alpha(c, "órbita")
    cw, ch = int(c.W * 0.2), int(c.W * 0.2 * 16 / 9)
    if "cards" not in st:
        st["cards"] = fuentes(o, 3, cw, ch, c)
        st["center"] = face_center(c.alpha)
    cx, cy = st["center"][0], st["center"][1] + c.H * 0.12
    R = c.W * 0.38
    bg = c.frame.copy()
    items = []
    for k in range(3):
        th = 2 * math.pi * k / 3 + 2 * math.pi * 0.4 * c.t + 0.5
        x, z = R * math.sin(th), R * 0.6 * math.cos(th)            # z>0 = detrás de la persona
        y = -c.H * 0.05 * math.cos(th) + float_y(c.t, 5, 2.4, k)
        sx, sy, s = project(x, y, z, cx, cy, focal=1100)
        pop = ease_out_back(stagger(c.t, k, 0.1, 0, 0.35), 0.1)
        if pop <= 0.01:
            continue
        frs = st["cards"][k]
        img = round_corners(frs[c.i % len(frs)], 12, 2)
        quad = rotate_y_quad(cw * s * pop, ch * s * pop, -math.degrees(th) * 0.35, sx, sy, focal=1400)
        lay, x0, y0 = warp_to_quad(img, quad)
        lay, pad = shadow(lay, 14, 0.45, (0, 8))
        items.append((z, lay, x0 - pad, y0 - pad))
    items.sort(key=lambda it: -it[0])
    for z, lay, x, y in items:
        if z > 0:
            paste(bg, lay, x, y)
    out = person_over(bg, c.frame, c.alpha)
    for z, lay, x, y in items:
        if z <= 0:
            paste(out, lay, x, y)
    return out

# ───────────────────────── 02 muro de videos ─────────────────────────

def e02(c, o, st):
    need_alpha(c, "muro de videos")
    cols, rows, gap = 3, 4, 8
    tw, th = (c.W - gap * (cols + 1)) // cols, (int(c.H * 1.04) - gap * (rows + 1)) // rows
    if "tiles" not in st:
        st["tiles"] = fuentes(o, cols * rows, tw, th, c)
    wall = solid(c.W, int(c.H * 1.04), "#0B0B0B")
    for k, frs in enumerate(st["tiles"]):
        r, q = divmod(k, cols)
        paste(wall, round_corners(frs[c.i % len(frs)], 10), gap + q * (tw + gap), gap + r * (th + gap))
    drift = int(c.H * 0.04 * c.p)                                   # el muro sube despacio (parallax: fondo lento)
    wall = zoom(wall[drift:drift + c.H], slow_zoom(c.t, c.n / c.fps, 0.03))
    return person_over(darken(wall, 0.4), c.frame, c.alpha)

# ───────────────────────── 03 mundo app ─────────────────────────

def e03(c, o, st):
    need_alpha(c, "mundo app")
    W, H = c.W, c.H
    if "bg" not in st:
        yy, xx = np.mgrid[0:H, 0:W]
        d = np.sqrt(((xx - W / 2) / W) ** 2 + ((yy - H * 0.3) / H) ** 2)
        base = np.array(color("#F5F1E8"), np.float32)
        st["bg"] = np.clip(base * (1.03 - 0.12 * d[..., None]), 0, 1).astype(np.float32)
        bw, bh = int(W * 0.86), int(H * 0.115)
        st["bar"] = (bw, bh)
        top = bbox(c.alpha)[1] if bbox(c.alpha) else int(H * 0.3)
        st["target"] = max(H * 0.2, top + H * 0.012)
    bw, bh = st["bar"]
    txt = o.texto or "Edítame este reel con mi estilo"
    n = int(len(txt) * prog(c.t, 0.35, 0.55))
    cursor = n < len(txt) or (c.t * 2.5) % 1 < 0.6
    bar, d = draw_layer(bw * 2, bh * 2)
    d.rounded_rectangle([0, 0, bw * 2 - 1, bh * 2 - 1], 44, fill=(255, 255, 255, 255), outline=(225, 222, 214, 255), width=2)
    f = font("regular", int(H * 0.0175) * 2)
    d.text((60, 52), txt[:n] + ("|" if cursor else ""), font=f, fill=(30, 30, 30, 255))
    fi = font("regular", int(H * 0.02) * 2)
    d.text((60, bh * 2 - 90), "+   ≡", font=fi, fill=(110, 110, 110, 255))
    s = int(bh * 0.55)
    d.rounded_rectangle([bw * 2 - 60 - s, bh * 2 - 40 - s, bw * 2 - 60, bh * 2 - 40], 14, fill=(20, 20, 20, 255))
    d.text((bw * 2 - 60 - s / 2, bh * 2 - 40 - s / 2), "↑", font=fi, fill=(255, 255, 255, 255), anchor="mm")
    bar = from_pil(bar.resize((bw, bh), Image.LANCZOS))
    bar, pad = shadow(bar, 26, 0.18, (0, 14))
    e = ease_out_back(prog(c.t, 0, 0.4), 0.08)
    y = lerp(-bh - pad * 2, st["target"], e) + (float_y(c.t, 3, 2.6) if c.t > 0.4 else 0)
    bg = st["bg"].copy()
    paste_center(bg, T("Claude", int(H * 0.017), "serif", "#5A5650"), W / 2, H * 0.075)
    paste(bg, bar, (W - bw) / 2 - pad, y - bh / 2 - pad)
    return person_over(bg, c.frame, c.alpha)

# ───────────────────────── 04 rompe el marco ─────────────────────────

def e04(c, o, st):
    need_alpha(c, "rompe el marco")
    W, H = c.W, c.H
    if "cut" not in st:
        st["cut"] = face_center(c.alpha)[1] + H * 0.035
    e = ease_out_back(prog(c.t, 0, 0.45), 0.05)
    s = lerp(1.0, 0.6, e)
    sw, sh = int(W * s), int(H * s)
    small = from_pil(to_pil(c.frame).resize((sw, sh), Image.LANCZOS))
    a_small = from_pil(to_pil(c.alpha).resize((sw, sh), Image.LANCZOS))
    x0, y0 = (W - sw) / 2, H * 0.56 - sh / 2 if s < 1 else 0
    y0 = lerp(0, H * 0.56 - sh / 2, e)
    cut = int(lerp(0, st["cut"], clamp(e)) * s)
    bg = darken(blur(c.frame, 34), 0.45)
    box = round_corners(small[cut:], int(36 * s + 1), 2, "#FFFFFF")
    box, pad = shadow(box, 30, 0.55, (0, 18))
    paste(bg, box, x0 - pad, y0 + cut - pad)
    paste(bg, with_alpha(small, a_small), x0, y0)                  # cabeza y hombros rompen el borde
    return bg

# ───────────────────────── 05 zoom digital ─────────────────────────

def palabras_voz(video, start, dur):
    from faster_whisper import WhisperModel
    import tempfile
    import subprocess
    wav = Path(tempfile.gettempdir()) / "vcv_seg.wav"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", str(start), "-t", str(dur), "-i", str(video),
                    "-ac", "1", "-ar", "16000", str(wav)], check=True)
    m = WhisperModel("base", device="cpu", compute_type="int8")
    segs, _ = m.transcribe(str(wav), word_timestamps=True)
    return [w.start for s in segs for w in (s.words or [])]


def e05(c, o, st):
    if "center" not in st:
        st["center"] = face_center(c.alpha) if c.alpha is not None else (c.W / 2, c.H * 0.36)
        D = c.n / c.fps
        times = [0, D * 0.25, D * 0.5, D * 0.75]
        if o.sync_voz:
            ws = [w for w in palabras_voz(c.video, c.T, D) if w > 0.12]
            if len(ws) >= 3:
                times = [0] + [ws[int(i * len(ws) / 3)] for i in range(3)]
        st["times"] = times
    levels = [1.0, 1.2, 1.4, 1.6]
    k = max(i for i, t0 in enumerate(st["times"]) if c.t >= t0)
    punch = 0.03 if k and (c.t - st["times"][k]) < 1.5 / c.fps else 0.0   # 1 fotograma de rebote al saltar
    return zoom(c.frame, levels[k] + punch, *st["center"])

# ───────────────────────── 06 teléfono ─────────────────────────

def phone_screen(w, h, t, o):
    img, d = draw_layer(w, h)
    d.rectangle([0, 0, w, h], fill=(14, 14, 16, 255))
    fb = font("bold", int(w * 0.075))
    fr = font("regular", int(w * 0.05))
    d.text((w * 0.1, h * 0.12), "Edita mis clips\nen un reel", font=fb, fill=(255, 255, 255, 255), spacing=6)
    items = (o.items.split("|") if o.items else ["Quita silencios", "Subtítulos", "Efectos de video"])[:4]
    for k, it in enumerate(items):
        y = h * 0.32 + k * h * 0.075
        e = ease_out_back(prog(t, 0.45 + k * 0.12, 0.22), 0.15)
        r = w * 0.035
        if e > 0:
            rr = r * e
            d.ellipse([w * 0.1 + r - rr, y + r - rr, w * 0.1 + r + rr, y + r + rr], fill=_rgba255(AMARILLO))
        else:
            d.ellipse([w * 0.1, y, w * 0.1 + 2 * r, y + 2 * r], outline=(120, 120, 120, 255), width=3)
        d.text((w * 0.1 + 3 * r, y - r * 0.2), it, font=fr, fill=(220, 220, 220, 255))
    done = t > 0.85
    by = h * 0.62
    pulse = ease_out_back(prog(t, 0.85, 0.25), 0.12)
    sc = 1 + 0.06 * math.sin(math.pi * clamp(prog(t, 0.85, 0.25)))
    bw2, bh2 = w * 0.8 * sc, h * 0.065 * sc
    d.rounded_rectangle([w / 2 - bw2 / 2, by, w / 2 + bw2 / 2, by + bh2], int(bh2 / 2),
                        fill=_rgba255(AMARILLO) if done else (60, 60, 64, 255))
    d.text((w / 2, by + bh2 / 2), "✓ Listo" if done else "Editar", font=fb,
           fill=(20, 20, 20, 255) if done else (230, 230, 230, 255), anchor="mm")
    if done and pulse < 1:
        rr = w * 0.5 * pulse
        d.ellipse([w / 2 - rr, by + bh2 / 2 - rr, w / 2 + rr, by + bh2 / 2 + rr],
                  outline=(255, 255, 255, int(200 * (1 - pulse))), width=3)
    return img


def e06(c, o, st):
    need_alpha(c, "teléfono")
    W, H = c.W, c.H
    pw, ph = int(W * 0.36), int(W * 0.36 * 2.05)
    body, d = draw_layer(pw, ph)
    d.rounded_rectangle([0, 0, pw - 1, ph - 1], int(pw * 0.15), fill=(8, 8, 8, 255), outline=(70, 70, 74, 255), width=3)
    m = int(pw * 0.035)
    scr = phone_screen(pw - 2 * m, ph - 2 * m, c.t, o)
    mask = Image.new("L", scr.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, scr.size[0] - 1, scr.size[1] - 1], int(pw * 0.12), fill=255)
    body.paste(scr, (m, m), mask)
    d.rounded_rectangle([pw / 2 - pw * 0.15, m + pw * 0.03, pw / 2 + pw * 0.15, m + pw * 0.1], 40, fill=(0, 0, 0, 255))
    body = from_pil(body)
    e = ease_out_back(prog(c.t, 0, 0.5), 0.07)
    cx = lerp(W + pw, W * 0.73, e)
    cy = H * 0.36 + (float_y(c.t, 6, 2.8) if c.t > 0.5 else 0)
    quad = rotate_y_quad(pw, ph, -15 + sway(c.t, 1.2, 3.0), cx, cy, focal=1600)
    lay, x0, y0 = warp_to_quad(body, quad)
    lay, pad = shadow(lay, 34, 0.55, (0, 26))
    bg = paste(c.frame.copy(), lay, x0 - pad, y0 - pad)
    return person_over(bg, c.frame, c.alpha)

# ───────────────────────── 07 checklist ─────────────────────────

def e07(c, o, st):
    need_alpha(c, "checklist")
    W, H = c.W, c.H
    items = (o.items.split("|") if o.items else ["Suelta tus clips", "Activa la skill", "Revisa el borrador", "Publícalo"])[:4]
    cw, chh = int(W * 0.48), int(W * 0.48 * 360 / 520)
    img, d = draw_layer(cw * 2, chh * 2)
    d.rounded_rectangle([0, 0, cw * 2 - 1, chh * 2 - 1], 48, fill=(14, 14, 14, 235), outline=(60, 60, 60, 255), width=2)
    fs = font("bold", int(cw * 0.032) * 2)
    fb = font("bold", int(cw * 0.05) * 2)
    t0s = [0.3 + 0.2 * k for k in range(len(items))]
    ndone = sum(c.t >= t for t in t0s)
    d.ellipse([44, 46, 60, 62], fill=_rgba255(ACENTO))
    d.text((80, 38), "E D I T A   C O N   C L A U D E", font=fs, fill=(150, 150, 150, 255))
    pill = f"{max(1, ndone)} de {len(items)}"
    d.rounded_rectangle([cw * 2 - 190, 30, cw * 2 - 40, 74], 22, fill=(40, 40, 40, 255))
    d.text((cw * 2 - 115, 52), pill, font=fs, fill=(220, 220, 220, 255), anchor="mm")
    for k, it in enumerate(items):
        y = 130 + k * (chh * 2 - 170) / len(items)
        e = ease_out_back(prog(c.t, t0s[k], 0.2), 0.15)
        r = 22
        cxk, cyk = 66, y + 26
        if e > 0:
            rr = r * e
            d.ellipse([cxk - rr, cyk - rr, cxk + rr, cyk + rr], fill=_rgba255(ACENTO))
            if e > 0.6:
                d.line([(cxk - 10, cyk), (cxk - 3, cyk + 8), (cxk + 11, cyk - 8)], fill=(255, 255, 255, 255), width=5, joint="curve")
        else:
            d.ellipse([cxk - r, cyk - r, cxk + r, cyk + r], outline=(110, 110, 110, 255), width=4)
        col = (255, 255, 255, 255) if c.t < t0s[k] else (150, 150, 150, 255)
        d.text((110, y), it, font=fb, fill=col)
        strike = prog(c.t, t0s[k] + 0.05, 0.15)
        if strike > 0:                                           # va tachando la tarea
            tw = d.textlength(it, font=fb)
            d.line([(110, cyk + 2), (110 + tw * ease_out_cubic(strike), cyk + 2)], fill=(150, 150, 150, 255), width=4)
    cardimg, pad = shadow(from_pil(img.resize((cw, chh), Image.LANCZOS)), 30, 0.5, (0, 16))
    e = ease_out_back(prog(c.t, 0, 0.35), 0.08)
    x = lerp(-cw - pad * 2, W * 0.10, e)
    y = lerp(-chh - pad * 2, H * 0.20, e) + (float_y(c.t, 4, 2.6) if c.t > 0.35 else 0)
    bg = paste(c.frame.copy(), cardimg, x - pad, y - pad)
    return person_over(bg, c.frame, c.alpha)

# ───────────────────────── 08 muro de titulares ─────────────────────────

TITULARES = ["Claude ya edita tus videos", "POV: Claude edita tu reel", "¿claude edita videos?", "Adiós editor",
             "Sóbrame el reel entero", "La IA ya corta tus silencios", "No editó ni un segundo",
             "claude efectos de video", "Edición en 5 minutos", "El reel que nadie editó", "¿Cómo lo hizo?",
             "Subtítulos solos", "Sin After Effects", "Esto lo hizo una IA", "Tu editor nuevo",
             "Hazlo con un prompt", "Cero plantillas", "Videos que se editan solos", "Sí, es código", "Pruébalo hoy"]


def headline_card(txt, kind, W, rng):
    if kind == "search":
        w, h = int(W * 0.34), int(W * 0.055)
        img, d = draw_layer(w * 2, h * 2)
        d.rounded_rectangle([0, 0, w * 2 - 1, h * 2 - 1], h, fill=(255, 255, 255, 255))
        d.text((40, h), "⌕  " + txt.lower(), font=font("regular", int(h * 0.75)), fill=(90, 90, 90, 255), anchor="lm")
    elif kind == "post":
        w, h = int(W * 0.3), int(W * 0.15)
        img, d = draw_layer(w * 2, h * 2)
        d.rounded_rectangle([0, 0, w * 2 - 1, h * 2 - 1], 16, fill=(255, 255, 255, 255))
        d.ellipse([24, 24, 64, 64], fill=_rgba255(ACENTO))
        d.text((78, 30), "@usuario", font=font("bold", 26), fill=(20, 20, 20, 255))
        d.multiline_text((24, 84), "\n".join(_wrap_lines(txt, 22)), font=font("regular", 30), fill=(40, 40, 40, 255), spacing=6)
    else:
        w = int(W * rng.uniform(0.2, 0.3))
        lines = _wrap_lines(txt, 13)
        fs = int(W * 0.03)
        h = int(fs * 1.25 * len(lines) + fs * 1.2)
        img, d = draw_layer(w * 2, h * 2)
        d.rectangle([0, 0, w * 2 - 1, h * 2 - 1], fill=(255, 255, 255, 255))
        d.multiline_text((fs, fs * 0.9), "\n".join(lines), font=font("serif-bold", fs * 2), fill=(15, 15, 15, 255), spacing=8)
    return from_pil(img.resize((w, h), Image.LANCZOS))


def _wrap_lines(txt, n):
    out, cur = [], ""
    for w in txt.split():
        if len(cur) + len(w) + 1 > n and cur:
            out.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    return out + [cur]


def e08(c, o, st):
    need_alpha(c, "muro de titulares")
    W, H = c.W, c.H
    if "cards" not in st:
        rng = random.Random(8)
        tit = o.items.split("|") if o.items else TITULARES
        cards = []
        for k in range(20):
            kind = ["paper", "paper", "search", "post"][k % 4]
            img = headline_card(tit[k % len(tit)], kind, W, rng)
            img = transform(img, angle=rng.uniform(-6, 6))
            img, pad = shadow(img, 12, 0.35, (0, 6))
            col, row = k % 4, k // 4
            x = (col + 0.5) * W / 4 + rng.uniform(-60, 60)
            y = H * 0.14 + row * H * 0.13 + rng.uniform(-40, 40)
            speed = rng.uniform(30, 90)                     # parallax: las tarjetas grandes suben más rápido
            cards.append((img, x, y, speed * img.shape[1] / (W * 0.3)))
        st["cards"] = cards
    bg = c.frame.copy()
    for k, (img, x, y, sp) in enumerate(st["cards"]):
        e = ease_out_back(stagger(c.t, k, 0.02, 0, 0.3), 0.1)
        if e <= 0.01:
            continue
        lay = transform(img, scale=e) if e < 0.999 else img
        paste_center(bg, lay, x, y - sp * c.t)
    return person_over(bg, c.frame, c.alpha)

# ───────────────────────── 09 zoom de corte ─────────────────────────

def e09(c, o, st):
    if "center" not in st:
        st["center"] = chest_center(c.alpha) if c.alpha is not None else (c.W / 2, c.H * 0.6)
    D = c.n / c.fps
    e = ease_in_expo(prog(c.t, 0.5, max(0.1, D - 0.5)))
    s = 1 + 4 * e
    img = zoom(c.frame, s, *st["center"])
    if e > 0.002:
        img = radial_blur(img, c.W / 2, c.H / 2, 0.45 * e, n=10)
    return img

# ───────────────────────── 10 gráfica que crece ─────────────────────────

def glow_fast(rgba, radius=16, k=4):
    h, w = rgba.shape[:2]
    small = from_pil(to_pil(rgba).resize((w // k, h // k), Image.BILINEAR))
    g = glow_layer(small, radius / k)
    return from_pil(to_pil(g).resize((w, h), Image.BILINEAR))


def polyline_partial(pts, frac):
    L = [0.0]
    for a, b in zip(pts, pts[1:]):
        L.append(L[-1] + math.dist(a, b))
    target = L[-1] * clamp(frac)
    out = [pts[0]]
    reached = [l / L[-1] for l in L]
    for k in range(1, len(pts)):
        if L[k] <= target:
            out.append(pts[k])
        else:
            u = (target - L[k - 1]) / max(1e-6, L[k] - L[k - 1])
            out.append((lerp(pts[k - 1][0], pts[k][0], u), lerp(pts[k - 1][1], pts[k][1], u)))
            break
    return out, reached


def e10(c, o, st):
    need_alpha(c, "gráfica que crece")
    W, H = c.W, c.H
    lime = "#E6F45A"
    if "grid" not in st:
        g, d = draw_layer(W, H)
        for x in range(0, W, 90):
            d.line([(x, 0), (x, H)], fill=(255, 255, 255, 20), width=1)
        for y in range(0, H, 90):
            d.line([(0, y), (W, y)], fill=(255, 255, 255, 20), width=1)
        st["grid"] = from_pil(g)
        fy = face_center(c.alpha)[1]
        ys = [0.02, 0.025, 0.03, 0.035, -0.04, -0.12, -0.2]
        xs = [0.06, 0.2, 0.33, 0.45, 0.62, 0.8, 0.94]
        st["pts"] = [(W * x, fy + H * y) for x, y in zip(xs, ys)]
    bg = paste(darken(c.frame, 0.55), st["grid"], 0, 0)
    frac = ease_in_out_cubic(prog(c.t, 0.05, 0.8))
    path, reached = polyline_partial(st["pts"], frac)
    lay, d = draw_layer(W, H)
    for (_, y) in st["pts"][1:]:
        if y < st["pts"][0][1] - 5:
            for x in range(0, W, 24):
                d.line([(x, y), (x + 10, y)], fill=(255, 255, 255, 60), width=2)
    if len(path) > 1:
        d.line(path, fill=_rgba255(lime), width=7, joint="curve")
    lay = from_pil(lay)
    bg = add(bg, glow_fast(lay, 22), strength=1.6)
    paste(bg, lay, 0, 0)
    dots, dd = draw_layer(W, H)
    for k, (x, y) in enumerate(st["pts"]):
        if frac + 1e-6 < reached[k]:
            continue
        tk = 0.05 + 0.8 * reached[k]
        e = bounce_pop(prog(c.t, tk, 0.25), 0.25)
        r = 10 * e
        dd.ellipse([x - r, y - r, x + r, y + r], fill=(255, 255, 255, 255), outline=_rgba255(lime), width=3)
    tip = path[-1]
    dd.ellipse([tip[0] - 14, tip[1] - 14, tip[0] + 14, tip[1] + 14], fill=(255, 255, 200, 255))
    dots = from_pil(dots)
    bg = add(bg, glow_fast(dots, 30), strength=1.4)
    paste(bg, dots, 0, 0)
    return person_over(bg, c.frame, c.alpha)

# ───────────────────────── 11 zoom hacia atrás ─────────────────────────

def e11(c, o, st):
    W, H = c.W, c.H
    win = (int(W * 0.04), int(H * 0.1), int(W * 0.96), int(H * 0.82))
    ph = int(H * 0.58)
    pw = int(ph * W / H)
    player_c = (win[0] + 30 + pw / 2, win[1] + 60 + ph / 2)
    if "canvas" not in st:
        yy = np.linspace(0, 1, H, dtype=np.float32)[:, None, None]
        cv = np.broadcast_to(np.array(color("#E4E2DC"), np.float32) * (1 - 0.06 * yy), (H, W, 3)).copy()
        img, d = draw_layer(W, H)
        d.rounded_rectangle(win, 26, fill=(250, 250, 248, 255), outline=(210, 208, 202, 255), width=2)
        for k, col in enumerate([(255, 95, 87), (254, 188, 46), (40, 200, 64)]):
            d.ellipse([win[0] + 24 + k * 30, win[1] + 20, win[0] + 42 + k * 30, win[1] + 38], fill=col + (255,))
        tl = win[1] + 60 + ph + 24
        d.rounded_rectangle([win[0] + 30, tl, win[0] + 30 + pw, tl + 56], 12, fill=(238, 238, 236, 255))
        rng = random.Random(3)
        for x in range(win[0] + 44, win[0] + 16 + pw, 9):
            hh = rng.uniform(4, 20)
            d.line([(x, tl + 28 - hh), (x, tl + 28 + hh)], fill=(90, 120, 220, 180), width=4)
        canvas = from_pil(img)
        base = paste(cv, canvas, 0, 0)
        st["canvas"] = base
    out = st["canvas"].copy()
    items = (o.items.split("|") if o.items else
             ["Transcribí la toma", "Corté 17 espacios", "Construí cada efecto", "Subtítulos listos", "Color y mezcla"])
    px0 = win[0] + 30 + pw + 24
    panel, d = draw_layer(win[2] - 30 - px0, int(H * 0.3))
    fb, fr = font("bold", int(W * 0.024)), font("regular", int(W * 0.022))
    d.text((10, 6), "● Trabajando en…", font=fb, fill=(60, 60, 60, 255))
    for k, it in enumerate(items):
        y = 60 + k * int(W * 0.045)
        e = ease_out_back(prog(c.t, 0.75 + k * 0.1, 0.2), 0.15)
        if e > 0:
            r = 12 * e
            d.ellipse([22 - r, y + 14 - r, 22 + r, y + 14 + r], fill=(40, 170, 90, 255))
            d.text((44, y), it, font=fr, fill=(40, 40, 40, 255))
        else:
            d.ellipse([10, y + 2, 34, y + 26], outline=(170, 170, 170, 255), width=3)
            d.text((44, y), it, font=fr, fill=(170, 170, 170, 255))
    paste(out, from_pil(panel), px0, win[1] + 70)
    e = ease_out_back(prog(c.t, 0.05, 0.7), 0.03)
    s = lerp(1.0, ph / H, e)
    cx, cy = lerp(W / 2, player_c[0], e), lerp(H / 2, player_c[1], e)
    sw, sh = int(W * s), int(H * s)
    small = from_pil(to_pil(c.frame).resize((sw, sh), Image.LANCZOS))
    lay = round_corners(small, int(lerp(0, 18, e)) + 1)
    if e > 0.05:
        lay, pad = shadow(lay, 20, 0.35 * e, (0, 10))
    else:
        pad = 0
    return paste(out, lay, cx - sw / 2 - pad, cy - sh / 2 - pad)

# ───────────────────────── 12 pantalla verde ─────────────────────────

def e12(c, o, st):
    need_alpha(c, "pantalla verde")
    if "bg" not in st:
        if o.fondo:
            st["bg"] = [f32(x) for x in load_frames(o.fondo, 0, c.n / c.fps + 0.1, (c.W, c.H), fps=c.fps, cover=True, loop=True)]
        elif o.clips:
            st["bg"] = fuentes(o, 1, c.W, c.H, c)[0]
        else:
            raise SystemExit("«pantalla verde» necesita --fondo otra_toma.mp4 (o --clips carpeta/)")
    bg = st["bg"][c.i % len(st["bg"])]
    a = feather(c.alpha, 1)
    fg = color_match(c.frame, a, bg, 0.25)
    return person_over(bg, fg, a)

# ───────────────────────── 13 corta y pega ─────────────────────────

def torn_poly(rng, pts, jag=14, step=26):
    out = []
    for a, b in zip(pts, pts[1:] + pts[:1]):
        L = math.dist(a, b)
        n = max(1, int(L / step))
        for k in range(n):
            u = k / n
            out.append((lerp(a[0], b[0], u) + rng.uniform(-jag, jag), lerp(a[1], b[1], u) + rng.uniform(-jag, jag)))
    return out


def collage(W, H, seed=13):
    rng = random.Random(seed)
    img = Image.new("RGBA", (W, H), (246, 243, 234, 255))
    d = ImageDraw.Draw(img)
    for x in range(0, W, 38):
        d.line([(x, 0), (x, H)], fill=(170, 200, 225, 90), width=1)
    for y in range(0, H, 38):
        d.line([(0, y), (W, y)], fill=(170, 200, 225, 90), width=1)
    papers = [((248, 232, 60), [(W * 0.25, -20), (W + 20, -20), (W + 20, H * 0.5), (W * 0.35, H * 0.42)]),
              ((196, 160, 116), [(-20, H * 0.33), (W * 0.42, H * 0.3), (W * 0.5, H * 0.75), (-20, H * 0.8)]),
              ((255, 255, 255), [(W * 0.55, H * 0.5), (W + 20, H * 0.46), (W + 20, H * 0.7), (W * 0.6, H * 0.72)])]
    for col, pts in papers:
        poly = torn_poly(rng, pts)
        sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(sh).polygon([(x + 8, y + 8) for x, y in poly], fill=(0, 0, 0, 60))
        img.alpha_composite(sh)
        d.polygon(poly, fill=col + (255,))
    for _ in range(70):                                            # garabato azul de bolígrafo
        x, y = rng.uniform(0, W * 0.4), rng.uniform(0, H * 0.25)
        d.line([(x, y), (x + rng.uniform(40, 160), y + rng.uniform(-30, 30))], fill=(40, 60, 170, 160), width=3)
    for _ in range(40):
        x, y = rng.uniform(W * 0.75, W), rng.uniform(H * 0.3, H * 0.45)
        d.line([(x, y), (x + rng.uniform(30, 90), y + rng.uniform(-20, 20))], fill=(230, 110, 150, 170), width=3)
    for k in range(2):
        x, y = W * 0.88, H * (0.38 + k * 0.035)
        d.line([(x - 14, y - 14), (x + 14, y + 14)], fill=(210, 40, 40, 255), width=4)
        d.line([(x - 14, y + 14), (x + 14, y - 14)], fill=(210, 40, 40, 255), width=4)
    return from_pil(img)


def ransom(txt, H, seed=7):
    rng = random.Random(seed)
    pal = [((15, 15, 15), (255, 255, 255)), ((255, 255, 255), (15, 15, 15)), ((200, 30, 40), (255, 255, 255)),
           ((25, 40, 120), (255, 255, 255)), ((236, 120, 160), (25, 25, 25)), ((248, 232, 60), (15, 15, 15))]
    fonts = ["serif-bold", "black", "impact", "serif"]
    letters = []
    size = int(H * 0.06)
    for ch in txt:
        if ch == " ":
            letters.append(None)
            continue
        bgc, fgc = rng.choice(pal)
        f = font(rng.choice(fonts), size)
        w = int(size * 0.95)
        img, d = draw_layer(w, int(size * 1.15))
        d.rectangle([0, 0, w, size * 1.15], fill=bgc + (255,))
        d.text((w / 2, size * 0.58), ch, font=f, fill=fgc + (255,), anchor="mm")
        letters.append(transform(from_pil(img), angle=rng.uniform(-8, 8)))
    return letters


def e13(c, o, st):
    need_alpha(c, "corta y pega")
    W, H = c.W, c.H
    if "col" not in st:
        st["col"] = collage(W + 40, H + 40)
        st["letters"] = ransom((o.texto or "CORTA Y PEGA").upper(), H)
        st["cache"] = {}
    k8 = int(c.t * 8)                                               # el collage tiembla a 8 fps
    if k8 not in st["cache"]:
        rng = random.Random(k8)
        dx, dy = rng.randint(-5, 5), rng.randint(-5, 5)
        st["cache"][k8] = st["col"][20 + dy:20 + dy + H, 20 + dx:20 + dx + W].copy()
    bg = st["cache"][k8].copy()[..., :3].copy()
    x, y, line_w = W * 0.07, H * 0.11, 0
    idx = 0
    for L in st["letters"]:
        if L is None:
            if line_w > W * 0.45:
                x, y, line_w = W * 0.12, y + H * 0.075, 0
            else:
                x += H * 0.03
            continue
        e = ease_out_back(stagger(c.t, idx, 0.06, 0, 0.22), 0.15)
        idx += 1
        if e > 0.01:
            sx, sy = squash(c.t - (idx - 1) * 0.06 - 0.22)
            paste_center(bg, transform(L, scale=e, sx=sx, sy=sy), x + L.shape[1] / 2, y + L.shape[0] / 2)
        x += L.shape[1] * 0.92
        line_w += L.shape[1]
    a = c.alpha
    d = dilate(a, 8)
    sh = np.zeros_like(d)
    sh[14:, 14:] = d[:-14, :-14]
    bg = bg * (1 - 0.85 * sh[..., None])
    bg = bg * (1 - d[..., None]) + d[..., None]
    return person_over(bg, c.frame, a)

# ───────────────────────── 14 garabato vivo ─────────────────────────

def star_path(cx, cy, R):
    pts = []
    for k in range(11):
        r = R if k % 2 == 0 else R * 0.45
        a = -math.pi / 2 + k * math.pi / 5
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def heart_path(cx, cy, s):
    return [(cx + s * 16 * math.sin(t) ** 3 / 16, cy - s * (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)) / 16)
            for t in np.linspace(0, 2 * math.pi, 40)]


def jitter(pts, rng, amt):
    return [(x + rng.uniform(-amt, amt), y + rng.uniform(-amt, amt)) for x, y in pts]


def e14(c, o, st):
    need_alpha(c, "garabato vivo")
    W, H = c.W, c.H
    boil = c.i // 3                                                # el trazo "hierve" cada 3 fotogramas
    rng = random.Random(boil)
    pts = contours(c.alpha, step=10)
    out = c.frame.copy()
    lay, d = draw_layer(W, H)
    if pts:
        cx = np.mean([p[0] for p in pts])
        cy = np.mean([p[1] for p in pts])
        seg = []
        for x, y in pts:
            if y > H - 10 or x < 4 or x > W - 4:
                if len(seg) > 2:
                    d.line(seg, fill=(255, 255, 255, 255), width=6, joint="curve")
                seg = []
                continue
            v = np.array([x - cx, y - cy])
            v = v / (np.linalg.norm(v) + 1e-6)
            seg.append((x + v[0] * 12 + rng.uniform(-3, 3), y + v[1] * 12 + rng.uniform(-3, 3)))
        if len(seg) > 2:
            d.line(seg, fill=(255, 255, 255, 255), width=6, joint="curve")
    star, _ = polyline_partial(jitter(star_path(W * 0.8, H * 0.3, W * 0.05), rng, 2), ease_out_cubic(prog(c.t, 0.1, 0.4)))
    if len(star) > 1:
        d.line(star, fill=_rgba255("#F5D90A"), width=6, joint="curve")
    if c.t > 0.5:
        sx, sy = W * 0.86, H * 0.26
        d.line([(sx - 12, sy), (sx + 12, sy)], fill=_rgba255("#F5D90A"), width=4)
        d.line([(sx, sy - 12), (sx, sy + 12)], fill=_rgba255("#F5D90A"), width=4)
    heart = jitter(heart_path(W * 0.22, H * 0.33, W * 0.045), rng, 2)
    hp, _ = polyline_partial(heart, ease_out_cubic(prog(c.t, 0.2, 0.35)))
    if prog(c.t, 0.6, 0.2) > 0:
        e = bounce_pop(prog(c.t, 0.6, 0.2), 0.2)
        hc = [(W * 0.22 + (x - W * 0.22) * e, H * 0.33 + (y - H * 0.33) * e) for x, y in heart]
        d.polygon(hc, fill=_rgba255("#F07AA0"))
    if len(hp) > 1:
        d.line(hp, fill=(255, 255, 255, 255), width=5, joint="curve")
    return paste(out, from_pil(lay), 0, 0)

# ───────────────────────── 15 vértigo ─────────────────────────

def e15(c, o, st):
    need_alpha(c, "vértigo")
    if c.plate is None:
        raise SystemExit("«vértigo» necesita base/plate.png (python preparar.py video.mp4 --solo-plate)")
    if "center" not in st:
        st["center"] = face_center(c.alpha)
    e = ease_in_out_cubic(c.p)
    bg = zoom(c.plate, lerp(1.0, 1.35, e), *st["center"])
    bg = edge_radial_blur(bg, *st["center"], strength=0.05 * e)
    return person_over(bg, c.frame, feather(c.alpha, 1.2))

# ───────────────────────── 16 portada ─────────────────────────

MESES = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]


def e16(c, o, st):
    need_alpha(c, "portada")
    W, H = c.W, c.H
    word = (o.texto or "STUDIO").upper()
    if "letters" not in st:
        size = int(H * 0.15 * 1.3)
        while size > 40 and T(word, size, "serif").shape[1] > W * 0.94:
            size -= 8
        st["size"] = size
        st["letters"] = [T(ch, size, "serif") for ch in word]
        total = sum(l.shape[1] for l in st["letters"]) * 0.98
        st["x0"] = (W - total) / 2
        top = bbox(c.alpha)[1] if bbox(c.alpha) else H * 0.3
        st["cy"] = top + H * 0.055
        hoy = datetime.date.today()
        st["front"] = [
            (T("Nº 16 · EDICIÓN", int(H * 0.011), "bold", "#FFFFFF"), W * 0.07, st["cy"] + size * 0.42, "l"),
            (T(f"{MESES[hoy.month - 1]} {hoy.year}", int(H * 0.011), "bold", "#FFFFFF"), W * 0.93, st["cy"] + size * 0.42, "r"),
            (T("CÓMO SE HIZO", int(H * 0.01), "bold", "#FFFFFF"), W * 0.07, H * 0.8, "l"),
            (T((o.items or "Claude editó\neste reel").replace("\\n", "\n"), int(H * 0.03), "serif-italic", "#FFFFFF", align="left"), W * 0.07, H * 0.815, "l"),
        ]
    s = st["size"]
    bg = darken(c.frame, 0.3)
    x = st["x0"]
    for k, L in enumerate(st["letters"]):
        e = ease_out_back(stagger(c.t, k, 0.06, 0, 0.35), 0.06)
        if e > 0:
            paste(bg, L, x, st["cy"] - L.shape[0] / 2 + (1 - e) * 30, opacity=clamp(e))
        x += L.shape[1] * 0.98
    out = person_over(bg, c.frame, c.alpha)
    for k, (img, fx_, fy, al) in enumerate(st["front"]):
        e = ease_out_cubic(stagger(c.t, k, 0.1, 0.35, 0.3))
        if e > 0:
            paste(out, img, fx_ - (img.shape[1] if al == "r" else 0), fy + (1 - e) * 12, opacity=e)
    fr = clamp(prog(c.t, 0.2, 0.4))
    if fr > 0:
        m = 18
        out[m:m + 2, m:W - m] = lerp(out[m:m + 2, m:W - m], 1, fr)
        out[H - m - 2:H - m, m:W - m] = lerp(out[H - m - 2:H - m, m:W - m], 1, fr)
        out[m:H - m, m:m + 2] = lerp(out[m:H - m, m:m + 2], 1, fr)
        out[m:H - m, W - m - 2:W - m] = lerp(out[m:H - m, W - m - 2:W - m], 1, fr)
    return zoom(out, 1 + 0.01 * c.p)                               # 1 % de zoom lento

# ───────────────────────── 17 texto de cristal ─────────────────────────

def e17(c, o, st):
    need_alpha(c, "texto de cristal")
    W, H = c.W, c.H
    word = o.texto or "CLAUDE"
    if "letters" not in st:
        size = int(H * 0.12)
        while size > 30 and T(word, size, "black").shape[1] > W * 0.86:
            size -= 6
        ls = [T(ch, size, "black")[..., 3] if ch != " " else None for ch in word]
        widths = [l.shape[1] if l is not None else size * 0.3 for l in ls]
        x = (W - sum(widths)) / 2
        cy = H * 0.3
        st["letters"] = []
        for l, w in zip(ls, widths):
            if l is not None:
                st["letters"].append((l, int(x), int(cy - l.shape[0] / 2)))
            x += w
        ys = [y for _, _, y in st["letters"]]
        st["box"] = (0, max(0, min(ys) - 60), W, min(H, max(ys) + max(l.shape[0] for l, _, _ in st["letters"]) + 60))
    x0, y0, x1, y1 = st["box"]
    m = np.zeros((y1 - y0, x1 - x0), np.float32)
    for k, (l, lx, ly) in enumerate(st["letters"]):
        e = ease_out_back(stagger(c.t, k, 0.07, 0, 0.3), 0.08)
        if e <= 0:
            continue
        yy = ly - y0 + int((1 - e) * 40)
        hh, ww = l.shape
        sl = m[max(0, yy):yy + hh, lx:lx + ww]
        m[max(0, yy):yy + hh, lx:lx + ww] = np.maximum(sl, l[:sl.shape[0], :sl.shape[1]] * clamp(e))
    region = c.frame[y0:y1, x0:x1]
    blurred = blur(region, 14)
    hgt = ndimage.gaussian_filter(np.clip(ndimage.distance_transform_edt(m > 0.5) / 18, 0, 1), 2)
    gy, gx = np.gradient(hgt)
    yy, xx = np.mgrid[0:m.shape[0], 0:m.shape[1]].astype(np.float32)
    k = 260.0                                                      # fuerza de refracción
    coords = [yy + gy * k, xx + gx * k]
    refr = np.dstack([ndimage.map_coordinates(blurred[..., ch], coords, order=1, mode="nearest") for ch in range(3)])
    refr = np.clip(refr * 1.06 + 0.02, 0, 1)
    rim = np.clip(m - np.roll(m, 2, axis=0), 0, 1)                 # filo de luz arriba
    low = np.clip(m - np.roll(m, -2, axis=0), 0, 1)
    out = c.frame.copy()
    reg = region * (1 - m[..., None]) + refr * m[..., None]
    reg = reg * (1 - 0.25 * low[..., None])
    reg = reg + (1 - reg) * 0.85 * rim[..., None]
    out[y0:y1, x0:x1] = reg
    return person_over(out, c.frame, c.alpha)

# ───────────────────────── 18 revelado con las manos (portal) ─────────────────────────

def e18(c, o, st):
    """Sin rastreo automático: --manos da dónde quedan las manos abiertas. Para rastreo real ver references."""
    W, H = c.W, c.H
    x1, y1, x2, y2 = [float(v) for v in (o.manos or "0.3,0.55,0.7,0.55").split(",")]
    cx, cy = (x1 + x2) / 2 * W, (y1 + y2) / 2 * H
    open_w = abs(x2 - x1) * W
    D = c.n / c.fps
    e = ease_out_back(prog(c.t, 0.25, 0.5), 0.06)
    if o.cerrar:
        e *= 1 - ease_in_cubic(prog(c.t, D - 0.3, 0.3))
    out = c.frame.copy()
    lay, d = draw_layer(W, H)
    hh = H * 0.16
    line_a = clamp(prog(c.t, 0, 0.2))
    d.line([(cx, cy - hh / 2), (cx, cy + hh / 2)], fill=(255, 230, 170, int(255 * line_a)), width=6)
    rw = open_w / 2 * e
    if rw > 2:
        d.ellipse([cx - rw, cy - hh / 2 - rw * 0.25, cx + rw, cy + hh / 2 + rw * 0.25], fill=(255, 240, 200, 235))
    lay = from_pil(lay)
    out = add(out, glow_fast(lay, 60), strength=1.8)
    paste(out, lay, 0, 0)
    if e > 0.05:
        word = T(o.texto or "¡HOLA!", int(H * 0.05), "black", "#2A3A66")
        paste_center(out, transform(word, scale=clamp(e, 0, 1.2)), cx, cy)
    return out

# ───────────────────────── 19 media pantalla ─────────────────────────

def _media_panel(c, o, st):
    """Panel de arriba (W × H/2): captura/video de --fondo sobre su propio fondo desenfocado, o tarjeta de texto."""
    W, half = c.W, c.H // 2
    cw, ch = int(W * 0.88), int(half * 0.76)
    src = o.fondo
    if src and src.lower().endswith(("png", "jpg", "jpeg", "webp")):
        im = Image.open(src).convert("RGB")
        st["bg"] = darken(blur(f32(np.array(ImageOps.fit(im, (W, half), Image.LANCZOS))), 40), 0.55)
        fit = ImageOps.contain(im, (cw, ch), Image.LANCZOS)
        st["content"] = [shadow(round_corners(f32(np.array(fit)), 28), 30, 0.55, (0, 14))]
    elif src:
        info = probe(src)
        k = min(cw / info["w"], ch / info["h"])
        size = (int(info["w"] * k) // 2 * 2, int(info["h"] * k) // 2 * 2)
        frs = [f32(x) for x in load_frames(src, 0, c.n / c.fps + 0.1, size, fps=c.fps)]
        st["bg"] = darken(blur(f32(np.array(ImageOps.fit(to_pil(frs[0]), (W, half), Image.LANCZOS))), 40), 0.55)
        st["content"] = [shadow(round_corners(f, 28), 30, 0.55, (0, 14)) for f in frs]
    else:
        g = np.linspace(0.10, 0.04, half, dtype=np.float32)[:, None, None]
        st["bg"] = np.broadcast_to(g, (half, W, 3)).copy()
        st["content"] = None
    st["texto"] = T(o.texto, int(c.H * (0.07 if not src else 0.024)), "black", AMARILLO if not src else "#111111") if o.texto else None
    st["items"], st["t_items"] = [], []                    # "texto@segundo": la línea entra cuando se dice
    for k, it in enumerate(x for x in (o.items or "").split("|") if x):
        txt, _, ts = it.rpartition("@")
        if not txt or not ts.replace(".", "", 1).isdigit():
            txt, ts = it, ""
        st["items"].append(T(txt, int(c.H * 0.032), "black", "#FFFFFF", max_width=W * 0.84))
        st["t_items"].append(float(ts) if ts else 0.35 + 0.12 * k)


def e19(c, o, st):
    W, H = c.W, c.H
    half = H // 2
    if "bg" not in st:
        _media_panel(c, o, st)
        st["y0"] = float(o.y0) * H
    d = half - st["y0"]                                   # cuánto baja el cuadro para que la cara quede abajo
    t = c.t + (5.0 if o.ya else 0.0)                      # --ya: arranca ya armado (el gancho en el cuadro 0)
    tp = c.t + (5.0 if o.ya or o.cambio else 0.0)         # --cambio: el panel ya está; solo entra el contenido nuevo
    e = ease_out_back(prog(tp, 0, 0.42), 0.06)
    es = ease_out_cubic(prog(tp, 0, 0.42))
    if o.cerrar:                                           # salida: se recoge en los últimos 0.3 s
        x = ease_in_cubic(prog(c.t, c.n / c.fps - 0.3, 0.3))
        e, es = e * (1 - x), es * (1 - x)
    fr = zoom(c.frame, 1 + 0.025 * c.p, W / 2, st["y0"] + half * 0.4)   # micro-zoom sobre la cara
    out = np.empty_like(fr)
    sh = int(round(d * es))
    out[sh:] = fr[:H - sh]
    out[:sh] = st["bg"][:1].mean(axis=1, keepdims=True) if sh else out[:sh]
    # panel de arriba
    panel = st["bg"].copy()
    if st["content"]:
        cimg = st["content"][min(c.i, len(st["content"]) - 1)][0]
        cimg = transform(cimg, scale=1 + 0.03 * c.p)
        ce = ease_out_back(prog(t, 0.0 if o.cambio else 0.12, 0.3 if o.cambio else 0.4), 0.1)
        cy = half * 0.57                                  # deja libre la franja de arriba que tapa la interfaz
        if ce > 0:
            paste_center(panel, transform(cimg, scale=0.85 + 0.15 * ce), W / 2, cy + float_y(c.t, 4, 2.8), opacity=clamp(ce))
        if st["texto"] is not None:
            te = ease_out_back(prog(t, 0.3, 0.3), 0.15)
            if te > 0:
                tw, th = st["texto"].shape[1], st["texto"].shape[0]
                pill = rounded_rect(tw + 44, th + 26, (th + 26) // 2, AMARILLO)
                paste_rgba(pill, st["texto"], 22, 13)
                sx, sy = squash(t - 0.6, 0.1)
                bottom = cy + (st["content"][0][0].shape[0] - 2 * st["content"][0][1]) / 2
                paste_center(panel, transform(pill, scale=te * min(1.25, W * 0.9 / pill.shape[1]), sx=sx, sy=sy), W / 2, bottom + float_y(c.t, 3, 2.2))
    else:
        y = half * (0.30 if st["items"] else 0.5)
        if st["texto"] is not None:
            te = ease_out_back(prog(c.t, 0.12, 0.35), 0.12)
            sx, sy = squash(c.t - 0.47, 0.1)
            if te > 0:
                paste_center(panel, transform(st["texto"], scale=0.6 + 0.4 * te, sx=sx, sy=sy), W / 2, y + float_y(c.t, 4, 3), opacity=clamp(te))
            y += st["texto"].shape[0] * 0.75 + half * 0.08
        for k, it in enumerate(st["items"]):
            ie = ease_out_back(prog(c.t, st["t_items"][k], 0.35), 0.1)
            if ie > 0:
                paste_center(panel, it, W / 2 + (1 - ie) * 60, y + it.shape[0] / 2, opacity=clamp(ie))
            y += it.shape[0] + half * 0.045
    py = int(round(-half + half * e))
    a, b = max(0, py), min(H, py + half)
    if b > a:
        out[a:b] = panel[a - py:b - py]
        lw = max(4, H // 400)                             # línea de división con el acento
        out[max(0, b - lw // 2):min(H, b + lw // 2)] = color(ACENTO)
    return out

# ───────────────────────── etiquetas y CLI ─────────────────────────

NOMBRES = {"01": "orbita", "02": "muro-videos", "03": "mundo-app", "04": "rompe-marco", "05": "zoom-digital",
           "06": "telefono", "07": "checklist", "08": "muro-titulares", "09": "zoom-corte", "10": "grafica",
           "11": "zoom-atras", "12": "pantalla-verde", "13": "corta-pega", "14": "garabato", "15": "vertigo",
           "16": "portada", "17": "cristal", "18": "portal", "19": "media-pantalla"}
DUR = {"01": 1.0, "02": 1.0, "03": 1.1, "04": 1.0, "05": 1.3, "06": 1.1, "07": 1.0, "08": 1.2, "09": 1.3,
       "10": 1.0, "11": 1.4, "12": 1.1, "13": 0.9, "14": 1.0, "15": 1.0, "16": 1.3, "17": 0.9, "18": 1.5, "19": 3.0}
ALIAS = {v: k for k, v in NOMBRES.items()} | {"muro": "02", "app": "03", "marco": "04", "zoom": "05",
                                               "titulares": "08", "corte": "09", "atras": "11", "verde": "12",
                                               "collage": "13", "dolly": "15", "revista": "16", "manos": "18", "media": "19"}


def overlay(img, c, o):
    W, H = c.W, c.H
    if o.cabecera:
        l1, *l2 = o.cabecera.split("|")
        paste_center(img, T(l1, int(H * 0.034), "black", AMARILLO, 3, "#1A1A1A"), W / 2, H * 0.115)
        if l2:
            paste_center(img, T(l2[0], int(H * 0.017), "black", "#FFFFFF", 2, "#1A1A1A"), W / 2, H * 0.145)
    if o.etiqueta:
        num, *nom = o.etiqueta.split("|")
        e1 = ease_out_back(prog(c.t, 0.0, 0.3), 0.1)
        e2 = ease_out_back(prog(c.t, 0.08, 0.3), 0.1)
        if e1 > 0:
            paste_center(img, transform(T(num, int(H * 0.014), "black", "#FFFFFF", 2, "#1A1A1A"), scale=0.9 + 0.1 * e1), W / 2, H * 0.765, opacity=clamp(e1))
        if nom and e2 > 0:
            sx, sy = squash(c.t - 0.38, 0.08)
            paste_center(img, transform(T(nom[0], int(H * 0.038), "black", AMARILLO, 3, "#1A1A1A"), scale=0.9 + 0.1 * e2, sx=sx, sy=sy), W / 2, H * 0.8, opacity=clamp(e2))
    return img


def main():
    global ACENTO
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("efecto")
    ap.add_argument("video")
    ap.add_argument("--start", type=float, default=0.0)
    ap.add_argument("--dur", type=float)
    ap.add_argument("--out")
    ap.add_argument("--texto")
    ap.add_argument("--items")
    ap.add_argument("--clips")
    ap.add_argument("--fondo")
    ap.add_argument("--acento", default=ACENTO)
    ap.add_argument("--etiqueta")
    ap.add_argument("--cabecera")
    ap.add_argument("--manos")
    ap.add_argument("--ya", action="store_true", help="(19) sin animación de entrada")
    ap.add_argument("--cambio", action="store_true", help="(19) sigue a otra media pantalla: solo cambia el contenido")
    ap.add_argument("--y0", default="0.25", help="(19) desde qué alto del cuadro (0–1) se ve la persona en la mitad de abajo")
    ap.add_argument("--cerrar", action="store_true")
    ap.add_argument("--sync-voz", action="store_true")
    ap.add_argument("--sin-audio", action="store_true")
    o = ap.parse_args()
    ACENTO = o.acento
    key = o.efecto.zfill(2) if o.efecto.isdigit() else ALIAS.get(o.efecto.lower())
    if key not in NOMBRES:
        raise SystemExit(f"Efecto desconocido: {o.efecto}. Usa 01–19 o: {', '.join(NOMBRES.values())}")
    fn = globals()[f"e{key}"]
    st = {}
    out = o.out or str(Path(o.video).resolve().parent / f"efecto_{key}.mp4")
    render(out, lambda c: overlay(fn(c, o, st), c, o), video=o.video, start=o.start,
           dur=o.dur or DUR[key], audio=not o.sin_audio)
    print(out)


if __name__ == "__main__":
    main()
