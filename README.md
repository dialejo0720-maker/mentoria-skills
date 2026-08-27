# Skills de la mentoría

Sistemas guiados para Claude Code. Se instalan una vez y quedan disponibles en tu computador.

| Skill | Qué hace |
|---|---|
| `/ecosistema` | Construye de cero el ecosistema completo de un producto digital: competencia → producto → keys → landing → creativos → campañas → producto real → order bumps |

---

## Instalación (la forma recomendada)

Necesitas **Claude Code** instalado. Se descarga en [claude.com/code](https://claude.com/code).

Abre Claude Code y escribe estos dos comandos, uno después del otro:

```
/plugin marketplace add dialejo0720-maker/mentoria-skills
```

```
/plugin install ecosistema@mentoria
```

Listo. Ya puedes escribir `/ecosistema` en cualquier proyecto.

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
4. **Mac / Linux:** abre la terminal en esa carpeta y ejecuta:
   ```
   bash instalar.sh
   ```

También puedes copiar a mano la carpeta `skills/ecosistema` dentro de:

- **Windows:** `C:\Users\TU_USUARIO\.claude\skills\`
- **Mac / Linux:** `~/.claude/skills/`

Debe quedar así: `.claude/skills/ecosistema/SKILL.md`

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

## Uso

Material de la mentoría. Uso personal de los alumnos. No redistribuir.
