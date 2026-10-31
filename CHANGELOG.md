# Cambios

## 1.1.0 — cuatro plugins nuevos

El marketplace pasa de 2 a 6 plugins. Las skills que se usan en todo el proceso de crear
y vender un producto digital ahora se instalan igual que `/ecosistema`.

- **producto-digital**: `/oferta-innegable`, `/check-oferta`, `/vsl` y `/digital-product-autopilot`
- **imagenes**: `/claude-banana`, prompts e imágenes para Nano Banana / Gemini
- **video**: `/video-con-vida` (17 efectos para videos a cámara y reglas de movimiento) y
  `/instalar-pizarra`, que baja `video-pizarra` de Horizontes IA desde su repositorio
  original y la ajusta para Windows (Python del `.venv`, bash en vez de zsh, carpeta temporal)
- **contenido**: `/guiones`, `/carrusel`, `/anuncio-ganador` y `/hook-generator`
- Las skills ya no dependen de rutas fijas: buscan sus scripts en su propia carpeta, así
  funcionan instaladas como plugin o a mano
- Los instaladores manuales encuentran cualquier skill del repositorio por su nombre y,
  si el nombre no existe, muestran la lista completa

## mi-bot 1.0.0

Primera versión de `/mi-bot`: bot de WhatsApp con IA para negocios, pensado para
gente que no programa.

- Flujo guiado de 6 fases, una pregunta por mensaje, en español sencillo
- El bot vive en la cuenta gratis de Cloudflare del dueño: **sin tarjeta de crédito**
- Cerebro gratis con la IA de Cloudflare (Llama 3.3 70B), con modelo de respaldo
  automático si el principal está saturado, y opción de subirlo a Claude
- Panel propio con 6 pestañas: Inicio, Conversaciones, Contactos, Mi negocio,
  Probar el bot y Conexiones — con letra y botones grandes, pensados para leerse bien
- Los datos del negocio viven en la base de datos, no en archivos: el dueño cambia
  precios y horarios desde el panel y el bot los aplica al instante, sin publicar de nuevo
- Captura de contactos automática (nombre, teléfono, interés) y descarga a Excel
- El dueño puede tomar el control de un chat y contestar él por WhatsApp
- Canales: prueba desde el panel, chat para página web (una línea de código) y
  WhatsApp por conexión directa con Meta
- Guías paso a paso para crear la cuenta de Cloudflare, conectar WhatsApp y resolver fallas
- El marketplace pasa a tener dos plugins: `ecosistema` y `mi-bot`, instalables por separado
- Los instaladores manuales ahora aceptan el nombre de la skill

## 1.0.0

Primera versión de `/ecosistema`.

- Proceso guiado de 10 fases (F0 encuadre → F9 iteración) con compuertas por fase
- Regla 80/20: qué se modela y qué se innova, con niveles de modelaje según experiencia
- F1 Espionaje: dónde buscar, umbrales de validación, cómo identificar el anuncio rentable,
  disección de anuncio y de landing, estructura invisible y GAP
- F2 Producto: 5 ideas con scoring, 6 patrones para bautizar el método y 4 tests del nombre
- F3 Keys: las 8 keys del VSL con mapa key → bloque de landing y key → ángulo de anuncio,
  stack de valor, precios por país y garantía
- F4 Landing: 14 bloques, plantilla HTML de un solo archivo, píxel de Meta, checkout de
  Hotmart y publicación en Vercel
- F5 Creativos: lectura de referencias del competidor, prompts de imagen (Nano Banana /
  Gemini) y de video (Veo / Sora / Kling), 5 ángulos, formatos, límites de copy de Meta y
  lista de rechazos frecuentes en LATAM
- F6 Campañas: CBO primero y ABO después, 6 países de LATAM, presupuestos mínimos,
  benchmarks, reglas de matar y escalar, tabla de diagnóstico
- F7 Producto: borrador, estructura de capítulos, producción del PDF y subida a Hotmart
- F8 Bumps y upsells: mapa de problemas siguientes, 6 arquetipos, precios y configuración
- F9 Iteración: los primeros 7 días, la decisión del día 5 y el ritmo semanal
- 7 plantillas de trabajo, incluida la landing HTML
- Instaladores para Windows, Mac y Linux, y soporte de instalación como plugin
