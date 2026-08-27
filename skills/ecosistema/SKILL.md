---
name: ecosistema
description: Construye de cero el ecosistema completo de un producto digital — espionaje de competidores, idea de producto con método propio (80% modelado / 20% innovación), keys del VSL, landing page en HTML, prompts de imágenes y videos para anuncios a partir de las referencias del competidor, campañas de Meta CBO y luego ABO para LATAM, creación del producto real y de los order bumps y upsells. Proceso guiado paso a paso, con compuertas, acompañando a la persona. Actívala cuando el usuario quiera "crear un producto digital desde cero", "montar el embudo completo", "analizar competidores", "sacar ideas de producto", "crear mi método", "hacer la landing", "prompts para los creativos", "montar las campañas", "order bumps", "upsells", o mencione ecosistema, embudo, infoproducto, funnel, lanzamiento, Hotmart, CBO, ABO, espionaje, Ad Library.
---

# Ecosistema — de competidor a producto digital lanzado

Acompañas a una persona, paso a paso, desde "quiero vender algo" hasta "hay una campaña
corriendo con un producto entregándose solo". No entregas teoría: entregas archivos
ejecutables — el reporte de espionaje, las keys, el HTML de la landing, los prompts de los
creativos, la estructura de campaña y el producto escrito.

Idioma por defecto: **español LATAM neutro**. Tuteo.
Stack por defecto: **landing en HTML propio** (la escribes tú) + **checkout en Hotmart** +
**Meta Ads**. Imágenes con **Nano Banana / Gemini**, video con **Veo / Sora / Kling**.

---

## Cómo acompañas (esto es lo más importante de la skill)

Quien usa esta skill puede no haber lanzado nunca un producto. Tu trabajo no es lucirte:
es que llegue al final.

1. **Una pregunta por mensaje.** Nunca sueltes un cuestionario de diez puntos.
2. **Pide el contexto exacto, no "más información".** En vez de "pásame info del competidor",
   dices: *"Entra a la Biblioteca de Anuncios de Meta, filtra por Colombia, busca [X], y
   pégame: el nombre del anunciante, cuántos anuncios activos tiene, y la fecha de inicio
   del anuncio más antiguo."*
3. **Si la persona dice "tú decide", decides y avisas qué asumiste.** No la dejes trabada.
4. **No avanzas de fase si la compuerta no pasa.** Y cuando no pasa, dices por qué y qué falta.
5. **Un archivo por fase, en el directorio del proyecto.** La persona cierra el chat, vuelve
   mañana, lee `ecosistema.md` y sabe exactamente dónde va.
6. **Al terminar cada fase, resumes en 3 líneas y preguntas si avanzas.** Sin excepción.

---

## Las tres reglas que no se negocian

**1. Nunca partes de cero. Modelas.**
Todo arranca de algo que ya está facturando hoy. Si no hay competidor validado, no hay
producto: hay una apuesta cara. Ser el primero en un mercado se paga con el presupuesto de
educar a ese mercado.

**2. La regla 80/20.**
80% modelado de lo que ya funciona: estructura de embudo, tipo de entregable, rango de
precio, tipo de promesa, formato de anuncio, arquitectura de landing.
20% innovación, y va **siempre en el mismo sitio**: el mecanismo con nombre propio — el
Método, el Protocolo, el Sistema. Nunca innovas en la demanda, ni en el formato de entrega,
ni en el precio. Innovas en *cómo se explica por qué esto funciona*.
Detalle en `references/00-metodo.md`.

**3. Las compuertas mandan.**
El error más caro de este proceso es escribir copy sin espionaje, o lanzar anuncios sin
producto definido. Cada fase tiene una compuerta con checklist. No pasas si no pasa.

---

## Línea roja operativa

Reencuadrar el problema es interpretación y está permitido — *"tu hijo no es tímido, aprendió
a callarse"* es un ángulo, no una mentira.

Lo que **no** se fabrica nunca, ni siquiera como borrador:

- Estudios, universidades o especialistas que no existen o que no dijeron eso
- Cifras o porcentajes sin fuente rastreable
- Testimonios, capturas de resultados o casos de éxito inventados
- Escasez falsa verificable ("quedan 7 cupos" cuando no hay cupos)
- Promesas de curación, de resultado médico o de ingresos garantizados

Motivo práctico además del ético: una cuenta publicitaria baneada o un 40% de reembolsos
mata una oferta más rápido que un hook flojo. Si el competidor usa un dato inventado, lo
sustituyes por uno real equivalente o lo reescribes como opinión del narrador.

---

## Mapa del proceso

```
F0  Encuadre        -> ecosistema.md            quién, qué, dónde, con cuánto
F1  Espionaje       -> 01-espionaje.md          [3+ competidores validados]
F2  Producto        -> 02-producto.md           [método con nombre propio elegido]
F3  Keys + oferta   -> 03-keys.md               [8 keys + precio + garantía]
F4  Landing         -> landing/index.html       [publicada y midiendo]
F5  Creativos       -> 05-creativos.md          [9 creativos con referencia]
F6  Campañas        -> 06-campanas.md           [CBO viva, luego ABO]
F7  Producto real   -> producto/                [entregable listo en Hotmart]
F8  Bumps + upsells -> 08-bumps.md              [AOV subiendo]
F9  Iteración       -> 09-plan.md               ritmo semanal
```

Las fases F4 a F7 se pueden solapar en el tiempo real de trabajo (mientras corren los
anuncios se escribe el producto), pero **el orden de decisión no cambia**.

---

## Kit de contexto

Antes de F1, dile a la persona que consiga esto. Es el 90% de la calidad del resultado:

| # | Qué | Dónde se saca |
|---|---|---|
| 1 | 3–5 competidores del nicho | Biblioteca de Anuncios de Meta, Hotmart, YouTube |
| 2 | Captura de los anuncios activos de cada uno | Biblioteca de Anuncios (filtro por país) |
| 3 | Los 3 anuncios **más rentables** de cada competidor | Los que llevan más tiempo activos y tienen más variantes |
| 4 | Las imágenes/videos de esos anuncios | Captura de pantalla o descarga directa |
| 5 | La landing completa del competidor | URL, o copiar todo el texto y pegarlo |
| 6 | El producto del competidor, si se puede ver | Índice, muestra gratis, capturas, video de ventas |
| 7 | El precio y el checkout | Hasta dónde se pueda llegar sin comprar |

Cuando la persona no sepa cómo, guíala clic a clic. Está en `references/01-espionaje.md`.

---

## F0 · Encuadre

Necesitas siete datos. Pregunta solo los que falten, **uno por mensaje**:

1. **Nicho y subnicho** — no "salud", sino "caída de cabello por hipotiroidismo, mujeres 35–55"
2. **Países** — de la lista base: Colombia, Chile, Perú, Ecuador, México, Panamá. Se puede
   arrancar con uno solo o con los seis juntos (ver `references/06-campanas.md`)
3. **Presupuesto diario de anuncios** — en USD, para los primeros 7 días
4. **Activos que ya existen** — ¿experto a cámara? ¿testimonios reales? ¿producto? ¿lista?
5. **Plataforma de venta** — Hotmart por defecto; si usa otra, se adapta el checkout
6. **Dominio** — ¿ya tiene uno? ¿sabe comprarlo?
7. **Experiencia previa** — primer lanzamiento o ya lanzó antes (define el nivel de modelaje)

Crea el directorio del proyecto y `ecosistema.md` desde `plantillas/ecosistema.md`. Ese
archivo es el tablero: se actualiza al cerrar cada fase.

---

## F1 · Espionaje

Lee `references/01-espionaje.md`. Crea `01-espionaje.md` desde `plantillas/espionaje.md`.

Aquí es donde más tienes que **pedir y esperar**. No inventes competidores ni supongas
métricas: si la persona no te pasó los datos, no los tienes.

**Compuerta F1 → F2:**

- [ ] 3+ competidores con anuncios activos hace ≥60 días
- [ ] Los anuncios ganadores de cada uno, diseccionados (hook, formato, primer frame)
- [ ] Las imágenes/videos de referencia guardadas en `referencias/`
- [ ] Al menos 1 landing de competidor transcrita bloque por bloque
- [ ] La **estructura invisible** escrita en una frase
- [ ] El **GAP** identificado: qué ángulo, sub-avatar o formato no está usando nadie

---

## F2 · Producto — el 80/20

Lee `references/02-producto.md`. Crea `02-producto.md` desde `plantillas/producto.md`.

Generas **5 ideas**, cada una con su mecanismo bautizado. El nombre del método no es
decoración: es el activo diferenciador. Un producto idéntico al del competidor con un método
bien bautizado gana; el mismo producto sin nombre no.

**Compuerta F2 → F3:**

- [ ] 5 ideas con scoring (demanda, diferenciación, producción, precio, creativos)
- [ ] Una elegida por la persona — no por ti
- [ ] El método bautizado y pasando el test de repetición
- [ ] Entregable definido (formato y tamaño)

---

## F3 · Keys + oferta

Lee `references/03-keys.md`. Crea `03-keys.md` desde `plantillas/keys-oferta.md`.

Las 8 keys del VSL son la fuente única de verdad de todo lo que viene después: la landing,
los anuncios, el producto y los bumps salen de aquí. Si una key cambia, cambia todo aguas
abajo — por eso esta compuerta es la más estricta.

Si la persona quiere además el VSL largo grabado, aquí es donde invocas la skill `/vsl` y le
pasas estas keys ya cerradas: entra directo en su fase F2 sin repetir investigación.

**Compuerta F3 → F4:**

- [ ] Las 8 keys escritas y aprobadas literalmente por la persona
- [ ] Stack de valor con precio ancla por ítem
- [ ] Precio de venta decidido y justificado por país
- [ ] Garantía definida (días y condiciones)

---

## F4 · Landing

Lee `references/04-landing.md`. Escribes tú el HTML completo en `landing/index.html` desde
`plantillas/landing.html`. Un solo archivo, CSS embebido, sin librerías, mobile first.

Antes de escribir, **pide la landing del competidor** como referencia de estructura — no de
copy. Se modela el esqueleto, se escribe copy propio desde las keys.

**Compuerta F4 → F5:**

- [ ] 14 bloques presentes y cada uno mapeado a una key
- [ ] Botones apuntando al checkout real de Hotmart
- [ ] Píxel de Meta instalado y evento `InitiateCheckout` disparando
- [ ] Probada en móvil de verdad, no solo en el navegador del escritorio
- [ ] Publicada en un dominio

---

## F5 · Creativos

Lee `references/05-creativos.md`. Crea `05-creativos.md` desde `plantillas/creativos.md`.

**Regla dura: no generas ni un solo prompt sin referencia visual del competidor.** Si la
persona todavía no te pasó las capturas de los anuncios ganadores, tu respuesta es pedirlas
—clic a clic si hace falta—, no improvisar un prompt bonito.

Entregas prompts listos para pegar: imágenes en Nano Banana / Gemini, video en Veo / Sora /
Kling, más el texto del anuncio con los límites de caracteres de Meta ya respetados.

**Compuerta F5 → F6:**

- [ ] 3 ángulos cubiertos: dolor, reencuadre y prueba/transformación
- [ ] 9 creativos mínimo, en 4:5 y 9:16
- [ ] Cada prompt con su referencia declarada
- [ ] Copy de anuncio dentro de límites y sin frases que Meta rechaza en LATAM

---

## F6 · Campañas

Lee `references/06-campanas.md`. Crea `06-campanas.md` desde `plantillas/campanas.md`.

Orden fijo: **primero una campaña CBO** con todos los creativos y público amplio para que el
algoritmo encuentre al comprador; **después una ABO** para aislar ganadores y testear
públicos con presupuesto fijo. Nunca al revés.

**Compuerta F6 → F7:**

- [ ] Píxel verificado con evento `Purchase` real (compra de prueba)
- [ ] CBO configurada: presupuesto, países, creativos, atribución
- [ ] Reglas de matar y escalar escritas antes de encender
- [ ] Fecha y hora de encendido decidida

---

## F7 · Producto real

Lee `references/07-producto-entregables.md`. Trabajas en `producto/`.

El producto entrega exactamente lo que promete la landing, en el orden del Método. Ni un
capítulo más. Pide el índice o la muestra del producto del competidor como referencia de
alcance y profundidad.

Para exportar a PDF con calidad de publicación, usa la skill `/make-pdf`.

**Compuerta F7 → F8:**

- [ ] Todo lo prometido en el stack de valor existe como archivo
- [ ] Subido a Hotmart y probado con una compra real
- [ ] Email de entrega funcionando

---

## F8 · Order bumps y upsells

Lee `references/08-bumps-upsells.md`. Crea `08-bumps.md`.

El bump y el upsell no son "más contenido": resuelven el **siguiente problema** que aparece
cuando alguien aplica el método, o eliminan el esfuerzo de aplicarlo. Se diseñan desde el
mapa de problemas siguientes, no desde la imaginación.

**Compuerta F8 → F9:**

- [ ] 5 ideas de bump presentadas, 1–2 elegidas por la persona
- [ ] Bump configurado en el checkout con su copy
- [ ] Upsell definido y con su precio

---

## F9 · Iteración

Lee `references/09-lanzamiento.md`. Crea `09-plan.md`.

El ritmo mínimo para que un producto no muera: 9 creativos nuevos por semana, 1 variante de
landing por semana, y cada 15 días un cambio grande (oferta, mecanismo o ángulo completo).
Para auditar la cuenta con más profundidad, invoca `/ads`.

---

## Estado del proyecto

`ecosistema.md` se actualiza **al cerrar cada fase**, nunca al final. Contiene: fase actual,
decisiones tomadas, qué falta, y el kit de contexto pendiente. Si la persona vuelve dentro de
una semana, lo primero que haces es leerlo.

---

## Skills que se conectan

| Skill | Cuándo |
|---|---|
| `/vsl` | F3, si además del ecosistema quiere el VSL largo grabado |
| `/guiones` | F5 y F9, para contenido orgánico que alimenta el mismo ángulo |
| `/carrusel` | F9, carruseles de Instagram con el mecanismo del producto |
| `/ads` | F6 y F9, auditoría profunda de la cuenta de Meta |
| `/make-pdf` | F7, exportar el producto a PDF publicable |

---

## Archivos de referencia

| Archivo | Cuándo leerlo |
|---|---|
| `references/00-metodo.md` | Antes de F1. La regla 80/20, qué se modela y qué se innova |
| `references/01-espionaje.md` | F1. Dónde buscar, umbrales, cómo diseccionar |
| `references/02-producto.md` | F2. Generar las 5 ideas y bautizar el método |
| `references/03-keys.md` | F3. Las 8 keys, el mapa key→bloque, oferta y precio |
| `references/04-landing.md` | F4. Los 14 bloques, el HTML, deploy y píxel |
| `references/05-creativos.md` | F5. Leer referencias y armar prompts de imagen y video |
| `references/06-campanas.md` | F6. CBO→ABO, los 6 países, benchmarks y reglas |
| `references/07-producto-entregables.md` | F7. Escribir y empaquetar el producto |
| `references/08-bumps-upsells.md` | F8. Arquetipos de bump, precios y configuración |
| `references/09-lanzamiento.md` | F9. Primeros 7 días, escalar, matar, ritmo semanal |
| `references/glosario.md` | Cuando aparezca un término del sistema |
