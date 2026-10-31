# Los 17 efectos (+ portal)

Fuente: «17 efectos de video que Claude puede crear» — Máquina IA · @ninodirector. Cada ficha: qué se ve, cuándo usarlo, qué necesita, cómo está hecho en `efectos.py` y qué ajustar. El prompt original de la guía va al final de cada ficha por si hay que rehacerlo desde cero en otro motor.

Leyenda de necesidades: **A** = `base/alpha.mp4` · **P** = `base/plate.png` · **C** = `--clips` opcional.

---

### 01 · órbita — 1 s · A (C)
**Se ve:** tres tarjetas verticales de video giran en 3D alrededor del cuerpo; pasan por detrás (entre fondo y persona) y por delante.
**Úsalo cuando:** mencionas varios ejemplos, clips o casos.
**Implementación:** perspectiva (`project`, `rotate_y_quad`, `warp_to_quad`), orden por z; z>0 detrás de la persona. Entrada escalonada con rebote; flotan ±5 px.
**Ajustar:** radio `R` (0.38·W), velocidad (0.4 vueltas/s), tamaño de tarjeta (0.2·W).
> Prompt original: tres tarjetas verticales de video (12 px de radio, borde blanco de 2 px, sombra) que giran en 3D alrededor de mi eje vertical. Cuando una tarjeta pasa por detrás, va entre el fondo y yo (alpha); por delante, encima. Proyección en perspectiva, escala por profundidad, orden por z. 1080x1920, 30 fps.

### 02 · muro de videos — 1 s · A (C)
**Se ve:** el fondo se vuelve una cuadrícula 3×4 de videos en bucle, oscurecida al 40 %; tú delante.
**Úsalo cuando:** prueba social, "mira todo lo que hice", portafolio.
**Implementación:** 12 miniaturas recortadas sin deformar, esquinas redondas; el muro sube despacio y hace un zoom del 3 % (parallax + micro-movimiento). Corte seco al entrar y salir.
> Prompt original: reemplaza mi fondo por una cuadrícula de 3 columnas × 4 filas de miniaturas de video en bucle (clips/ o capturas de mis videos), con capa negra al 40 %. Píntame encima con alpha. Corte seco.

### 03 · mundo app — 1.1 s · A
**Se ve:** fondo crema (#F5F1E8), una barra de prompt blanca baja (con rebote) hasta quedar detrás de la cabeza y escribe una frase letra por letra con cursor.
**Úsalo cuando:** "le pides a Claude…", "solo escribes esto".
**Opciones:** `--texto "Edítame este reel con mi estilo"`.
> Prompt original: fondo crema; barra de prompt blanca con esquinas redondas y sombra suave baja desde arriba hasta quedar detrás de mi cabeza; dentro se escribe la frase con cursor parpadeante. Barra con PIL a 2x y reducir. Yo encima con alpha.

### 04 · rompe el marco — 1 s · A
**Se ve:** el video se encoge al 60 % en un recuadro con esquinas redondas; cabeza y hombros sobresalen por arriba. Fondo: el mismo video muy desenfocado y oscuro.
**Úsalo cuando:** algo "se sale de lo normal", romper la cuarta pared.
**Ajustar:** `st["cut"]` (altura donde corta el recuadro; default boca).
> Prompt original: reduce el video al 60 % en el centro con esquinas redondas y sombra; de fondo el mismo video desenfocado y oscurecido; encima pega solo cabeza y hombros con alpha para que sobresalgan. Encogimiento ease-out.

### 05 · zoom digital — 1.3 s · (sin alpha)
**Se ve:** tres saltos secos de escala a la cara: 120 %, 140 %, 160 %.
**Úsalo cuando:** hook, énfasis, remate de una frase.
**Implementación:** saltos sin interpolar con 1 fotograma de "punch" (+3 %). `--sync-voz` pone cada salto en una palabra (faster-whisper). Centro de cara estimado desde el alpha si existe.
> Prompt original: saltos de escala escalonados sin interpolar 100→120→140→160 %, centrados en mi cara; cada salto ~3 fotogramas y cae en una palabra.

### 06 · teléfono — 1.1 s · A
**Se ve:** un iPhone (marco negro, isla dinámica) con una app de edición entra desde la derecha girado −15° en Y, queda detrás de ti; dentro se marcan tareas y el botón pasa a "✓ Listo".
**Úsalo cuando:** "desde el celular", una app, un resultado en pantalla.
**Opciones:** `--items` (tareas de la pantalla).
> Prompt original: iPhone con pantalla de app de edición entra desde el borde derecho hasta el 30 % del ancho con rotación −15° en Y y ease-out; detrás de mí (alpha); sombra suave.

### 07 · checklist — 1 s · A
**Se ve:** tarjeta negra (520×360 a 1080 de ancho) entra desde arriba-izquierda a (10 %, 20 %), detrás de ti; cada 0.2 s una tarea se marca con palomita naranja y se tacha.
**Úsalo cuando:** pasos, lista, "solo haces 3 cosas".
**Opciones:** `--items "a|b|c|d"` (máx. 4), `--acento`.
> Prompt original: tarjeta negra 520x360 con esquinas redondas y 4 tareas blancas entra desde arriba a la izquierda, se coloca en 10 % X, 20 % Y, detrás de mí; cada 0.2 s una tarea se marca con palomita naranja. Con PIL, sin drawtext de ffmpeg.

### 08 · muro de titulares — 1.2 s · A
**Se ve:** detrás de ti, 20 tarjetas blancas (titulares, búsquedas, posts) giradas ±6°, superpuestas, que suben despacio.
**Úsalo cuando:** "todo el mundo habla de esto", tendencia, noticia.
**Opciones:** `--items "titular 1|titular 2|…"`. **Cuidado:** no inventes titulares atribuidos a medios reales; usa frases genéricas o titulares verdaderos con fuente.
**Implementación:** entrada escalonada (20 ms), las tarjetas grandes suben más rápido (parallax).

### 09 · zoom de corte — 1.3 s · (sin alpha)
**Se ve:** 0.5 s normal; luego el plano entra hasta el pecho (100→500 %) con aceleración y desenfoque radial; el último fotograma queda casi liso para empalmar.
**Úsalo cuando:** transición a otro tema u otro efecto. Pon el siguiente clip justo después.
> Prompt original: escala de 100 % a 500 % hacia el centro del pecho con aceleración + desenfoque radial (promedia 10 copias escaladas); último fotograma casi liso.

### 10 · gráfica que crece — 1 s · A
**Se ve:** fondo oscurecido 55 %, cuadrícula tenue, una línea amarillo-lima con brillo se traza de izquierda a derecha detrás de ti, subiendo en escalones; en cada vértice salta un punto con rebote.
**Úsalo cuando:** números, crecimiento, resultados, "de X a Y".
**Ajustar:** `xs`/`ys` en `e10` (forma de la curva, relativa a la altura de la cara).

### 11 · zoom hacia atrás — 1.4 s · (sin alpha)
**Se ve:** el plano completo se encoge (100 → ~58 % de alto) y cae dentro del reproductor de una ventana tipo macOS; a la derecha un panel "Trabajando en…" va marcando tareas.
**Úsalo cuando:** mostrar el proceso, "detrás de cámaras", "esto lo hizo una IA".
**Opciones:** `--items` (tareas del panel).

### 12 · pantalla verde — 1.1 s · A
**Se ve:** tu fondo se reemplaza por otro video en movimiento, con corrección suave de color de piel y borde suavizado 1 px.
**Úsalo cuando:** "imagina que estás en…", cambio de escenario.
**Necesita:** `--fondo otra_toma.mp4` (o `--clips`).

### 13 · corta y pega — 0.9 s · A
**Se ve:** contorno blanco grueso (alpha dilatado 8 px), sombra negra dura desplazada; fondo de papeles rotos (amarillo, kraft, blanco) sobre papel cuadriculado con garabatos; letras tipo carta de rescate que entran escalonadas con rebote y aplastamiento; el collage tiembla a 8 fps.
**Úsalo cuando:** tono divertido, DIY, "lo armé yo".
**Opciones:** `--texto "CORTA Y PEGA"`.

### 14 · garabato vivo — 1 s · A
**Se ve:** contorno blanco a mano alrededor de ti que "hierve" (se recalcula cada 3 fotogramas), una estrella amarilla que se traza sola y un corazón que se dibuja y se rellena.
**Úsalo cuando:** emoción, algo que te encanta, cierre simpático.
**Implementación:** `contours()` (OpenCV) + desplazamiento hacia afuera + ruido.

### 15 · vértigo — 1 s · A + P
**Se ve:** dolly zoom: tu tamaño no cambia y el fondo se estira (100 → 135 %), con desenfoque radial leve en los bordes.
**Úsalo cuando:** revelación, "y entonces me di cuenta…".
**Necesita:** un plate bueno (ver SKILL: el de mediana deja relleno borroso donde estabas).

### 16 · portada — 1.3 s · A
**Se ve:** fondo oscurecido 30 %; una palabra enorme en serif blanca, letra por letra, queda detrás de tu cabeza; delante, textos editoriales pequeños (edición, fecha, titular en itálica), un marco fino y 1 % de zoom lento.
**Úsalo cuando:** presentarte, nombre de marca/programa, título del video.
**Opciones:** `--texto ESTUDIO`, `--items "Titular\nen dos líneas"`.

### 17 · texto de cristal — 0.9 s · A
**Se ve:** letras sin color que desenfocan (gauss 14) y refractan el video de detrás según el borde de cada letra; filo de luz blanco arriba. Detrás de la persona.
**Úsalo cuando:** hook elegante, palabra clave, marca.
**Opciones:** `--texto CLAUDE` (frases largas se reducen solas al ancho).

### 18 · portal / revelado con las manos — 1.5 s · (sin alpha)
**Se ve:** línea de luz entre las manos juntas que se abre como portal y revela un texto que crece con la abertura; con `--cerrar`, se cierra al final.
**Graba así:** manos juntas al pecho → sepáralas en ~0.5 s → mantén.
**Opciones:** `--manos "x1,y1,x2,y2"` (0–1, manos abiertas), `--texto`, `--cerrar`.

---

## Montaje tipo "reel de los 17"

La guía cierra uniendo efecto_01…17 con cortes secos, cabecera fija arriba («17 efectos que Claude puede crear») y etiqueta numerada abajo. En `plan.json`: `"solo_efectos": true`, `"cabecera": "17 efectos de video|que claude puede crear"` y `"etiqueta": "NN/17|nombre"` en cada efecto. Truco de la guía: dos efectos seguidos = corte seco entre ellos (09 zoom de corte es la transición natural).
