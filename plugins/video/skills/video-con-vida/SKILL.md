---
name: video-con-vida
description: Le da vida y efectos visuales a cualquier video — sobre todo a videos de alguien hablando a cámara — con 17 efectos por capas listos (órbita de tarjetas, muro de videos, mundo app, rompe el marco, zoom digital, teléfono, checklist, muro de titulares, zoom de corte, gráfica que crece, zoom hacia atrás, pantalla verde, corta y pega, garabato vivo, vértigo, portada de revista, texto de cristal) más revelado con las manos, y las reglas de movimiento que hacen que nada se mueva "como robot" (curvas con rebote, entradas escalonadas, parallax por capas, micro-movimiento constante). Actívala cuando el usuario quiera "editar mi video hablando a cámara", "ponerle efectos a mi video", "que mi reel se vea más visual/dinámico/pro", "darle vida a las animaciones", "que no se vea plano", "efectos tipo Ninodirector/Máquina IA", o mencione cualquiera de esos efectos, recorte de persona, fondo detrás de mí, texto detrás de la cabeza, dolly zoom, zoom a la cara, easing, rebote u overshoot. También la consultan video-pizarra, cancion-video-karaoke y cualquier edición de video (Remotion, Hyperframes, GSAP, ffmpeg) para aplicar las reglas de movimiento.
---

# video-con-vida

Dos cosas en una skill:

1. **Las reglas de movimiento** — se aplican SIEMPRE que edites o animes cualquier video (pizarra, animado, karaoke, a cámara, Remotion, Hyperframes). Están en `references/principios.md`.
2. **Los efectos para videos a cámara** — 17 efectos por capas (fondo → elementos → persona → elementos delante) ya programados en `scripts/efectos.py`, más `montar.py` que los mete en el video completo.

Catálogo visual (3 fotogramas de cada efecto, probados en un clip real): `catalogo/efectos-01-06.jpg`, `efectos-07-12.jpg`, `efectos-13-18.jpg` — muéstraselos a la persona con Read si no sabe cuál elegir.

Fuentes: guía «17 efectos de video que Claude puede crear» (Máquina IA · @ninodirector) y guía «Dale vida a tus animaciones» (@SantiMunozIA). Detalle de cada efecto, su prompt original y cuándo usarlo: `references/efectos.md`.

## Las reglas (resumen — no te las saltes)

| Regla | Valor | Por qué |
|---|---|---|
| **Nada lineal** | entradas con ease-out + rebote del 5–10 % (`ease_out_back(t, 0.08)`); salidas con ease-in | lo lineal se ve falso |
| **Aplastar y estirar** al aterrizar | `squash()` ±8–12 % durante ~0.25 s | se siente con peso |
| **Entradas escalonadas** | 80–120 ms entre elementos, en orden de lectura; el último con remate | el ojo sabe a dónde mirar |
| **Parallax por capas** | fondo lento + algo desenfocado, medio normal, frente rápido | profundidad |
| **Micro-movimiento** | nunca pantalla quieta: zoom lento 1–3 %, flotar ±4–6 px, respirar ±1 %, balanceo ±1.5° | lo quieto se siente congelado |
| **Un efecto = una idea del guion** | el efecto ilustra lo que se dice en ese momento | si no, es decoración |

Equivalencias por motor (GSAP, CSS, Remotion, Python) en `references/principios.md`.

## Qué aplicar según el tipo de video

- **Motion graphics sin persona** (logo animado, dato animado, intro/outro, video de lanzamiento, "como este reel pero con mi marca"): usa Remotion o Hyperframes si los tienes instalados. Esta skill aporta las reglas de tono y los efectos sobre personas.

- **Hablando a cámara** (reel, anuncio, VSL corto): flujo completo de abajo. Un efecto cada 3–6 s, de 0.9–1.4 s cada uno; entre efectos, el video normal con micro-zoom.
- **Pizarra / animado** (`video-pizarra`): solo las reglas de movimiento al construir escenas. Si la persona se grabó a cámara (`componer.sh`), en sus tramos de cara puedes usar los efectos de esta skill antes de componer.
- **Karaoke / fotos** (`cancion-video-karaoke`): rebote al entrar cada foto, Ken Burns con ease (no lineal), palabras del karaoke con pop escalonado, nunca una foto quieta.
- **Remotion / Hyperframes**: traduce las reglas con la tabla de `principios.md`; los efectos se pueden recrear allí con la misma lógica de capas si el proyecto ya vive en ese motor.

## Flujo para un video a cámara

### 0 · Preparar (una sola vez por video)
```bash
S="<carpeta base de esta skill>/scripts"   # la ruta que aparece al cargar la skill; usa / en Windows
python $S/preparar.py video.mp4                      # todo el video
python $S/preparar.py video.mp4 --desde 3 --hasta 25 # solo el tramo con efectos (más rápido)
```
Crea `base/alpha.mp4` (recorte de la persona), `base/plate.png` (fondo vacío) y `base/check.jpg`. **Abre `check.jpg` con Read**: si la máscara pierde torso, brazos, manos, gorra o pelo, repite con `--modelo birefnet-portrait` (mejor borde, ~5x más lento). Sin GPU, `u2net_human_seg` tarda ~0.3–0.5 s por fotograma: córrelo en segundo plano.

Fondo vacío (`plate.png`): por defecto intenta Gemini (necesita `GEMINI_API_KEY` con facturación activa: en plan gratis la generación de imágenes da error 429); si no hay clave o falla, cae solo al modo `mediana` (mediana de fotogramas + inpaint de OpenCV). Ese relleno sirve para fondos oscurecidos/desenfocados; para «vértigo» u «órbita» con fondo nítido conviene un plate real: pedirle a la persona 2 s del set vacío (sale de cuadro al final de la toma) y guardar ese fotograma como `base/plate.png`, o activar facturación en Gemini.

### 1 · Guion → momentos
Transcribe (faster-whisper; o `vo_words.py` de video-pizarra) y elige los momentos por lo que se DICE. Guía rápida:

| Cuando dice… | Efecto |
|---|---|
| el hook / la primera frase | 05 zoom digital, 09 zoom de corte como transición, 17 texto de cristal |
| un número, crecimiento, resultado | 10 gráfica que crece |
| pasos, lista, "solo haces 3 cosas" | 07 checklist |
| una app, un prompt, "le pides a Claude" | 03 mundo app, 06 teléfono, 11 zoom hacia atrás |
| "todos hablan de esto", prueba social | 08 muro de titulares, 02 muro de videos |
| varios ejemplos / casos | 01 órbita, 02 muro de videos |
| un cambio de lugar o de tema | 12 pantalla verde, 09 zoom de corte |
| una revelación, "imagina…" | 18 portal con las manos, 15 vértigo, 17 texto de cristal |
| la marca, el título, la autoridad | 16 portada |
| momento divertido / informal | 13 corta y pega, 14 garabato vivo |
| algo que "se sale" de lo normal | 04 rompe el marco |

No repitas el mismo efecto seguido ni pongas dos efectos pesados juntos. Muestra a la persona la lista `segundo → efecto → por qué` y espera su visto bueno (salvo que pida hacerlo directo).

### 2 · Probar cada efecto suelto
```bash
python $S/efectos.py 07 video.mp4 --start 6.1 --items "Graba|Suelta el video|Pide el efecto|Publica"
```
Cada render guarda `efecto_NN_qa.jpg` (inicio, mitad, final). **Ábrelo con Read** y compáralo con la descripción de `references/efectos.md`. Si algo se ve raro (texto tapando la cara, elemento fuera de cuadro, borde del recorte feo), ajusta y repite.

### 3 · Montar el video completo
Escribe `plan.json` (formato en `scripts/montar.py`) y corre `python $S/montar.py plan.json`. Mete los efectos en su lugar con el audio original del tramo (la voz no se desfasa) y saca `-movil.mp4` si pesa más de 30 MB. Para el formato "reel de los 17" usa `"solo_efectos": true`, `"cabecera"` y `"etiqueta"` por efecto.

### 4 · QA final y entrega
`ffmpeg -i final.mp4 -vf "fps=2,scale=-2:300,tile=12x2" -frames:v 1 contact.jpg` y revísalo. Entrega la ruta del final y del móvil, más la lista de efectos usados.

## Opciones útiles de efectos.py

`--texto` (03, 13, 16, 17, 18) · `--items "a|b|c"` (06, 07, 08, 11; en 16 el titular) · `--clips carpeta/` (01, 02, 08, 12) · `--fondo otra_toma.mp4` (12) · `--acento "#hex"` (color de marca) · `--etiqueta "NN/17|nombre"` · `--cabecera "línea 1|línea 2"` · `--manos "x1,y1,x2,y2"` (18) · `--sync-voz` (05: cada salto cae en una palabra) · `--dur` · `--sin-audio`.
Sin `--clips`, las tarjetas y muros usan otros momentos del mismo video.

## Requisitos (revísalos la primera vez)

- **Python 3.10+** con: `pip install numpy scipy Pillow rembg[cpu] opencv-python-headless faster-whisper librosa`, y **ffmpeg** en el PATH. Si falta algo, instálalo tú antes de seguir y avísale a la persona en una línea.
- No necesita GPU ni MediaPipe. La cara se estima desde el recorte (`face_center`); verifica en el `_qa.jpg` que el zoom caiga en la cara. Si no, pasa el centro a mano editando el efecto.
- El revelado con las manos (18) va con posiciones manuales (`--manos`); el rastreo real necesitaría MediaPipe en un venv de Python 3.12.
- Fuentes: pensadas para Windows (Segoe UI Black, Georgia, Consolas, Segoe Script). En Mac/Linux cae a Arial/Times o a la fuente por defecto: si el texto se ve pobre, pasa la ruta de un `.ttf` en `font()`.

## Para crear un efecto nuevo

Copia el más parecido en `efectos.py`, respeta el orden de capas y usa los helpers de `fx.py` (`ease_out_back`, `stagger`, `squash`, `float_y`, `breathe`, `person_over`, `paste`, `card`, `shadow`, `warp_to_quad`, `rotate_y_quad`, `zoom`, `radial_blur`, `glow_layer`, `dilate`, `contours`, `text`). Un efecto es una función `eNN(c, o, st)` que devuelve el fotograma; `st` es un diccionario para guardar lo que se calcula una sola vez. Regístralo en `NOMBRES` y `DUR`.
