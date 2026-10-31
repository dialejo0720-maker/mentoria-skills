"""
Instala la skill video-pizarra (Horizontes IA, github.com/santmun/video-pizarra) en ~/.claude/skills
y le aplica los ajustes de la mentoría: compatibilidad con Windows y las reglas de movimiento de video-con-vida.

Uso:  python instalar_pizarra.py            -> instala o actualiza
      python instalar_pizarra.py --solo-parches   -> solo vuelve a aplicar los ajustes

Se puede correr las veces que haga falta: cada ajuste se aplica una sola vez.
"""
import io, shutil, sys, tempfile, urllib.request, zipfile
from pathlib import Path

ZIP = "https://github.com/santmun/video-pizarra/archive/refs/heads/main.zip"
DESTINO = Path.home() / ".claude" / "skills" / "video-pizarra"
MARCA = "<!-- ajustes-mentoria -->"

NOTA = MARCA + """
## Si la computadora es Windows — léelo antes de correr comandos

Los comandos de este skill están escritos para Mac. En Windows:
- **Puedes no crear `.venv`.** Instala una vez en el Python del sistema: `python -m pip install numpy Pillow librosa rembg[cpu] faster-whisper`. Donde diga `python3 -m venv .venv && .venv/bin/pip install …` o `.venv/bin/python X.py`, usa directamente `python X.py`. Si sí usas `.venv`, el ejecutable está en `.venv/Scripts/python.exe` (los `build.sh` ya lo buscan ahí).
- **Scripts `.sh`**: córrelos con Git Bash: `bash build.sh <nombre>`, `bash componer.sh aroll.mov nombre`. `cp -r` también va en Bash.
- **Llaves**: guárdalas en `~/.config/video-pizarra/keys.env` (en Windows `C:\\Users\\<usuario>\\.config\\video-pizarra\\keys.env`), una por línea: `SUNO_API_KEY=...` y `ASSEMBLYAI_API_KEY=...`. Cuando la persona diga "guarda mi llave de Suno/AssemblyAI", agrégala ahí (sin borrar la otra) y no la repitas en el chat.
- **Chromium de Playwright**: si el render falla, `npx playwright install chromium` dentro del proyecto.

## Movimiento con vida (aplícalo en cada escena)

Reglas completas en `references/principios.md` de la skill **video-con-vida** (plugin `video` de la mentoría; cárgala para ver su carpeta base). En este motor (GSAP):
- **Nada lineal.** Entradas de tarjetas, textos y props: `back.out(1.5)` (≈8 % de rebote); íconos y la mascota caricatura pueden llegar a `back.out(2.5–3)`. Salidas: `power2.in`, más cortas que la entrada. Lo único lineal: tecleo y trazos que se dibujan.
- **Aplastar-estirar** cuando algo aterriza o la mascota salta: `scaleX: 1.1, scaleY: 0.9` y volver con `elastic.out(1, 0.4)`.
- **Escalonado** 80–120 ms entre elementos de una lista o titular (`stagger: 0.1`), en orden de lectura, con un remate en el último.
- **Parallax**: si la cámara se mueve, fondo ×0.4 y desenfocado, medio ×1, frente ×1.5.
- **Micro-movimiento**: nunca más de ~1.5 s de pantalla quieta — zoom lento de cámara 1–3 %, la mascota respira/parpadea, props flotan ±4–6 px.
- Repasa el checklist del final de `principios.md` antes del QA visual.

**Si la persona se grabó a cámara** (`componer.sh`): en los tramos donde se ve su cara puedes aplicar los efectos de `video-con-vida` (zoom digital, portada, checklist, gráfica que crece, etc.) sobre `aroll.mov` antes de componer, con su `scripts/montar.py plan.json`. Así el video alterna animación de pizarra y tramos a cámara que también se ven editados.

"""

PY_OLD = "PY=python3; [ -x .venv/bin/python ] && PY=.venv/bin/python\n"
PY_NEW = "PY=python3; [ -x .venv/bin/python ] && PY=.venv/bin/python; [ -x .venv/Scripts/python.exe ] && PY=.venv/Scripts/python.exe\n"

# (archivo, texto original, texto ajustado)
PARCHES = [
    ("template/build.sh", PY_OLD, PY_NEW),
    ("template-estilos/build.sh", PY_OLD, PY_NEW),
    ("template-estilos/componer.sh", "#!/bin/zsh\n", "#!/usr/bin/env bash\n"),
    ("template-estilos/vo_words.py", "mp3 = '/tmp/_vo_words.mp3';",
     "import tempfile; mp3 = os.path.join(tempfile.gettempdir(), '_vo_words.mp3');"),
]


def descargar():
    print("  Descargando video-pizarra de github.com/santmun/video-pizarra ...")
    datos = urllib.request.urlopen(ZIP, timeout=120).read()
    tmp = Path(tempfile.mkdtemp())
    zipfile.ZipFile(io.BytesIO(datos)).extractall(tmp)
    raiz = next(tmp.iterdir())
    if not (raiz / "SKILL.md").is_file():
        sys.exit("  ERROR: la descarga no trae SKILL.md. Revisa tu conexión e intenta de nuevo.")
    if DESTINO.exists():
        respaldo = DESTINO.with_name("video-pizarra.backup")
        shutil.rmtree(respaldo, ignore_errors=True)
        DESTINO.rename(respaldo)
        print("  Versión anterior respaldada en video-pizarra.backup")
    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(raiz, DESTINO)
    shutil.rmtree(tmp, ignore_errors=True)


def leer(p):
    return p.read_bytes().decode("utf-8").replace("\r\n", "\n")


def parchear():
    for rel, viejo, nuevo in PARCHES:
        p = DESTINO / rel
        if not p.is_file():
            print(f"  Aviso: no existe {rel} (¿cambió el skill original?)")
            continue
        t = leer(p)
        if nuevo in t:
            continue
        if viejo not in t:
            print(f"  Aviso: {rel} cambió en el original; ese ajuste no se aplicó")
            continue
        p.write_bytes(t.replace(viejo, nuevo, 1).encode("utf-8"))

    s = DESTINO / "SKILL.md"
    t = leer(s)
    if MARCA not in t:
        ancla = "## Modo estilos"
        t = t.replace(ancla, NOTA + ancla, 1) if ancla in t else t + "\n" + NOTA
        s.write_bytes(t.encode("utf-8"))


if __name__ == "__main__":
    if "--solo-parches" not in sys.argv:
        descargar()
    if not (DESTINO / "SKILL.md").is_file():
        sys.exit(f"  ERROR: no encuentro {DESTINO / 'SKILL.md'}")
    parchear()
    print(f"\n  LISTO: video-pizarra instalada en {DESTINO}")
    print("  Cierra y vuelve a abrir Claude Code para que aparezca /video-pizarra.\n")
