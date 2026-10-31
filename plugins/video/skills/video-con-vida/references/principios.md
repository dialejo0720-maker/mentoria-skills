# Reglas de movimiento — "dale vida a tus animaciones"

Fuente: guía de @SantiMunozIA (5 prompts) + lo que usan los 17 efectos. Aplica a TODO video que edites o animes.

## 0 · El tono decide cuánto rebote (léelo primero)

| Tono | Ejemplos | Rebote en entradas | Aparición |
|---|---|---|---|
| **Serio / premium** | VSL, servicios, inmobiliaria, salud, marca de lujo, dato animado | 0–3 % (spring sin rebote o `snappy`) | opacidad + subir 16–40 px + blur 4–8 px, desde escala 0.95 |
| **Cercano / reel** | reels de infoproductos, tips, anuncios UGC, videos a cámara | 5–10 % | igual, desde escala 0.9–0.95 |
| **Juguetón / caricatura** | pizarra con mascota, infantil, karaoke de cumpleaños, corta y pega | 10–25 %, aplastar-estirar | puede "saltar" desde chico |

- **Nunca escalar desde 0** títulos, tarjetas, botones ni logos: arrancan en 0.9–0.96 con opacidad 0. Desde 0 solo puntos, palomitas o íconos diminutos (< ~40 px) en tono cercano o juguetón.
- Más de un rebote visible se ve barato. Nada elástico en texto largo.
- Una sola cosa se mueve "en grande" a la vez; lo demás espera.
- Texto: mínimo 1 s en pantalla + ~3 fotogramas por letra en frases cortas.
- 9:16: nada importante en el 14 % superior ni en el 20 % inferior (interfaz de Reels/TikTok).
- Sonido: usa efectos CC0 (por ejemplo de freesound.org o pixabay.com/sound-effects). Úsalos también en pizarra, efectos y karaoke: impactos suaves para revelaciones, clics para palomitas y tecleo.

## 1 · Curvas con rebote (la base de todo)

> Usa curvas de easing en todas las animaciones, nada lineal. Que cada elemento acelere al entrar, frene suave y haga un pequeño rebote al llegar a su lugar (ease-out con overshoot de 5–10 %), y que se aplaste y estire un poco al aterrizar para que se sienta con vida.

- **Entrada**: ease-out con overshoot 5–10 %. Elementos de interfaz (tarjetas, barras, teléfonos): 5–8 %. Íconos, puntos, palomitas, letras que "saltan": 15–25 %. Personajes caricatura (pizarra): hasta 20–25 %.
- **Salida**: ease-in (acelera al irse), sin rebote, más corta que la entrada (60–70 %).
- **Aterrizaje**: aplastar-estirar ±8–12 % (ancho sube cuando la altura baja) que se amortigua en ~0.25 s.
- **Movimiento de cámara** (zooms, paneos): ease-in-out; zoom de corte con ease-in expo (acelera hacia el corte).
- **Lo único lineal permitido**: tecleo de texto letra por letra, barras de progreso de "carga", el giro continuo de una órbita.

### Equivalencias por motor

| Rebote | Python (`fx.py`) | GSAP | CSS | Remotion (aprox., verifícalo con un still) |
|---|---|---|---|---|
| 5 % | `ease_out_back(t, 0.05)` | `back.out(1.17)` | `cubic-bezier(0.34, 1.4, 0.64, 1)` | `spring({frame, fps, config: {damping: 18, stiffness: 120}})` |
| 8 % | `ease_out_back(t, 0.08)` | `back.out(1.5)` | `cubic-bezier(0.34, 1.5, 0.64, 1)` | `damping: 14` |
| 10 % | `ease_out_back(t, 0.10)` | `back.out(1.7)` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | `damping: 12` |
| pop 20 % | `bounce_pop(t, 0.2)` | `back.out(2.5)` | — | `damping: 8` |
| salida | `ease_in_cubic` | `power2.in` | `cubic-bezier(0.55, 0, 1, 0.45)` | `interpolate(..., {easing: Easing.in(Easing.cubic)})` |
| aterrizaje | `squash(t - t_llegada)` | `scaleX:1.1, scaleY:0.9` → `elastic.out(1, 0.4)` | keyframes scale | `interpolate` sobre scaleX/scaleY |

(Los valores GSAP se calcularon con la misma fórmula easeOutBack: s=1.70158 ⇒ 10 %.)

## 2 · Entradas escalonadas

> Haz que los elementos entren uno después de otro, no todos al mismo tiempo. Deja entre 80 y 120 ms entre cada uno, en orden de lectura, y que cada uno entre con su propio rebote. Que el último cierre con un pequeño remate.

- `stagger(t, i, gap=0.10, dur=0.45)` en Python; `stagger: 0.1` en GSAP; `delay: i * 3` frames a 30 fps en Remotion.
- Orden de lectura: arriba→abajo, izquierda→derecha; letras de un titular 40–70 ms.
- **Remate** del último: un rebote más grande, un brillo, un pequeño "punch" de escala (1 → 1.08 → 1) o un sonido.

## 3 · Parallax por capas

> Separa la escena en tres capas: fondo, medio y frente. Cuando la cámara se mueva, el fondo lento, el medio a velocidad normal y el frente más rápido que todo; desenfoca un poco el fondo para que se sienta la profundidad.

- Velocidades de referencia: fondo ×0.3–0.5, medio ×1, frente ×1.4–1.8. Desenfoque de fondo 2–6 px.
- En video a cámara las capas ya existen: **plate (fondo) → elementos → persona (alpha) → elementos delante**. Muévelas a distinta velocidad en cualquier efecto con cámara (vértigo, muro de titulares, muro de videos).
- **Nivel pro**: generar con IA una imagen por capa (mismo estilo, fondo transparente — plugin `creative-architect`, skills `direccion-de-arte` y `animar`; o solo el prompt con `claude-banana`), animarlas con parallax y meter entre medio y frente un clip animado por IA (p. ej. un personaje caminando; Higgsfield).

## 4 · Micro-movimiento constante

> Nunca dejes la pantalla completamente quieta. Cuando no esté pasando nada, agrega un movimiento sutil y constante: un zoom lento de cámara, elementos que respiren o floten un poco, parpadeos y un leve balanceo.

- Zoom lento: 1–3 % por plano (`slow_zoom`). En video a cámara, entre efectos, un push-in del 2–4 % por frase evita el plano "muerto".
- Flotar: ±4–6 px, periodo 2.4–3.5 s, con fase distinta por elemento (`float_y(t, 5, 2.8, fase)`).
- Respirar: escala ±1 % (`breathe`). Balanceo: ±1–2° (`sway`). Parpadeo de mascotas cada 3–4 s (`blink`).
- Sutil = que no se note conscientemente. Si se nota, bájalo.

## 5 · Revelado con las manos

> Rastrea mis manos en el video. Cuando las junte, dibuja una línea de luz entre ellas, y conforme las separe, que esa línea se abra como un portal y revele una palabra, un objeto o un texto que crezca con la abertura. Si cierro las manos, que se cierre.

- Se graba a propósito: manos juntas frente al pecho → separarlas despacio (~0.5 s) → mantener.
- Implementado como efecto 18 (`--manos`, `--cerrar`) con posiciones manuales. Rastreo automático: MediaPipe Hands (necesita Python 3.12 en un venv aparte).

## Checklist antes de entregar cualquier video

- [ ] ¿Hay algo que entre/salga con movimiento lineal? → cámbialo.
- [ ] ¿Aparecen varios elementos a la vez? → escalónalos.
- [ ] ¿Hay más de ~1.5 s con la pantalla totalmente quieta? → micro-movimiento.
- [ ] ¿Cada efecto ilustra algo que se dice en ese momento?
- [ ] ¿El texto en pantalla es legible en el teléfono y no tapa la cara?
