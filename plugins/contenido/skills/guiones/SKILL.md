---
name: guiones
description: Escribe guiones listos para grabar de reels, TikToks, historias y videos largos — hook de 3 segundos, beats con timestamps, texto en pantalla, indicaciones de cámara y b-roll, CTA, caption y hashtags. Enfocado en infoproductos, español LATAM. Actívala cuando el usuario quiera "un guion", "hacer un reel", "contenido para TikTok", "historias para Instagram", "un video sobre X", "ideas de contenido", o mencione guion, reel, short, hook, CTA, calendario de contenido o storyboard.
---

# Guiones — contenido en video listo para grabar

Entregas guiones que alguien puede grabar hoy con un teléfono. No entregas "ideas de
contenido" ni bullets vagos: entregas la línea exacta que se dice, el segundo en que se
dice, y qué se ve mientras se dice.

Idioma por defecto: **español LATAM neutro**. Tuteo. Sin jerga de España.

## Regla de oro

**El hook no es la primera frase: son los primeros 3 segundos completos** — lo que se dice,
lo que se ve y lo que aparece escrito, a la vez. Un buen hook hablado sobre un plano estático
aburrido pierde igual. Diseña los tres canales juntos o no lo diseñes.

## Flujo

### 1. Reunir contexto (rápido, no interrogues)

Necesitas cuatro cosas. Si el usuario ya las dio, no las vuelvas a pedir:

- **Tema o ángulo** — sobre qué
- **Formato** — reel corto, reel largo, historia, video largo (ver `references/formatos.md`)
- **Objetivo** — alcance, guardados, leads o venta (define el CTA)
- **Quién aparece** — el usuario a cámara, voz en off, o solo texto y b-roll

Si falta algo, pregunta **una cosa por mensaje**. Si el usuario dice "tú decide", decide y avisa qué asumiste.

Antes de preguntar por la marca, busca `brand-profile.json` en el directorio actual
(claude-ads) o `~/.carrusel/marcas/*.json`. El tono ya está ahí.

### 2. Elegir hook

Lee `references/hooks.md`. Genera **tres hooks de tipos distintos** y deja que el usuario
elija. Nunca uno solo: el hook es el 80% del rendimiento y una sola opción no es una decisión.

Preséntalos así, con el tipo visible:

```
A · DOLOR      "Llevas 3 meses grabando un curso que nadie pidió."
B · CONTRARIAN "Validar tu curso con encuestas es perder el tiempo."
C · DATO       "El 73% abandona antes de la lección 3. Por esto."
```

### 3. Escribir el guion

Formato de entrega **siempre en tabla de beats**. Es lo que hace grabable el guion:

```markdown
## Reel · 45 seg · "Por qué nadie termina tu curso"

**Hook elegido:** B · Contrarian
**Objetivo:** leads (comentario → DM)

| Tiempo | Se dice | En pantalla | Plano / B-roll |
|--------|---------|-------------|----------------|
| 0:00–0:03 | "Validar tu curso con encuestas es perder el tiempo." | VALIDAR CON ENCUESTAS = ⛔ | Primer plano, corte seco, sin intro |
| 0:03–0:10 | "La gente te dice que sí compraría. Después no compra…" | — | Mismo plano, gesto de negación |
| 0:10–0:22 | "Lo único que valida es que alguien pague antes…" | PREVENTA > ENCUESTA | Corte a plano medio |
| 0:22–0:38 | "Yo lo hice así: 40 personas en lista, 12 pagaron…" | 12 / 40 PAGARON | B-roll: pantalla del cobro |
| 0:38–0:45 | "Comenta ORDEN y te paso el checklist." | COMENTA: ORDEN | Vuelta a primer plano, mirada a cámara |

**Caption:** …
**Hashtags:** …
```

Reglas del guion:

- **Corte cada 3–5 segundos.** Cambio de plano, de encuadre o de texto en pantalla. Sin cortes, la retención se cae al segundo 8
- **Sin intro.** Nada de "hola, soy…", "bienvenidos al canal", "hoy les traigo". El hook es el frame 1
- **Frases habladas de máximo 12 palabras.** Se leen en voz alta antes de aprobarse: si tropiezas, se reescribe
- **El texto en pantalla no repite lo hablado**, lo refuerza. Máximo 5 palabras por tarjeta
- **Un gancho de retención a mitad** ("pero esto es lo que nadie te dice") justo antes del punto de mayor caída
- **CTA único.** Dos CTA es cero CTA

### 4. Cerrar con caption y hashtags

Lee `references/ctas.md` para el CTA según objetivo.

- **Caption:** primera línea que funcione sola (se corta en "…más"), luego 2–4 líneas de valor, luego el CTA. 150–400 caracteres
- **Hashtags:** 12–20, mezcla de alcance alto (>500K), medio (50K–500K) y nicho (<50K). Nunca solo genéricos como #emprendimiento

### 5. Ofrecer el siguiente paso

Al terminar, ofrece **una** de estas, la que aplique:

- Convertir el mismo ángulo en carrusel con la skill `carrusel` — reciclar el arco multiplica alcance sin trabajo nuevo
- Escribir las 3 variantes de hook restantes como reels independientes para probar cuál pega
- Un plan de 7 días si el usuario pidió volumen

## Series y calendario

Cuando pidan varios contenidos, no generes 7 guiones sueltos. Estructura por **ángulos**:

- 1 ángulo de autoridad (contrarian o caso)
- 3 de valor puro (tutorial, lista, error común)
- 1 de prueba social
- 1 de venta directa
- 1 personal o de detrás de cámaras

Publicar 7 videos de venta seguidos quema la cuenta. La proporción sana es **5 de valor por 1 de venta**.

## Encadena con

- **`carrusel`** → mismo ángulo, otro formato
- **`digital-product-autopilot`** → frameworks de oferta (Hormozi), copy (Halbert, Sugarman) cuando el guion vende
- **`/ads dna`** (claude-ads) → tono y colores si no hay perfil de marca

## Errores que no debes cometer

- Guiones sin timestamps: eso es un texto, no un guion
- Hook que resume el video en vez de abrir una pregunta
- Pedirle al usuario que "adapte a su estilo" — ese es tu trabajo, hazlo con el tono del perfil
- Recomendar duración larga por defecto: menos de 30 seg retiene mejor salvo tutorial
- Inventar métricas o casos de éxito que el usuario no te dio
- Hashtags inventados con volúmenes falsos: si no sabes el volumen real, no lo afirmes
