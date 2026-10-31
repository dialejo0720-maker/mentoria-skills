---
name: instalar-pizarra
description: Instala o actualiza la skill video-pizarra (videos animados tipo pizarrón / whiteboard, de Horizontes IA) desde su GitHub oficial y le aplica los ajustes de la mentoría para Windows y las reglas de movimiento de video-con-vida. Actívala cuando el usuario quiera "instalar video pizarra", "hacer videos tipo pizarrón" y /video-pizarra no exista, "actualizar video pizarra", o cuando video-pizarra falle en Windows (build.sh no encuentra Python, componer.sh pide zsh, error con /tmp).
---

# instalar-pizarra

`video-pizarra` es una skill gratuita de **Horizontes IA** (github.com/santmun/video-pizarra). No viene copiada dentro de este plugin: se baja siempre del repositorio original, y esta skill le aplica encima los ajustes de la mentoría:

- `build.sh` encuentra el Python del `.venv` también en Windows (`.venv/Scripts/python.exe`)
- `componer.sh` corre con bash (el original pide zsh, que Windows no tiene)
- la transcripción usa la carpeta temporal del sistema en vez de `/tmp`
- el `SKILL.md` gana una sección para Windows y las reglas de movimiento de `video-con-vida`

## Pasos

Habla en español sencillo y haz tú todo el trabajo técnico; la persona solo confirma.

1. **Instalar.** Corre el script que está en la carpeta base de esta skill (usa `/` en las rutas también en Windows):
   ```bash
   python "<carpeta base de esta skill>/scripts/instalar_pizarra.py"
   ```
   Si ya estaba instalada, la versión anterior queda en `~/.claude/skills/video-pizarra.backup`. Si la persona solo necesita volver a aplicar los ajustes (por ejemplo, la actualizó a mano), usa `--solo-parches`.
   Si el script imprime un **Aviso** de que un archivo cambió en el original, dile en una línea que el autor actualizó ese archivo y que ese ajuste ya no hace falta o hay que revisarlo; no lo parchees a mano sin mirarlo.

2. **Revisar lo que necesita** para renderizar, y avisar en una lista corta qué falta:
   - **Node.js 18+** (`node -v`) — lo usa el motor de animación
   - **ffmpeg** (`ffmpeg -version`) — une video y audio
   - **Python 3.10+** con `numpy Pillow librosa rembg[cpu] faster-whisper` — instálalos con `python -m pip install ...` si faltan
   - **Git Bash** en Windows — viene con Git (git-scm.com)

   Para lo que falte, dale el enlace oficial de descarga y espera a que confirme. No instales programas del sistema sin su sí.

3. **Llaves (opcionales).** La música con IA usa Suno y la transcripción precisa usa AssemblyAI. Sin ellas el skill funciona igual (música propia y transcripción local con faster-whisper). Si la persona las tiene, guárdalas en `~/.config/video-pizarra/keys.env`, una por línea (`SUNO_API_KEY=...`, `ASSEMBLYAI_API_KEY=...`), y no las repitas en el chat.

4. **Cerrar.** Dile que cierre y vuelva a abrir Claude Code, y que después escriba `/video-pizarra` o pida "hazme un video tipo pizarrón sobre …".
