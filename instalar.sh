#!/usr/bin/env bash
# Instalador manual de las skills de la mentoria para Claude Code — Mac / Linux
# Solo hace falta si NO quieres instalarlas como plugin.
#
# Uso:  bash instalar.sh            -> instala ecosistema
#       bash instalar.sh mi-bot     -> instala mi-bot

set -euo pipefail

SKILL="${1:-ecosistema}"

echo ""
echo "  Instalador de la skill: $SKILL"
echo "  ----------------------------------"
echo ""

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# La skill puede estar en skills/<nombre>, en plugins/<nombre>/skills/<nombre>,
# o junto al script (si bajaron la carpeta suelta)
ORIGEN=""
for C in "$RAIZ/skills/$SKILL" "$RAIZ/plugins/$SKILL/skills/$SKILL" "$RAIZ"; do
  if [ -f "$C/SKILL.md" ]; then ORIGEN="$C"; break; fi
done

if [ -z "$ORIGEN" ]; then
  echo "  ERROR: no encuentro la skill '$SKILL'."
  echo "  Ejecuta el instalador desde la raiz de la carpeta descargada."
  echo "  Skills disponibles: ecosistema, mi-bot"
  echo ""
  exit 1
fi

CARPETA_SKILLS="$HOME/.claude/skills"
DESTINO="$CARPETA_SKILLS/$SKILL"

if [ "$ORIGEN" = "$DESTINO" ]; then
  echo "  La skill ya esta instalada en:"
  echo "  $DESTINO"
  echo ""
  echo "  Abre Claude Code y escribe /$SKILL"
  echo ""
  exit 0
fi

mkdir -p "$CARPETA_SKILLS"

if [ -d "$DESTINO" ]; then
  rm -rf "$DESTINO.backup"
  mv "$DESTINO" "$DESTINO.backup"
  echo "  Version anterior respaldada en $SKILL.backup"
fi

mkdir -p "$DESTINO"
cp -R "$ORIGEN/." "$DESTINO/"

if [ -f "$DESTINO/SKILL.md" ]; then
  REFS=$(ls -1 "$DESTINO/references" 2>/dev/null | wc -l | tr -d ' ')
  echo ""
  echo "  LISTO"
  echo "  Instalada en: $DESTINO"
  echo "  $REFS archivos de referencia."
  echo ""
  echo "  Como se usa:"
  echo "    1. Crea una carpeta para tu proyecto"
  echo "    2. Abrela con Claude Code"
  echo "    3. Escribe:  /$SKILL"
  echo ""
  echo "  Si Claude Code ya estaba abierto, cierralo y vuelvelo a abrir."
else
  echo ""
  echo "  ERROR: la copia no se completo."
  echo "  Copia manualmente la carpeta de la skill dentro de: $CARPETA_SKILLS"
  exit 1
fi

echo ""
