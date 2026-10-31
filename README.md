# Skills de la mentoría

Sistemas guiados para Claude Code. Se instalan una vez y quedan disponibles en tu computador.

| Plugin | Skills que trae | Qué hace |
|---|---|---|
| `ecosistema` | `/ecosistema` | Construye de cero el ecosistema completo de un producto digital: competencia → producto → keys → landing → creativos → campañas → producto real → order bumps |
| `producto-digital` | `/oferta-innegable` `/check-oferta` `/vsl` `/digital-product-autopilot` | Arma y afina la oferta: tu mecanismo con nombre propio, el check de la oferta, el VSL con las 8 keys, el copy y la landing |
| `imagenes` | `/claude-banana` | Convierte una idea en un prompt de imagen profesional para Nano Banana / Gemini, y si quieres genera la imagen |
| `video` | `/video-con-vida` `/instalar-pizarra` | 17 efectos para videos hablando a cámara, y los videos animados tipo pizarrón |
| `contenido` | `/guiones` `/carrusel` `/anuncio-ganador` `/hook-generator` | Guiones de reels e historias, carruseles listos para subir, hooks y el método para encontrar tu anuncio ganador |
| `mi-bot` | `/mi-bot` | Arma un bot de WhatsApp con IA para tu negocio, gratis y en tu propia cuenta. Con panel para ver conversaciones y contactos, y para cambiar precios sin tocar código |

**El orden del proceso:** `ecosistema` te lleva de la mano por todo el lanzamiento. Las demás
son las herramientas de cada parte: `producto-digital` para la oferta, `imagenes` y `video`
para los creativos, `contenido` para lo orgánico y los anuncios.

---

## Instalación (la forma recomendada)

Necesitas **Claude Code** instalado. Se descarga en [claude.com/code](https://claude.com/code).

Abre Claude Code y escribe primero esto:

```
/plugin marketplace add dialejo0720-maker/mentoria-skills
```

Y después, los plugins que quieras (puedes instalarlos todos, uno por línea):

```
/plugin install ecosistema@mentoria
/plugin install producto-digital@mentoria
/plugin install imagenes@mentoria
/plugin install video@mentoria
/plugin install contenido@mentoria
/plugin install mi-bot@mentoria
```

Listo. Ya puedes escribir `/ecosistema`, `/vsl`, `/carrusel`… en cualquier proyecto.

> **Videos tipo pizarrón:** después de instalar `video`, escribe `/instalar-pizarra` una vez.
> Baja la skill `video-pizarra` (gratis, de Horizontes IA) y la deja lista para Windows.

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
   Para instalar otra skill, agrégale el nombre (`mi-bot`, `vsl`, `carrusel`, `video-con-vida`…):
   ```
   powershell -ExecutionPolicy Bypass -File .\instalar.ps1 -Skill mi-bot
   ```
4. **Mac / Linux:** abre la terminal en esa carpeta y ejecuta:
   ```
   bash instalar.sh
   ```
   Para otra skill:
   ```
   bash instalar.sh mi-bot
   ```

También puedes copiar a mano la carpeta de la skill dentro de:

- **Windows:** `C:\Users\TU_USUARIO\.claude\skills\`
- **Mac / Linux:** `~/.claude/skills/`

Debe quedar así: `.claude/skills/ecosistema/SKILL.md` (o `.claude/skills/vsl/SKILL.md`, etc.).
Las demás skills están en `plugins/<plugin>/skills/<skill>`. Si no sabes el nombre, corre el
instalador con un nombre cualquiera y te muestra la lista.

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

## Las herramientas del proceso

Cada skill se activa sola cuando pides lo que hace ("revisa mi oferta", "hazme un carrusel"),
o la llamas por su nombre.

### `producto-digital` — la oferta

| Skill | Para qué |
|---|---|
| `/oferta-innegable` | Le pasas tu verbalización (transcripción de tu Zoom o nota de voz) y sale tu oferta completa: persona, problema, oportunidad, beneficio, **mecanismo con nombre propio** y creencia central |
| `/check-oferta` | Revisa una oferta ya escrita: qué sirve, qué arreglar y el arreglo listo para pegar |
| `/vsl` | El guion de tu video de ventas con las 8 keys |
| `/digital-product-autopilot` | Análisis de competidores, copy de alta conversión, estructura de landing y lanzamiento en Hotmart |

### `imagenes` — los creativos

`/claude-banana` convierte "quiero una foto de mi ebook en una mesa" en un prompt profesional
para Nano Banana / Gemini. **Gratis** si pegas el prompt en gemini.google.com. Si quieres que
genere la imagen sola, necesitas una clave de Google AI Studio (aistudio.google.com) con
facturación activa y Python instalado.

### `video` — los videos

| Skill | Para qué |
|---|---|
| `/video-con-vida` | Le pone efectos a un video tuyo hablando a cámara (zoom a la cara, texto detrás de ti, checklist, gráfica que crece… 17 en total) |
| `/instalar-pizarra` | Instala `/video-pizarra`: videos animados tipo pizarrón con mascota, música y voz, sin grabarte |

**Estas necesitan programas instalados** (Claude te dice cuáles faltan y te pasa el enlace):
Python, ffmpeg y Node.js. En Windows, también Git (trae Git Bash). La música con IA (Suno) y la
transcripción precisa (AssemblyAI) son opcionales y de pago aparte.

`video-pizarra` es una skill gratuita de **Horizontes IA**
([github.com/santmun/video-pizarra](https://github.com/santmun/video-pizarra)). No viene copiada
aquí: `/instalar-pizarra` la baja de su repositorio original y le hace los ajustes para Windows.

### `contenido` — lo que vende el producto

| Skill | Para qué |
|---|---|
| `/guiones` | Guiones de reels, TikToks, historias y videos largos: hook de 3 segundos, texto en pantalla, CTA |
| `/carrusel` | Carruseles de Instagram/LinkedIn con tu marca, exportados a PNG listos para subir (usa Chrome o Edge) |
| `/hook-generator` | Ganchos para la primera línea de tus posts y videos |
| `/anuncio-ganador` | El método Recon: matriz 3×3 de versiones de oferta, prueba de fricción con USD 5 por versión, qué apagar y cómo escalar |

---

## Créditos

- `claude-banana` está basada en [claude-banana](https://github.com/Hainrixz/claude-banana)
  (licencia MIT, incluida en su carpeta).
- `video-pizarra` es de Horizontes IA y se instala desde su repositorio original.
- Las reglas de movimiento de `video-con-vida` se basan en las guías de @SantiMunozIA y
  Máquina IA (@ninodirector).

---

## Uso

Material de la mentoría. Uso personal de los alumnos. No redistribuir.
