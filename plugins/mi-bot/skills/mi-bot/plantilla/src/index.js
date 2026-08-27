// ─────────────────────────────────────────────────────────────
//  La puerta de entrada de tu bot.
//  Aquí llegan los mensajes de WhatsApp, de tu página y del panel.
// ─────────────────────────────────────────────────────────────

import { panel } from './panel.js';
import { atender } from './atender.js';
import { responderVerificacion, leerMensajes, enviarWhatsApp } from './whatsapp.js';
import { guionChatWeb, paginaInicio } from './web.js';
import { yaVisto } from './datos.js';

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const ruta = url.pathname;

    try {
      if (ruta === '/panel' || ruta.startsWith('/panel/')) {
        return await panel(request, env, url);
      }

      // WhatsApp: Meta confirma el webhook con un GET y manda los mensajes por POST.
      if (ruta === '/whatsapp') {
        if (request.method === 'GET') return responderVerificacion(url, env);
        if (request.method === 'POST') {
          const payload = await request.json().catch(() => ({}));
          // Le decimos "recibido" a Meta de inmediato y contestamos aparte,
          // porque si tardamos vuelve a mandar el mismo mensaje.
          ctx.waitUntil(atenderWhatsApp(env, payload));
          return new Response('ok');
        }
      }

      // El chat para tu página web
      if (ruta === '/chat.js') {
        return new Response(guionChatWeb(url.origin, env.NOMBRE_BOT || 'Asistente'), {
          headers: { 'Content-Type': 'application/javascript; charset=utf-8', 'Cache-Control': 'public, max-age=300' },
        });
      }
      if (ruta === '/chat' && request.method === 'POST') {
        return await atenderWeb(request, env);
      }
      if (ruta === '/chat' && request.method === 'OPTIONS') {
        return new Response(null, { headers: cabecerasWeb() });
      }

      if (ruta === '/') {
        return new Response(paginaInicio(env.NOMBRE_BOT || 'Tu bot', env.NOMBRE_NEGOCIO || ''), {
          headers: { 'Content-Type': 'text/html; charset=utf-8' },
        });
      }

      return new Response('Aquí no hay nada. Tu panel está en /panel', { status: 404 });
    } catch (error) {
      console.log('Algo falló:', error.stack || error.message);
      return new Response('Algo falló de nuestro lado. Ya quedó anotado.', { status: 500 });
    }
  },
};

async function atenderWhatsApp(env, payload) {
  for (const mensaje of leerMensajes(payload)) {
    try {
      if (await yaVisto(env, mensaje.id)) continue;
      const { texto } = await atender(env, 'whatsapp', mensaje.de, mensaje.nombre, mensaje.texto);
      if (texto) await enviarWhatsApp(env, mensaje.de, texto);
    } catch (error) {
      console.log('No pude contestar un mensaje de WhatsApp:', error.stack || error.message);
    }
  }
}

const cabecerasWeb = () => ({
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
});

async function atenderWeb(request, env) {
  const { texto, visitante } = await request.json().catch(() => ({}));
  if (!texto || !visitante) {
    return Response.json({ respuesta: 'No entendí el mensaje.' }, { headers: cabecerasWeb() });
  }
  const respuesta = await atender(env, 'web', String(visitante).slice(0, 60), null, String(texto).slice(0, 2000));
  return Response.json(
    { respuesta: respuesta.texto || 'En un momento te contesta una persona del negocio.' },
    { headers: cabecerasWeb() }
  );
}
