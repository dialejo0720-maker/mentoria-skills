// ─────────────────────────────────────────────────────────────
//  La memoria del bot: guardar y leer de la base de datos.
// ─────────────────────────────────────────────────────────────

const ahora = () => Date.now();
const nuevoId = () => crypto.randomUUID();

// Los datos de tu negocio que el bot usa para contestar.
// Todos se editan desde el panel, sin tocar código ni volver a publicar.
export const CAMPOS_NEGOCIO = [
  { clave: 'que_hace', titulo: 'A qué se dedica tu negocio', ayuda: 'En una o dos frases, como se lo dirías a un vecino.' },
  { clave: 'ofrece', titulo: 'Qué vendes y a qué precio', ayuda: 'Una cosa por renglón. Ejemplo: Corte de cabello — $25.000' },
  { clave: 'horario', titulo: 'Horario de atención', ayuda: 'Ejemplo: Lunes a sábado de 9 a 7. Domingos cerrado.' },
  { clave: 'ubicacion', titulo: 'Dónde estás', ayuda: 'Dirección o zona. Si atiendes a domicilio, dilo aquí.' },
  { clave: 'telefono', titulo: 'Teléfono de contacto', ayuda: 'El número al que quieres que llame la gente.' },
  { clave: 'web', titulo: 'Página web o redes', ayuda: 'Si no tienes, déjalo vacío.' },
  { clave: 'pagos', titulo: 'Cómo te pueden pagar', ayuda: 'Ejemplo: efectivo, transferencia, tarjeta.' },
  { clave: 'preguntas', titulo: 'Lo que más te pregunta la gente', ayuda: 'Escribe las preguntas y sus respuestas. Una por renglón.' },
  { clave: 'reglas', titulo: 'Lo que el bot NO debe hacer', ayuda: 'Ejemplo: no prometer descuentos, no dar la dirección exacta antes de confirmar.' },
  { clave: 'tono', titulo: 'Cómo quieres que hable', ayuda: 'Ejemplo: cercano y con "usted", o relajado y de "tú".' },
];

export async function leerNegocio(env) {
  const { results } = await env.DB.prepare('SELECT clave, valor FROM negocio').all();
  const datos = {};
  for (const fila of results || []) datos[fila.clave] = fila.valor;
  return datos;
}

export async function guardarNegocio(env, cambios) {
  const t = ahora();
  const consultas = Object.entries(cambios).map(([clave, valor]) =>
    env.DB.prepare(
      'INSERT INTO negocio (clave, valor, actualizado) VALUES (?, ?, ?) ' +
      'ON CONFLICT(clave) DO UPDATE SET valor = excluded.valor, actualizado = excluded.actualizado'
    ).bind(clave, String(valor ?? ''), t)
  );
  if (consultas.length) await env.DB.batch(consultas);
}

// Busca la conversación de esta persona; si es la primera vez, la crea.
export async function abrirConversacion(env, canal, usuarioId, nombre) {
  const t = ahora();
  const existente = await env.DB
    .prepare('SELECT * FROM conversaciones WHERE canal = ? AND usuario_id = ?')
    .bind(canal, usuarioId).first();

  if (existente) {
    await env.DB.prepare('UPDATE conversaciones SET ultimo_mensaje = ?, nombre = COALESCE(?, nombre) WHERE id = ?')
      .bind(t, nombre || null, existente.id).run();
    return { ...existente, ultimo_mensaje: t };
  }

  const id = nuevoId();
  try {
    await env.DB.prepare(
      'INSERT INTO conversaciones (id, canal, usuario_id, nombre, iniciada, ultimo_mensaje) VALUES (?, ?, ?, ?, ?, ?)'
    ).bind(id, canal, usuarioId, nombre || null, t, t).run();
  } catch (error) {
    // Si la persona mandó dos mensajes al mismo tiempo, otra copia del bot pudo
    // haber creado la conversación un instante antes. Nos quedamos con esa.
    const creadaAparte = await env.DB
      .prepare('SELECT * FROM conversaciones WHERE canal = ? AND usuario_id = ?')
      .bind(canal, usuarioId).first();
    if (creadaAparte) return creadaAparte;
    throw error;
  }
  return { id, canal, usuario_id: usuarioId, nombre, iniciada: t, ultimo_mensaje: t, pausado_hasta: null };
}

export async function guardarMensaje(env, conversacionId, quien, texto) {
  await env.DB.prepare('INSERT INTO mensajes (id, conversacion_id, quien, texto, creado) VALUES (?, ?, ?, ?, ?)')
    .bind(nuevoId(), conversacionId, quien, texto, ahora()).run();
  if (quien === 'cliente') {
    await env.DB.prepare('UPDATE conversaciones SET no_leidos = no_leidos + 1, ultimo_mensaje = ? WHERE id = ?')
      .bind(ahora(), conversacionId).run();
  }
}

export async function historial(env, conversacionId, limite = 20) {
  const { results } = await env.DB
    .prepare('SELECT quien, texto FROM mensajes WHERE conversacion_id = ? ORDER BY creado DESC LIMIT ?')
    .bind(conversacionId, limite).all();
  return (results || []).reverse();
}

// ¿El dueño tomó el control de este chat?
export function estaPausada(conversacion) {
  return !!(conversacion?.pausado_hasta && conversacion.pausado_hasta > ahora());
}

export async function pausarBot(env, conversacionId, horas) {
  const hasta = horas > 0 ? ahora() + horas * 3600 * 1000 : null;
  await env.DB.prepare('UPDATE conversaciones SET pausado_hasta = ? WHERE id = ?')
    .bind(hasta, conversacionId).run();
}

export async function guardarContacto(env, conversacionId, { nombre, telefono, interes, notas }) {
  await env.DB.prepare(
    'INSERT INTO contactos (id, conversacion_id, nombre, telefono, interes, notas, creado) VALUES (?, ?, ?, ?, ?, ?, ?)'
  ).bind(nuevoId(), conversacionId, nombre || null, telefono || null, interes || '', notas || '', ahora()).run();
}

// Evita contestar dos veces si WhatsApp reenvía el mismo mensaje.
export async function yaVisto(env, id) {
  try {
    await env.DB.prepare('INSERT INTO vistos (id, creado) VALUES (?, ?)').bind(id, ahora()).run();
    return false;
  } catch (error) {
    // Solo es "repetido" si chocó con uno que ya estaba guardado. Cualquier otro
    // problema de la base de datos se avisa: si no, el bot se quedaría mudo sin
    // que nadie sepa por qué.
    if (/UNIQUE|PRIMARY KEY|constraint/i.test(error.message || '')) return true;
    console.log('No pude anotar el mensaje como visto:', error.message);
    return false;
  }
}

export async function estadisticas(env) {
  const hoy = ahora() - 24 * 3600 * 1000;
  const semana = ahora() - 7 * 24 * 3600 * 1000;
  const [personasHoy, mensajesHoy, contactosSemana, sinLeer] = await env.DB.batch([
    env.DB.prepare('SELECT COUNT(*) AS n FROM conversaciones WHERE ultimo_mensaje > ?').bind(hoy),
    env.DB.prepare('SELECT COUNT(*) AS n FROM mensajes WHERE creado > ?').bind(hoy),
    env.DB.prepare('SELECT COUNT(*) AS n FROM contactos WHERE creado > ?').bind(semana),
    env.DB.prepare('SELECT COUNT(*) AS n FROM conversaciones WHERE no_leidos > 0'),
  ]);
  return {
    personasHoy: personasHoy.results?.[0]?.n ?? 0,
    mensajesHoy: mensajesHoy.results?.[0]?.n ?? 0,
    contactosSemana: contactosSemana.results?.[0]?.n ?? 0,
    sinLeer: sinLeer.results?.[0]?.n ?? 0,
  };
}
