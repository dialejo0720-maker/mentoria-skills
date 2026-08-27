# F1 · Espionaje

Objetivo: salir con 3+ competidores validados, sus anuncios ganadores diseccionados, sus
landings transcritas, la estructura invisible del nicho y el GAP.

**Tú no navegas: la persona navega y te pega.** Guíala clic a clic. Si tienes herramienta de
búsqueda web disponible úsala para complementar, pero nunca sustituyas los datos reales de la
Biblioteca de Anuncios por suposiciones.

---

## Dónde se busca

### 1. Biblioteca de Anuncios de Meta (la fuente principal)

`facebook.com/ads/library`

Instrucciones exactas para pasarle a la persona:

```
1. Abre facebook.com/ads/library
2. En "Categoría de anuncios" elige: Todos los anuncios
3. En "País" elige: Colombia  (repite después con México, Chile, Perú, Ecuador, Panamá)
4. En el buscador escribe la palabra del nicho, no la marca:
   "ansiedad", "adelgazar", "mi hijo no me habla", "recuperar a mi ex", "inglés en 30 días"
5. Ordena por los que tengan MÁS anuncios activos
6. De cada anunciante que aparezca, pégame:
   - Nombre del anunciante
   - Cuántos anuncios activos tiene (aparece arriba: "~120 resultados")
   - La fecha de inicio del anuncio más antiguo que veas
   - El link de la landing a la que manda
```

Trucos de búsqueda que se le pasan cuando no encuentra nada:

- Buscar el **dolor**, no la solución: "no puedo dormir" antes que "insomnio"
- Buscar en **portugués** (Brasil suele ir 6–12 meses adelante) y traducir el ángulo
- Buscar en **inglés** el mismo nicho: casi todo lo que factura en LATAM ya pasó por EE. UU.
- Buscar palabras de la oferta: "guía", "protocolo", "método", "plan de 21 días"
- Buscar el nombre de un competidor conocido y mirar "Anuncios de páginas similares"

### 2. Marketplaces

- **Hotmart** — sección de productos más vendidos por categoría y país
- **ClickBank** — gravity alta = está vendiendo hoy
- **Amazon Kindle** — los títulos más vendidos del nicho dan el lenguaje del mercado

### 3. Voz del cliente (para el copy, no para validar)

Grupos de Facebook del nicho, comentarios de los anuncios del competidor, reseñas de 3
estrellas en Amazon, hilos de Reddit/Quora, comentarios de YouTube. De aquí salen las frases
textuales que después se usan como headline.

Pídele a la persona **10 frases textuales** de gente describiendo el problema con sus
palabras. Sin editar. Sin corregir la ortografía.

---

## Umbrales de validación

Un competidor cuenta como validado si cumple **al menos tres** de estos:

| Señal | Umbral | Qué significa |
|---|---|---|
| Anuncios activos | ≥ 20 | Está invirtiendo de verdad |
| Antigüedad del anuncio más viejo | ≥ 60 días | Es rentable. Nadie quema plata 2 meses |
| Variantes del mismo creativo | ≥ 5 | Está escalando ese ganador |
| Landing con checkout propio | sí | Es un negocio, no un afiliado casual |
| Presencia en 2+ países | sí | Ya escaló geográficamente |

**Veredicto del nicho:**

- 3+ competidores validados → **APTO**, se sigue
- 1–2 competidores validados → **DÉBIL**, se sigue con cautela y se busca más
- 0 competidores validados → **NO APTO**, se cambia de nicho. Dilo claro.

---

## Cómo se identifica el anuncio rentable

Esta es la pregunta que más se falla. El anuncio rentable **no es el más bonito**: es el que
lleva más tiempo vivo y tiene más hermanos.

Señales, en orden de peso:

1. **Fecha de inicio antigua.** Un anuncio corriendo desde hace 4 meses es rentable. No hay
   otra explicación.
2. **Muchas variantes del mismo concepto.** Si ves el mismo video con 6 títulos distintos,
   ese concepto es el ganador y lo están exprimiendo.
3. **El mismo hook repetido en creativos diferentes.** El hook es lo que ganó, y lo están
   probando en otros formatos.
4. **Aparece en varios países a la vez.** Escalaron geográficamente porque funcionó.

Lo que **no** es señal: cantidad de reacciones (se pueden comprar), calidad de producción,
que a la persona le guste.

Pídele a la persona los **3 anuncios más antiguos y con más variantes** de cada competidor, y
la captura o descarga del creativo. Esas imágenes y videos son la materia prima de F5.

---

## Ficha por competidor

Una por cada uno, en `01-espionaje.md`:

```markdown
### Competidor N — [Nombre]

| Campo | Dato |
|---|---|
| Anuncios activos | |
| Anuncio más antiguo | (fecha) |
| Países donde aparece | |
| Landing | (URL) |
| Producto | (formato y tamaño) |
| Precio | (moneda local + USD) |
| Checkout | (Hotmart / propio / otro) |
| Bump visible | (sí/no + cuál) |
| Garantía | (días) |
| Veredicto | VALIDADO / NO |
```

---

## Disección del anuncio ganador

Por cada anuncio ganador (mínimo 3 en total, idealmente 3 por competidor):

```markdown
### Anuncio ganador — [Competidor] — [formato]

**Corriendo desde:** (fecha) · **Variantes vistas:** (n)

**Hook (0–3 s), literal:**
> "..."

**Primer frame:** qué se ve exactamente en el segundo 0
**Formato:** video UGC / video producido / imagen / carrusel / captura de chat
**Sujeto:** quién aparece (edad, género, rol) o qué objeto
**Encuadre:** primer plano, plano medio, cenital, selfie a mano alzada
**Paleta y luz:** cálida/fría, luz de ventana, luz dura, exterior
**Texto en pantalla:** literal, y en qué segundo aparece
**Estructura del video:** hook → agitación → mecanismo → oferta → CTA (marca los segundos)
**Prueba usada:** testimonio / captura de chat / demostración / autoridad / ninguna
**CTA:** botón y texto exacto
**Por qué frena el scroll:** una frase
```

Esta ficha se reusa tal cual en F5 como referencia del prompt. Guárdala completa.

---

## Disección de la landing

Se transcribe **bloque por bloque, en orden**. No un resumen: la secuencia:

```markdown
### Landing — [Competidor]

| # | Bloque | Qué dice (resumido) | Longitud |
|---|---|---|---|
| 1 | Barra de urgencia | | 1 línea |
| 2 | Hero | Headline literal: "..." | |
| 3 | ... | | |

**Promesa principal, literal:** "..."
**Dónde aparece el precio por primera vez:** (bloque n)
**Número de CTAs:** (n)
**Tipo y cantidad de testimonios:** 
**Garantía:** (días, condiciones)
**Longitud total:** corta (1 pantalla) / media / larga (10+ pantallas)
```

---

## La estructura invisible

El entregable más valioso de F1. Es el patrón compartido por todo lo que factura en el nicho,
y casi nunca es obvio a simple vista.

Se escribe completando literalmente esta frase:

> *"Todo lo que está escalando en este nicho tiene en común que ______, y además comparte:
> 1) ______ 2) ______ 3) ______."*

Ejemplos de estructuras invisibles reales:

- *"Todos venden un PDF corto con un plan de días numerados, nunca un curso en video."*
- *"Todos abren el anuncio con una madre hablando a cámara sin edición, en su cocina."*
- *"Todos reposicionan la culpa: el problema nunca es del comprador, es de algo que le
  enseñaron."*
- *"Todos venden entre 15 y 25 USD con garantía de 7 días y bump de audio."*

Si la persona no ve el patrón, ayúdala comparando los tres competidores columna a columna en
una tabla: formato, promesa, precio, arquetipo de historia, tipo de prueba, duración.

---

## El GAP

Cuatro preguntas. Basta con que una tenga respuesta fuerte:

1. **Ángulo:** ¿qué explicación del problema no está usando nadie?
2. **Sub-avatar:** ¿a quién le habla el nicho de forma genérica y podría hablársele de forma
   específica? (padres además de madres; mujeres de 45+ además de 30+; hijos únicos)
3. **Formato:** ¿qué entregable falta? (audio para quien no lee; imprimible; guiones listos)
4. **Precio:** ¿hay un hueco? (todos a 47 y nadie a 17; o todos a 9 y nadie a 27 con más valor)

El **GAP de ángulo vale más que el GAP de producto**. El mismo producto con una explicación
que nadie usa gana; un producto distinto con la explicación de todos, no.

---

## Compuerta F1 → F2

- [ ] 3+ competidores validados con ficha completa
- [ ] 3+ anuncios ganadores diseccionados con su creativo guardado en `referencias/`
- [ ] 1+ landing transcrita bloque por bloque
- [ ] 10 frases textuales del mercado
- [ ] Estructura invisible escrita en una frase
- [ ] GAP identificado y aprobado por la persona

Cierra preguntando:
> "¿Este mapa del nicho coincide con lo que ves tú? ¿Falta algún competidor que conozcas?"
