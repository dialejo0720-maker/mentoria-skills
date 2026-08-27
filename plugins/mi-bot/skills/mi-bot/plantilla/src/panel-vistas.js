// ─────────────────────────────────────────────────────────────
//  Cómo se ve el panel.
//  Letra grande, botones grandes y palabras normales.
// ─────────────────────────────────────────────────────────────

export const escapar = (t) => String(t ?? '')
  .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
  .replace(/"/g, '&quot;').replace(/'/g, '&#39;');

const ESTILOS = `
  :root {
    --tinta: #16202e;
    --tinta-suave: #4a5a6f;
    --fondo: #f4f6f9;
    --tarjeta: #ffffff;
    --borde: #d3dae4;
    --acento: #1d61d4;
    --acento-suave: #e8f0fd;
    --verde: #12734a;
    --verde-suave: #e3f5ec;
    --rojo: #b4231f;
    --rojo-suave: #fdeceb;
    --sombra: 0 1px 3px rgba(22, 32, 46, .09);
  }
  * { box-sizing: border-box; }
  body {
    margin: 0; background: var(--fondo); color: var(--tinta);
    font-family: -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 18px; line-height: 1.6;
  }
  .cabecera {
    background: var(--tarjeta); border-bottom: 1px solid var(--borde);
    padding: 16px 20px; position: sticky; top: 0; z-index: 10;
  }
  .cabecera h1 { margin: 0 0 4px; font-size: 21px; }
  .cabecera p { margin: 0; color: var(--tinta-suave); font-size: 15px; }
  .menu { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 14px; }
  .menu a {
    display: block; padding: 11px 18px; border-radius: 10px; text-decoration: none;
    color: var(--tinta); background: var(--fondo); border: 1px solid var(--borde);
    font-weight: 600; font-size: 16px;
  }
  .menu a.activo { background: var(--acento); border-color: var(--acento); color: #fff; }
  .menu a:hover:not(.activo) { background: var(--acento-suave); border-color: var(--acento); }
  main { max-width: 900px; margin: 0 auto; padding: 24px 20px 80px; }
  h2 { font-size: 24px; margin: 0 0 6px; }
  .sub { color: var(--tinta-suave); margin: 0 0 24px; font-size: 17px; }
  .tarjeta {
    background: var(--tarjeta); border: 1px solid var(--borde); border-radius: 14px;
    padding: 22px; margin-bottom: 18px; box-shadow: var(--sombra);
  }
  .tarjeta h3 { margin: 0 0 12px; font-size: 19px; }
  .numeros { display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 14px; margin-bottom: 26px; }
  .numero { background: var(--tarjeta); border: 1px solid var(--borde); border-radius: 14px; padding: 20px; box-shadow: var(--sombra); }
  .numero .cifra { font-size: 42px; font-weight: 700; line-height: 1.1; }
  .numero .etiqueta { color: var(--tinta-suave); font-size: 16px; margin-top: 4px; }
  label { display: block; font-weight: 600; margin: 20px 0 4px; font-size: 17px; }
  label.primero { margin-top: 0; }
  .ayuda { color: var(--tinta-suave); font-size: 15px; margin: 0 0 8px; }
  input[type=text], input[type=password], textarea, select {
    width: 100%; padding: 13px 14px; font-size: 17px; font-family: inherit;
    border: 2px solid var(--borde); border-radius: 10px; background: #fff; color: var(--tinta);
  }
  textarea { min-height: 110px; resize: vertical; }
  input:focus, textarea:focus, select:focus { outline: 3px solid var(--acento-suave); border-color: var(--acento); }
  .boton {
    display: inline-block; padding: 14px 26px; font-size: 17px; font-weight: 700;
    background: var(--acento); color: #fff; border: none; border-radius: 10px;
    cursor: pointer; font-family: inherit; text-decoration: none; min-height: 50px;
  }
  .boton:hover { filter: brightness(1.08); }
  .boton.gris { background: var(--tarjeta); color: var(--tinta); border: 2px solid var(--borde); }
  .boton.verde { background: var(--verde); }
  .boton.rojo { background: var(--rojo); }
  .fila { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; }
  .aviso { padding: 15px 18px; border-radius: 10px; margin-bottom: 18px; font-size: 17px; }
  .aviso.ok { background: var(--verde-suave); color: var(--verde); border: 1px solid var(--verde); }
  .aviso.mal { background: var(--rojo-suave); color: var(--rojo); border: 1px solid var(--rojo); }
  .lista { list-style: none; padding: 0; margin: 0; }
  .lista li { border-bottom: 1px solid var(--borde); }
  .lista li:last-child { border-bottom: none; }
  .lista a { display: block; padding: 16px 4px; text-decoration: none; color: var(--tinta); }
  .lista a:hover { background: var(--acento-suave); }
  .lista .quien { font-weight: 700; font-size: 18px; }
  .lista .ultimo { color: var(--tinta-suave); font-size: 16px; margin-top: 2px;
    overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .marca { display: inline-block; padding: 3px 11px; border-radius: 999px; font-size: 14px; font-weight: 700; }
  .marca.nueva { background: var(--acento); color: #fff; }
  .marca.si { background: var(--verde-suave); color: var(--verde); }
  .marca.no { background: var(--rojo-suave); color: var(--rojo); }
  .chat { display: flex; flex-direction: column; gap: 12px; margin-bottom: 20px; }
  .burbuja { max-width: 78%; padding: 13px 17px; border-radius: 18px; font-size: 17px; white-space: pre-wrap; word-break: break-word; }
  .burbuja.cliente { align-self: flex-start; background: var(--fondo); border: 1px solid var(--borde); border-bottom-left-radius: 5px; }
  .burbuja.bot { align-self: flex-end; background: var(--acento); color: #fff; border-bottom-right-radius: 5px; }
  .burbuja.dueno { align-self: flex-end; background: var(--verde); color: #fff; border-bottom-right-radius: 5px; }
  .cuando { font-size: 13px; opacity: .75; margin-top: 5px; display: block; }
  .vacio { text-align: center; padding: 44px 20px; color: var(--tinta-suave); font-size: 17px; }
  .vacio .icono { font-size: 46px; display: block; margin-bottom: 10px; }
  code { background: var(--fondo); padding: 3px 7px; border-radius: 6px; font-size: 15px; word-break: break-all; }
  .paso { display: flex; gap: 14px; margin-bottom: 16px; align-items: flex-start; }
  .paso .n { flex: 0 0 34px; height: 34px; border-radius: 50%; background: var(--acento);
    color: #fff; font-weight: 700; display: flex; align-items: center; justify-content: center; }
  @media (max-width: 640px) {
    body { font-size: 17px; }
    main { padding: 18px 14px 70px; }
    .menu a { flex: 1 1 calc(50% - 8px); text-align: center; }
    .numero .cifra { font-size: 36px; }
  }
`;

const SECCIONES = [
  ['/panel', 'Inicio'],
  ['/panel/chats', 'Conversaciones'],
  ['/panel/contactos', 'Contactos'],
  ['/panel/negocio', 'Mi negocio'],
  ['/panel/probar', 'Probar el bot'],
  ['/panel/conexiones', 'Conexiones'],
];

export function pagina({ titulo, activo, nombreBot, nombreNegocio, contenido }) {
  const menu = SECCIONES.map(([ruta, nombre]) =>
    `<a href="${ruta}" class="${ruta === activo ? 'activo' : ''}">${nombre}</a>`
  ).join('');
  return `<!doctype html>
<html lang="es"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${escapar(titulo)}</title>
<style>${ESTILOS}</style>
</head><body>
<div class="cabecera">
  <h1>${escapar(nombreBot)}, tu asistente</h1>
  <p>${escapar(nombreNegocio)}</p>
  <nav class="menu">${menu}</nav>
</div>
<main>${contenido}</main>
</body></html>`;
}

export function paginaEntrar(error) {
  return `<!doctype html>
<html lang="es"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Entrar al panel</title>
<style>${ESTILOS}
  .centro { max-width: 420px; margin: 12vh auto; padding: 0 20px; }
</style>
</head><body>
<div class="centro">
  <div class="tarjeta">
    <h2>Tu panel</h2>
    <p class="sub">Escribe tu contraseña para entrar.</p>
    ${error ? '<div class="aviso mal">Esa contraseña no es. Inténtalo otra vez.</div>' : ''}
    <form method="POST" action="/panel/entrar">
      <label class="primero" for="clave">Contraseña</label>
      <input type="password" id="clave" name="clave" autofocus autocomplete="current-password">
      <div style="margin-top:18px"><button class="boton" type="submit">Entrar</button></div>
    </form>
  </div>
</div>
</body></html>`;
}

export function nada(icono, texto) {
  return `<div class="vacio"><span class="icono">${icono}</span>${escapar(texto)}</div>`;
}

export function cuando(ms) {
  const min = Math.floor((Date.now() - ms) / 60000);
  if (min < 1) return 'hace un momento';
  if (min < 60) return `hace ${min} min`;
  const h = Math.floor(min / 60);
  if (h < 24) return `hace ${h} ${h === 1 ? 'hora' : 'horas'}`;
  const d = Math.floor(h / 24);
  if (d === 1) return 'ayer';
  if (d < 30) return `hace ${d} días`;
  return new Date(ms).toLocaleDateString('es');
}
