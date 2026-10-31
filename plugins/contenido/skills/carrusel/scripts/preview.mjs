#!/usr/bin/env node
// Genera un preview HTML autocontenido con los PNG ya renderizados.
// Uso: node preview.mjs <carpeta>   →   escribe <carpeta>/preview.html

import fs from "node:fs";
import path from "node:path";

const folder = path.resolve(process.argv[2] ?? ".");
const pngDir = path.join(folder, "png");

if (!fs.existsSync(pngDir)) {
  console.error(`No existe ${pngDir}. Renderiza primero con render.mjs`);
  process.exit(1);
}

const files = fs.readdirSync(pngDir).filter((f) => f.endsWith(".png")).sort();
if (files.length === 0) {
  console.error(`No hay PNG en ${pngDir}`);
  process.exit(1);
}

const slides = files
  .map((f, i) => {
    const b64 = fs.readFileSync(path.join(pngDir, f)).toString("base64");
    return `<figure><img src="data:image/png;base64,${b64}" alt="Slide ${i + 1}"><figcaption>${i + 1} / ${files.length} · ${f}</figcaption></figure>`;
  })
  .join("\n");

const titulo = path.basename(folder);

const html = `<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Preview · ${titulo}</title>
<style>
:root{color-scheme:dark}
*{margin:0;padding:0;box-sizing:border-box}
body{background:#101014;color:#e8e8ec;font:16px/1.5 system-ui,-apple-system,sans-serif;padding:40px 24px}
h1{font-size:20px;font-weight:600;margin-bottom:8px}
.meta{color:#8a8a99;font-size:14px;margin-bottom:32px}
.tira{display:flex;gap:20px;overflow-x:auto;padding-bottom:24px;scroll-snap-type:x mandatory}
figure{flex:0 0 auto;scroll-snap-align:center}
img{display:block;width:auto;height:70vh;max-height:760px;border-radius:12px;background:#000}
figcaption{margin-top:10px;font-size:13px;color:#8a8a99;text-align:center}
</style></head><body>
<h1>${titulo}</h1>
<p class="meta">${files.length} slides · desliza horizontalmente para simular el carrusel</p>
<div class="tira">
${slides}
</div>
</body></html>`;

const out = path.join(folder, "preview.html");
fs.writeFileSync(out, html, "utf-8");
console.log(`Preview: ${out}  (${(html.length / 1024 / 1024).toFixed(1)} MB)`);
