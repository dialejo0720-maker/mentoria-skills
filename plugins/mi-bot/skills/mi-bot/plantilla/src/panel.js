// ─────────────────────────────────────────────────────────────
//  El panel: donde el dueño ve y maneja todo.
// ─────────────────────────────────────────────────────────────

import { pagina, paginaEntrar, escapar, nada, cuando } from './panel-vistas.js';
import {
  CAMPOS_NEGOCIO, leerNegocio, guardarNegocio, estadisticas,
  guardarMensaje, pausarBot,
} from './datos.js';
import { atender } from './atender.js';
import { enviarWhatsApp } from './whatsapp.js';

// ── Entrar y salir ──────────────────────────────────────────

async function huella(clave) {
  const datos = new TextEncoder().encode(`mi-bot|${clave}`);
  const hash = await crypto.subtle.digest('SHA-256', datos);
  return [...new Uint8Array(hash)].map((b) => b.toString(16).padStart(2, '0')).join('');
}

async function tienePase(request, env) {
  if (!env.CLAVE_PANEL) return false;
  const galletas = request.headers.get('Cookie') || '';
  const pase = galletas.match(/(?:^|;\s*)pase=([a-f0-9]{64})/);
  return !!pase && pase[1] === (await huella(env.CLAVE_PANEL));
}

const irA = (ruta) => new Response(null, { status: 303, headers: { Location: ruta } });

const html = (cuerpo, extra = {}) =>
  new Response(cuerpo, { headers: { 'Content-Type': 'text/html; charset=utf-8', ...extra } });

// ── El repartidor de rutas del panel ────────────────────────

export async function panel(request, env, url) {
  const ruta = url.pathname;

  if (ruta === '/panel/entrar' && request.method === 'POST') {
    const formulario = await request.formData();
    if (env.CLAVE_PANEL && formulario.get('clave') === env.CLAVE_PANEL) {
      const cookie = `pase=${await huella(env.CLAVE_PANEL)}; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=2592000`;
      return new Response(null, { status: 303, headers: { Location: '/panel', 'Set-Cookie': cookie } });
    }
    return html(paginaEntrar(true), { 'Cache-Control': 'no-store' });
  }

  if (!(await tienePase(request, env))) {
    return html(paginaEntrar(false), { 'Cache-Control': 'no-store' });
  }

  if (ruta === '/panel/salir') {
    return new Response(null, {
      status: 303,
      headers: { Location: '/panel', 'Set-Cookie': 'pase=; Path=/; Max-Age=0' },
    });
  }

  const chatDetalle = ruta.match(/^\/panel\/chats\/([0-9a-f-]{36})$/);
  const chatAccion = ruta.match(/^\/panel\/chats\/([0-9a-f-]{36})\/(responder|control)$/);
  const contactoAccion = ruta.match(/^\/panel\/contactos\/([0-9a-f-]{36})\/atendido$/);

  if (ruta === '/panel') return vistaInicio(env, url);
  if (ruta === '/panel/chats') return vistaChats(env);
  if (chatDetalle) return vistaChat(env, chatDetalle[1], url);
  if (chatAccion && request.method === 'POST') return accionChat(request, env, chatAccion[1], chatAccion[2]);
  if (ruta === '/panel/contactos') return vistaContactos(env, url);
  if (ruta === '/panel/contactos.csv') return descargarContactos(env);
  if (contactoAccion && request.method === 'POST') return marcarAtendido(env, contactoAccion[1]);
  if (ruta === '/panel/negocio' && request.method === 'POST') return guardarFormularioNegocio(request, env);
  if (ruta === '/panel/negocio') return vistaNegocio(env, url);
  if (ruta === '/panel/probar' && request.method === 'POST') return responderPrueba(request, env);
  if (ruta === '/panel/probar') return vistaProbar(env);
  if (ruta === '/panel/conexiones') return vistaConexiones(env, url);

  return irA('/panel');
}

// ── Inicio ──────────────────────────────────────────────────

async function vistaInicio(env, url) {
  const [numeros, negocio] = await Promise.all([estadisticas(env), leerNegocio(env)]);
  const { results } = await env.DB
    .prepare('SELECT id, nombre, usuario_id, canal, ultimo_mensaje, no_leidos FROM conversaciones ORDER BY ultimo_mensaje DESC LIMIT 5')
    .all();

  const faltantes = CAMPOS_NEGOCIO.filter((c) => !negocio[c.clave]?.trim());
  const avisoFaltantes = faltantes.length
    ? `<div class="aviso mal">Tu bot todavía no sabe ${faltantes.length === 1 ? 'una cosa' : `${faltantes.length} cosas`} de tu negocio.
       <a href="/panel/negocio">Completar ahora</a>.</div>`
    : '';

  const recientes = (results || []).length
    ? `<ul class="lista">${results.map((c) => `
        <li><a href="/panel/chats/${c.id}">
          <span class="quien">${escapar(c.nombre || c.usuario_id)}</span>
          ${c.no_leidos > 0 ? '<span class="marca nueva">nuevo</span>' : ''}
          <div class="ultimo">${escapar(c.canal)} · ${cuando(c.ultimo_mensaje)}</div>
        </a></li>`).join('')}</ul>`
    : nada('💬', 'Todavía no te ha escrito nadie. Cuando lo hagan, aparecen aquí.');

  return html(pagina({
    titulo: 'Inicio',
    activo: '/panel',
    nombreBot: env.NOMBRE_BOT,
    nombreNegocio: env.NOMBRE_NEGOCIO,
    contenido: `
      <h2>Cómo va tu bot</h2>
      <p class="sub">Esto es lo que pasó en las últimas 24 horas.</p>
      ${avisoFaltantes}
      <div class="numeros">
        <div class="numero"><div class="cifra">${numeros.personasHoy}</div><div class="etiqueta">personas escribieron hoy</div></div>
        <div class="numero"><div class="cifra">${numeros.mensajesHoy}</div><div class="etiqueta">mensajes en total</div></div>
        <div class="numero"><div class="cifra">${numeros.contactosSemana}</div><div class="etiqueta">contactos esta semana</div></div>
        <div class="numero"><div class="cifra">${numeros.sinLeer}</div><div class="etiqueta">chats sin leer</div></div>
      </div>
      <div class="tarjeta">
        <h3>Últimas conversaciones</h3>
        ${recientes}
      </div>
      <div class="fila">
        <a class="boton" href="/panel/probar">Probar el bot</a>
        <a class="boton gris" href="/panel/negocio">Cambiar los datos del negocio</a>
      </div>`,
  }));
}

// ── Conversaciones ──────────────────────────────────────────

async function vistaChats(env) {
  const { results } = await env.DB
    .prepare('SELECT id, nombre, usuario_id, canal, ultimo_mensaje, no_leidos, pausado_hasta FROM conversaciones ORDER BY ultimo_mensaje DESC LIMIT 100')
    .all();

  const lista = (results || []).length
    ? `<ul class="lista">${results.map((c) => `
        <li><a href="/panel/chats/${c.id}">
          <span class="quien">${escapar(c.nombre || c.usuario_id)}</span>
          ${c.no_leidos > 0 ? '<span class="marca nueva">nuevo</span>' : ''}
          ${c.pausado_hasta > Date.now() ? '<span class="marca no">lo atiendes tú</span>' : ''}
          <div class="ultimo">${escapar(c.canal)} · ${cuando(c.ultimo_mensaje)}</div>
        </a></li>`).join('')}</ul>`
    : nada('💬', 'Aquí van a aparecer todas las personas que le escriban a tu bot.');

  return html(pagina({
    titulo: 'Conversaciones',
    activo: '/panel/chats',
    nombreBot: env.NOMBRE_BOT,
    nombreNegocio: env.NOMBRE_NEGOCIO,
    contenido: `<h2>Conversaciones</h2>
      <p class="sub">Toca una para leerla completa o para contestar tú.</p>
      <div class="tarjeta">${lista}</div>`,
  }));
}

async function vistaChat(env, id, url) {
  const chat = await env.DB.prepare('SELECT * FROM conversaciones WHERE id = ?').bind(id).first();
  if (!chat) return irA('/panel/chats');

  await env.DB.prepare('UPDATE conversaciones SET no_leidos = 0 WHERE id = ?').bind(id).run();
  const { results } = await env.DB
    .prepare('SELECT quien, texto, creado FROM mensajes WHERE conversacion_id = ? ORDER BY creado LIMIT 200')
    .bind(id).all();

  const pausado = chat.pausado_hasta > Date.now();
  const burbujas = (results || []).map((m) => `
    <div class="burbuja ${m.quien}">${escapar(m.texto)}<span class="cuando">${cuando(m.creado)}</span></div>`).join('');

  const control = pausado
    ? `<form method="POST" action="/panel/chats/${id}/control">
         <input type="hidden" name="horas" value="0">
         <button class="boton verde" type="submit">Que vuelva a contestar el bot</button>
       </form>`
    : `<form method="POST" action="/panel/chats/${id}/control">
         <input type="hidden" name="horas" value="4">
         <button class="boton gris" type="submit">Contesto yo (4 horas)</button>
       </form>`;

  const puedeEscribir = chat.canal === 'whatsapp';

  return html(pagina({
    titulo: 'Conversación',
    activo: '/panel/chats',
    nombreBot: env.NOMBRE_BOT,
    nombreNegocio: env.NOMBRE_NEGOCIO,
    contenido: `
      <h2>${escapar(chat.nombre || chat.usuario_id)}</h2>
      <p class="sub">Por ${escapar(chat.canal)} · empezó ${cuando(chat.iniciada)}</p>
      ${url.searchParams.get('ok') ? '<div class="aviso ok">Listo, mensaje enviado.</div>' : ''}
      ${pausado ? '<div class="aviso mal">El bot está callado en este chat. Las respuestas las estás dando tú.</div>' : ''}
      <div class="tarjeta"><div class="chat">${burbujas || nada('💬', 'Sin mensajes todavía.')}</div></div>
      ${puedeEscribir ? `
      <div class="tarjeta">
        <h3>Escribir tú</h3>
        <form method="POST" action="/panel/chats/${id}/responder">
          <textarea name="texto" placeholder="Escribe aquí lo que quieres decirle..." required></textarea>
          <div style="margin-top:14px" class="fila">
            <button class="boton" type="submit">Enviar por WhatsApp</button>
            ${control}
          </div>
        </form>
      </div>` : `<div class="tarjeta"><h3>Tomar el control</h3>
        <p class="ayuda">Este chat es de prueba o de la página web, así que desde aquí no se puede escribir. En WhatsApp sí.</p>
        ${control}</div>`}
      <a class="boton gris" href="/panel/chats">Volver a la lista</a>`,
  }));
}

async function accionChat(request, env, id, accion) {
  const formulario = await request.formData();

  if (accion === 'control') {
    await pausarBot(env, id, Number(formulario.get('horas') || 0));
    return irA(`/panel/chats/${id}`);
  }

  const texto = String(formulario.get('texto') || '').trim();
  if (!texto) return irA(`/panel/chats/${id}`);

  const chat = await env.DB.prepare('SELECT * FROM conversaciones WHERE id = ?').bind(id).first();
  if (!chat) return irA('/panel/chats');

  const enviado = await enviarWhatsApp(env, chat.usuario_id, texto);
  if (!enviado) return irA(`/panel/chats/${id}`);

  await guardarMensaje(env, id, 'dueno', texto);
  // Si el dueño contesta, el bot se calla un rato para no pisarlo.
  if (!(chat.pausado_hasta > Date.now())) await pausarBot(env, id, 4);
  return irA(`/panel/chats/${id}?ok=1`);
}

// ── Contactos ───────────────────────────────────────────────

async function vistaContactos(env, url) {
  const { results } = await env.DB
    .prepare('SELECT * FROM contactos ORDER BY creado DESC LIMIT 200').all();

  const lista = (results || []).length
    ? `<ul class="lista">${results.map((c) => `
        <li style="padding:16px 4px">
          <span class="quien">${escapar(c.nombre || 'Sin nombre')}</span>
          <span class="marca ${c.atendido ? 'si' : 'no'}">${c.atendido ? 'atendido' : 'pendiente'}</span>
          <div class="ultimo" style="white-space:normal">
            ${escapar(c.telefono || 'sin teléfono')} · ${escapar(c.interes || '')} · ${cuando(c.creado)}
          </div>
          <div class="fila" style="margin-top:10px">
            ${c.telefono ? `<a class="boton gris" href="https://wa.me/${escapar(String(c.telefono).replace(/[^0-9]/g, ''))}">Escribirle por WhatsApp</a>` : ''}
            ${c.atendido ? '' : `<form method="POST" action="/panel/contactos/${c.id}/atendido">
              <button class="boton verde" type="submit">Ya lo atendí</button></form>`}
            ${c.conversacion_id ? `<a class="boton gris" href="/panel/chats/${c.conversacion_id}">Ver la conversación</a>` : ''}
          </div>
        </li>`).join('')}</ul>`
    : nada('📇', 'Cuando alguien deje su nombre y su teléfono, lo vas a encontrar aquí.');

  return html(pagina({
    titulo: 'Contactos',
    activo: '/panel/contactos',
    nombreBot: env.NOMBRE_BOT,
    nombreNegocio: env.NOMBRE_NEGOCIO,
    contenido: `<h2>Contactos</h2>
      <p class="sub">Gente interesada que dejó sus datos hablando con tu bot.</p>
      ${url.searchParams.get('ok') ? '<div class="aviso ok">Marcado como atendido.</div>' : ''}
      <div class="tarjeta">${lista}</div>
      <a class="boton gris" href="/panel/contactos.csv">Descargar la lista (Excel)</a>`,
  }));
}

async function marcarAtendido(env, id) {
  await env.DB.prepare('UPDATE contactos SET atendido = 1 WHERE id = ?').bind(id).run();
  return irA('/panel/contactos?ok=1');
}

async function descargarContactos(env) {
  const { results } = await env.DB
    .prepare('SELECT nombre, telefono, interes, notas, creado FROM contactos ORDER BY creado DESC').all();
  const celda = (v) => `"${String(v ?? '').replace(/"/g, '""')}"`;
  const filas = [['Nombre', 'Teléfono', 'Qué quería', 'Notas', 'Fecha'].join(',')];
  for (const c of results || []) {
    filas.push([c.nombre, c.telefono, c.interes, c.notas, new Date(c.creado).toLocaleString('es')].map(celda).join(','));
  }
  return new Response('﻿' + filas.join('\r\n'), {
    headers: {
      'Content-Type': 'text/csv; charset=utf-8',
      'Content-Disposition': 'attachment; filename="contactos.csv"',
    },
  });
}

// ── Mi negocio ──────────────────────────────────────────────

async function vistaNegocio(env, url) {
  const negocio = await leerNegocio(env);
  const campos = CAMPOS_NEGOCIO.map((c, i) => `
    <label class="${i === 0 ? 'primero' : ''}" for="${c.clave}">${escapar(c.titulo)}</label>
    <p class="ayuda">${escapar(c.ayuda)}</p>
    <textarea id="${c.clave}" name="${c.clave}">${escapar(negocio[c.clave] || '')}</textarea>`).join('');

  return html(pagina({
    titulo: 'Mi negocio',
    activo: '/panel/negocio',
    nombreBot: env.NOMBRE_BOT,
    nombreNegocio: env.NOMBRE_NEGOCIO,
    contenido: `
      <h2>Lo que tu bot sabe</h2>
      <p class="sub">Cambia lo que quieras y guarda. El bot lo usa en el siguiente mensaje: no hay que esperar nada ni volver a instalar.</p>
      ${url.searchParams.get('ok') ? '<div class="aviso ok">Guardado. Tu bot ya lo sabe.</div>' : ''}
      <form method="POST" action="/panel/negocio">
        <div class="tarjeta">${campos}</div>
        <button class="boton" type="submit">Guardar los cambios</button>
      </form>`,
  }));
}

async function guardarFormularioNegocio(request, env) {
  const formulario = await request.formData();
  const cambios = {};
  for (const campo of CAMPOS_NEGOCIO) cambios[campo.clave] = formulario.get(campo.clave) || '';
  await guardarNegocio(env, cambios);
  return irA('/panel/negocio?ok=1');
}

// ── Probar el bot ───────────────────────────────────────────

async function vistaProbar(env) {
  return html(pagina({
    titulo: 'Probar el bot',
    activo: '/panel/probar',
    nombreBot: env.NOMBRE_BOT,
    nombreNegocio: env.NOMBRE_NEGOCIO,
    contenido: `
      <h2>Habla con tu bot</h2>
      <p class="sub">Escríbele como si fueras un cliente. Así ves exactamente qué contesta.</p>
      <div class="tarjeta">
        <div class="chat" id="chat"></div>
        <form id="forma">
          <textarea id="texto" placeholder="Escribe aquí, por ejemplo: hola, ¿a qué hora abren?" required></textarea>
          <div style="margin-top:14px"><button class="boton" type="submit" id="enviar">Enviar</button></div>
        </form>
      </div>
      <script>
        const chat = document.getElementById('chat');
        const forma = document.getElementById('forma');
        const caja = document.getElementById('texto');
        const boton = document.getElementById('enviar');

        function burbuja(quien, texto) {
          const d = document.createElement('div');
          d.className = 'burbuja ' + quien;
          d.textContent = texto;
          chat.appendChild(d);
          d.scrollIntoView({ behavior: 'smooth', block: 'end' });
        }

        forma.addEventListener('submit', async (e) => {
          e.preventDefault();
          const texto = caja.value.trim();
          if (!texto) return;
          burbuja('cliente', texto);
          caja.value = '';
          boton.disabled = true;
          boton.textContent = 'Pensando...';
          try {
            const r = await fetch('/panel/probar', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({ texto }),
            });
            const datos = await r.json();
            burbuja('bot', datos.respuesta || 'No pude contestar. Revisa la pestaña Conexiones.');
          } catch (error) {
            burbuja('bot', 'Algo falló al contestar. Intenta otra vez.');
          }
          boton.disabled = false;
          boton.textContent = 'Enviar';
          caja.focus();
        });
      </script>`,
  }));
}

async function responderPrueba(request, env) {
  const { texto } = await request.json();
  // Pasa por el MISMO camino que un mensaje real de WhatsApp, para que lo
  // que veas aquí sea exactamente lo que va a vivir tu cliente.
  const respuesta = await atender(env, 'prueba', 'panel', 'Prueba desde el panel', texto);
  return Response.json({ respuesta: respuesta.texto });
}

// ── Conexiones ──────────────────────────────────────────────

async function vistaConexiones(env, url) {
  const base = url.origin;
  const whatsappListo = !!(env.WHATSAPP_TOKEN && env.WHATSAPP_PHONE_ID);
  const cerebro = env.CEREBRO === 'claude' && env.ANTHROPIC_API_KEY
    ? 'Claude (tu propia llave)'
    : 'La IA gratis de Cloudflare';

  return html(pagina({
    titulo: 'Conexiones',
    activo: '/panel/conexiones',
    nombreBot: env.NOMBRE_BOT,
    nombreNegocio: env.NOMBRE_NEGOCIO,
    contenido: `
      <h2>Conexiones</h2>
      <p class="sub">Por dónde puede atender tu bot.</p>

      <div class="tarjeta">
        <h3>Cerebro <span class="marca si">funcionando</span></h3>
        <p class="ayuda">Ahora mismo tu bot piensa con: <strong>${escapar(cerebro)}</strong></p>
      </div>

      <div class="tarjeta">
        <h3>Panel de prueba <span class="marca si">funcionando</span></h3>
        <p class="ayuda">Puedes hablar con tu bot desde la pestaña "Probar el bot".</p>
      </div>

      <div class="tarjeta">
        <h3>WhatsApp <span class="marca ${whatsappListo ? 'si' : 'no'}">${whatsappListo ? 'conectado' : 'sin conectar'}</span></h3>
        ${whatsappListo
          ? '<p class="ayuda">Tu bot está contestando en WhatsApp. Escríbele desde tu celular para comprobarlo.</p>'
          : `<p class="ayuda">Todavía no está conectado. Dile a Claude Code: <strong>"conecta mi bot a WhatsApp"</strong> y te lleva de la mano.</p>
             <p class="ayuda">Cuando Meta te pida estos dos datos, son estos:</p>
             <p class="ayuda">Dirección del webhook: <code>${escapar(base)}/whatsapp</code></p>`}
      </div>

      <div class="tarjeta">
        <h3>Chat en tu página web <span class="marca si">disponible</span></h3>
        <p class="ayuda">Si tienes página, pega esta línea en ella y aparece el chat abajo a la derecha:</p>
        <p><code>&lt;script src="${escapar(base)}/chat.js"&gt;&lt;/script&gt;</code></p>
      </div>

      <div class="tarjeta">
        <h3>Tu dirección</h3>
        <p class="ayuda">Esta es la dirección de tu bot. Guárdala:</p>
        <p><code>${escapar(base)}</code></p>
        <a class="boton gris" href="/panel/salir">Cerrar sesión</a>
      </div>`,
  }));
}
