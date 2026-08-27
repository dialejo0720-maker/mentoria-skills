# F4 · Landing page en HTML

Escribes tú el HTML completo: un solo archivo, CSS embebido, sin librerías, sin frameworks,
sin build. La persona lo sube y ya está vendiendo. Plantilla base en `plantillas/landing.html`.

**Antes de escribir, pide la landing del competidor.** Se modela el esqueleto y las
longitudes (80%); el copy se escribe desde las keys (20% + voz propia). Nunca se copia texto.

---

## Los 14 bloques

Orden fijo. Cada bloque con su key dueña (ver mapa en `03-keys.md`):

| # | Bloque | Qué contiene | Longitud |
|---|---|---|---|
| 1 | Barra de urgencia | Fija arriba. Promesa corta + precio + "hoy" | 1 línea |
| 2 | Hero | Pre-headline · headline (KEY 1) · subheadline (KEY 7) · imagen · CTA · garantía | 1 pantalla |
| 3 | Agitación | La escena del problema, narrada. 3 señales reconocibles | 300–500 pal |
| 4 | Giro | La pregunta paradójica (KEY 2) y su respuesta | 150–250 pal |
| 5 | Mecanismo del problema | KEY 4 con su nombre propio, explicado | 300–400 pal |
| 6 | Testimonios A | 2 testimonios que validan el mecanismo | |
| 7 | Por qué falló todo lo demás | KEY 6, la causa raíz reposicionada | 200–300 pal |
| 8 | El Método | KEY 5 con los pasos numerados y su nombre propio | 400–600 pal |
| 9 | Qué incluye | Stack de valor con mockups + tabla valor ancla vs precio | |
| 10 | Testimonios B | 3 testimonios. Al menos 1 del sub-avatar ampliado | |
| 11 | Para quién sí / para quién no | Dos listas. Filtra y precalifica | |
| 12 | Garantía | Sello visual grande + condiciones exactas | 100 pal |
| 13 | FAQ | 5–6 preguntas. La primera es la objeción principal | |
| 14 | CTA final | Bloque oscuro: recap de la oferta + precio + botón + medios de pago | |

### Reglas de escritura

- **Móvil primero.** El 85% del tráfico de Meta en LATAM es móvil. Párrafos de 2–3 líneas
  máximo. Nada de bloques de texto densos.
- **Un CTA cada 2 bloques.** Mínimo 5 botones en toda la página. Todos al mismo checkout.
- **El precio aparece por primera vez donde lo pone el competidor.** Si el nicho lo pone
  arriba, arriba. Si lo esconde hasta el bloque 9, igual.
- **Especificidad sobre adjetivos.** "El tercer día me contó lo del recreo" convierte más que
  "cambió nuestra relación".
- **Sin jerga de España** si el mercado es LATAM. Tuteo, nunca "vosotros".

### Testimonios

Solo testimonios **reales**. Si no hay todavía, hay tres caminos honestos, en este orden:

1. Regalar el producto a 10 personas del avatar a cambio de una opinión honesta (2–3 días)
2. Usar testimonios sobre el *método* si viene de la práctica de un profesional real
3. Publicar la v1 sin testimonios y sustituir ese bloque por "cómo funciona por dentro"
   (capturas del producto, índice, muestra de una página)

Nunca inventarlos. Formato del testimonio que convierte:

```
★★★★★
"[micro-victoria específica] en [tiempo exacto]. [detalle humano que lo hace creíble]"
— Nombre, Ciudad
```

Micro-victorias creíbles > transformaciones dramáticas. "Me habló del recreo" gana a "cambió
mi vida".

---

## Reglas técnicas del HTML

Obligatorias, sin excepción:

- **Un solo archivo** `index.html` con `<style>` embebido. Cero dependencias externas de JS.
- **Peso total < 500 KB** con imágenes. Imágenes en `.webp`, ancho máximo 1200px,
  `loading="lazy"` en todas menos la del hero.
- **Fuentes del sistema** por defecto (`system-ui, -apple-system, Segoe UI, Roboto`). Si se
  usa Google Fonts, máximo una familia y dos pesos.
- **`<meta name="viewport" content="width=device-width, initial-scale=1">`** — sin esto no
  hay móvil.
- **Contenedor de 640px máximo** centrado. Padding lateral de 20px.
- **Tamaño de fuente base 17–18px** en móvil. El cuerpo nunca por debajo de 16px.
- **Botones de 56px de alto mínimo**, ancho completo en móvil, texto en verbo primera persona
  ("Quiero mi acceso ahora").
- **FAQ con `<details>/<summary>` nativo.** Nada de JS para un acordeón.
- **Barra fija con `position:sticky`** arriba.
- `<title>` y `<meta name="description">` con la promesa. Y `og:image` para cuando se comparta.

### Paleta por nicho

| Nicho | Fondo | Primario (botones) | Texto |
|---|---|---|---|
| Crianza / familia | `#FFFFFF` | `#E84A1F` | `#2D2D2D` |
| Salud / bienestar | `#FFFFFF` | `#2A9D5C` | `#333333` |
| Dinero / negocios | `#0A0A0A` | `#F0B429` | `#E8E8E8` |
| Relaciones / psicología | `#FAF8F5` | `#7B5EA7` | `#2D2D2D` |
| Fitness | `#111111` | `#FF4444` | `#EDEDED` |

Un solo color primario. Todo lo demás en neutros. Dos colores primarios en una landing de
venta directa es ruido.

---

## Checkout de Hotmart

```html
<a class="cta" href="https://pay.hotmart.com/XXXXXXX?checkoutMode=10">
  Quiero mi acceso ahora
</a>
```

- El link se saca de Hotmart → Producto → Enlaces de pago.
- `checkoutMode=10` abre el checkout de una sola página, que convierte mejor en móvil.
- Todos los botones apuntan al **mismo** link. Un solo destino.
- Si hay order bump (F8), se configura dentro de Hotmart, no en la landing.

---

## Píxel de Meta

Sin esto no hay campaña. Va en el `<head>`, antes de cerrar:

```html
<!-- Meta Pixel -->
<script>
!function(f,b,e,v,n,t,s){/* código estándar del píxel */}(window,document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', 'TU_PIXEL_ID');
fbq('track', 'PageView');
</script>
```

Y en cada botón de compra:

```html
<a class="cta" href="..." onclick="fbq('track','InitiateCheckout');">…</a>
```

El evento `Purchase` **no** se dispara en la landing: lo dispara Hotmart. Hay que conectar el
píxel dentro de Hotmart:

```
Hotmart → Herramientas → Píxeles de seguimiento → Facebook Pixel
  · Pegar el ID del píxel
  · Activar API de Conversiones (pide el token de acceso desde Meta Events Manager)
  · Marcar el evento Purchase
```

Verificación antes de encender campañas: instalar la extensión **Meta Pixel Helper** en
Chrome, abrir la landing y confirmar `PageView`; hacer clic en el botón y confirmar
`InitiateCheckout`; hacer una **compra real de prueba** y confirmar `Purchase` en el
Administrador de Eventos. Sin ese `Purchase` real verificado, no se lanza.

---

## Publicación

Opción más rápida y gratis: **Vercel**.

```
1. Entrar a vercel.com y crear cuenta
2. Add New → Project → Deploy sin Git → arrastrar la carpeta landing/
3. Queda en algo.vercel.app en 30 segundos
4. Settings → Domains → agregar el dominio propio
5. En el registrador del dominio, apuntar los DNS a Vercel (Vercel muestra los valores)
```

Alternativas: Netlify Drop (igual de simple), Hostinger (si ya paga hosting), Cloudflare Pages.

Dominio: `.com` corto con el nombre del método o de la promesa. Comprarlo en Namecheap,
Hostinger o Cloudflare. USD 10–15 al año.

---

## Checklist antes de publicar

- [ ] Se abre en un móvil real y se lee sin hacer zoom
- [ ] Todos los botones llegan al checkout correcto
- [ ] El precio de la landing es idéntico al de Hotmart
- [ ] Píxel verificado con Pixel Helper: `PageView` e `InitiateCheckout`
- [ ] `Purchase` verificado con compra de prueba
- [ ] La garantía aparece en 3 sitios
- [ ] Carga en menos de 3 segundos con datos móviles
- [ ] Ortografía revisada — un error tipográfico en el hero cuesta conversión
- [ ] `og:image` puesta (se ve al compartir por WhatsApp)

---

## Compuerta F4 → F5

- [ ] 14 bloques presentes y mapeados a sus keys
- [ ] Publicada en dominio propio
- [ ] Checkout y píxel verificados
- [ ] Probada en móvil real
