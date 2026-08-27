# F6 · Campañas de Meta — CBO primero, ABO después

Objetivo: dejar una estructura encendida, midiendo bien, con reglas de decisión escritas
**antes** de gastar el primer dólar.

---

## Antes de tocar el Administrador de Anuncios

- [ ] Cuenta publicitaria dentro de un Business Manager (no una cuenta personal)
- [ ] Página de Facebook e Instagram conectadas
- [ ] Medio de pago cargado y verificado
- [ ] Dominio verificado en Business Manager → Seguridad de la marca → Dominios
- [ ] Píxel creado y conectado a la landing
- [ ] **API de Conversiones activada desde Hotmart** (esto sube la calidad de la señal y hoy
      es la diferencia entre optimizar bien y optimizar a ciegas)
- [ ] Evento `Purchase` verificado con una compra real de prueba
- [ ] Eventos priorizados configurados en Aggregated Event Measurement, con `Purchase` en el
      puesto 1

Si el `Purchase` real no aparece en el Administrador de Eventos, **no se enciende nada**.
Optimizar hacia un evento que no llega es quemar presupuesto.

---

## Por qué CBO primero y ABO después

**CBO** (presupuesto a nivel campaña): Meta reparte el dinero entre conjuntos y entre
creativos buscando el que convierte. Es lo que quieres al principio, cuando no sabes nada:
el algoritmo encuentra al comprador más rápido que tú.

**ABO** (presupuesto a nivel conjunto): tú fijas cuánto gasta cada conjunto. Es lo que
quieres después, cuando ya sabes qué funciona y necesitas comparar cosas de forma limpia —
un público contra otro, un ángulo contra otro — sin que Meta le dé todo el dinero al que
arrancó mejor el primer día.

Al revés no funciona: hacer ABO desde el día 1 con presupuestos pequeños divide una señal
que ya era débil en tres señales inservibles.

---

## FASE 1 · La campaña CBO (días 1 a 5)

```
CAMPAÑA  [Producto] · CBO · Test
  Objetivo:              Ventas
  Presupuesto:           a nivel campaña (CBO / Advantage campaign budget)
  Presupuesto diario:    ver tabla de abajo
  Estrategia de puja:    Costo más bajo (sin límite de costo)
  Atribución:            7 días clic, 1 día visualización

  CONJUNTO 1  ·  Amplio LATAM
    Evento de conversión:  Purchase   (ver excepción abajo)
    Países:                Colombia, México, Perú, Ecuador, Chile, Panamá
    Edad:                  la del avatar, con ±5 años de margen
    Género:                todos, salvo que el producto sea claramente de uno
    Intereses:             NINGUNO. Público amplio
    Ubicaciones:           Advantage+ (automáticas)
    Advantage+ creativo:   desactivado en el test
    ANUNCIOS:              los 9 creativos de F5
```

Un solo conjunto. Nueve anuncios. El trabajo del día 1 es que Meta encuentre al comprador,
no que tú demuestres una hipótesis de segmentación.

**Por qué público amplio y no intereses:** con el volumen de señal que da la API de
Conversiones, la segmentación por intereses en productos de bajo precio suele rendir igual o
peor, y encarece el CPM. Los intereses se prueban en la ABO de la fase 2, ya con datos.

**Por qué los 6 países juntos:** con presupuestos pequeños, separar por país deja a cada
conjunto sin señal. Juntos, el algoritmo va a donde la conversión sale más barata. La
separación por país llega en fase 3, si los datos la justifican.

### Excepción del evento de conversión

Si el presupuesto no alcanza para ~15 compras por semana, optimizar a `Purchase` deja el
conjunto en aprendizaje para siempre. En ese caso:

1. Optimiza a **`InitiateCheckout`** durante los primeros 5–7 días
2. Cuando acumules 30–50 compras reales, cambia a `Purchase` (campaña nueva, no editar la
   existente)

### Presupuesto diario de arranque

Regla práctica: el presupuesto diario debe permitir **al menos 3 compras al día** al CPA que
esperas.

| Precio del producto | CPA objetivo | Presupuesto diario mínimo | Recomendado |
|---|---|---|---|
| USD 9–14 | USD 4–6 | USD 15 | USD 20–25 |
| USD 15–25 | USD 6–10 | USD 20 | USD 30–40 |
| USD 27–47 | USD 12–18 | USD 35 | USD 50–70 |

Por debajo de eso no hay test: hay ruido. Si la persona no puede poner ese mínimo durante 5
días seguidos, es mejor esperar a tenerlo que quemarlo en 2 días.

### Las tres reglas de la fase 1

1. **No tocar nada durante 72 horas.** Ni presupuesto, ni creativos, ni públicos. Cada
   edición reinicia el aprendizaje.
2. **No mirar las métricas cada hora.** Una vez al día, a la misma hora.
3. **Encender a medianoche** hora del mercado principal, para que el primer día sea un día
   completo y el reparto de presupuesto no salga distorsionado.

---

## FASE 2 · La campaña ABO (a partir del día 5–6)

Se abre cuando la CBO ya dijo qué creativo gana. Ahora sí se aísla y se compara.

```
CAMPAÑA  [Producto] · ABO · Escala
  Objetivo:            Ventas
  Presupuesto:         a nivel conjunto
  Atribución:          7 días clic, 1 día visualización

  CONJUNTO A · Amplio          USD 15/día  — el mismo público de la CBO, con el ganador
  CONJUNTO B · Intereses       USD 15/día  — 3–5 intereses del nicho agrupados
  CONJUNTO C · Lookalike 1%    USD 15/día  — solo si ya hay 100+ compradores en el píxel

  Cada conjunto lleva el creativo ganador + 2 variantes nuevas del mismo ángulo
```

Reglas de la ABO:

- **Un cambio por conjunto.** Si el conjunto B cambia público *y* creativo respecto del A, el
  resultado no dice nada.
- **Mismo presupuesto en todos.** Si no, no es comparable.
- **5 días mínimo** antes de sacar conclusiones.
- El **lookalike no se crea antes de tener 100 compradores** en el píxel. Con menos, la
  semilla es ruido.

---

## FASE 3 · Separar por país (solo si los datos lo piden)

Se separa un país en su propio conjunto cuando cumple las dos condiciones:

1. Ya generó **10+ compras** dentro de la campaña conjunta, y
2. Su CPA es **claramente distinto** (±40%) del promedio

Antes de eso, separar solo fragmenta la señal.

### Los 6 países

| País | Moneda | CPM típico (USD) | Notas |
|---|---|---|---|
| **Colombia** | COP | 1,5 – 4 | Volumen alto y tráfico barato. Buen mercado de arranque. Pagos: tarjeta, PSE, Efecty |
| **México** | MXN | 2 – 5 | El mercado más grande. OXXO es clave: muchas compras se completan horas después |
| **Perú** | PEN | 1,5 – 3,5 | Tráfico barato. Menor penetración de tarjeta; PagoEfectivo ayuda |
| **Ecuador** | USD | 2 – 4,5 | Volumen medio, precio directo en dólares, sin fricción de conversión |
| **Chile** | CLP | 3 – 7 | El CPM más caro de los seis y el mayor poder adquisitivo. Soporta precio más alto |
| **Panamá** | USD | 3 – 6 | Volumen bajo. Va de acompañante, no de mercado principal |

Son rangos de referencia, no promesas: el CPM real depende del nicho, la época del año y la
calidad del creativo. Se usan para detectar anomalías, no para presupuestar al centavo.

Notas de idioma: español neutro sirve para los seis. Evita "vos" (Argentina), "vosotros"
(España) y el mexicanismo cerrado si vendes en los seis a la vez. "Platicar" no se entiende
igual en Chile que en México; "conversar" funciona en todos.

Sobre OXXO y pagos en efectivo: en México y Perú una parte de las compras se registran
**horas o días después** del clic. No mates una campaña mexicana por el CPA de las primeras
24 horas; revisa a las 72.

---

## Convención de nombres

Sin esto, a la semana 3 nadie entiende su propia cuenta:

```
Campaña:   [PRODUCTO]_[CBO|ABO]_[OBJETIVO]_[FECHA]
           SILENCIO_CBO_VENTAS_2026-03-01

Conjunto:  [PUBLICO]_[PAISES]_[EVENTO]
           AMPLIO_LATAM6_PURCHASE

Anuncio:   [ANGULO]_[FORMATO]_[VARIANTE]
           DOLOR_9x16_V2
```

---

## Métricas y umbrales

Se miran en este orden. La de arriba explica a la de abajo:

| Métrica | Alerta | Bien | Muy bien | Qué significa si falla |
|---|---|---|---|---|
| CPM | > USD 8 | 2 – 5 | < 2 | Público muy chico o creativo con baja relevancia |
| Tasa de enganche (3 s / impresiones) | < 20% | 25 – 35% | > 40% | El primer frame no frena el scroll |
| Tasa de retención (video visto 75%) | < 8% | 12 – 20% | > 25% | El cuerpo del video pierde a la gente |
| CTR (enlace) | < 1% | 1,5 – 3% | > 3% | El anuncio no genera ganas de saber más |
| Costo por clic en el enlace | > USD 0,60 | 0,20 – 0,40 | < 0,20 | |
| Tasa de conversión de landing | < 1% | 2 – 4% | > 5% | La landing no sostiene lo que prometió el anuncio |
| CPA | > 1,5× precio ÷ 2 | ver tabla | | |
| ROAS | < 1,3 | 1,8 – 2,5 | > 3 | |

**El diagnóstico está en dónde se rompe la cadena:**

```
CPM alto            -> problema de público o de relevancia del creativo
Enganche bajo       -> problema del primer frame
CTR bajo            -> problema del hook o del copy
Conversión baja     -> problema de la landing o de coherencia anuncio↔landing
CPA alto con todo lo demás bien -> problema de precio u oferta
```

---

## Reglas de decisión (se escriben antes de encender)

### Matar un anuncio

- Gastó **3× el precio del producto** sin una sola compra → apagar
- CTR por debajo de 1% después de 2.000 impresiones → apagar
- Tasa de enganche por debajo de 15% → apagar (el creativo no sirve, el copy da igual)

### Matar la campaña entera

- Gastó **5× el precio** sin ninguna compra **y** la landing tiene menos de 1% de conversión
  con más de 300 visitas → el problema no son los anuncios. Volver a F3 o F4.

### Escalar

- **Escalado vertical:** +20% al presupuesto cada 3 días, mientras el CPA aguante. Subidas
  mayores reinician el aprendizaje.
- **Escalado horizontal:** duplicar el conjunto ganador en una campaña nueva con presupuesto
  2–3× mayor, y dejar corriendo el original.
- No se escala nunca un viernes ni antes de un fin de semana largo sin poder vigilarlo.

### Refrescar creativos

Cuando la frecuencia pasa de **2,5** en 7 días, o cuando el CPA sube 30% dos días seguidos
sin haber tocado nada: fatiga de creativo. Toca subir tanda nueva, no bajar presupuesto.

---

## Errores que se repiten y cuestan caro

1. Editar la campaña cada dos horas — cada edición reinicia el aprendizaje
2. Optimizar a `Purchase` con presupuesto que no da ni 3 compras al día
3. Juzgar a las 24 horas — el mínimo honesto son 72
4. 15 conjuntos con USD 5 cada uno en lugar de 1 con USD 40
5. Lanzar 9 creativos que son el mismo ángulo con distinto fondo
6. Encender sin haber verificado `Purchase` con una compra real
7. Duplicar un anuncio rechazado en vez de reescribir la frase que lo hizo caer

---

## Compuerta F6 → F7

- [ ] `Purchase` verificado con compra real
- [ ] API de Conversiones activa desde Hotmart
- [ ] CBO configurada con los 9 creativos y presupuesto suficiente
- [ ] Reglas de matar y escalar escritas en `06-campanas.md`
- [ ] Nomenclatura aplicada
- [ ] Fecha y hora de encendido decididas

Para auditar la cuenta a fondo más adelante, invoca `/ads`.
