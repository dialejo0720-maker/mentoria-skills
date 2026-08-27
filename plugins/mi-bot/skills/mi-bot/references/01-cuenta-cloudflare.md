# Crear la cuenta de Cloudflare

Es la única cuenta obligatoria. Es gratis y **no pide tarjeta**.

## Cómo explicárselo

> "Cloudflare es la empresa donde va a vivir tu asistente. Piénsalo como el local
> donde vive tu negocio: la cuenta queda a tu nombre, es gratis, y si algún día
> quieres llevarte todo, es tuyo."

Si pregunta si le van a cobrar: **no**. Este bot usa solo las partes gratuitas.
Cloudflare no pide tarjeta para lo que estamos usando.

## Los pasos

1. > "Abre esto en tu navegador: **https://dash.cloudflare.com/sign-up**"
2. > "Pon tu correo y una contraseña nueva. **Anótala en un papel**, la vas a
   > necesitar después."
3. > "Dale al botón **Sign Up**."
4. > "Ahora revisa tu correo. Te llegó un mensaje de Cloudflare con un botón para
   > confirmar. Tócalo."
   - Si no le llega en dos minutos: que mire en Spam o Promociones.
5. > "Cuando te pregunte qué quieres hacer o te ofrezca planes de pago, sáltatelo.
   > No necesitamos nada de eso."
6. > "Avísame cuando estés adentro y veas tu panel."

**Espera a que confirme.** No corras `wrangler login` antes.

## Conectar la computadora con su cuenta

Avísale primero:

> "Ahora se te va a abrir el navegador solo, con una pantalla de Cloudflare que pide
> permiso. Es para que yo pueda publicar tu bot. Dale al botón azul que dice
> **Allow** (Permitir)."

```bash
npx wrangler login
```

## Si algo sale mal

**No se abre el navegador.** El comando imprime una dirección larga en la terminal.
Cópiala y pásasela para que la abra a mano.

**Se abrió pero con otra cuenta.** Si tiene varias cuentas de Cloudflare, que cierre
sesión en el navegador y lo intenten de nuevo:

```bash
npx wrangler logout
npx wrangler login
```

**Dice que ya está conectado, pero no sabes con cuál cuenta:**

```bash
npx wrangler whoami
```

**Le aparece algo de "verify your email".** No confirmó el correo del paso 4. Que
lo busque y lo confirme antes de seguir.

## Lo que hay que saber de los límites gratis

Por si pregunta cuánto aguanta:

- **100.000 mensajes al día** al bot.
- **10.000 respuestas de IA al día** (unas 300 conversaciones diarias).
- **5 GB** de base de datos: años de conversaciones.

Un negocio pequeño usa una fracción de eso. Si algún día lo supera, es porque le está
yendo muy bien, y ahí sí conviene mirar el plan de $5 al mes.
