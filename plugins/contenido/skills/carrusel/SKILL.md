---
name: carrusel
description: Crea carruseles de Instagram/LinkedIn listos para publicar — arco narrativo, copy con hook y CTA, slides en HTML/CSS con la marca exacta, y exportación a PNG 1080px con Chrome headless. Enfocado en infoproductos. Actívala cuando el usuario quiera "hacer un carrusel", "post de varias slides", "carrusel para Instagram", "slides para LinkedIn", "convertir esto en carrusel", o mencione carrusel, swipe post, slides, o post de 8 imágenes.
---

# Carrusel — de idea a PNGs listos para publicar

Produces carruseles completos: el copy, el diseño y los archivos exportados. El usuario
publica; tú haces todo lo demás. Idioma por defecto: **español LATAM neutro**.

## Regla de oro

**Un carrusel no es un post con más imágenes: es una historia con fricción.** Cada slide
existe para que el dedo siga deslizando. Si una slide no crea una pregunta abierta que la
siguiente responde, esa slide sobra.

## Flujo

### 1. Resolver marca (nunca preguntes lo que puedes leer)

Busca en este orden y usa el primero que exista:

1. `brand-profile.json` en el directorio actual — formato de claude-ads (`/ads dna`)
2. `~/.carrusel/marcas/*.json` — perfiles guardados por esta skill
3. Si no hay ninguno: pregunta **solo** nombre, color de acento y tipografía preferida
   (una pregunta por mensaje), y guarda el perfil en `~/.carrusel/marcas/<slug>.json`

Estructura mínima del perfil:

```json
{
  "nombre": "Mi Marca",
  "colores": { "fondo": "#0d0d12", "texto": "#ffffff", "acento": "#e94560", "sutil": "#8a8a99" },
  "fuentes": { "titulo": "Poppins", "cuerpo": "Inter" },
  "tono": "directo, sin relleno, tutea al lector",
  "handle": "@mimarca"
}
```

Si existe `campaign-brief.md` de claude-ads en el directorio, léelo: ya tiene ángulos y
copy validados. No reinventes el mensaje.

### 2. Elegir arco narrativo

Lee `references/arcos.md` y elige el arco según la intención. Para infoproductos el
default es **Dolor → Mecanismo → Prueba → Oferta**. No inventes arcos nuevos sin razón.

Longitud: **8 slides** salvo que el usuario pida otra cosa. Máximo 10 (límite de Instagram).

### 3. Escribir el copy ANTES de tocar diseño

Escribe el guion completo en texto plano y muéstraselo al usuario en una sola tanda:

```
S1 HOOK    → "El 90% de los cursos online no fracasan por el contenido."
S2 GIRO    → "Fracasan porque nadie llega al día 3."
...
S8 CTA     → "Guarda esto. Lo vas a necesitar cuando lances."
```

Reglas de copy:

- **Hook (S1): máximo 8 palabras.** Si necesita 12, no es un hook, es un resumen.
- Una idea por slide. Si necesita dos, son dos slides.
- Sin relleno corporativo: nada de "en el mundo actual", "hoy en día", "es importante destacar".
- Cierra cada slide con tensión abierta, no con conclusión.
- CTA final concreto: *guardar*, *comentar una palabra*, *link en bio*. Nunca "espero que te sirva".

Espera aprobación del copy antes de diseñar. Cambiar texto es barato; re-renderizar no.

### 4. Generar el HTML de cada slide

Usa las plantillas de `references/plantillas.md`. Contrato de render:

- Cada slide es un archivo HTML completo e independiente
- Dimensiones exactas: **1080×1350** (4:5, default) · 1080×1080 (1:1) · 1080×1920 (9:16)
- Tokens de marca como variables CSS en `:root` — nunca colores hardcodeados
- Padding mínimo **80px** por lado; contenido crítico dentro del **80% central**
  (Instagram recorta al centro 1:1 en la cuadrícula del perfil)
- Fuentes de Google Fonts vía `<link>`; el renderer espera a que carguen
- **Sin `<script>`.** Nada de JS, ni animaciones, ni `fetch`
- Varía el layout entre slides. Ocho slides con la misma composición se leen como plantilla barata

Guarda en `<carpeta-del-carrusel>/html/01.html` … `08.html`.

### 5. Fondos con IA — solo cuando aportan

Por defecto los fondos son CSS (gradientes, ruido, formas). Genera imagen con Higgsfield
(`generate_image`, 1080×1350) **solo** en estos casos:

- La slide de hook, para frenar el scroll con textura o escena real
- Una slide de "transformación" donde la foto ES el mensaje
- El usuario lo pide

Presupuesto sano: **1–2 imágenes por carrusel**, no ocho. Guarda en `assets/` y referencia
con ruta relativa. El texto siempre va en HTML encima — nunca dentro de la imagen generada.

Si generas fondo, pide siempre un `overlay` oscuro o claro en CSS para garantizar contraste
de texto ≥ 4.5:1.

### 6. Renderizar a PNG

```bash
node <carpeta base de esta skill>/scripts/render.mjs <carpeta-del-carrusel> --ratio 4:5
```

Usa Chrome o Edge ya instalados — no descarga nada. Escribe `png/01.png` … `08.png`.
Si un PNG sale con tipografía de sistema en vez de la de marca, sube `--wait` a 8000.

### 7. Entregar

Muestra al usuario:

1. La ruta de la carpeta con los PNG numerados (listos para arrastrar a Instagram)
2. Un preview navegable: publica los slides como Artifact (carga antes la skill `artifact-design`)
3. El caption con hashtags — pídelo a la skill `guiones` si necesitas la biblioteca completa

Estructura final:

```
<carpeta>/
├── guion.md          ← copy aprobado, slide por slide
├── html/             ← 01.html … 08.html
├── assets/           ← fondos IA, logo
├── png/              ← 01.png … 08.png  ← esto es lo que publica
└── caption.md        ← caption + hashtags
```

## Ubicación de salida

Si el usuario no dice dónde, usa `~/Carruseles/<slug-del-tema>-<YYYY-MM-DD>/`.
Nunca escribas PNGs sueltos en el escritorio ni en el directorio de trabajo.

## Iteración

Cuando pidan cambios ("la 3 más simple", "cambia el acento a azul"):

1. Edita solo el HTML afectado
2. Re-renderiza **solo** esa slide: `node scripts/render.mjs <carpeta> --solo 03`
3. No regeneres el carrusel entero por un ajuste

## Encadena con

- **`/ads dna`** (claude-ads) → genera `brand-profile.json` si la marca no tiene perfil
- **`digital-product-autopilot`** → frameworks de oferta y copy si el carrusel vende un infoproducto
- **`guiones`** → convierte el mismo ángulo en reel o historia; reciclar el arco multiplica alcance

## Errores que no debes cometer

- Renderizar antes de aprobar el copy
- Texto por debajo de 24px (ilegible en móvil)
- Contraste bajo por poner texto sobre foto sin overlay
- Última slide sin CTA accionable
- Ocho slides con el mismo layout
- Meter el logo enorme en la slide 1: el hook manda, la marca va en la última
