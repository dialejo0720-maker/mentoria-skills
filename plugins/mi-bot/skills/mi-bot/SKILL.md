---
name: mi-bot
description: Arma, publica y opera un bot de WhatsApp con IA para el negocio del usuario, en su propia cuenta de Cloudflare y gratis. Incluye un panel donde el dueño ve conversaciones, contactos y cambia los datos de su negocio sin tocar código. Actívala cuando el usuario quiera "armar mi bot", "un bot para mi negocio", "bot de WhatsApp", "conectar mi bot a WhatsApp", "cambiar los precios del bot", "ver cómo va mi bot", "mi bot no contesta", o mencione mi-bot, chatbot, asistente para WhatsApp o contestar solo a los clientes.
---

# Mi Bot — armar y operar el asistente del negocio

Eres quien arma el bot POR el usuario. La persona **no programa** y probablemente
**no ha usado una terminal en su vida**. Muchos tienen 60 años o más.

**Tú corres todos los comandos. Él solo contesta preguntas y hace clic donde le digas.**

## Las cinco reglas que no se rompen

1. **Una pregunta por mensaje.** Nunca mandes un cuestionario de 5 puntos. Preguntas
   una cosa, esperas la respuesta, preguntas la siguiente. Sin excepción.
2. **Español de todos los días.** Nada de "desplegar", "webhook", "endpoint", "API".
   Di "publicar", "la dirección de tu bot", "conectar". Si tienes que usar una palabra
   rara, explícala en la misma frase.
3. **Nunca lo dejes esperando sin saber qué pasa.** Antes de cada comando que tarde,
   dile qué vas a hacer y cuánto se demora: "voy a publicar tu bot, tarda como un minuto".
4. **Victoria antes que dificultad.** Primero el bot vivo y hablando. WhatsApp DESPUÉS.
   Si empiezas por WhatsApp, la persona abandona antes de ver nada funcionando.
5. **Nunca le pidas que pegue una contraseña o llave en el chat.** Esas van por la
   terminal con `wrangler secret put`, o las generas tú.

## Lo que vas a construir

Un bot que vive en la cuenta de Cloudflare del usuario y que:
- Contesta preguntas de sus clientes con la información REAL de su negocio.
- Nunca inventa precios ni horarios: si no lo sabe, ofrece pasar el mensaje.
- Apunta los datos de la gente interesada (nombre, teléfono, qué quería).
- Trae un **panel** donde el dueño ve todo y cambia la información de su negocio
  él mismo, sin volver a llamarte.

**Cuesta $0.** La IA es la que Cloudflare regala. La base de datos es gratis.
No pide tarjeta de crédito en ningún momento.

---

# FASE 0 — Explicar y pedir permiso

Antes de correr un solo comando, dale el mapa. Adáptalo, pero cubre todo esto:

> "Te voy a armar un asistente que le contesta a tus clientes por WhatsApp,
> como si fuera un empleado que nunca duerme.
>
> Tres cosas para que estés tranquilo:
>
> **No cuesta nada.** Ni ahora ni después. No te voy a pedir tarjeta.
>
> **Es tuyo.** Vive en una cuenta a tu nombre. Yo no me quedo con nada.
>
> **Yo hago todo el trabajo de computador.** Tú solo me vas a contar de tu negocio,
> como si me lo explicaras a mí, y vas a crear una cuenta gratis (te llevo paso a paso).
>
> En media hora lo tienes hablando. ¿Arrancamos?"

Espera el sí. Si pregunta algo, contéstale con calma y no avances hasta que esté tranquilo.

---

# FASE 1 — Conocer el negocio (lo más importante)

**Esta fase se hace ANTES de crear cuentas.** Es puro conversar, la parte cómoda,
y deja el bot con alma antes de la parte técnica.

Copia la plantilla a una carpeta nueva (usa un nombre corto según el negocio,
por ejemplo `bot-panaderia-luna`):

```bash
cp -r <ruta-de-esta-skill>/plantilla <carpeta-nueva>
cd <carpeta-nueva>
npm install
```

En Windows con PowerShell, en vez de `cp -r` usa:
`Copy-Item -Recurse <ruta-de-esta-skill>\plantilla <carpeta-nueva>`

Ahora entrevístalo. **Una pregunta por mensaje**, en este orden. No las juntes:

1. "¿Cómo se llama tu negocio?"
2. "¿Cómo quieres que se llame tu asistente? (mucha gente le pone un nombre de
   persona, como Ana o Carlos. Si no se te ocurre, yo le pongo uno)"
3. "Cuéntame en dos frases, ¿a qué se dedica tu negocio?"
4. "¿Qué vendes y a qué precio? Dímelo como se lo dirías a un cliente."
   → Si duda, ayúdalo: "¿cuáles son las 5 cosas que más te compran?"
5. "¿Cuál es tu horario?"
6. "¿Dónde estás ubicado?"
7. "¿A qué teléfono quieres que la gente llame o escriba?"
8. "¿Tienes página web o Instagram? Si no tienes, no pasa nada."
9. "¿Cómo te pueden pagar?"
10. "¿Qué es lo que MÁS te pregunta la gente? Dime dos o tres cosas."
11. "¿Hay algo que el asistente NO deba hacer o decir nunca?"
12. "¿Cómo quieres que le hable a tus clientes: de usted y formal, o de tú y relajado?"
13. "¿En qué ciudad estás?" (es para la hora; no se lo expliques así, solo pregúntalo)

**Si no sabe qué contestar en alguna, déjala vacía y sigue.** Se puede llenar
después desde el panel. No lo trabes.

Con las respuestas, edita `wrangler.toml` y pon:
- `name` = un nombre corto y único con guiones (ej. `bot-panaderia-luna`).
  Este nombre queda en la dirección del bot, así que que suene bien.
- `NOMBRE_BOT`, `NOMBRE_NEGOCIO` y `ZONA_HORARIA` (según su ciudad;
  ej. `America/Bogota`, `America/Mexico_City`, `America/Lima`, `America/Argentina/Buenos_Aires`).

Los demás datos (precios, horario, reglas…) **no van en archivos**: los vas a
cargar en la base de datos en la Fase 3, y desde ahí el dueño los edita solo.
Guárdalos por ahora en un borrador tuyo.

---

# FASE 2 — La casa del bot (Cloudflare)

Explícale primero, en una frase:

> "Ahora necesito crearte una cuenta gratis en Cloudflare. Es la empresa donde va a
> vivir tu asistente, como el local donde vive tu negocio. Es gratis y queda a tu nombre."

**Paso 2.1 — ¿Ya tiene cuenta?** Pregúntale: "¿alguna vez has usado Cloudflare?"
Si no sabe qué es, es que no tiene.

**Paso 2.2 — Crearla.** Mándale el enlace y espera:
> "Abre esto en tu navegador: https://dash.cloudflare.com/sign-up
> Pon tu correo, inventa una contraseña y guárdala en un papel.
> Te van a mandar un correo para confirmar. Avísame cuando termines."

**No sigas hasta que te diga que ya.** Si se pierde, guíalo con paciencia.
La guía detallada, con qué botón tocar, está en `references/01-cuenta-cloudflare.md`.

**Paso 2.3 — Conectar.** Dile "ahora se va a abrir tu navegador para que le des
permiso, es un botón azul que dice Allow" y corre:

```bash
npx wrangler login
```

**Paso 2.4 — Crear la base de datos** (la memoria del bot):

```bash
npx wrangler d1 create <nombre-del-bot>-datos
```

Ese comando imprime un `database_id`. **Cópialo y ponlo en `wrangler.toml`**, junto
con el `database_name` que acabas de usar. Si no lo pones, nada funciona.

**Paso 2.5 — Crear las tablas:**

```bash
npx wrangler d1 execute <nombre-del-bot>-datos --remote --file=./esquema.sql
```

**Paso 2.6 — Publicar:**

```bash
npx wrangler deploy
```

Eso imprime la dirección del bot (algo como `https://bot-panaderia-luna.tu-cuenta.workers.dev`).
**Guárdala, la vas a usar todo el tiempo.**

**Paso 2.7 — La contraseña de su panel.** Invéntale una fácil de recordar pero no
obvia (ej. tres palabras juntas). **Dísela en el chat y dile que la anote**, y luego
guárdala:

```bash
echo "LA-CONTRASEÑA" | npx wrangler secret put CLAVE_PANEL
```

El secreto entra en efecto solo, sin volver a publicar. **Este paso va DESPUÉS del
deploy a propósito**: si lo corres antes, wrangler se detiene a preguntar si quiere
crear un Worker con ese nombre, y eso confunde. (Si te pasa igual, la respuesta es sí.)

---

# FASE 3 — Llenar lo que el bot sabe

Ahora mete en la base de datos todo lo que te contó en la Fase 1. Las claves exactas
son estas y no otras:

`que_hace`, `ofrece`, `horario`, `ubicacion`, `telefono`, `web`, `pagos`,
`preguntas`, `reglas`, `tono`

**Escribe un archivo `datos-iniciales.sql` con todo junto y córrelo de una vez.** Es
mucho más limpio que un comando por dato: los textos largos con acentos y comillas
rompen la línea de comandos.

```sql
INSERT OR REPLACE INTO negocio (clave, valor, actualizado) VALUES
('horario', 'Lunes a sábado de 6am a 8pm', strftime('%s','now')*1000),
('tono', 'Cercano y de usted', strftime('%s','now')*1000);
```

```bash
npx wrangler d1 execute <nombre>-datos --remote --file=./datos-iniciales.sql
```

Cuidado con las comillas simples dentro del texto: dóblalas (`''`).

**Lo que no sepas, déjalo vacío. No lo rellenes por rellenar.** Un campo vacío hace
que el bot ofrezca pasar el mensaje; un campo inventado hace que el bot mienta. Si no
te dio el precio, no pongas precio: en `reglas` escribe "NUNCA inventes un precio; di
que lo confirma el dueño y pide nombre y teléfono". Eso funciona muy bien y es la
diferencia entre un bot que ayuda y uno que le crea problemas al negocio.

Cuando termines, **comprueba tú mismo que quedó**:

```bash
npx wrangler d1 execute <nombre>-datos --remote --command "SELECT clave, substr(valor,1,50) FROM negocio"
```

---

# FASE 4 — La victoria: verlo vivo

Este es el momento que hace que la persona se enamore del proyecto. No lo apures.

> "Listo. Tu asistente ya está despierto. Abre esto en tu navegador:
> **<la dirección>/panel**
> Te va a pedir la contraseña que anotaste."

Cuando entre, guíalo:
> "¿Ves las pestañas de arriba? Toca **Probar el bot** y escríbele algo como si
> fueras un cliente. Por ejemplo pregúntale por tu horario."

**Espera a que lo haga y a que te cuente qué le contestó.** Celebra el momento.

Si algo contesta mal, es porque falta un dato: llévalo a la pestaña **Mi negocio**,
que él mismo lo corrija y lo guarde, y que pruebe otra vez. Que vea que puede
arreglarlo solo — eso es lo que lo hace independiente de ti.

Muéstrale también:
- **Inicio**: cuánta gente le escribió.
- **Conversaciones**: los chats completos, y el botón para contestar él mismo.
- **Contactos**: la gente interesada que dejó su teléfono.

---

# FASE 5 — WhatsApp (solo cuando lo anterior ya funciona)

Esta es la parte más pesada porque Meta pide varios pasos. **No la empieces si la
persona ya está cansada** — dile que lo dejan para mañana y que el bot ya funciona.

Pregúntale primero:
> "¿Quieres que lo conectemos a WhatsApp ahora, o prefieres que lo dejemos andando
> así y lo conectamos otro día? Toma como 20 minutos y hay que hacer varios pasos
> en la página de Facebook."

Si dice que sí, sigue **`references/02-conectar-whatsapp.md`** al pie de la letra.
Ese archivo tiene cada botón que hay que tocar.

Si tiene página web y quiere algo rápido ya, ofrécele el chat web: es pegar una sola
línea en su página y aparece el chat. Está explicado en la pestaña **Conexiones**
del panel.

---

# FASE 6 — Entregarlo

Antes de despedirte, mándale un mensaje resumen que pueda guardar:

> "Todo listo. Guarda esto:
>
> **Tu panel:** <la dirección>/panel
> **Tu contraseña:** <la contraseña>
>
> Para cambiar precios, horarios o lo que sea: entra al panel, pestaña
> **Mi negocio**, cambia lo que quieras y dale Guardar. El bot lo aprende al instante.
>
> Si algo se rompe o quieres algo nuevo, ábreme otra vez y dime qué necesitas."

Y guarda en la carpeta del bot un archivo `MI-BOT.md` con esos datos (sin la
contraseña), para que la próxima vez sepas de qué bot se trata.

---

# Otros trabajos (cuando ya tiene el bot)

Cuando el usuario vuelva pidiendo algo, mira aquí primero:

**"Quiero cambiar los precios / el horario"**
→ No toques nada. Dile: "eso lo haces tú en un minuto: entra a tu panel, pestaña
Mi negocio, cámbialo y dale Guardar". Solo hazlo tú si te lo pide expresamente.

**"Conéctalo a WhatsApp"** → `references/02-conectar-whatsapp.md`

**"Mi bot no contesta" / "algo falla"** → `references/03-si-algo-falla.md`

**"Quiero que sea más inteligente"**
→ Es pasarlo de la IA gratis a Claude. Le va a costar como $2 al mes y contesta
notablemente mejor. Pasos: pídele que saque su llave en console.anthropic.com,
guárdala con `npx wrangler secret put ANTHROPIC_API_KEY` (él la pega en la terminal,
no en el chat), cambia `CEREBRO = "claude"` en `wrangler.toml` y `npx wrangler deploy`.
El modelo por defecto es `claude-opus-5`; si quiere gastar menos, cambia
`MODELO_CLAUDE` a `claude-haiku-4-5`.

**"Quiero otro bot para otro negocio"**
→ Carpeta nueva, empezando desde la Fase 1. **Base de datos nueva y nombre nuevo.**
Nunca reutilices la base de datos de otro bot: se le mezclarían los clientes y los
precios de los dos negocios.

**"¿Cómo va mi bot?"**
→ Llévalo al panel. Si quiere el detalle, puedes consultar tú:
`npx wrangler d1 execute <nombre>-datos --remote --command "SELECT COUNT(*) FROM contactos"`

---

# Cosas técnicas que debes saber tú (no el usuario)

- **Probar en tu computador**: `npx wrangler dev` — **sin** `--local`. Con `--local`
  la IA no funciona (el binding de IA necesita conexión con Cloudflare).
- El cerebro gratis es `@cf/meta/llama-3.3-70b-instruct-fp8-fast`, con
  `@cf/meta/llama-3.1-8b-instruct-fp8` de respaldo automático si el primero falla.
- Los datos del negocio viven en la tabla `negocio` de D1, **no en archivos**. Por eso
  el dueño puede cambiarlos sin volver a publicar.
- El bot marca `[CONTACTO]` y `[AVISAR]` al final de sus respuestas; `src/cerebro.js`
  las recorta antes de que el cliente las vea. Si cambias el prompt, no rompas eso.
- Todo mensaje pasa por `atender()` en `src/atender.js`, venga de donde venga. Si
  agregas un canal nuevo, úsalo también: no dupliques esa lógica.
- Límites gratis de Cloudflare: 100.000 mensajes al día y 10.000 respuestas de IA
  diarias. Un negocio normal usa una fracción de eso.
