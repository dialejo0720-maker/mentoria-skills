// ─────────────────────────────────────────────────────────────
//  El chat para la página web del negocio y la portada del bot.
// ─────────────────────────────────────────────────────────────

// Esto es lo que se pega en la página del negocio con una sola línea:
// <script src="https://tu-bot.workers.dev/chat.js"></script>
export function guionChatWeb(origen, nombreBot) {
  return `(function () {
  var ORIGEN = ${JSON.stringify(origen)};
  var NOMBRE = ${JSON.stringify(nombreBot)};

  var visitante = localStorage.getItem('mibot_visitante');
  if (!visitante) {
    visitante = 'v' + Date.now() + Math.random().toString(36).slice(2, 8);
    localStorage.setItem('mibot_visitante', visitante);
  }

  var estilos = document.createElement('style');
  estilos.textContent =
    '#mibot-boton{position:fixed;right:20px;bottom:20px;width:62px;height:62px;border-radius:50%;' +
    'background:#1d61d4;color:#fff;border:none;cursor:pointer;font-size:27px;z-index:2147483000;' +
    'box-shadow:0 4px 16px rgba(0,0,0,.28)}' +
    '#mibot-caja{position:fixed;right:20px;bottom:94px;width:340px;max-width:calc(100vw - 40px);' +
    'height:470px;max-height:calc(100vh - 130px);background:#fff;border-radius:16px;display:none;' +
    'flex-direction:column;overflow:hidden;z-index:2147483000;box-shadow:0 10px 40px rgba(0,0,0,.24);' +
    'font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif}' +
    '#mibot-caja.abierta{display:flex}' +
    '#mibot-titulo{background:#1d61d4;color:#fff;padding:15px 18px;font-weight:700;font-size:16px}' +
    '#mibot-mensajes{flex:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:10px;background:#f4f6f9}' +
    '.mibot-b{max-width:80%;padding:11px 15px;border-radius:16px;font-size:15px;line-height:1.5;white-space:pre-wrap}' +
    '.mibot-b.yo{align-self:flex-end;background:#1d61d4;color:#fff;border-bottom-right-radius:4px}' +
    '.mibot-b.el{align-self:flex-start;background:#fff;color:#16202e;border:1px solid #d3dae4;border-bottom-left-radius:4px}' +
    '#mibot-pie{display:flex;gap:8px;padding:12px;border-top:1px solid #d3dae4;background:#fff}' +
    '#mibot-texto{flex:1;padding:11px 13px;font-size:15px;border:2px solid #d3dae4;border-radius:9px;font-family:inherit}' +
    '#mibot-enviar{padding:11px 17px;background:#1d61d4;color:#fff;border:none;border-radius:9px;cursor:pointer;font-weight:700}';
  document.head.appendChild(estilos);

  var boton = document.createElement('button');
  boton.id = 'mibot-boton';
  boton.setAttribute('aria-label', 'Abrir el chat');
  boton.textContent = '💬';

  var caja = document.createElement('div');
  caja.id = 'mibot-caja';
  caja.innerHTML =
    '<div id="mibot-titulo"></div>' +
    '<div id="mibot-mensajes"></div>' +
    '<form id="mibot-pie">' +
    '<input id="mibot-texto" autocomplete="off" placeholder="Escribe tu mensaje...">' +
    '<button id="mibot-enviar" type="submit">Enviar</button>' +
    '</form>';

  document.body.appendChild(boton);
  document.body.appendChild(caja);
  caja.querySelector('#mibot-titulo').textContent = NOMBRE;

  var mensajes = caja.querySelector('#mibot-mensajes');
  var forma = caja.querySelector('#mibot-pie');
  var entrada = caja.querySelector('#mibot-texto');
  var saludado = false;

  function decir(quien, texto) {
    var d = document.createElement('div');
    d.className = 'mibot-b ' + quien;
    d.textContent = texto;
    mensajes.appendChild(d);
    mensajes.scrollTop = mensajes.scrollHeight;
  }

  boton.addEventListener('click', function () {
    caja.classList.toggle('abierta');
    if (caja.classList.contains('abierta')) {
      if (!saludado) {
        saludado = true;
        decir('el', 'Hola, soy ' + NOMBRE + '. ¿En qué te ayudo?');
      }
      entrada.focus();
    }
  });

  forma.addEventListener('submit', function (e) {
    e.preventDefault();
    var texto = entrada.value.trim();
    if (!texto) return;
    decir('yo', texto);
    entrada.value = '';
    fetch(ORIGEN + '/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ texto: texto, visitante: visitante })
    })
      .then(function (r) { return r.json(); })
      .then(function (d) { decir('el', d.respuesta); })
      .catch(function () { decir('el', 'Se me fue la señal. ¿Lo intentas otra vez?'); });
  });
})();`;
}

// La portada: lo primero que ve el dueño cuando abre la dirección de su bot.
export function paginaInicio(nombreBot, nombreNegocio) {
  const limpio = (t) => String(t).replace(/</g, '&lt;');
  return `<!doctype html>
<html lang="es"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${limpio(nombreBot)}</title>
<style>
  body { font-family: -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    background: #f4f6f9; color: #16202e; display: flex; align-items: center;
    justify-content: center; min-height: 100vh; margin: 0; padding: 20px; }
  .caja { background: #fff; border: 1px solid #d3dae4; border-radius: 16px; padding: 40px;
    text-align: center; max-width: 430px; box-shadow: 0 1px 3px rgba(22,32,46,.09); }
  h1 { margin: 0 0 8px; font-size: 25px; }
  p { color: #4a5a6f; font-size: 17px; line-height: 1.6; }
  .ok { display: inline-block; background: #e3f5ec; color: #12734a; padding: 6px 14px;
    border-radius: 999px; font-weight: 700; font-size: 15px; margin-bottom: 18px; }
  a { display: inline-block; margin-top: 14px; padding: 14px 28px; background: #1d61d4;
    color: #fff; text-decoration: none; border-radius: 10px; font-weight: 700; font-size: 17px; }
</style>
</head><body>
  <div class="caja">
    <div class="ok">Funcionando</div>
    <h1>${limpio(nombreBot)} está despierto</h1>
    <p>El asistente de ${limpio(nombreNegocio)} está listo para atender.</p>
    <a href="/panel">Entrar a mi panel</a>
  </div>
</body></html>`;
}
