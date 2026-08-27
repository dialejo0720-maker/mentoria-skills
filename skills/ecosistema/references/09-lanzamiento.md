# F9 · Lanzamiento e iteración

Objetivo: los primeros 7 días con criterio, y un ritmo semanal que impida que el producto
muera de abandono.

---

## Checklist final antes de encender

Se lee en voz alta, ítem por ítem, con la persona. Un ítem sin evidencia no pasa:

```
LANDING
  [ ] Publicada en dominio propio, carga en menos de 3 s en datos móviles
  [ ] Todos los botones llegan al checkout correcto
  [ ] Precio idéntico en landing y en Hotmart
  [ ] Garantía visible en 3 lugares
  [ ] Revisada en un móvil real

PRODUCTO
  [ ] Todos los archivos del stack subidos
  [ ] Compra real de prueba hecha y entregada en menos de 2 minutos
  [ ] Email de entrega personalizado
  [ ] Order bump configurado y probado

MEDICIÓN
  [ ] Píxel con PageView e InitiateCheckout verificados con Pixel Helper
  [ ] Purchase verificado con compra real en el Administrador de Eventos
  [ ] API de Conversiones activa desde Hotmart
  [ ] Dominio verificado en Business Manager
  [ ] Purchase en el puesto 1 de eventos priorizados

CAMPAÑA
  [ ] CBO configurada con los 9 creativos
  [ ] Presupuesto suficiente para 3 compras/día durante 5 días seguidos
  [ ] Nomenclatura aplicada
  [ ] Reglas de matar y escalar escritas
  [ ] Medio de pago de la cuenta publicitaria con saldo o cupo
```

Encendido: **medianoche del mercado principal**, preferiblemente jueves o viernes.

---

## Los primeros 7 días

| Día | Qué se mira | Qué se hace |
|---|---|---|
| 1 | Que los anuncios estén aprobados y entregando. Que el píxel registre PageView | Nada más. No tocar |
| 2 | CPM y tasa de enganche por creativo | Nada. Es demasiado pronto |
| 3 | CTR, clics en el enlace, primeras compras | Apagar solo los anuncios que ya gastaron 3× el precio sin compra |
| 4 | CPA por creativo | Identificar el ganador. Todavía no escalar |
| 5 | CPA de campaña, conversión de la landing | Decisión: escalar, iterar o parar (tabla abajo) |
| 6 | Take rate del bump, AOV real | Ajustar el copy del bump si va por debajo de 15% |
| 7 | Todo junto. Frecuencia | Montar la ABO con el ganador. Subir la tanda nueva de creativos |

**No se mira la cuenta más de una vez al día.** Mirar cada hora lleva a editar, y cada
edición reinicia el aprendizaje.

---

## La decisión del día 5

Con el gasto acumulado de 5 días sobre la mesa:

| Situación | Diagnóstico | Qué se hace |
|---|---|---|
| ROAS > 1,8 | Funciona | Escalar +20% cada 3 días. Abrir la ABO. Producir 9 creativos nuevos |
| ROAS 1,0 – 1,8 | Está cerca | No escalar. Subir AOV con el bump y mejorar la landing. Creativos nuevos del ángulo ganador |
| ROAS < 1,0 con CTR bueno y conversión de landing < 1,5% | El anuncio vende, la landing no | Volver a F4: reescribir hero, mecanismo y precio |
| ROAS < 1,0 con CTR < 1% | El anuncio no engancha | Volver a F5 con otro ángulo. La oferta puede estar bien |
| Cero compras con 5× el precio gastado y landing con 300+ visitas | La oferta no la quiere nadie | Volver a F3. Puede ser precio, promesa o avatar |
| Cero compras y menos de 100 visitas | No hay datos todavía | Presupuesto insuficiente. Esperar o subirlo |

Regla de honestidad: si dos ciclos completos (unos 15 días, dos ángulos distintos, dos
versiones de landing) no mueven el ROAS de 1,0, el problema no es de ejecución — es de
oferta o de nicho. Decirlo claro es más útil que seguir cambiando colores de botón.

---

## Ritmo semanal permanente

Lo que separa un producto que escala de uno que muere en la semana 3:

| Cadencia | Qué |
|---|---|
| **Semanal** | 9 creativos nuevos (mínimo). 6 variantes del ángulo ganador + 3 de un ángulo nuevo |
| **Semanal** | 1 variante de un bloque de la landing (hero, precio o garantía) |
| **Semanal** | Revisión de frecuencia; si pasa de 2,5, la tanda nueva es urgente |
| **Cada 15 días** | Un cambio grande: oferta, mecanismo nombrado o ángulo completo |
| **Mensual** | Revisar reembolsos y leer los correos de los compradores — de ahí salen los bumps |

El contenido orgánico multiplica esto sin costo de medios: usa `/guiones` para reels con el
mismo ángulo y `/carrusel` para carruseles que expliquen el mecanismo. El orgánico también
alimenta al píxel y baja el CPM.

---

## Escalar

**Vertical:** +20% al presupuesto de la campaña cada 3 días mientras el CPA aguante. Subidas
del 50% o más reinician el aprendizaje y suelen costar dos días de rendimiento.

**Horizontal:** duplicar el conjunto ganador en una campaña nueva con presupuesto 2–3× mayor
y dejar el original corriendo. Es la forma más segura de doblar el gasto.

**Geográfico:** cuando un país acumule 10+ compras y su CPA sea claramente distinto del
promedio, se le da su propio conjunto (ver `06-campanas.md`).

**Nunca se escala** un viernes por la tarde, ni el día antes de un feriado del mercado
principal, ni el mismo día que se cambian los creativos. Un cambio a la vez.

---

## Cuándo se mata el producto

Se mata cuando se cumplen las tres a la vez:

1. Dos ángulos distintos probados, con creativos producidos de verdad (no variaciones de color)
2. Dos versiones de landing probadas
3. Gasto acumulado de 20× el precio del producto sin llegar a ROAS 1,0

En ese punto, lo barato es volver a F1 con otro GAP o con otro nicho. Lo caro es insistir.

Lo que **sí** se conserva del intento: el reporte de espionaje, las keys, el aprendizaje sobre
el avatar y los creativos producidos. Nada de eso se tira.

---

## Cierre del proceso

Cuando el producto ya está corriendo con ROAS positivo, deja escrito en `ecosistema.md`:

```markdown
## Estado final del lanzamiento
- Fecha de encendido:
- Creativo ganador y su ángulo:
- CPA y ROAS estables:
- AOV con bump:
- Próximo cambio grande programado para:
- Qué haría distinto la próxima vez:
```

Ese último punto es el que hace que el segundo producto salga en la mitad de tiempo.
