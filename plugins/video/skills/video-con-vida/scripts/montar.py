"""
montar.py — mete los efectos dentro del video completo. Fuera de los efectos se ve el video normal.

  python montar.py plan.json            → <salida>.mp4 (+ <salida>-movil.mp4 si pesa > 30 MB)

plan.json:
{
  "video": "video.mp4",
  "salida": "final",
  "cabecera": "17 efectos de video|que claude puede crear",      (opcional, fija arriba en cada efecto)
  "efectos": [
    {"efecto": "05", "start": 2.4},
    {"efecto": "07", "start": 6.1, "items": "Graba|Suelta el video|Pide el efecto|Publica"},
    {"efecto": "16", "start": 11.0, "dur": 1.3, "texto": "ESTUDIO", "etiqueta": "16/17|portada"}
  ]
}
Cada efecto usa el audio original de su tramo, así que la voz no se corta ni se desfasa.
Con "solo_efectos": true se pegan solo los efectos seguidos (corte seco), como el reel de los 17.
"""
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from fx import concat, probe  # noqa: E402
import efectos as E  # noqa: E402

HERE = Path(__file__).parent


def cut(video, a, b, out):
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", f"{a:.4f}", "-i", str(video), "-t", f"{b - a:.4f}",
                    "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-c:a", "aac", "-b:a", "192k", str(out)],
                   check=True)
    return out


def main():
    plan_path = Path(sys.argv[1]).resolve()
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    root = plan_path.parent
    video = (root / plan["video"]).resolve()
    info = probe(video)
    W, H, fps, D = info["w"], info["h"], round(info["fps"]), info["duration"]
    work = root / "efectos_tmp"
    work.mkdir(exist_ok=True)
    items = sorted(plan["efectos"], key=lambda e: e["start"])
    pieces, cursor = [], 0.0
    for k, e in enumerate(items):
        key = e["efecto"].zfill(2) if str(e["efecto"]).isdigit() else E.ALIAS[e["efecto"]]
        dur = e.get("dur", E.DUR[key])
        if e["start"] < cursor - 1e-3:
            raise SystemExit(f"El efecto {key} en {e['start']}s se encima con el anterior (que termina en {cursor:.2f}s)")
        if not plan.get("solo_efectos") and e["start"] - cursor > 1 / fps:
            pieces.append(cut(video, cursor, e["start"], work / f"seg_{k:02d}.mp4"))
        out = work / f"fx_{k:02d}_{key}.mp4"
        cmd = [sys.executable, str(HERE / "efectos.py"), key, str(video), "--start", str(e["start"]), "--dur", str(dur),
               "--out", str(out)]
        for opt in ("texto", "items", "clips", "fondo", "acento", "etiqueta", "manos", "y0"):
            if e.get(opt):
                v = str(e[opt])
                if opt in ("clips", "fondo"):
                    v = str((root / v).resolve())
                cmd += [f"--{opt}", v]
        if e.get("cabecera", plan.get("cabecera")):
            cmd += ["--cabecera", e.get("cabecera", plan.get("cabecera"))]
        if e.get("cerrar"):
            cmd.append("--cerrar")
        for flag in ("ya", "cambio"):
            if e.get(flag):
                cmd.append(f"--{flag}")
        if e.get("sync_voz"):
            cmd.append("--sync-voz")
        print(f"[{k + 1}/{len(items)}] efecto {key} en {e['start']}s ({dur}s)…", flush=True)
        subprocess.run(cmd, check=True)
        pieces.append(out)
        cursor = e["start"] + dur
    if not plan.get("solo_efectos") and D - cursor > 1 / fps:
        pieces.append(cut(video, cursor, D, work / "seg_fin.mp4"))
    final = root / f"{plan.get('salida', 'final')}.mp4"
    print("uniendo…", flush=True)
    concat(pieces, final, W, H, fps)
    if final.stat().st_size > 30 * 1024 * 1024:
        movil = root / f"{plan.get('salida', 'final')}-movil.mp4"
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(final), "-c:v", "libx264", "-crf", "26",
                        "-preset", "slow", "-vf", "scale=720:-2", "-c:a", "aac", "-b:a", "128k", str(movil)], check=True)
        print(movil)
    print(final)


if __name__ == "__main__":
    main()
