// ─────────────────────────────────────────────────────────────
//  El corazón del bot.
//  Todo mensaje que llega (WhatsApp, página web o la prueba del
//  panel) pasa por aquí, para que en todos lados se comporte igual.
// ─────────────────────────────────────────────────────────────

import { pensar } from './cerebro.js';
import {
  abrirConversacion, guardarMensaje, historial, leerNegocio,
  guardarContacto, estaPausada,
} from './datos.js';

export async function atender(env, canal, usuarioId, nombre, texto) {
  const conversacion = await abrirConversacion(env, canal, usuarioId, nombre);
  await guardarMensaje(env, conversacion.id, 'cliente', texto);

  // Si el dueño tomó el control de este chat, el bot se queda callado.
  if (estaPausada(conversacion)) return { conversacionId: conversacion.id, texto: null };

  const negocio = await leerNegocio(env);
  const anteriores = await historial(env, conversacion.id, 20);
  const respuesta = await pensar(env, negocio, anteriores);

  await guardarMensaje(env, conversacion.id, 'bot', respuesta.texto);

  if (respuesta.contacto) {
    await guardarContacto(env, conversacion.id, {
      nombre: respuesta.contacto.nombre || nombre,
      telefono: respuesta.contacto.telefono || (canal === 'whatsapp' ? usuarioId : ''),
      interes: respuesta.contacto.interes,
      notas: '',
    });
  }

  // La persona pidió hablar con alguien de verdad: dejamos el chat marcado
  // como sin leer para que salte en el panel.
  if (respuesta.avisar) {
    await env.DB.prepare('UPDATE conversaciones SET no_leidos = no_leidos + 1 WHERE id = ?')
      .bind(conversacion.id).run();
  }

  return { conversacionId: conversacion.id, texto: respuesta.texto };
}
