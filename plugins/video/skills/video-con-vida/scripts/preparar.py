"""
preparar.py — Paso 0: se hace UNA vez por video y lo reutilizan todos los efectos.

Crea junto al video una carpeta base/ con:
  alpha.mp4   recorte de la persona en blanco y negro (mismo tamaño y fps)
  plate.png   un fotograma con el fondo vacío (sin la persona)
  check.jpg   3 fotogramas: original | máscara | persona sobre magenta  → REVÍSALO antes de seguir
  meta.json   desde qué segundo empieza alpha.mp4

Uso:
  python preparar.py video.mp4                       # todo el video
  python preparar.py video.mp4 --desde 3 --hasta 21  # solo el tramo donde van efectos (más rápido)
  python preparar.py video.mp4 --solo-plate --plate gemini
Opciones:
  --modelo u2net_human_seg (default, rápido en CPU) | birefnet-portrait (mejor borde, ~5x más lento)
  --plate gemini (borra a la persona con Gemini, necesita GEMINI_API_KEY) | mediana (sin internet)
  --proc 0.5  procesa la máscara a media resolución (más rápido; se reescala y suaviza)
"""
import argparse
import base64
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

sys.path.insert(0, str(Path(__file__).parent))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from fx import Writer, contact, f32, iter_frames, probe, to_u8  # noqa: E402


def make_alpha(video, base, desde, hasta, modelo, proc):
    from rembg import new_session, remove

    info = probe(video)
    W, H, fps = info["w"], info["h"], round(info["fps"])
    dur = (hasta or info["duration"]) - desde
    n_est = int(dur * fps)
    session = new_session(modelo)
    pw, ph = int(W * proc) // 2 * 2, int(H * proc) // 2 * 2
    prev = None
    t0 = time.time()
    with Writer(base / "alpha.mp4", W, H, fps, crf=12) as w:
        for i, fr in enumerate(iter_frames(video, desde, dur, (W, H), fps=fps)):
            img = Image.fromarray(fr)
            if proc != 1:
                img = img.resize((pw, ph), Image.LANCZOS)
            m = remove(img, session=session, only_mask=True, post_process_mask=False)
            if m.size != (W, H):
                m = m.resize((W, H), Image.BICUBIC)
            a = f32(np.array(m))
            # suavizado temporal leve: quita el parpadeo del borde sin dejar estela
            if prev is not None:
                a = 0.7 * a + 0.3 * prev
            prev = a
            a = ndimage.gaussian_filter(a, 0.8)
            w.write(np.dstack([a, a, a]))
            if i % 30 == 0:
                el = time.time() - t0
                print(f"  máscara {i}/{n_est}  ({el:.0f}s, ~{el / max(1, i) * (n_est - i):.0f}s restantes)", flush=True)
    (base / "meta.json").write_text(json.dumps({"alpha_start": desde, "alpha_end": desde + dur, "modelo": modelo}))


def check_sheet(video, base, desde, hasta):
    info = probe(video)
    W, H = info["w"], info["h"]
    dur = (hasta or info["duration"]) - desde
    tiles = []
    for frac in (0.1, 0.5, 0.9):
        t = desde + dur * frac
        fr = f32(next(iter_frames(video, t, 0.1, (W, H))))
        a = f32(next(iter_frames(base / "alpha.mp4", t - desde, 0.1, (W, H), gray=True)))
        mag = np.zeros_like(fr)
        mag[..., 0] = 1.0
        mag[..., 2] = 1.0
        comp = mag * (1 - a[..., None]) + fr * a[..., None]
        tiles += [fr, np.dstack([a, a, a]), comp]
    contact(tiles, base / "check.jpg", height=520)
    print(f"  revisa {base / 'check.jpg'}: ¿la máscara conserva torso, brazos, manos, gorra y pelo?")


def _mid_frame(video, t=None):
    info = probe(video)
    t = info["duration"] * 0.3 if t is None else t
    return next(iter_frames(video, t, 0.1)), info


def plate_gemini(video, base, t=None, model="gemini-3.1-flash-image-preview"):
    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_AI_API_KEY")
    if not key:
        env = Path.home() / ".config/watch/.env"
        if env.exists():
            for line in env.read_text().splitlines():
                if line.startswith("GEMINI_API_KEY="):
                    key = line.split("=", 1)[1].strip().strip('"')
    if not key:
        raise SystemExit("No hay GEMINI_API_KEY. Usa --plate mediana.")
    fr, info = _mid_frame(video, t)
    src = base / "plate_src.png"
    Image.fromarray(fr).save(src)
    prompt = ("Remove the person completely from this photo and reconstruct the empty set behind them exactly as it is: "
              "same wall, lights, furniture, microphone, camera angle, lighting and colors. Do not add anything new, "
              "do not change the framing or aspect ratio. Photorealistic clean background plate.")
    payload = {"contents": [{"parts": [{"inlineData": {"mimeType": "image/png",
                                                      "data": base64.b64encode(src.read_bytes()).decode()}},
                                       {"text": prompt}]}],
               "generationConfig": {"responseModalities": ["IMAGE"]}}
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
    req = urllib.request.Request(url, json.dumps(payload).encode(), {"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            res = json.loads(r.read())
    except urllib.error.HTTPError as e:
        raise SystemExit(f"Gemini respondió {e.code}: {e.read()[:400]!r}  → prueba --plate mediana")
    for part in res.get("candidates", [{}])[0].get("content", {}).get("parts", []):
        if "inlineData" in part:
            out = base / "plate_raw.png"
            out.write_bytes(base64.b64decode(part["inlineData"]["data"]))
            img = Image.open(out).convert("RGB").resize((info["w"], info["h"]), Image.LANCZOS)
            img.save(base / "plate.png")
            print(f"  plate.png listo (Gemini {model}). Compáralo con plate_src.png: el set debe ser el mismo.")
            return
    raise SystemExit("Gemini no devolvió imagen → prueba --plate mediana")


def plate_mediana(video, base, samples=40):
    """Sin internet: mediana de fotogramas donde se ve el fondo + relleno por difusión donde nunca se vio."""
    meta = json.loads((base / "meta.json").read_text())
    info = probe(video)
    W, H = info["w"], info["h"]
    s, e = meta["alpha_start"], meta["alpha_end"]
    ts = np.linspace(s, e - 0.1, samples)
    stack, masks = [], []
    for t in ts:
        stack.append(f32(next(iter_frames(video, t, 0.05, (W // 2, H // 2)))))
        m = f32(next(iter_frames(base / "alpha.mp4", t - s, 0.05, (W // 2, H // 2), gray=True))) > 0.05
        masks.append(ndimage.binary_dilation(m, iterations=6))   # sin halo del borde de la persona
    stack, masks = np.array(stack), np.array(masks)
    data = np.where(masks[..., None], np.nan, stack)
    with np.errstate(all="ignore"):
        import warnings
        warnings.simplefilter("ignore", RuntimeWarning)
        plate = np.nanmedian(data, axis=0)
    hole = np.isnan(plate[..., 0])
    known = ~hole
    plate = np.nan_to_num(plate)
    try:
        import cv2
        u8 = to_u8(plate)
        filled = cv2.inpaint(u8, hole.astype(np.uint8) * 255, 12, cv2.INPAINT_TELEA)
        filled = cv2.GaussianBlur(filled, (0, 0), 3)            # suaviza solo el relleno
        plate = np.where(hole[..., None], f32(filled), plate)
        Image.fromarray(to_u8(plate)).resize((W, H), Image.LANCZOS).save(base / "plate.png")
        print(f"  plate.png listo (mediana + inpaint). {hole.mean() * 100:.0f}% del cuadro es relleno: "
              f"sirve para fondos desenfocados u oscurecidos; para 'vértigo' mejor un plate real (ver SKILL).")
        return
    except ImportError:
        pass
    kf = known.astype(np.float32)
    # relleno grueso → fino: el sigma grande cubre todo el hueco, los chicos afinan cerca del borde
    for k, sig in enumerate((200, 100, 50, 25, 12, 6)):
        num = ndimage.gaussian_filter(plate * kf[..., None], (sig, sig, 0))
        den = ndimage.gaussian_filter(kf, sig)[..., None]
        fill = num / np.maximum(den, 1e-6)
        ok = hole[..., None] & ((den > 0.05) | (k == 0))
        plate = np.where(ok, fill, plate)
    img = Image.fromarray(to_u8(plate)).resize((W, H), Image.LANCZOS)
    img.save(base / "plate.png")
    print(f"  plate.png listo (mediana). {hole.mean() * 100:.0f}% del cuadro se rellenó por difusión: "
          f"sirve para fondos desenfocados u oscurecidos; para 'vértigo' o 'órbita' mejor --plate gemini.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--desde", type=float, default=0.0)
    ap.add_argument("--hasta", type=float, default=None)
    ap.add_argument("--modelo", default="u2net_human_seg")
    ap.add_argument("--proc", type=float, default=1.0)
    ap.add_argument("--plate", choices=["gemini", "mediana", "no"], default="gemini")
    ap.add_argument("--plate-t", type=float, default=None, help="segundo del fotograma para el plate")
    ap.add_argument("--solo-plate", action="store_true")
    a = ap.parse_args()

    video = Path(a.video).resolve()
    base = video.parent / "base"
    base.mkdir(exist_ok=True)
    if not a.solo_plate:
        print(f"1/3 recorte de persona con {a.modelo}…")
        make_alpha(video, base, a.desde, a.hasta, a.modelo, a.proc)
        print("2/3 hoja de verificación…")
        check_sheet(video, base, a.desde, a.hasta)
    if a.plate != "no":
        print(f"3/3 fondo vacío ({a.plate})…")
        try:
            if a.plate == "gemini":
                plate_gemini(video, base, a.plate_t)
            else:
                plate_mediana(video, base)
        except SystemExit as e:
            print(f"  {e}\n  usando mediana como respaldo…")
            plate_mediana(video, base)
    print("listo:", base)


if __name__ == "__main__":
    main()
