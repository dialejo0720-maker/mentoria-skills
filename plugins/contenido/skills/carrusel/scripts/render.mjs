#!/usr/bin/env node
// Renderiza slides HTML a PNG con Chrome/Edge headless ya instalado.
// Uso: node render.mjs <carpeta> [--ratio 4:5] [--solo 03] [--wait 5000] [--out png]
//
// Espera <carpeta>/html/*.html y escribe <carpeta>/png/*.png a tamaño exacto.

import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { pathToFileURL } from "node:url";

const RATIOS = {
  "4:5": { w: 1080, h: 1350 },
  "1:1": { w: 1080, h: 1080 },
  "9:16": { w: 1080, h: 1920 },
};

function parseArgs(argv) {
  const out = { folder: null, ratio: "4:5", solo: null, wait: 5000, outDir: "png" };
  const rest = [];
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--ratio") out.ratio = argv[++i];
    else if (a === "--solo") out.solo = argv[++i];
    else if (a === "--wait") out.wait = Number(argv[++i]);
    else if (a === "--out") out.outDir = argv[++i];
    else rest.push(a);
  }
  out.folder = rest[0] ?? null;
  return out;
}

function findBrowser() {
  if (process.env.CARRUSEL_BROWSER && fs.existsSync(process.env.CARRUSEL_BROWSER)) {
    return process.env.CARRUSEL_BROWSER;
  }

  const candidates = [];
  if (process.platform === "win32") {
    const pf = process.env["ProgramFiles"] ?? "C:\\Program Files";
    const pf86 = process.env["ProgramFiles(x86)"] ?? "C:\\Program Files (x86)";
    const local = process.env.LOCALAPPDATA ?? path.join(os.homedir(), "AppData", "Local");
    candidates.push(
      path.join(pf, "Google", "Chrome", "Application", "chrome.exe"),
      path.join(pf86, "Google", "Chrome", "Application", "chrome.exe"),
      path.join(local, "Google", "Chrome", "Application", "chrome.exe"),
      path.join(pf86, "Microsoft", "Edge", "Application", "msedge.exe"),
      path.join(pf, "Microsoft", "Edge", "Application", "msedge.exe")
    );
  } else if (process.platform === "darwin") {
    candidates.push(
      "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
      "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
      "/Applications/Chromium.app/Contents/MacOS/Chromium"
    );
  } else {
    candidates.push(
      "/usr/bin/google-chrome",
      "/usr/bin/chromium",
      "/usr/bin/chromium-browser",
      "/usr/bin/microsoft-edge",
      "/snap/bin/chromium"
    );
  }

  return candidates.find((c) => fs.existsSync(c)) ?? null;
}

function render(browser, htmlPath, pngPath, dims, waitMs, profileDir) {
  const args = [
    "--headless=new",
    "--disable-gpu",
    "--hide-scrollbars",
    "--force-device-scale-factor=1",
    "--no-first-run",
    "--no-default-browser-check",
    "--disable-extensions",
    "--disable-background-networking",
    `--user-data-dir=${profileDir}`,
    `--window-size=${dims.w},${dims.h}`,
    `--virtual-time-budget=${waitMs}`,
    `--screenshot=${pngPath}`,
    pathToFileURL(htmlPath).href,
  ];

  const res = spawnSync(browser, args, {
    encoding: "utf-8",
    timeout: Math.max(30000, waitMs * 4),
    windowsHide: true,
  });

  if (!fs.existsSync(pngPath)) {
    const detail = (res.stderr ?? "").split("\n").filter(Boolean).slice(-3).join(" | ");
    throw new Error(`no se generó el PNG${detail ? ` — ${detail}` : ""}`);
  }
  return fs.statSync(pngPath).size;
}

function main() {
  const opts = parseArgs(process.argv.slice(2));

  if (!opts.folder) {
    console.error("Uso: node render.mjs <carpeta> [--ratio 4:5] [--solo 03] [--wait 5000]");
    process.exit(1);
  }

  const dims = RATIOS[opts.ratio];
  if (!dims) {
    console.error(`Ratio inválido: ${opts.ratio}. Usa ${Object.keys(RATIOS).join(", ")}`);
    process.exit(1);
  }

  const folder = path.resolve(opts.folder);
  const htmlDir = path.join(folder, "html");
  if (!fs.existsSync(htmlDir)) {
    console.error(`No existe ${htmlDir} — se esperan los slides en <carpeta>/html/*.html`);
    process.exit(1);
  }

  let files = fs
    .readdirSync(htmlDir)
    .filter((f) => f.toLowerCase().endsWith(".html"))
    .sort();

  if (opts.solo) {
    files = files.filter((f) => path.basename(f, path.extname(f)) === opts.solo);
    if (files.length === 0) {
      console.error(`No se encontró el slide "${opts.solo}" en ${htmlDir}`);
      process.exit(1);
    }
  }

  if (files.length === 0) {
    console.error(`No hay archivos .html en ${htmlDir}`);
    process.exit(1);
  }

  const browser = findBrowser();
  if (!browser) {
    console.error(
      "No encontré Chrome ni Edge. Instala uno, o define CARRUSEL_BROWSER con la ruta al ejecutable."
    );
    process.exit(1);
  }

  const pngDir = path.join(folder, opts.outDir);
  fs.mkdirSync(pngDir, { recursive: true });

  const profileDir = fs.mkdtempSync(path.join(os.tmpdir(), "carrusel-"));

  console.log(`Navegador: ${path.basename(browser)}`);
  console.log(`Formato:   ${opts.ratio} (${dims.w}x${dims.h})`);
  console.log(`Slides:    ${files.length}\n`);

  let ok = 0;
  const fallos = [];

  for (const file of files) {
    const htmlPath = path.join(htmlDir, file);
    const name = path.basename(file, path.extname(file)) + ".png";
    const pngPath = path.join(pngDir, name);
    try {
      const bytes = render(browser, htmlPath, pngPath, dims, opts.wait, profileDir);
      console.log(`  OK  ${name}  ${(bytes / 1024).toFixed(0)} KB`);
      ok++;
    } catch (err) {
      console.log(`  ERR ${name}  ${err.message}`);
      fallos.push(name);
    }
  }

  try {
    fs.rmSync(profileDir, { recursive: true, force: true });
  } catch {
    // perfil temporal, no es crítico
  }

  console.log(`\n${ok}/${files.length} slides renderizados → ${pngDir}`);
  if (fallos.length > 0) {
    console.log(`Fallaron: ${fallos.join(", ")}`);
    console.log("Si el texto salió con fuente de sistema, reintenta con --wait 8000.");
    process.exit(1);
  }
}

main();
