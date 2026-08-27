# F6 · Campañas — [PRODUCTO]

**Cuenta publicitaria:** · **Píxel ID:** · **Fecha de encendido:**

---

## Verificación previa

- [ ] Cuenta dentro de Business Manager
- [ ] Página de FB e IG conectadas
- [ ] Medio de pago verificado
- [ ] Dominio verificado en Seguridad de la marca
- [ ] Píxel en la landing (`PageView` + `InitiateCheckout` verificados con Pixel Helper)
- [ ] API de Conversiones activa desde Hotmart
- [ ] **`Purchase` verificado con compra real** ← sin esto no se enciende
- [ ] `Purchase` en el puesto 1 de eventos priorizados

---

## FASE 1 · CBO (días 1–5)

```
CAMPAÑA  [PRODUCTO]_CBO_VENTAS_[FECHA]
  Objetivo:            Ventas
  Presupuesto:         CBO, USD ___ /día
  Estrategia de puja:  Costo más bajo
  Atribución:          7 días clic, 1 día visualización

  CONJUNTO  AMPLIO_LATAM6_PURCHASE
    Evento:       Purchase   (o InitiateCheckout si el presupuesto no da 3 compras/día)
    Países:       Colombia, México, Perú, Ecuador, Chile, Panamá
    Edad:         __ – __
    Género:       
    Intereses:    ninguno (público amplio)
    Ubicaciones:  Advantage+ automáticas
    Anuncios:     los 9 creativos de F5
```

| Campo | Decisión |
|---|---|
| Presupuesto diario | USD |
| Evento de conversión elegido | |
| CPA objetivo | USD |
| Hora de encendido | 00:00 hora de |

---

## Reglas de decisión (escritas ANTES de encender)

### Matar un anuncio
- [ ] Gastó 3× el precio del producto (USD ___) sin una compra
- [ ] CTR de enlace < 1% con 2.000+ impresiones
- [ ] Tasa de enganche < 15%

### Matar la campaña
- [ ] Gastó 5× el precio (USD ___) sin compras **y** la landing convierte < 1% con 300+ visitas

### Escalar
- [ ] +20% al presupuesto cada 3 días mientras el CPA aguante
- [ ] Duplicar el conjunto ganador en campaña nueva con 2–3× presupuesto
- [ ] Nunca escalar viernes ni el mismo día que se cambian creativos

### Refrescar creativos
- [ ] Frecuencia > 2,5 en 7 días
- [ ] CPA sube 30% dos días seguidos sin haber tocado nada

---

## Registro diario

| Día | Gasto | Impr. | Engan. | CTR | Clics | Visitas | Compras | CPA | ROAS | Acción tomada |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | | | no tocar |
| 2 | | | | | | | | | | no tocar |
| 3 | | | | | | | | | | |
| 4 | | | | | | | | | | |
| 5 | | | | | | | | | | decisión |
| 6 | | | | | | | | | | |
| 7 | | | | | | | | | | abrir ABO |

---

## Rendimiento por creativo

| Creativo | Ángulo | Gasto | Engan. | CTR | Compras | CPA | Estado |
|---|---|---|---|---|---|---|---|
| 01 | Dolor | | | | | | activo / apagado |
| 02 | | | | | | | |
| … | | | | | | | |

**Creativo ganador:**
**Ángulo ganador:**

---

## FASE 2 · ABO (desde el día 5–6)

```
CAMPAÑA  [PRODUCTO]_ABO_ESCALA_[FECHA]
  CONJUNTO A · AMPLIO        USD ___/día  — ganador + 2 variantes
  CONJUNTO B · INTERESES     USD ___/día  — intereses: ______
  CONJUNTO C · LOOKALIKE 1%  USD ___/día  — solo con 100+ compradores en el píxel
```

- [ ] Mismo presupuesto en todos los conjuntos
- [ ] Un solo cambio entre conjuntos
- [ ] 5 días mínimo antes de concluir

| Conjunto | Gasto | Compras | CPA | ROAS | Veredicto |
|---|---|---|---|---|---|
| A · Amplio | | | | | |
| B · Intereses | | | | | |
| C · Lookalike | | | | | |

---

## FASE 3 · Separación por país

Solo cuando un país tenga 10+ compras y CPA ±40% del promedio.

| País | Compras | CPA | ¿Separar? |
|---|---|---|---|
| Colombia | | | |
| México | | | |
| Perú | | | |
| Ecuador | | | |
| Chile | | | |
| Panamá | | | |

---

## Diagnóstico

| Dónde se rompe | Qué revisar |
|---|---|
| CPM alto | público o relevancia del creativo |
| Enganche bajo | primer frame |
| CTR bajo | hook y copy |
| Conversión de landing baja | landing y coherencia anuncio↔landing |
| CPA alto con todo bien | precio u oferta |
