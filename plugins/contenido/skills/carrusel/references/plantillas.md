# Plantillas de slide

Seis layouts. Adáptalos — no los copies literal ocho veces.

## Base común

Todo slide arranca con esto. Solo cambian los tokens de `:root` (de `brand-profile.json`)
y el contenido de `<body>`.

```html
<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=TITULO:wght@700;800&family=CUERPO:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{
  --fondo:#0d0d12; --texto:#ffffff; --acento:#e94560; --sutil:#8a8a99;
  --f-titulo:'TITULO',sans-serif; --f-cuerpo:'CUERPO',sans-serif;
  --pad:80px;
}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden}
body{background:var(--fondo);color:var(--texto);font-family:var(--f-cuerpo);padding:var(--pad);position:relative}
</style></head><body>
  <!-- layout aquí -->
</body></html>
```

Para fondo claro invierte: `--fondo:#f6f5f2; --texto:#0d0d12; --sutil:#4a4a55`.

---

## 1. HOOK — tipografía dominante

Slide 1. El texto ocupa el escenario; todo lo demás desaparece.

```html
<body style="display:flex;flex-direction:column;justify-content:center">
  <div style="position:absolute;inset:0;background:radial-gradient(circle at 70% 20%,rgba(233,69,96,.28),transparent 55%)"></div>
  <h1 style="font-family:var(--f-titulo);font-weight:800;font-size:92px;line-height:1.08;position:relative">
    El 90% de los cursos no fracasan por el <span style="color:var(--acento)">contenido</span>.
  </h1>
  <div style="position:absolute;bottom:var(--pad);left:var(--pad);font-size:26px;color:var(--sutil);letter-spacing:.08em">DESLIZA →</div>
</body>
```

Tamaño de titular según largo: ≤6 palabras → 104px · 7–10 → 88px · 11+ → recorta el texto, no la fuente.

---

## 2. GIRO — una frase, mucho aire

Slide 2 y momentos de golpe. El vacío es el diseño.

```html
<body style="display:flex;align-items:center">
  <h2 style="font-family:var(--f-titulo);font-weight:700;font-size:76px;line-height:1.15;max-width:820px">
    Fracasan porque nadie llega al día 3.
  </h2>
</body>
```

---

## 3. PUNTO DE LISTA — barra + título + apoyo

Para slides 3–7 de arcos de lista o tutorial.

```html
<body style="display:flex;flex-direction:column;justify-content:center;gap:40px">
  <div style="display:flex;align-items:center;gap:24px">
    <span style="font-family:var(--f-titulo);font-size:120px;font-weight:800;color:var(--acento);line-height:1">03</span>
    <div style="width:100px;height:8px;background:var(--acento);border-radius:99px"></div>
  </div>
  <h2 style="font-family:var(--f-titulo);font-weight:700;font-size:64px;line-height:1.15">Grabas antes de validar</h2>
  <p style="font-size:32px;line-height:1.5;color:var(--sutil);max-width:820px">
    Doce lecciones producidas para una promesa que nadie pidió. El orden correcto es al revés.
  </p>
</body>
```

---

## 4. DATO — el número manda

```html
<body style="display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;gap:32px">
  <span style="font-family:var(--f-titulo);font-size:240px;font-weight:800;color:var(--acento);line-height:.9">73%</span>
  <p style="font-size:38px;line-height:1.4;max-width:760px">abandona un curso online antes de la tercera lección</p>
  <span style="font-size:24px;color:var(--sutil)">Fuente: nombre real de la fuente</span>
</body>
```

Nunca inventes cifras. Si no tienes fuente, usa un dato propio y dilo: "de mis 40 clientes…".

---

## 5. COMPARATIVA — antes / después

```html
<body style="display:flex;flex-direction:column;justify-content:center;gap:48px">
  <h2 style="font-family:var(--f-titulo);font-weight:700;font-size:56px">El orden importa</h2>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:32px">
    <div style="padding:48px;border-radius:28px;background:rgba(255,255,255,.06);border:2px solid rgba(255,255,255,.1)">
      <span style="font-size:26px;color:var(--sutil);letter-spacing:.06em">ANTES</span>
      <p style="font-size:34px;line-height:1.35;margin-top:20px">Grabar → vender → descubrir que nadie lo quería</p>
    </div>
    <div style="padding:48px;border-radius:28px;background:rgba(233,69,96,.14);border:2px solid var(--acento)">
      <span style="font-size:26px;color:var(--acento);letter-spacing:.06em">DESPUÉS</span>
      <p style="font-size:34px;line-height:1.35;margin-top:20px">Vender → grabar con 20 clientes esperando</p>
    </div>
  </div>
</body>
```

---

## 6. CTA — cierre con marca

Solo aquí aparece el handle.

```html
<body style="display:flex;flex-direction:column;justify-content:center;gap:36px">
  <h2 style="font-family:var(--f-titulo);font-weight:800;font-size:72px;line-height:1.12">
    Guarda esto antes de tu próximo lanzamiento.
  </h2>
  <p style="font-size:34px;line-height:1.45;color:var(--sutil);max-width:820px">
    Comenta <strong style="color:var(--acento)">ORDEN</strong> y te mando el checklist de validación.
  </p>
  <div style="position:absolute;bottom:var(--pad);left:var(--pad);display:flex;align-items:center;gap:16px">
    <img src="../assets/logo.png" alt="" style="height:56px">
    <span style="font-size:28px;color:var(--sutil)">@mimarca</span>
  </div>
</body>
```

---

## Fondo con imagen IA

Cuando uses `generate_image` de Higgsfield, el texto **siempre** va en HTML encima, con overlay:

```html
<div style="position:absolute;inset:0">
  <img src="../assets/fondo-01.png" alt="" style="width:100%;height:100%;object-fit:cover">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(13,13,18,.35) 0%,rgba(13,13,18,.88) 100%)"></div>
</div>
<!-- contenido con position:relative encima -->
```

Prompt de imagen: pide **textura o escena sin texto ni personas mirando a cámara centradas**,
y deja la mitad inferior visualmente tranquila para que el titular respire.

---

## Checklist antes de renderizar

- [ ] Ningún texto por debajo de 24px
- [ ] Contraste texto/fondo ≥ 4.5:1
- [ ] Contenido crítico dentro del 80% central (Instagram recorta al centro en la cuadrícula)
- [ ] Padding ≥ 80px en los cuatro lados
- [ ] Layouts alternados: ninguna composición se repite en slides consecutivas
- [ ] Cero `<script>`
- [ ] Rutas de imagen relativas (`../assets/…`), nunca absolutas
