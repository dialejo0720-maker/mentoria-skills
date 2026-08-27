// ─────────────────────────────────────────────────────────────
//  El cerebro: aquí el bot decide qué contestar.
//
//  Arranca con la IA GRATIS de Cloudflare (no pide tarjeta).
//  Si algún día pones tu llave de Claude, usa Claude sin cambiar nada más.
// ─────────────────────────────────────────────────────────────

import Anthropic from '@anthropic-ai/sdk';

const MODELO_GRATIS = '@cf/meta/llama-3.3-70b-instruct-fp8-fast';
const MODELO_GRATIS_RESPALDO = '@cf/meta/llama-3.1-8b-instruct-fp8';

// Arma las instrucciones del bot con los datos que el dueño llenó en el panel.
export function instrucciones(env, negocio) {
  const nombreBot = env.NOMBRE_BOT || 'Ana';
  const nombreNegocio = env.NOMBRE_NEGOCIO || 'el negocio';
  const seccion = (titulo, valor) => (valor && valor.trim() ? `\n## ${titulo}\n${valor.trim()}\n` : '');

  return `Eres ${nombreBot}, quien atiende por chat a los clientes de ${nombreNegocio}.
Hablas como una persona real del negocio, no como un robot.

# Cómo contestas
- Respuestas CORTAS: dos o tres frases. Esto es un chat, no un correo.
- Un tema a la vez. Si necesitas varios datos, pídelos de uno en uno.
- Nada de listas con viñetas ni negritas: se ven mal en WhatsApp.
- Si te saludan, saluda y pregunta en qué ayudas. No sueltes todo el menú de golpe.

# La regla más importante
Solo puedes usar la información que está aquí abajo. Si te preguntan algo que no
aparece (un precio que no está, si hay domicilio a una zona que no se menciona,
una fecha), NO lo inventes. Di que lo confirmas con el negocio y ofrece pasar
el mensaje. Inventar un dato es el peor error que puedes cometer.
${seccion('Qué es el negocio', negocio.que_hace)}${seccion('Lo que vendemos y los precios', negocio.ofrece)}${seccion('Horario', negocio.horario)}${seccion('Dónde estamos', negocio.ubicacion)}${seccion('Teléfono', negocio.telefono)}${seccion('Página web y redes', negocio.web)}${seccion('Formas de pago', negocio.pagos)}${seccion('Preguntas frecuentes', negocio.preguntas)}${seccion('Cosas que NO debes hacer', negocio.reglas)}${seccion('Tono con el que debes hablar', negocio.tono)}
# Dos avisos que puedes usar
Estas dos líneas son señales internas para el negocio. SIEMPRE van al final y
SIEMPRE después de haberle escrito algo a la persona. Nunca contestes solo con
una señal: primero el mensaje para el cliente, y en el último renglón la señal.

Cuando la persona muestre interés real de comprar o de que la contacten, pídele
su nombre y su teléfono. Cuando ya te los haya dado, confírmale que quedó
anotado y que lo van a contactar, y recién ahí cierra con esta línea:
[CONTACTO] nombre | teléfono | qué quería

Cuando la persona pida hablar con una persona de verdad, o esté molesta, o
pregunte algo que no puedes resolver, termina tu mensaje con esta línea:
[AVISAR]

Esas dos líneas son señales internas. El cliente nunca las ve. Nunca las
expliques ni las menciones.`;
}

// Le pregunta a la IA y devuelve el texto de la respuesta.
export async function pensar(env, negocio, conversacion) {
  const sistema = instrucciones(env, negocio);
  const mensajes = conversacion.map((m) => ({
    role: m.quien === 'cliente' ? 'user' : 'assistant',
    content: m.texto,
  }));

  const usarClaude = env.CEREBRO === 'claude' && env.ANTHROPIC_API_KEY;
  const crudo = usarClaude
    ? await pensarConClaude(env, sistema, mensajes)
    : await pensarGratis(env, sistema, mensajes);

  return separarSeñales(crudo);
}

async function pensarGratis(env, sistema, mensajes) {
  const cuerpo = { messages: [{ role: 'system', content: sistema }, ...mensajes], max_tokens: 800 };
  try {
    const r = await env.IA.run(MODELO_GRATIS, cuerpo);
    return (r.response || '').trim();
  } catch (error) {
    // Si el modelo grande está saturado, contestamos con el pequeño antes que quedarnos callados.
    console.log('Cerebro gratis: fallo el modelo principal, uso el de respaldo.', error.message);
    const r = await env.IA.run(MODELO_GRATIS_RESPALDO, cuerpo);
    return (r.response || '').trim();
  }
}

async function pensarConClaude(env, sistema, mensajes) {
  const cliente = new Anthropic({ apiKey: env.ANTHROPIC_API_KEY });
  const respuesta = await cliente.messages.create({
    model: env.MODELO_CLAUDE || 'claude-opus-5',
    max_tokens: 1000,
    output_config: { effort: 'low' },
    system: [{ type: 'text', text: sistema, cache_control: { type: 'ephemeral' } }],
    messages: mensajes,
  });
  if (respuesta.stop_reason === 'refusal') {
    return 'Disculpa, eso no lo puedo responder por aquí. ¿Te paso con alguien del negocio?';
  }
  return respuesta.content.filter((b) => b.type === 'text').map((b) => b.text).join('').trim();
}

// Saca las señales internas del texto para que el cliente nunca las vea.
function separarSeñales(texto) {
  let limpio = texto;
  let contacto = null;
  let avisar = false;

  const marcaContacto = limpio.match(/\[CONTACTO\]\s*([^\n]*)/i);
  if (marcaContacto) {
    const partes = marcaContacto[1].split('|').map((p) => p.trim());
    contacto = { nombre: partes[0] || '', telefono: partes[1] || '', interes: partes[2] || '' };
    limpio = limpio.replace(marcaContacto[0], '');
  }

  if (/\[AVISAR\]/i.test(limpio)) {
    avisar = true;
    limpio = limpio.replace(/\[AVISAR\]/gi, '');
  }

  limpio = limpio.replace(/\n{3,}/g, '\n\n').trim();
  // Si la IA solo mandó la señal y se le olvidó escribirle al cliente,
  // decimos algo con sentido en vez de dejarlo sin respuesta.
  if (!limpio) {
    limpio = contacto
      ? 'Listo, ya quedaron anotados tus datos. Te contactamos muy pronto.'
      : 'Déjame confirmarlo y te cuento enseguida.';
  }
  return { texto: limpio, contacto, avisar };
}
