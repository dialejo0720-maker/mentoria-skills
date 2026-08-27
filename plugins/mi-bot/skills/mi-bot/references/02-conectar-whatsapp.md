# Conectar el bot a WhatsApp

Esta es la parte más pesada de todas. Meta pide varios pasos y la pantalla cambia
cada tanto. **Tómalo con calma y no adelantes pasos.**

## Antes de empezar, avísale de esto

> "Vamos a conectar tu WhatsApp. Son unos 20 minutos y hay que dar varios clics en
> la página de Facebook para desarrolladores. Yo te voy diciendo exactamente dónde
> tocar. Si en algún momento no ves lo que te digo, mándame una foto de la pantalla
> y te ubico.
>
> Vamos a empezar con un **número de prueba que regala Meta**, para que veas tu bot
> contestando hoy mismo sin trámites. Después, cuando lo veas funcionando, ponemos
> tu número real."

Ese orden importa: número de prueba primero, número real después. Si empiezas por el
número real, se topa con la verificación del negocio y abandona.

---

## Parte 1 — La cuenta de desarrollador

1. > "Entra a https://developers.facebook.com y toca **Iniciar sesión** con tu
   > Facebook de siempre."
2. > "Arriba a la derecha busca **Mis aplicaciones** y tócalo."
3. Si le pide registrarse como desarrollador: que acepte, ponga su teléfono y confirme
   el código que le llega. Es gratis.

## Parte 2 — Crear la aplicación

4. > "Toca el botón verde **Crear aplicación**."
5. > "Te pregunta qué quieres hacer. Elige la opción que dice algo como
   > **Otro** y luego **Empresa** (o *Business*). Dale Siguiente."
6. > "Ponle un nombre. Puede ser el de tu negocio. Y dale **Crear aplicación**.
   > Te va a pedir tu contraseña de Facebook."

## Parte 3 — Agregar WhatsApp

7. > "Ahora te aparece una lista de productos. Busca **WhatsApp** y toca **Configurar**."
8. Si le pide crear o elegir una cuenta de empresa, que cree una nueva con el nombre
   de su negocio.

Al terminar cae en la pantalla de **Configuración de la API** (*API Setup*). **Esa es
la pantalla donde vive todo lo importante.** Dile que no la cierre.

## Parte 4 — Los tres datos que necesitas

En esa pantalla hay tres cosas. Pídeselas **de una en una**, nunca las tres juntas.

**a) El token temporal.** Arriba dice *Token de acceso temporal* con un botón de copiar.

> "¿Ves donde dice **Token de acceso temporal**? Toca el botón de copiar que está al
> lado. Ahora pégalo en tu terminal cuando te lo pida — no me lo mandes por el chat."

Corre y que él lo pegue (no se ve mientras escribe, eso es normal — avísale):

```bash
npx wrangler secret put WHATSAPP_TOKEN
```

> Ese token **se vence en 24 horas**. Es solo para probar hoy. En la Parte 7 lo
> cambiamos por uno que no se vence.

**b) El identificador del número.** Más abajo dice *Identificador del número de
teléfono* (*Phone number ID*): un número largo.

> "Debajo busca **Identificador del número de teléfono**. Cópialo y pásamelo por
> el chat, ese sí no es secreto."

```bash
echo "EL-NUMERO-QUE-TE-DIO" | npx wrangler secret put WHATSAPP_PHONE_ID
```

**c) Su celular en la lista de pruebas.** En la misma pantalla, en *Para*
(*To*), hay un menú para agregar números.

> "Donde dice **Para**, abre el menú y toca **Administrar lista de números**.
> Agrega tu propio celular con el código de tu país. Te va a llegar un código por
> WhatsApp para confirmarlo."

Esto es obligatorio: el número de prueba de Meta **solo puede escribirle a números
que estén en esa lista** (hasta 5).

## Parte 5 — Conectar el webhook

Ahora inventa tú una palabra secreta (cualquier cosa, ej. `pan-caliente-2026`) y guárdala:

```bash
echo "pan-caliente-2026" | npx wrangler secret put WHATSAPP_VERIFICAR
npx wrangler deploy
```

**El deploy es obligatorio aquí**: sin él, Meta no va a poder verificar nada.

Luego:

9. > "En el menú de la izquierda busca **Configuración** (debajo de WhatsApp).
   > Vas a ver un cuadro que dice **Webhook** y un botón **Editar**. Tócalo."
10. Se abre una ventana con dos casillas. Dale los valores exactos:
    - **URL de devolución de llamada**: `https://TU-BOT.workers.dev/whatsapp`
    - **Token de verificación**: `pan-caliente-2026`
11. > "Dale **Verificar y guardar**."

Si dice que falló: revisa que hiciste el deploy después de guardar la palabra secreta,
que la dirección termine exactamente en `/whatsapp`, y que la palabra sea idéntica.

12. > "Ahora, en ese mismo cuadro, toca **Administrar**. Te sale una lista larga.
    > Busca el renglón que dice **messages** y marca la casilla **Suscribirse**."

**Ese paso se olvida siempre y sin él no llega ningún mensaje.** Verifícalo.

## Parte 6 — Probar

> "Listo. Agarra tu celular y escríbele al número de prueba que aparece en la pantalla
> de Meta (donde dice **De**). Mándale un 'hola'."

Debería contestar en unos segundos. Si no:

```bash
npx wrangler tail
```

Deja eso corriendo, que mande otro mensaje y mira qué aparece. Si no aparece **nada**,
el problema es la suscripción a *messages* del paso 12.

Cuando conteste, celebra. Y muéstrale que la conversación ya aparece en su panel,
en **Conversaciones**.

## Parte 7 — El token que no se vence

El token de la Parte 4 se muere en 24 horas. Para que el bot siga vivo:

13. > "Entra a https://business.facebook.com/settings"
14. > "En el menú de la izquierda busca **Usuarios** y dentro **Usuarios del sistema**."
15. > "Toca **Agregar**, ponle de nombre 'bot' y en el rol elige **Administrador**."
16. > "Con ese usuario seleccionado, toca **Agregar activos**, elige tu aplicación y
    > dale control total."
17. > "Ahora toca **Generar nuevo token**, elige tu aplicación, en caducidad elige
    > **Nunca**, y marca los permisos `whatsapp_business_messaging` y
    > `whatsapp_business_management`."
18. > "Copia ese token. Ese sí guárdalo bien, no lo vuelves a ver."

```bash
npx wrangler secret put WHATSAPP_TOKEN
```

(él lo pega en la terminal)

## Parte 8 — Su número real

Solo cuando ya lo vio funcionando. En la pantalla de *Configuración de la API* hay un
botón **Agregar número de teléfono**. Requisitos que debes advertirle **antes**:

- El número **no puede estar registrado en WhatsApp** (ni normal ni Business). Si lo
  está, hay que borrar esa cuenta primero, y **se pierden los chats de ese número**.
- Por eso mucha gente prefiere **comprar un chip nuevo** solo para el bot. Suele ser
  la opción más tranquila; propónsela.
- Meta le va a pedir verificar su negocio para levantar los límites de envío. Con
  pocos mensajes al día puede vivir sin eso un buen rato.

---

## Notas para ti (no para el usuario)

- El código del canal está en `src/whatsapp.js`. Llama a
  `https://graph.facebook.com/<PHONE_ID>/messages` **sin número de versión**, a
  propósito: así Meta usa la versión estable de la app y no se rompe cuando
  deprecan versiones viejas.
- El webhook responde `200` de inmediato y contesta aparte con `ctx.waitUntil`. Si
  tardara en responder, Meta reenvía el mismo mensaje una y otra vez.
- Los reenvíos se filtran con la tabla `vistos` (el id del mensaje de Meta).
- Solo se atienden mensajes de texto. Audios, fotos y stickers se ignoran en silencio.
- La ventana de 24 horas de Meta: fuera de ella solo se puede escribir con plantillas
  aprobadas. Como el bot solo **responde**, no le afecta. Pero si el dueño contesta
  desde el panel un día después, va a fallar — explícaselo si pasa.
