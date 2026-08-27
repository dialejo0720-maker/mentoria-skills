#!/usr/bin/env bash
# Instalador manual de la skill "ecosistema" para Claude Code — Mac / Linux
# Solo hace falta si NO quieres instalarla como plugin.
#
# Uso:  bash instalar.sh

set -euo pipefail

echo ""
echo "  Instalador de la skill: ecosistema"
echo "  ----------------------------------"
echo ""

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# La skill puede estar en skills/ecosistema (repo) o junto al script (carpeta suelta)
ORIGEN=""
for C in "$RAIZ/skills/ecosistema" "$RAIZ"; do
  if [ -f "$C/SKILL.md" ]; then ORIGEN="$C"; break; fi
done

if [ -z "$ORIGEN" ]; then
  echo "  ERROR: no encuentro SKILL.md."
  echo "  Ejecuta el instalador desde la raiz de la carpeta descargada."
  echo ""
  exit 1
fi

CARPETA_SKILLS="$HOME/.claude/skills"
DESTINO="$CARPETA_SKILLS/ecosistema"

if [ "$ORIGEN" = "$DESTINO" ]; then
  echo "  La skill ya esta instalada en:"
  echo "  $DESTINO"
  echo ""
  echo "  Abre Claude Code y escribe /ecosistema"
  echo ""
  exit 0
fi

mkdir -p "$CARPETA_SKILLS"

if [ -d "$DESTINO" ]; then
  rm -rf "$DESTINO.backup"
  mv "$DESTINO" "$DESTINO.backup"
  echo "  Version anterior respaldada en ecosistema.backup"
fi

mkdir -p "$DESTINO"
cp -R "$ORIGEN/." "$DESTINO/"

if [ -f "$DESTINO/SKILL.md" ]; then
  REFS=$(ls -1 "$DESTINO/references" 2>/dev/null | wc -l | tr -d ' ')
  PLAS=$(ls -1 "$DESTINO/plantillas" 2>/dev/null | wc -l | tr -d ' ')
  echo ""
  echo "  LISTO"
  echo "  Instalada en: $DESTINO"
  echo "  $REFS archivos de referencia, $PLAS plantillas."
  echo ""
  echo "  Como se usa:"
  echo "    1. Crea una carpeta para tu proyecto"
  echo "    2. Abrela con Claude Code"
  echo "    3. Escribe:  /ecosistema"
  echo ""
  echo "  Si Claude Code ya estaba abierto, cierralo y vuelvelo a abrir."
else
  echo ""
  echo "  ERROR: la copia no se completo."
  echo "  Copia manualmente la carpeta 'skills/ecosistema' dentro de: $CARPETA_SKILLS"
  exit 1
fi

echo ""
