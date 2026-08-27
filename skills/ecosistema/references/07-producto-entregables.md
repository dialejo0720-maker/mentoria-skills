# F7 · El producto real

Objetivo: que exista, como archivo, todo lo que la landing prometió — y que se entregue solo.

Tiempo objetivo: **2 a 3 días**. No dos semanas. La calidad se mide en si cumple la promesa,
no en el número de páginas.

---

## Regla única

> **El producto entrega exactamente lo que promete la landing, en el orden del Método.**

Ni un capítulo más. Cada vez que aparece la tentación de agregar un tema "que también es
importante", la respuesta es no: eso es material para un order bump (F8).

El índice del producto **ya está escrito**: son los pasos de la KEY 5. Si el Método tiene 4
pasos, el producto tiene 4 capítulos centrales. No 12.

---

## Pedir la referencia del producto del competidor

Antes de escribir, pídele a la persona lo que se pueda ver del producto del competidor. Sirve
para calibrar alcance y profundidad, no para copiar contenido:

```
De lo que vende el competidor, mándame lo que puedas conseguir sin comprar:
- El índice o tabla de contenidos (suele estar en la landing o en un video de ventas)
- Cuántas páginas / cuánto dura
- Si regala una muestra o un capítulo gratis, descárgalo
- Capturas del interior si aparecen en el anuncio o en el video
- Los bonos que incluye y qué formato tienen
```

Con eso defines: cuántas páginas espera este mercado, qué densidad, y qué bonos se dan por
sentados en el nicho.

---

## Borrador en 30 minutos

Antes de escribir una sola página, cierra esto con la persona:

```markdown
## Borrador del producto

**Título:** (el nombre del método, o la promesa)
**Subtítulo:** (la promesa completa con tiempo)
**Formato:** PDF de N páginas + audiolibro + plan imprimible
**Lector:** (el avatar de F3, en una frase)
**Transformación:** de [estado A concreto] a [estado B concreto]
**Promesa que debe cumplir:** (copiada literal de KEY 7)

**Índice**
1. Carta al lector — por qué esto es distinto
2. Diagnóstico — cómo saber si te está pasando
3. [Mecanismo del problema con su nombre] — por qué pasa de verdad
4. Por qué falló lo que ya intentaste
5. [El Método con su nombre] — visión general
6. Paso 1 · [nombre]
7. Paso 2 · [nombre]
8. Paso 3 · [nombre]
9. Paso 4 · [nombre]
10. El plan de N días
11. Los 5 errores que arruinan el proceso
12. Preguntas frecuentes
13. Qué hacer a partir de aquí
```

Los capítulos 6 a 9 son el corazón. Los demás son marco.

---

## Cómo se escribe cada capítulo

Estructura fija, cuatro partes:

```
1. La escena      — una situación concreta que el lector reconoce como suya  (150–200 pal)
2. Qué pasa aquí  — la explicación, sin tecnicismos                          (300–400 pal)
3. Qué se hace    — el procedimiento, en pasos numerados                     (300–500 pal)
4. Hazlo hoy      — una sola acción, hoy, con tiempo estimado                (80–120 pal)
```

Reglas de escritura:

- **Segunda persona, tuteo.** "Cuando le preguntas cómo le fue…", no "cuando el padre pregunta".
- **Cada capítulo termina en una acción**, no en una reflexión. Si el lector cierra el
  capítulo y no sabe qué hacer hoy, el capítulo falló.
- **Frases cortas.** Párrafos de 2 a 4 líneas. Se lee en el celular.
- **Ejemplos con nombre y detalle**, aunque sean compuestos — y si son compuestos, se dice:
  "un caso típico que he visto muchas veces".
- **Nada de relleno histórico.** Nadie compró para leer la historia de la disciplina.
- **Guiones literales donde aplique.** En productos de comunicación, relaciones o ventas, las
  frases exactas para decir son lo más valorado del producto entero.

Extensión de referencia: **50 a 80 páginas** (12.000–18.000 palabras) para un producto de
USD 15–25. Más largo no vale más: vale menos, porque no se termina.

---

## El resto del stack

| Pieza | Cómo se produce | Tiempo |
|---|---|---|
| **Audiolibro** | TTS sobre el texto del PDF (ElevenLabs, o la voz del propio autor) | 2–4 h |
| **Plan imprimible** | Una página por día, con la acción y un espacio para escribir | 2 h |
| **Guiones / tarjetas** | Extraer las frases literales del PDF y ponerlas en tarjetas | 2 h |
| **Portada** | Nano Banana o Canva. Título grande, legible a 200px de ancho | 30 min |
| **Mockups** | Portada montada en tablet/libro para la landing. Canva o Nano Banana | 30 min |

El audiolibro es el bono con mejor relación valor percibido / costo de producción de todo el
catálogo. Va siempre.

---

## Producción del PDF

1. Escribir todo en Markdown, un archivo por capítulo, en `producto/`
2. Revisar de corrido en voz alta — se detecta el relleno al oírlo
3. Exportar con la skill `/make-pdf`, o con `pandoc` si está disponible
4. Comprobar en el móvil: tipografía de 12pt mínimo, márgenes anchos, números de página

Diseño interior: sobrio. Una tipografía para títulos, una para cuerpo. Nada de fondos de
color a página completa: el 30% de los compradores lo va a imprimir.

---

## Subir a Hotmart

```
Hotmart → Productos → Crear producto
  Tipo:        Ebook / Archivo digital
  Nombre:      idéntico al de la landing
  Descripción: el bloque "qué incluye" de la landing
  Precio:      idéntico al de la landing, en la moneda decidida en F3
  Portada:     el mockup

Contenido → subir todos los archivos del stack (PDF, MP3, plan, tarjetas)
Configuración → Garantía: los días decididos en F3
Configuración → Email de entrega: personalizado (ver abajo)
Herramientas → Píxeles: el píxel de Meta + API de Conversiones
```

### Email de entrega

Se escribe, no se deja el genérico. Tres párrafos:

```
1. Confirmación y bienvenida — repetir la promesa que compró, con sus palabras
2. Acceso — el link, grande y claro, y qué archivo abrir primero
3. La primera acción — qué hacer hoy, en 5 minutos. Reduce reembolsos más que nada
```

Añade una línea de contacto real. Un correo de soporte que responde baja los reembolsos y
las disputas de tarjeta.

---

## Prueba antes de dar por cerrado

- [ ] Compra real de prueba con tarjeta propia
- [ ] Llegó el email de entrega en menos de 2 minutos
- [ ] Todos los archivos se descargan y se abren
- [ ] El PDF se lee bien en un móvil
- [ ] El audio suena en el reproductor del teléfono
- [ ] El evento `Purchase` apareció en el Administrador de Eventos de Meta
- [ ] El reembolso de esa compra de prueba se procesa sin problemas

---

## Compuerta F7 → F8

- [ ] Todo el stack de valor existe como archivo
- [ ] Subido y probado con compra real
- [ ] Email de entrega escrito y funcionando
- [ ] Garantía configurada
