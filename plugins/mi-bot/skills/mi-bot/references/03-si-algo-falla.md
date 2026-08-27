# Si algo falla

Primera regla: **no le muestres errores en inglés al usuario.** Tradúcelos a qué pasó
y qué vas a hacer.

Segunda regla: la herramienta que resuelve el 80% de los casos es ver los mensajes
del bot en vivo. Déjala corriendo y pide que mande un mensaje de prueba:

```bash
npx wrangler tail
```

---

## "Mi bot no contesta en WhatsApp"

Descarta en este orden:

**1. ¿Contesta en el panel?** Que entre a **Probar el bot** y le escriba.
- Si ahí SÍ contesta → el problema es la conexión con WhatsApp, sigue al punto 2.
- Si ahí TAMPOCO contesta → el problema es el cerebro, salta a "El bot no responde nada".

**2. ¿Llegan los mensajes?** Con `npx wrangler tail` corriendo, que le escriba al bot.
- Si no aparece **nada**: Meta no está mandando los mensajes. Casi siempre es que
  falta suscribir el campo **messages** (Parte 5, paso 12 de la guía de WhatsApp).
- Si aparece un error de envío: sigue al punto 3.

**3. ¿Se venció el token?** El token temporal de Meta dura **24 horas**. Es la causa
número uno de "ayer funcionaba y hoy no". Solución: el token permanente
(Parte 7 de la guía de WhatsApp).

**4. ¿El número está en la lista?** Con el número de prueba de Meta, el bot solo puede
escribirle a los números registrados en la lista de pruebas (máximo 5).

---

## "El bot no responde nada" (tampoco en el panel)

```bash
npx wrangler tail
```

**Si dice `Binding IA needs to be run remotely`:** estás corriendo `wrangler dev --local`.
Quita el `--local`. En el bot publicado esto no pasa.

**Si dice algo de `D1` o `no such table`:** faltó crear las tablas.

```bash
npx wrangler d1 execute <nombre>-datos --remote --file=./esquema.sql
```

**Si dice `capacity` o `429`:** la IA gratis está saturada en ese momento. El bot ya
reintenta solo con el modelo de respaldo. Si pasa seguido, es momento de proponerle
pasar a Claude (~$2 al mes).

**Si no dice nada de nada:** revisa que la dirección sea la correcta y que el deploy
haya salido bien (`npx wrangler deploy` otra vez).

---

## "Se inventó un precio" / "dijo algo que no es"

No es una falla del programa: es que **le falta el dato**.

1. Entra al panel → **Mi negocio**.
2. Mira si esa información está escrita ahí. Casi siempre falta o está vaga.
3. Escríbela clara y guarda.
4. Vuelve a probar la misma pregunta.

Si el dato SÍ estaba y aun así lo inventó, es el modelo gratis quedándose corto.
Dos opciones, en este orden:
- Escribe el dato de forma más directa en **Mi negocio** (funciona la mayoría de veces).
- Súbelo a Claude (`CEREBRO = "claude"`): la diferencia es notoria.

Refuerzo útil en el campo **Lo que el bot NO debe hacer**:
> "Si no estás seguro de un precio, NO lo digas. Ofrece pasar el mensaje al dueño."

---

## "No puedo entrar al panel"

- **Dice que la contraseña no es:** revisa que la guardaste bien.
  Vuelve a ponerla y publica de nuevo:
  ```bash
  echo "NUEVA-CONTRASEÑA" | npx wrangler secret put CLAVE_PANEL
  npx wrangler deploy
  ```
- **La página no carga:** revisa que la dirección termine en `/panel`.
- **Le pide la contraseña una y otra vez:** está entrando por `http` en vez de
  `https`. La sesión solo viaja por conexión segura.

---

## "Quedó contestando cosas raras / se volvió loco"

Casi siempre es que se acumuló un historial confuso en un chat de prueba. Borra esa
conversación puntual:

```bash
npx wrangler d1 execute <nombre>-datos --remote --command "DELETE FROM mensajes WHERE conversacion_id IN (SELECT id FROM conversaciones WHERE canal='prueba')"
```

---

## Revisión general del bot

Cuando no sabes por dónde empezar:

```bash
# ¿Está vivo?
curl -s -o /dev/null -w "%{http_code}\n" https://TU-BOT.workers.dev/

# ¿Tiene los datos del negocio?
npx wrangler d1 execute <nombre>-datos --remote --command "SELECT clave, length(valor) FROM negocio"

# ¿Están todos los secretos?
npx wrangler secret list

# ¿Cuánta actividad ha tenido?
npx wrangler d1 execute <nombre>-datos --remote --command "SELECT canal, COUNT(*) FROM conversaciones GROUP BY canal"
```

`wrangler secret list` debe mostrar como mínimo `CLAVE_PANEL`. Con WhatsApp conectado,
también `WHATSAPP_TOKEN`, `WHATSAPP_PHONE_ID` y `WHATSAPP_VERIFICAR`.

---

## Volver a publicar (arregla más de lo que parece)

Si tocaste `wrangler.toml`, cambiaste un secreto o algo quedó raro:

```bash
npx wrangler deploy
```

Los datos del negocio y las conversaciones **no se pierden**: viven en la base de
datos, no en el código.
