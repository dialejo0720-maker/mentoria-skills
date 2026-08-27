// ─────────────────────────────────────────────────────────────
//  WhatsApp (conexión directa con Meta, sin intermediarios).
// ─────────────────────────────────────────────────────────────

// Meta pide confirmar una sola vez que el webhook es tuyo.
export function responderVerificacion(url, env) {
  const modo = url.searchParams.get('hub.mode');
  const token = url.searchParams.get('hub.verify_token');
  const reto = url.searchParams.get('hub.challenge');
  if (modo === 'subscribe' && token && token === env.WHATSAPP_VERIFICAR) {
    return new Response(reto, { status: 200 });
  }
  return new Response('La palabra secreta no coincide', { status: 403 });
}

// Saca los mensajes de la caja que manda Meta (puede traer varios o ninguno).
export function leerMensajes(payload) {
  const encontrados = [];
  for (const entrada of payload?.entry || []) {
    for (const cambio of entrada?.changes || []) {
      const valor = cambio?.value;
      const nombres = {};
      for (const c of valor?.contacts || []) nombres[c.wa_id] = c?.profile?.name;
      for (const m of valor?.messages || []) {
        if (m.type !== 'text' || !m.text?.body) continue;
        encontrados.push({ id: m.id, de: m.from, nombre: nombres[m.from] || null, texto: m.text.body });
      }
    }
  }
  return encontrados;
}

export async function enviarWhatsApp(env, para, texto) {
  if (!env.WHATSAPP_TOKEN || !env.WHATSAPP_PHONE_ID) {
    console.log('WhatsApp no está conectado todavía: falta el token o el id del número.');
    return false;
  }
  // Sin número de versión: Meta usa la versión estable de tu app.
  const url = `https://graph.facebook.com/${env.WHATSAPP_PHONE_ID}/messages`;
  const r = await fetch(url, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${env.WHATSAPP_TOKEN}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      messaging_product: 'whatsapp',
      recipient_type: 'individual',
      to: para,
      type: 'text',
      text: { preview_url: false, body: texto },
    }),
  });
  if (!r.ok) {
    console.log('WhatsApp rechazó el envío:', r.status, await r.text());
    return false;
  }
  return true;
}
