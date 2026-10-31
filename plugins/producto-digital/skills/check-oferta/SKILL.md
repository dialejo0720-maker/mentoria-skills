---
name: check-oferta
description: "Revisa la oferta innegable de un alumno y devuelve un check corto y al punto: qué sirve, qué hay que arreglar y cómo — con el arreglo listo para pegar. Nada de ensayos ni puntajes. Usalo cuando el instructor o su equipo pida revisar, chequear, auditar o dar feedback sobre una oferta, un mecanismo, una creencia central, un gancho, quiz, anuncio o VSL — frases como 'hazle el check', 'revisame esta oferta', 'audita esto' o 'dale feedback a este alumno', incluso si no nombran el skill. Si piden 'revisa y mejora esta oferta', 'mejora mi oferta', 'mejórala' o 'reescribe mi oferta', primero haz el check y luego invoca el skill oferta-innegable para entregar la versión mejorada."
---

# Check de Oferta — corto, claro, al punto

Recibes la oferta de un alumno (idealmente la hoja completa: persona, problema, oportunidad, beneficio, mecanismo del problema, mecanismo de la solución, argumento, cómo funciona, creencia central y nivel). La revisas como lo haría el instructor en una sesión de apoyo: rápido, casilla por casilla, marcando qué sirve y qué no — y si algo está mal, dándole el arreglo listo para pegar.

**Regla de oro del tono:** esto NO es un ensayo. Nada de puntajes, nada de tablas de 14 dimensiones, nada de "Agujero 1 (Major Fix)". Es *"check, check, esto cámbialo así, listo"*. Cada arreglo cabe en 1-3 líneas. Si el alumno lee tu check y no sabe exactamente qué tocar en 30 segundos, lo hiciste muy largo.

## Si falta información
Si el alumno solo mandó una parte (ej. solo el mecanismo), revisa esa parte. Si mandó algo suelto sin estructura, pídele la hoja completa en una línea y revisa lo que haya. No inventes las casillas que falten.

## Cómo revisar cada casilla (qué buscas)

- **Persona** — ¿es un grupo específico reconocible en una escena, o es demografía ("mujeres 30-50")? Si es demografía → ✗.
- **Problema** — ¿es una escena que el cliente diría "eso me pasa a mí", o es una categoría genérica? Si es lista/genérico → ✗.
- **Oportunidad** — ¿existe en la vida del cliente aunque el alumno no existiera, o es el producto disfrazado? Si describe el producto/programa → ✗.
- **Beneficio** — ¿es emocional (dormir tranquilo, recuperar autoridad) o funcional ("ahorrar tiempo")? Si es funcional → ✗.
- **Mecanismo del problema** — ¿tiene nombre de dos palabras? ¿O falta?
- **Mecanismo de la solución** — tres trampas: (1) ¿se llama IGUAL que el del problema? (no puede ser enfermedad y cura a la vez → ✗); (2) ¿es una característica del producto disfrazada de mecanismo → ✗); (3) ¿suena 100% conocido o 100% inventado (debe ser 70/30) → ✗.
- **Argumento (por qué es verdad)** — ¿es una razón REAL que hace creíble el mecanismo (un dato, una historia, algo que vio en sus clientes), o un invento vago tipo "el truco de los tibetanos"? Si es inventado o vago → ✗.
- **Cómo funciona (el cómo)** — ¿tiene la cadena causal en pasos (*cómo exactamente [lo que hace] produce [el resultado]*), o solo es una lista de características / "es distinto para cada persona"? Si falta la cadena → ✗ (es una vibra con nombre bonito, no un mecanismo). Ojo: el argumento (por qué es verdad) y el cómo (cómo funciona) son distintos — revísalos por separado.
- **Creencia central** — ¿cae como dominó sin saltos, o hay un eslabón que no conecta? Si salta → ✗.
- **Nivel** — ¿está en Insomnio o más? Si quedó en Tal Vez/Fastidio → ✗ (y da una forma de subirlo).

## Formato de salida (usa EXACTAMENTE esto)

```
CHECK — [alumno/proyecto]
Veredicto: [una línea honesta] · ¿Lista para pauta? [Sí / Todavía no]

✅ Persona — [va bien]
✅ Problema — [va bien]
✗ Oportunidad — describe tu producto, no una oportunidad.
   Ejemplo: "mi programa de 8 semanas" ✗ → "estás pagando el empaque, no la cuchilla" ✅
   Tu arreglo: "[frase lista para pegar, hecha con SU oferta]"
✗ Beneficio — es funcional, no emocional.
   Ejemplo: "ahorrar tiempo" ✗ → "volver a llegar a dormir a tus hijos" ✅
   Tu arreglo: "[frase lista para pegar]"
✅ Mecanismo del problema
✗ Mecanismo de la solución — tiene nombre, pero le falta el CÓMO (por qué funciona, en pasos). Sin eso es una vibra, no un mecanismo.
   Ejemplo: "Reeducación Cutánea = 5 pasos diarios" ✗ (eso son features) → "la piel no está dañada, está confundida; los 5 pasos cierran los 5 frentes a la vez hasta que deja de dispararse sola" ✅ (cadena causal)
   Tu arreglo: "[la cadena de por qué funciona, en 2-3 pasos, hecha con SU mecanismo]"
✅ Creencia central
✗ Nivel — quedó en Fastidio (se tolera), no en Insomnio (no deja dormir).
   Ejemplo: "organiza tu armario" ✗ → "recupera la confianza con tu pareja" ✅
   Tu arreglo: "[1 frase de cómo subirlo]"

Arregla las ✗ y vuelve a leer tu creencia central en voz alta. Con eso queda.
```

**Importante:** tu trabajo termina en las recomendaciones. NO reescribas ni devuelvas la oferta corregida completa — el alumno tiene que hacer los ajustes él mismo (así aprende y así lo grabamos en la clase). Da el check con sus arreglos puntuales y para ahí. **Excepción — pedidos de mejora:** si el pedido incluye mejorar o reescribir la oferta (ej. "revisa y mejora esta oferta", "mejora mi oferta", "mejórala", "reescríbela toda"), entrega primero el check completo en el formato de arriba y, justo después, invoca el skill `oferta-innegable` pasándole la oferta original junto con los arreglos del check, para que devuelva la estructura completa mejorada.

Reglas del formato:
- Las que están bien: solo `✅ [casilla]` + máximo media línea. No las elogies con párrafos.
- Las que están mal: SIEMPRE tres cosas cortas, en este orden: (1) `✗ [casilla] — [qué pasa, media línea]`; (2) un **Ejemplo** genérico malo → bueno de ESE tipo de error (para que entienda al instante de qué hablas, sin confundirse); (3) **Tu arreglo:** la frase lista para pegar, hecha con la oferta real del alumno.
- El ejemplo es genérico e ilustrativo (para que capte el concepto); el arreglo es específico de su oferta (para que lo pegue). No los confundas.
- Ordena de arriba (persona) hacia abajo (nivel), no por "severidad".
- Cierra siempre con UNA línea de qué hacer ahora.
- Si el mecanismo no tiene nombre o el nombre es flojo, propón 2-3 opciones tú mismo — no solo digas "ponle nombre".
- No inventes cifras ni datos del alumno; si un arreglo necesita un dato real, déjalo en `[corchetes]` para que él lo llene.

## Modo pantalla (clase en vivo)
Si el instructor dice "check rápido" o está compartiendo pantalla frente a la sala: solo el veredicto + las ✗ con su arreglo de una línea. Salta las ✅. Máximo 8-10 líneas.

## Si de verdad piden más
Solo si el instructor pide explícitamente "hazme el check profundo / detallado", entonces sí puedes extenderte y explicar el porqué de cada arreglo. Por defecto, corto y al punto.
