# Skills de la mentoría

Sistemas guiados para Claude Code. Se instalan una vez y quedan disponibles en tu computador.

| Skill | Qué hace |
|---|---|
| `/ecosistema` | Construye de cero el ecosistema completo de un producto digital: competencia → producto → keys → landing → creativos → campañas → producto real → order bumps |
| `/mi-bot` | Arma un bot de WhatsApp con IA para tu negocio, gratis y en tu propia cuenta. Con panel para ver conversaciones y contactos, y para cambiar precios sin tocar código |

---

## Instalación (la forma recomendada)

Necesitas **Claude Code** instalado. Se descarga en [claude.com/code](https://claude.com/code).

Abre Claude Code y escribe primero esto:

```
/plugin marketplace add dialejo0720-maker/mentoria-skills
```

Y después, la skill que quieras (puedes instalar las dos):

```
/plugin install ecosistema@mentoria
```

```
/plugin install mi-bot@mentoria
```

Listo. Ya puedes escribir `/ecosistema` o `/mi-bot` en cualquier proyecto.

> Si te pregunta si confías en el marketplace, acepta.
> Después de instalar, cierra Claude Code y vuélvelo a abrir.

### Para actualizar

Cuando salga una versión nueva:

```
/plugin marketplace update mentoria
```

```
/plugin update ecosistema@mentoria
```

### Para desinstalar

```
/plugin uninstall ecosistema@mentoria
```

---

## Instalación manual (si no quieres usar plugins)

1. Descarga el repositorio: botón verde **Code** → **Download ZIP**
2. Descomprime
3. **Windows:** clic derecho en `instalar.ps1` → *Ejecutar con PowerShell*
   Si Windows lo bloquea, abre PowerShell en esa carpeta y ejecuta:
   ```
   powershell -ExecutionPolicy Bypass -File .\instalar.ps1
   ```
   Para instalar la otra skill, agrégale el nombre:
   ```
   powershell -ExecutionPolicy Bypass -File .\instalar.ps1 -Skill mi-bot
   ```
4. **Mac / Linux:** abre la terminal en esa carpeta y ejecuta:
   ```
   bash instalar.sh
   ```
   Para la otra skill:
   ```
   bash instalar.sh mi-bot
   ```

También puedes copiar a mano la carpeta de la skill dentro de:

- **Windows:** `C:\Users\TU_USUARIO\.claude\skills\`
- **Mac / Linux:** `~/.claude/skills/`

Debe quedar así: `.claude/skills/ecosistema/SKILL.md` (o `.claude/skills/mi-bot/SKILL.md`).
La carpeta de `/mi-bot` está en `plugins/mi-bot/skills/mi-bot`.

---

## Cómo se usa `/ecosistema`

1. Crea una carpeta para tu proyecto y ábrela con Claude Code
2. Escribe `/ecosistema`
3. Claude te hace **una pregunta a la vez**. Contestas y avanzas.

Cada fase deja un archivo en tu carpeta. Si cierras y vuelves días después, escribe
`/ecosistema` otra vez: lee el tablero `ecosistema.md` y retoma donde quedaste.

### Las 10 fases

| Fase | Qué sale de ahí |
|---|---|
| F0 · Encuadre | Tu nicho, países, presupuesto y activos, en un tablero |
| F1 · Espionaje | Reporte de competidores, anuncios ganadores diseccionados, el GAP |
| F2 · Producto | 5 ideas rankeadas y tu método bautizado (el 20% que te diferencia) |
| F3 · Keys + oferta | Las 8 decisiones que alimentan todo lo demás, más precio y garantía |
| F4 · Landing | El `index.html` completo, listo para subir |
| F5 · Creativos | 9 anuncios con sus prompts de imagen y video, y el copy |
| F6 · Campañas | La estructura de Meta: primero CBO, después ABO, para 6 países de LATAM |
| F7 · Producto real | El ebook, el audiolibro y los bonos, escritos y subidos a Hotmart |
| F8 · Bumps y upsells | Las ofertas que suben lo que ganas por cada venta |
| F9 · Iteración | El ritmo semanal para que el producto no muera |

**La regla que gobierna todo:** 80% modelado de lo que ya está facturando, 20% de innovación
concentrada en tu método con nombre propio.

---

## Lo que te van a pedir — consíguelo antes de empezar

El 90% de la calidad del resultado depende de esto:

- 3 a 5 competidores del nicho
- Capturas de sus anuncios activos en la Biblioteca de Anuncios de Meta
- Los 3 anuncios **más antiguos** de cada uno (esos son los rentables)
- Las imágenes y videos de esos anuncios
- La landing del competidor (el link, o el texto copiado)
- Lo que se pueda ver del producto: índice, muestra gratis, capturas
- El precio y cómo cobra

Si no sabes cómo conseguir algo, pregúntale a Claude dentro de la skill: te guía clic a clic.

---

## Preguntas frecuentes

**¿Necesito saber programar?** No. Ni una línea.

**¿Necesito pagar algo aparte?** No. La skill no usa API keys ni servicios externos.

**¿Sirve para cualquier nicho?** Sí, mientras haya competidores facturando. Si no los hay,
la skill te lo dice y te recomienda cambiar de nicho antes de que gastes dinero.

**¿Funciona fuera de LATAM?** Sí. Viene calibrada para español y seis países (Colombia,
Chile, Perú, Ecuador, México, Panamá), pero le dices que trabajas en otro mercado y se adapta.

**¿Y si no vendo en Hotmart?** Dilo al principio y adapta los pasos de checkout y entrega.

**¿Genera las imágenes y los videos?** Genera los **prompts** listos para pegar en Nano
Banana / Gemini (imágenes) y Veo, Sora o Kling (video), construidos a partir de los anuncios
que ya le funcionan a tu competencia.

**¿Puedo saltarme fases?** Puedes, pero te dice el riesgo primero y lo deja anotado.

---

## Cómo se usa `/mi-bot`

1. Crea una carpeta para tu bot y ábrela con Claude Code
2. Escribe `/mi-bot`
3. Claude te va a preguntar por tu negocio, **una cosa a la vez**, y él hace todo lo demás

En media hora tienes tu asistente contestando. No necesitas saber programar ni escribir
un solo comando.

### Lo que hace tu bot

- Le contesta a tus clientes por WhatsApp con la información **real** de tu negocio
- **Nunca inventa** precios ni horarios: si no lo sabe, ofrece pasarle el mensaje a un humano
- Apunta a la gente interesada, con su nombre, teléfono y qué quería
- Te avisa cuando alguien quiere hablar con una persona de verdad

### Tu panel

Entras desde tu celular o tu computador, con una contraseña:

| Pestaña | Para qué |
|---|---|
| Inicio | Cuánta gente te escribió, cuántos contactos nuevos |
| Conversaciones | Los chats completos. Puedes tomar el control y contestar tú |
| Contactos | La gente interesada, con botón para escribirle. Se descarga a Excel |
| Mi negocio | Cambias precios, horarios y reglas. **El bot lo aprende al instante** |
| Probar el bot | Le escribes como si fueras un cliente, para ver qué contesta |
| Conexiones | Qué está conectado y la línea para poner el chat en tu página web |

### Lo que cuesta

**Nada.** Ni tarjeta de crédito. El bot vive en tu propia cuenta gratis de Cloudflare
y usa la IA que Cloudflare regala (aguanta unas 300 conversaciones al día).

Si algún día quieres que conteste mejor, se le puede poner el cerebro de Claude por
unos 2 dólares al mes. Es opcional y se cambia en un minuto.

### Preguntas frecuentes

**¿Necesito una cuenta de WhatsApp Business?** Para probarlo no. Meta regala un número
de prueba con el que ves tu bot funcionando el mismo día. Tu número real se conecta después.

**¿Pierdo mi WhatsApp actual?** Un número que ya está en WhatsApp no se puede usar para
el bot sin borrar esa cuenta. Por eso lo más tranquilo es un chip nuevo solo para el bot.

**¿El bot puede inventarse cosas?** Está instruido para no hacerlo, y si no sabe algo
ofrece pasar el mensaje. Si aun así se equivoca, casi siempre es que falta ese dato en
la pestaña Mi negocio.

**¿Puedo cambiar los precios sin llamar a nadie?** Sí, esa es la idea. Entras al panel,
pestaña Mi negocio, cambias y guardas.

**¿Puedo tener un bot para cada negocio?** Sí. Carpeta nueva y `/mi-bot` otra vez.

---

## Uso

Material de la mentoría. Uso personal de los alumnos. No redistribuir.
