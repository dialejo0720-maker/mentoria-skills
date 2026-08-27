-- La memoria de tu bot. El asistente corre esto una sola vez, al instalar.

-- Todo lo que tu bot sabe de tu negocio (editable desde el panel, sin tocar código)
CREATE TABLE IF NOT EXISTS negocio (
  clave TEXT PRIMARY KEY,
  valor TEXT NOT NULL,
  actualizado INTEGER NOT NULL
);

-- Una fila por cada persona que le escribe a tu bot
CREATE TABLE IF NOT EXISTS conversaciones (
  id TEXT PRIMARY KEY,
  canal TEXT NOT NULL,              -- 'whatsapp' | 'web' | 'prueba'
  usuario_id TEXT NOT NULL,         -- el teléfono o el id del visitante
  nombre TEXT,
  iniciada INTEGER NOT NULL,
  ultimo_mensaje INTEGER NOT NULL,
  pausado_hasta INTEGER,            -- si el dueño tomó el control, hasta cuándo
  no_leidos INTEGER DEFAULT 0
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_conv_unica ON conversaciones(canal, usuario_id);
CREATE INDEX IF NOT EXISTS idx_conv_reciente ON conversaciones(ultimo_mensaje DESC);

-- Cada mensaje, de ida y de vuelta
CREATE TABLE IF NOT EXISTS mensajes (
  id TEXT PRIMARY KEY,
  conversacion_id TEXT NOT NULL,
  quien TEXT NOT NULL,              -- 'cliente' | 'bot' | 'dueno'
  texto TEXT NOT NULL,
  creado INTEGER NOT NULL,
  FOREIGN KEY (conversacion_id) REFERENCES conversaciones(id) ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS idx_msg_conv ON mensajes(conversacion_id, creado);
CREATE INDEX IF NOT EXISTS idx_msg_fecha ON mensajes(creado);

-- Los clientes interesados que el bot alcanzó a identificar
CREATE TABLE IF NOT EXISTS contactos (
  id TEXT PRIMARY KEY,
  conversacion_id TEXT,
  nombre TEXT,
  telefono TEXT,
  interes TEXT,
  notas TEXT,
  atendido INTEGER DEFAULT 0,
  creado INTEGER NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_contactos_fecha ON contactos(creado DESC);

-- Evita contestar dos veces el mismo mensaje de WhatsApp
CREATE TABLE IF NOT EXISTS vistos (
  id TEXT PRIMARY KEY,
  creado INTEGER NOT NULL
);
