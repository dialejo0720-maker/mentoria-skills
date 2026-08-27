# Instalador manual de las skills de la mentoria para Claude Code — Windows
# Solo hace falta si NO quieres instalarlas como plugin.
#
# Uso:  clic derecho -> Ejecutar con PowerShell        (instala ecosistema)
# O:    powershell -ExecutionPolicy Bypass -File .\instalar.ps1
# O:    powershell -ExecutionPolicy Bypass -File .\instalar.ps1 -Skill mi-bot

param(
    [string]$Skill = "ecosistema"
)

$ErrorActionPreference = "Stop"

function Pausa {
    # No falla si se ejecuta sin consola interactiva
    try { Read-Host "  Enter para salir" | Out-Null } catch { }
}

Write-Host ""
Write-Host "  Instalador de la skill: $Skill" -ForegroundColor Cyan
Write-Host "  ----------------------------------"
Write-Host ""

# Carpeta donde vive este script
$raiz = $PSScriptRoot
if ([string]::IsNullOrEmpty($raiz)) { $raiz = (Get-Location).Path }
$raiz = [System.IO.Path]::GetFullPath($raiz)

# La skill puede estar en skills\<nombre>, en plugins\<nombre>\skills\<nombre>,
# o junto al script (si bajaron la carpeta suelta)
$origen = $null
$candidatos = @(
    (Join-Path $raiz "skills\$Skill"),
    (Join-Path $raiz "plugins\$Skill\skills\$Skill"),
    $raiz
)
foreach ($c in $candidatos) {
    if (Test-Path (Join-Path $c "SKILL.md")) { $origen = [System.IO.Path]::GetFullPath($c); break }
}

if ($null -eq $origen) {
    Write-Host "  ERROR: no encuentro la skill '$Skill'." -ForegroundColor Red
    Write-Host "  Ejecuta el instalador desde la raiz de la carpeta descargada."
    Write-Host "  Skills disponibles: ecosistema, mi-bot"
    Write-Host ""
    Pausa
    exit 1
}

$carpetaSkills = Join-Path $env:USERPROFILE ".claude\skills"
$destino = [System.IO.Path]::GetFullPath((Join-Path $carpetaSkills $Skill))

# Ya esta instalada en el sitio correcto
if ($origen.TrimEnd('\') -ieq $destino.TrimEnd('\')) {
    Write-Host "  La skill ya esta instalada en:" -ForegroundColor Green
    Write-Host "  $destino"
    Write-Host ""
    Write-Host "  Abre Claude Code y escribe /$Skill"
    Write-Host ""
    Pausa
    exit 0
}

# Crear ~/.claude/skills si no existe
if (-not (Test-Path $carpetaSkills)) {
    New-Item -ItemType Directory -Path $carpetaSkills -Force | Out-Null
    Write-Host "  Carpeta de skills creada." -ForegroundColor DarkGray
}

# Respaldar instalacion anterior
if (Test-Path $destino) {
    $respaldo = "$destino.backup"
    if (Test-Path $respaldo) { Remove-Item -Path $respaldo -Recurse -Force }
    Move-Item -Path $destino -Destination $respaldo
    Write-Host "  Version anterior respaldada en $Skill.backup" -ForegroundColor Yellow
}

# Copiar
Copy-Item -Path $origen -Destination $destino -Recurse -Force

# Verificar
if (Test-Path (Join-Path $destino "SKILL.md")) {
    $refs = @(Get-ChildItem (Join-Path $destino "references") -File -ErrorAction SilentlyContinue).Count
    Write-Host ""
    Write-Host "  LISTO" -ForegroundColor Green
    Write-Host "  Instalada en: $destino"
    Write-Host "  $refs archivos de referencia."
    Write-Host ""
    Write-Host "  Como se usa:" -ForegroundColor Cyan
    Write-Host "    1. Crea una carpeta para tu proyecto"
    Write-Host "    2. Abrela con Claude Code"
    Write-Host "    3. Escribe:  /$Skill"
    Write-Host ""
    Write-Host "  Si Claude Code ya estaba abierto, cierralo y vuelvelo a abrir."
} else {
    Write-Host ""
    Write-Host "  ERROR: la copia no se completo." -ForegroundColor Red
    Write-Host "  Copia manualmente la carpeta de la skill dentro de:"
    Write-Host "  $carpetaSkills"
}

Write-Host ""
Pausa
