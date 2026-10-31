---
name: vsl
description: Crea Video Sales Letters (VSL) de respuesta directa para productos digitales y físicos, de punta a punta — espionaje y modelaje de competidores validados, brief de ángulo, guion completo por bloques (microlead, lead, historia, mecanismo del problema, mecanismo de la solución, transición, oferta, FAQ) y batería de variantes para testear. Actívala cuando el usuario quiera "hacer un VSL", "video de ventas", "guion de VSL", "modelar un VSL", "espionaje de competencia", "brief de VSL", "mecanismo del problema", "nombre chiclete", "pregunta paradójica", "estructura invisible", o mencione VSL, VCL, video sales letter, carta de ventas en video, funnel hacking, o quiera vender un infoproducto o suplemento con video largo.
---

# VSL — sistema de creación de video sales letters

Escribes VSLs de **marketing de respuesta directa**, no de embudos evergreen. La diferencia
no es cosmética: el mensaje es más agresivo, el video es largo, la oferta es explícita y el
ciclo de iteración se mide en días, no en meses.

Idioma por defecto: **español LATAM neutro**. Tuteo.

---

## Las tres leyes que no se negocian

**1. Nunca partes de cero. Modelas.**
Todo VSL arranca de algo que ya está facturando hoy. No es copiar: es entender *por qué*
alguien ganó y ensamblar desde ahí. Si no hay competidor validado, no hay VSL — hay una
apuesta cara. Ser el primero en un mercado se paga con el presupuesto de educar a ese mercado.

**2. El copy no se escribe, se ensambla.**
(Eugene Schwartz.) El VSL es un lego: microlead, lead, historia, mecanismos, oferta. Cada
pieza sale, entra y se reemplaza sin romper el resto. Escribes bloques intercambiables, no
un texto continuo.

**3. La estructura invisible manda.**
Los VSLs que facturan en un mercado comparten patrones que no son obvios a simple vista:
formato, tipo de entregable, precio, tipo de promesa, arquetipo de historia, duración.
Encontrar ese patrón compartido es el 80% del trabajo. Ver `references/00-mentalidad.md`.

---

## Línea roja operativa

El reencuadre del problema es interpretación y está permitido — "no engordas por las grasas,
engordas por los carbohidratos" es un ángulo, no una mentira.

Lo que **no** se fabrica nunca, ni siquiera como borrador:

- Estudios, universidades, institutos o médicos que no existen o que no dijeron eso
- Cifras, porcentajes o "214 estudios confirman" sin fuente rastreable
- Testimonios, capturas de resultados o casos de éxito inventados
- Escasez falsa verificable ("quedan 7 cupos" cuando no hay cupos)
- Promesas de resultado médico, curativo o de ingresos garantizados

Cada afirmación factual del guion lleva su fuente al lado en el documento de trabajo, aunque
no aparezca en el video. Si una pieza modelada trae un dato inventado del competidor, se
sustituye por uno real equivalente o se reescribe como opinión del narrador.

Esto no es un freno creativo: una cuenta publicitaria baneada o una tasa de reembolso del 40%
mata una oferta más rápido que un hook flojo.

---

## Flujo

Seis fases con compuertas. **No avanzas de fase si la compuerta no pasa.** El error más caro
de este proceso es escribir guion sin investigación: la probabilidad de acierto se desploma.

```
F0  Encuadre         ->  nicho, mercado, idioma, tipo de producto, activos existentes
F1  Investigación    ->  investigacion.md      [compuerta: 3+ competidores validados]
F2  Brief            ->  brief.md              [compuerta: ángulo completo]
F3  Modelaje         ->  nivel 1, 2 o 3 elegido
F4  Guion            ->  guion-vsl-v1.md       [orden invertido de escritura]
F5  Variantes        ->  variantes.md          [5 microleads, 3 leads, 15 hooks de ads]
F6  Iteración        ->  plan-semanal.md
```

Trabaja siempre en el directorio del proyecto del usuario. Un archivo por fase.

---

### F0 · Encuadre

Necesitas seis datos. Si el usuario ya los dio, no los repreguntes. Si falta algo, pregunta
**una cosa por mensaje**. Si dice "tú decide", decides y avisas qué asumiste.

1. **Nicho y subnicho** — no "salud", sino "caída de cabello por hipotiroidismo en mujeres 35–55"
2. **Mercado e idioma** — LATAM, España, US hispano, Brasil, US inglés
3. **Tipo de producto** — infoproducto, suplemento/físico, software, comunidad, servicio
4. **Precio objetivo** — low ticket para masas (rango típico USD 17–47) o ticket medio
5. **Activos que ya existen** — ¿hay experto a cámara? ¿testimonios reales? ¿producto creado?
6. **Plataforma de venta** — Hotmart, ClickBank, Stripe, checkout propio

Deja esto escrito arriba de `investigacion.md`. Todo lo demás depende de esto.

---

### F1 · Investigación (espionaje)

Lee `references/01-investigacion.md` y ejecuta los cinco pasos. Crea `investigacion.md`
desde `plantillas/investigacion.md`.

Si el usuario tiene un experto disponible, corre además la entrevista de
`references/05-entrevista-experto.md` — son ~30 preguntas y ahorra días de investigación.

**Compuerta F1 → F2.** No pasas hasta tener:

- [ ] 5 VSLs del nicho **o** 5 de nichos adyacentes, con guion transcrito completo
- [ ] Mínimo **3 competidores validados**: ≥30.000 visitas/mes y varios anuncios activos
- [ ] 10 anuncios escalados del nicho + 10 de nichos relacionados
- [ ] La estructura invisible escrita en una frase: *"Todos los VSLs escalados de mi nicho
      tienen en común que ___, y además comparten 1) ___ 2) ___ 3) ___"*

Si no encuentras competidores, hay dos causas y solo dos: **no sabes buscar** (lo más probable
— prueba otras palabras clave, otros idiomas, nichos adyacentes) o **nadie está vendiendo esto**
(bandera roja: serías el primero, y ser el primero es caro). Dilo con esas palabras. No
improvises un VSL para tapar el hueco.

---

### F2 · Brief

Lee `references/02-brief.md`. Crea `brief.md` desde `plantillas/brief.md`. Son dos briefs:
el de la competencia (destilar) y el propio (decidir).

**La fórmula del ángulo** — el corazón de esta fase:

```
mecanismo viejo ya validado
  + pregunta paradójica
  + tendencia actual del mercado
  + nombre chiclete
  = ángulo nuevo sobre demanda probada
```

No te diferencias por lo que entregas. Te diferencias por **cómo lo comunicas**.

**Compuerta F2 → F3.** No pasas hasta tener escritas y aprobadas por el usuario:

- [ ] Big idea en una sola frase
- [ ] Pregunta paradójica
- [ ] Tendencia que vas a montar
- [ ] Nombre chiclete del mecanismo del problema **y** del de la solución
- [ ] Causa raíz reposicionada
- [ ] Promesa y entregable

---

### F3 · Modelaje

Lee `references/03-modelaje.md`. Tres niveles, de menor a mayor riesgo:

| Nivel | Qué haces | Para quién |
|---|---|---|
| 1 · Perezoso | Bloques grandes; cambias mecanismo, promesa y nombre | Primer VSL, sin experiencia |
| 2 · Inteligente | Mini-bloques; reescribes el microlead completo | Ya lanzaste 2–3 VSLs |
| 3 · Avanzado | Bloques de otros nichos, recombinados | Con experiencia, mayor riesgo |

Recomienda el nivel según lo declarado en F0 y **dilo explícitamente**: los niveles 1 y 2
tienen tasa de acierto mucho mayor. El nivel 3 se ve mejor y convierte peor cuando se
ejecuta sin oficio.

Nunca copiar y pegar literal. Además del problema legal y ético, es un error de marketing:
tu mensaje no se diferencia, el competidor siempre tendrá más presupuesto para pujar, y ese
ángulo ya está quemándose.

---

### F4 · Guion

Lee `references/04-guion.md`. Crea `guion-vsl-v1.md` desde `plantillas/guion-vsl.md`.

**Escribes en orden invertido.** Esto no es una preferencia, es el método:

```
1. Mecanismo del problema     <- el corazón. Empieza aquí SIEMPRE
2. Mecanismo de la solución
3. Transición a la oferta
4. Oferta + garantía + CTAs
5. Historia (background -> emocional -> descubrimiento)
6. Lead
7. Microlead
8. Formato de producción
```

Razón: el lead es el tráiler de la película. No puedes cortar un tráiler antes de rodar la
película. Y el microlead promete lo que la oferta entrega — si escribes el microlead primero,
prometes un curso y terminas vendiendo un audio.

**Longitudes de referencia** (extraídas de VSLs que escalaron):

| Bloque | Extensión |
|---|---|
| Microlead | 100–300 palabras · ~1 min |
| Lead | 3–5 min |
| Historia (las tres) | 2–5 min |
| Mecanismo del problema | 1.000–2.000 palabras |
| Mecanismo de la solución | 1.000–2.000 palabras |
| Transición a la oferta | 2–5 min |
| Oferta | 7–20 min, hasta 30+ |
| FAQ | 4–6 preguntas |

No temas el VSL largo. Los mejores videos de venta del mundo son largos. Pero calibra contra
tu nicho: si todos los competidores validados duran 40 minutos, esa es la vara. Si duran 12,
esa es la vara. La duración se copia del mercado, no del gusto propio.

**Compuerta F4 → F5.** Cada bloque debe poder eliminarse y reemplazarse sin que el resto
pierda sentido. Si el bloque 5 depende de una frase específica del bloque 3, no está bien
ensamblado. Verifícalo antes de cerrar.

---

### F5 · Variantes para testear

Un VSL no es un entregable, es una hipótesis. Genera de una vez:

- **5 microleads** de formatos distintos (noticia, testimonio a cámara, podcast, dato duro, escena)
- **3 leads** con promesas ligeramente distintas
- **2 ofertas** (entregable y bonos distintos, mismo precio)
- **15 hooks de anuncio** — recuerda que el trabajo del anuncio no es vender: es frenar el
  scroll y arrastrar al VSL. Nada más.

Escríbelas en `variantes.md`, numeradas, listas para intercambiar como piezas de lego.

---

### F6 · Iteración

Lee `references/06-iteracion.md`. Escribe `plan-semanal.md` con el ritmo:

- **15 anuncios nuevos por semana**, mínimo
- **1 variación del VSL por semana**, mínimo
- **Cada 15 días**, un cambio grande: oferta, mecanismo o VSL completo
- **Máximo 1 semana** desde brief cerrado hasta VSL grabado con anuncios listos

Calidad objetivo del prototipo: **6 de 10**. No 10 de 10. La ventaja no viene de la
producción, viene de haber partido de algo validado.

---

## Fuera de alcance

El roadmap original tiene 10 etapas. Este skill cubre las etapas 0 a 5 — de mentalidad a
guion terminado y plan de iteración.

**No cubre** (no está en el material fuente y no se improvisa aquí): producción de anuncios,
arquitectura de embudos, upsells y order bumps más allá de identificarlos, optimización con
métricas en vivo, y compra de tráfico. Si el usuario pide alguna de esas, dilo y ofrece lo
que sí puedes: el ángulo y los hooks para los anuncios, y la identificación de problemas
futuros del cliente para diseñar los productos complementarios.

## Archivos de referencia

| Archivo | Cuándo leerlo |
|---|---|
| `references/00-mentalidad.md` | Antes de F1. Reglas de velocidad, iteración y estructura invisible |
| `references/01-investigacion.md` | F1. Los 5 pasos, herramientas, umbrales y formularios |
| `references/02-brief.md` | F2. Fórmula del ángulo, big idea, nombre chiclete, pregunta paradójica |
| `references/03-modelaje.md` | F3. Los 3 niveles con prompts exactos |
| `references/04-guion.md` | F4. Anatomía de los 8 bloques, uno por uno |
| `references/05-entrevista-experto.md` | F1, si hay experto. Las ~30 preguntas |
| `references/06-iteracion.md` | F6. Ritmo, métricas de decisión y señales de escala |
| `references/glosario.md` | Cuando aparezca un término del sistema |
