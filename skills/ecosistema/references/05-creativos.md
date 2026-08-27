# F5 · Creativos — imágenes y videos desde referencias

Objetivo: 9 creativos mínimo, listos para producir, cada uno con su prompt y su referencia
declarada.

---

## La regla dura

**No se escribe un solo prompt sin la referencia visual del anuncio ganador del competidor.**

Si la persona no la pasó todavía, tu respuesta no es un prompt bonito: es pedirla, clic a
clic. Un prompt sin referencia produce una imagen de stock genérica que no frena el scroll.
Un prompt derivado de un anuncio que lleva 4 meses corriendo produce algo que ya demostró
frenarlo.

### Cómo pedirla

```
Necesito ver los anuncios que ya están funcionando. Haz esto:

1. facebook.com/ads/library → filtra por [país] → busca [competidor]
2. Ordena mentalmente por fecha: los que llevan más tiempo corriendo son los rentables
3. De los 3 más antiguos:
   - Captura de pantalla del anuncio completo (con el texto de arriba)
   - Si es video: descárgalo o mándame captura del PRIMER FRAME y de 2 momentos más
   - Cópiame el texto del anuncio tal cual, con emojis y saltos de línea
4. Mándame las 3. Con eso armo los prompts.
```

Las imágenes se guardan en `referencias/` del proyecto y se citan por nombre de archivo en
cada prompt.

---

## Cómo se lee una referencia

Por cada anuncio de referencia, extrae esta ficha antes de escribir nada:

```markdown
### REF-01 · [competidor] · [formato]

**Primer frame:** qué se ve exactamente en el segundo 0
**Sujeto:** quién aparece — edad aparente, género, rol, vestuario
**Encuadre:** selfie a mano alzada / plano medio / primer plano / cenital / producto solo
**Entorno:** cocina, auto, dormitorio, exterior, fondo neutro
**Luz:** ventana lateral, luz dura de techo, hora dorada, luz de pantalla
**Paleta:** cálida / fría / desaturada / saturada. Colores dominantes
**Nivel de producción:** UGC crudo (teléfono, sin edición) / semiproducido / publicidad
**Texto en pantalla:** literal, tipografía, posición, en qué segundo entra
**Emoción del rostro:** preocupación, alivio, sorpresa, cansancio
**Qué frena el scroll aquí:** una frase
```

**El hallazgo más común y más importante:** en infoproductos de LATAM, lo que gana casi
siempre es **UGC crudo** — teléfono, luz de ventana, sin edición, persona real hablando.
Cuando la referencia dice eso, el prompt tiene que producir eso, no una foto de publicidad.
Si generas algo que se ve "de agencia", perdiste antes de empezar.

---

## Los 5 ángulos

Los 3 primeros son obligatorios en la primera tanda. Los otros dos, en la segunda semana.

| # | Ángulo | Key que usa | Cómo abre |
|---|---|---|---|
| 1 | **Dolor** | KEY 4 + frase textual del avatar | La escena del problema, reconocible al instante |
| 2 | **Reencuadre / contrarian** | KEY 2 | Contradice lo que el avatar cree. Genera fricción |
| 3 | **Prueba / transformación** | KEY 7 + testimonio real | Alguien que ya lo vivió, contándolo |
| 4 | **Demostración del método** | KEY 5 | "Esto es lo que haces en el minuto 1" |
| 5 | **Enemigo común** | Enemigo + KEY 6 | Contra el consejo de siempre, contra la industria |

Batería mínima para arrancar: **3 ángulos × 3 variantes = 9 creativos**, en 4:5 y 9:16.

---

## Formatos y tamaños

| Ubicación | Relación | Píxeles | Nota |
|---|---|---|---|
| Feed de Facebook e Instagram | 4:5 | 1080 × 1350 | El que más ocupa pantalla en el feed |
| Reels y Stories | 9:16 | 1080 × 1920 | Obligatorio: aquí está el inventario barato |
| Cuadrado (respaldo) | 1:1 | 1080 × 1080 | Opcional |

**Zonas seguras en 9:16:** deja libres los **250 px de arriba** y los **420 px de abajo** — ahí
van el nombre del perfil, el copy y el botón de la interfaz. Todo el texto importante va en la
franja central.

---

## Prompts de imagen — Nano Banana / Gemini

Estructura de 6 componentes. Se escribe en párrafo continuo, no en lista de etiquetas:
estos modelos responden mejor a una descripción de escena que a palabras sueltas.

```
[1 SUJETO]        quién o qué, con edad, rasgos y vestuario concretos
[2 ACCIÓN+EMOCIÓN] qué está haciendo y qué se le ve en la cara
[3 ENTORNO]        dónde, con dos o tres detalles que lo hagan real
[4 CÁMARA]         encuadre, altura, distancia focal aparente
[5 LUZ Y PALETA]   fuente de luz, temperatura, saturación
[6 ESTILO]         el nivel de producción + qué evitar
```

### Ejemplo completo, derivado de una referencia UGC

```
Foto tomada con teléfono móvil, sin edición: una mujer latina de unos 38 años, en pijama,
sentada en el borde de la cama de un cuarto infantil con estrellas fosforescentes en el
techo. Mira hacia la puerta entreabierta con expresión de cansancio y preocupación
contenida, la mano apoyada en el edredón. Plano medio ligeramente por debajo del nivel de
los ojos, como si otra persona la estuviera grabando desde la puerta, distancia focal corta
tipo cámara frontal de celular. Luz cálida y baja de una lámpara de mesa a la derecha, resto
del cuarto en penumbra, colores apagados. Estética documental cruda, grano leve, ligero
desenfoque de movimiento, aspecto de foto real de familia. Vertical 4:5.

Evitar: iluminación de estudio, sonrisa publicitaria, fondo limpio, aspecto de banco de
imágenes, texto en la imagen, manos deformes.
```

### Reglas de los prompts de imagen

- **Especificidad sobre adjetivos.** "Cocina con platos sin lavar y un imán de nevera torcido"
  vale más que "cocina realista".
- **La relación de aspecto va escrita en el prompt** además de configurarla en la
  herramienta: "Vertical 4:5" / "Vertical 9:16".
- **El texto grande NO se genera con IA.** Nano Banana puede escribir frases cortas, pero el
  titular del anuncio se pone después en Canva o en el editor de Meta: control total, cero
  errores de ortografía, y se pueden hacer 5 variantes de texto sobre la misma imagen.
  Si aun así se pide texto en la imagen, va entre comillas y con máximo 5 palabras.
- **Usar la referencia como imagen de entrada.** Nano Banana edita a partir de una imagen:
  si la persona sube la captura del anuncio del competidor y pide "misma composición, luz y
  encuadre, pero con esta otra persona y este otro entorno", el resultado se parece más a lo
  que ya funciona. Es la forma más directa de aplicar el 80%.
- **Consistencia de personaje entre creativos:** se sube la primera imagen generada como
  referencia y se pide "la misma mujer de la imagen adjunta, ahora en la cocina".

---

## Prompts de video — Veo / Sora / Kling

Los tres funcionan por clips cortos: **piensa en beats de 8 segundos**, no en un video de 30
seguido. Un anuncio de 20 s se arma con 2–3 clips más el corte.

Estructura del prompt:

```
[ESCENA]     dónde y cuándo
[SUJETO]     quién, con detalle físico y vestuario
[ACCIÓN]     qué pasa, en orden temporal, con marcas de segundo
[CÁMARA]     tipo de plano y movimiento (o "cámara fija en mano")
[LUZ]        fuente y temperatura
[AUDIO]      diálogo entre comillas + ambiente  (Veo y Sora lo generan; Kling no)
[ESTILO]     nivel de producción + negativos
```

### Ejemplo de beat 1 (el hook, segundos 0–8)

```
Cocina de casa real, de mañana. Mujer latina de unos 38 años, sudadera gris, pelo recogido
sin arreglar, sostiene el teléfono con una mano frente a su cara mientras habla, de pie
junto a la nevera.

0–2 s: mira directo a cámara y dice, en voz baja y rápida, como confesando:
       "Mi hijo dejó de contarme cosas y yo tardé dos años en darme cuenta."
2–6 s: baja un poco la mirada, respira, vuelve a mirar a cámara y sigue hablando.
6–8 s: hace una pausa y levanta las cejas, como si fuera a decir algo importante.

Cámara: selfie a mano alzada, vertical 9:16, leve temblor natural, sin movimientos de grúa.
Luz: ventana a la izquierda, luz natural de mañana, algo de contraluz.
Audio: voz femenina latina, tono confidencial, sonido ambiente de cocina de fondo.
Estilo: video casero de teléfono, sin edición, sin música, sin filtros, sin transiciones.

Evitar: iluminación de estudio, movimientos de cámara suaves de trípode, música de fondo,
subtítulos quemados, aspecto de anuncio de televisión.
```

### Reglas de los prompts de video

- **El hook vive en el segundo 0.** No hay logo, ni intro, ni "hola, hoy les voy a contar".
  La primera palabra ya es el hook. Si el modelo mete un fundido de entrada, se corta en
  edición.
- **Movimiento en el primer frame.** Un plano quieto se salta. Que alguien entre en cuadro,
  gire la cabeza, deje algo sobre la mesa.
- **Diálogo corto y coloquial.** Veo y Sora generan mal los párrafos largos. Una o dos frases
  por clip.
- **Kling no genera diálogo:** ahí el audio se graba aparte o se pone voz en off con TTS.
- **Nunca pedir marcas, logos ni caras de personas reales conocidas.**
- **Los subtítulos se ponen después**, no se piden al modelo: salen con errores.

---

## El texto del anuncio

Cada creativo va con su copy. Límites prácticos de Meta:

| Campo | Recomendado | Nota |
|---|---|---|
| Texto principal | ~125 caracteres antes del "ver más" | Lo decisivo va antes del corte |
| Titular | ~40 caracteres | Se trunca en móvil pasado eso |
| Descripción | ~30 caracteres | Solo se ve en algunas ubicaciones |
| Botón | "Más información" / "Comprar" | "Más información" suele bajar el CPC |

Estructura del texto principal:

```
[Línea 1: el hook — la misma frase del video]
[Línea 2: agitación o dato en una línea]
[Línea 3: el mecanismo con su nombre]
[Línea 4: la promesa con tiempo]
[Línea 5: CTA + link]
```

### Lo que Meta rechaza en LATAM (revisar antes de subir)

- **Atributos personales en segunda persona:** "¿Estás gorda?", "¿Sufres de ansiedad?",
  "¿Tu hijo tiene TDAH?". Se reescribe en tercera persona o como observación general:
  "Muchas mamás notan que…"
- **Antes y después** en salud, peso o estética. Prohibido.
- **Promesas de ingresos** con cifras, garantizadas o no.
- **Lenguaje médico:** curar, tratar, diagnosticar, eliminar la enfermedad.
- **Urgencia falsa verificable** o contadores que se reinician.
- **Texto que da a entender que Meta o Instagram avalan el producto.**

Si un anuncio se rechaza: no se apela de inmediato ni se duplica igual. Se identifica la
frase, se reescribe y se sube como creativo nuevo.

---

## Entregable de F5

En `05-creativos.md`, por cada uno de los 9:

```markdown
### CREATIVO 01 · Ángulo dolor · 9:16 · video

**Referencia:** REF-01 (referencias/competidorA-anuncio1.png)
**Qué se modela de ella:** encuadre selfie, cocina, luz de ventana, tono confesional
**Qué se innova:** el mecanismo nombrado en el segundo 6

**Prompt de video (Veo/Sora):**
```
…
```

**Texto en pantalla (se pone en edición):** "…"

**Copy del anuncio:**
Texto principal: …
Titular: …
Descripción: …
Botón: Más información
```

---

## Compuerta F5 → F6

- [ ] 9 creativos con prompt y referencia declarada
- [ ] Los 3 ángulos obligatorios cubiertos
- [ ] 4:5 y 9:16 producidos
- [ ] Copy dentro de límites y revisado contra la lista de rechazos
- [ ] Archivos exportados y nombrados: `angulo_variante_formato.mp4`
