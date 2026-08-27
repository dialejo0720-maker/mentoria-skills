# F8 · Order bumps y upsells

Objetivo: subir el valor promedio del pedido (AOV) sin subir el costo de adquisición. Es la
palanca más barata de todo el ecosistema: el tráfico ya está pagado.

Aritmética de por qué importa: si el producto vale USD 17 y el CPA es USD 12, el margen es
USD 5. Un bump de USD 9 que acepta el 30% de los compradores añade USD 2,70 por venta — más
del 50% de margen extra, con cero gasto adicional en anuncios. Muchas ofertas que parecían
inviables se vuelven rentables solo con el bump.

---

## El principio

El bump y el upsell **no son "más contenido"**. Son una de estas dos cosas:

1. **El siguiente problema.** Lo que aparece justo después de aplicar el método.
2. **La eliminación del esfuerzo.** Lo mismo que ya compró, pero hecho por ti o más rápido.

Lo que **no** es un bump: un capítulo que le quitaste al producto principal, un descuento en
otro producto sin relación, o "un pack de 200 plantillas" que nadie pidió.

---

## El mapa de problemas siguientes

Este es el ejercicio que genera las ideas. Se hace con la persona, en 15 minutos:

```
Alguien compra el producto y aplica el Método. Lista, en orden, qué pasa después:

Semana 1 → ¿con qué se traba?          → …
Semana 2 → ¿qué le empieza a faltar?   → …
Semana 4 → ¿qué problema nuevo aparece porque el primero se resolvió? → …
¿Qué parte del método le da más pereza o miedo hacer?  → …
¿Qué pregunta va a mandar por correo?  → …
¿Qué le va a pasar con otra persona de su entorno?     → …
```

Cada respuesta es un producto complementario. Las mejores suelen ser la cuarta (lo que da
pereza → producto "hecho por ti") y la tercera (el problema que nace del éxito).

---

## Los 6 arquetipos de bump

| # | Arquetipo | Qué es | Ejemplo |
|---|---|---|---|
| 1 | **Hecho por ti** | Quita el trabajo de aplicar el método | 50 guiones literales listos para usar |
| 2 | **Acelerador** | El mismo resultado, más rápido | Plan express de 3 días en vez de 21 |
| 3 | **Traducción** | El método aplicado a otro contexto o persona | La versión para adolescentes; para el papá |
| 4 | **Soporte** | Acompaña la aplicación | Audios diarios de 5 min para los 21 días |
| 5 | **Herramienta** | Algo que se usa, no que se lee | Tracker imprimible, tarjetas, plantillas |
| 6 | **Profundización** | El nivel 2, para cuando el 1 funcionó | Qué hacer cuando ya te habla |

Presenta **5 ideas** repartidas entre arquetipos distintos, con su precio y su motivo. La
persona elige 1 o 2. El bump es uno solo en el checkout: dos bumps bajan la conversión de
ambos.

### Cómo se elige el ganador entre las 5

| Criterio | Peso |
|---|---|
| ¿Resuelve un problema que el comprador ya siente hoy? | alto |
| ¿Se explica en una frase? | alto — si necesita dos, no funciona en el checkout |
| ¿Se produce en menos de 1 día? | alto |
| ¿Se puede consumir en menos de 30 minutos? | medio |

El mejor bump del catálogo casi siempre es del arquetipo 1: **"hecho por ti"**. La gente paga
por no tener que hacerlo.

---

## Precios

| Pieza | Precio | Regla |
|---|---|---|
| Producto principal | P | El de F3 |
| **Order bump** | 30–50% de P | Nunca más caro que el principal. Decisión de 3 segundos |
| **Upsell 1** | 2–4× P | El salto grande. Se muestra después de pagar |
| **Downsell** | ~50% del upsell | Si rechaza el upsell, versión reducida |

Ejemplo con producto de USD 17:

```
Principal      USD 17
Bump           USD  9   (guiones listos)        → esperado: 25–35% lo toman
Upsell         USD 47   (programa de 8 semanas) → esperado: 5–12% lo toman
Downsell       USD 24   (solo los audios)       → esperado: 20% de los que rechazaron
```

AOV esperado en ese ejemplo: entre USD 22 y USD 27. Ese es el número que decide si la
campaña es rentable, no los USD 17.

---

## Copy del order bump

Vive en una caja pequeña dentro del checkout. Se lee en 3 segundos. Estructura fija:

```
☑  SÍ, quiero agregar [NOMBRE DEL BUMP] por solo USD 9

    [Una frase de qué es y qué resuelve — máximo 20 palabras]
    [Una frase de por qué justo ahora — la conexión con lo que acaba de comprar]

    Precio normal USD 27 · Solo en esta página
```

Reglas:

- **Primera persona y afirmativo:** "Sí, quiero agregar…". Nunca "¿Deseas agregar?".
- **La conexión explícita** con lo que acaba de comprar: "Ya tienes el método; esto te da las
  palabras exactas".
- **Precio tachado** visible.
- **Una imagen pequeña** del bump (mockup). Sube la aceptación de forma consistente.
- Nada de urgencia falsa. "Solo en esta página" es verdad; "quedan 3" no lo es.

---

## Configuración en Hotmart

### Order bump

```
Hotmart → Producto principal → Herramientas → Order Bump
  · Elegir el producto que será el bump (tiene que existir como producto propio)
  · Definir el precio especial del bump
  · Escribir el título y la descripción (el copy de arriba)
  · Subir la imagen del mockup
  · Activar
```

El bump debe existir primero como producto independiente, con su propio contenido subido.

### Upsell de un clic

```
Hotmart → Herramientas → Embudos (Funnel)
  · Producto de entrada: el principal
  · Página de upsell: se muestra después del pago, antes del "gracias"
  · Producto de upsell: el de 2–4× el precio
  · Configurar downsell para quien rechace
```

El upsell de un clic no vuelve a pedir datos de tarjeta: por eso convierte. Si la plataforma
obliga a volver a pagar desde cero, la conversión cae a la mitad y no vale la pena.

### Página del upsell

Es una landing corta, 4 bloques, escrita con el mismo método de F4:

```
1. "Espera — tu compra está confirmada" (que no crea que algo falló)
2. El siguiente problema, nombrado
3. Qué es esto y qué incluye
4. Botón grande + "No gracias, seguir a mi compra" (link chico, gris, debajo)
```

El "no gracias" tiene que existir y ser visible. Esconderlo genera disputas de tarjeta.

---

## Qué se mide

| Métrica | Umbral | Qué hacer si falla |
|---|---|---|
| Take rate del bump | 20–40% | Bajo 15%: el bump no conecta con lo comprado, o cuesta demasiado |
| Take rate del upsell | 5–12% | Bajo 3%: el salto de precio es muy grande, o la página no explica |
| AOV | subir 25%+ sobre P | Si no sube, probar otro arquetipo de bump |
| Tasa de reembolso | < 8% | Si sube con el bump, el bump prometió algo que no cumple |

Se prueba **un bump a la vez**, durante al menos 50 ventas. Con menos, el dato no dice nada.

---

## Orden de construcción

1. **Bump primero.** Es más barato de producir y afecta a todos los compradores.
2. **Upsell después**, cuando el bump ya esté midiendo.
3. **Downsell al final**, solo si el upsell tiene tráfico suficiente para justificarlo.

No se construyen los tres a la vez en el primer lanzamiento.

---

## Compuerta F8 → F9

- [ ] 5 ideas presentadas desde arquetipos distintos
- [ ] 1 bump elegido, producido y subido como producto en Hotmart
- [ ] Bump configurado en el checkout con copy e imagen
- [ ] Upsell definido con precio (aunque se construya después)
- [ ] Compra de prueba hecha con el bump incluido
