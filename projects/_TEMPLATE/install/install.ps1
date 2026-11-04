# Generic installer skeleton. Edit $Tools and the Install section per app. Never put secret values here.
param([switch]$Check)
$ErrorActionPreference = 'Continue'
$root = Split-Path -Parent $PSScriptRoot
$Tools = @('git','node','npm')   # add python, uv, supabase, vercel as needed
$bad = 0
foreach ($t in $Tools) {
  if (Get-Command $t -ErrorAction SilentlyContinue) { Write-Host "OK      $t" }
  else { Write-Host "MISSING $t"; $bad++ }
}
if (Test-Path (Join-Path $root 'secrets\SECRETS-CHECKLIST.md')) { Write-Host "OK      secrets checklist found" }
else { Write-Host "MISSING secrets checklist"; $bad++ }
if ($Check) { Write-Host "Check done. Problems: $bad"; exit $bad }
# --- Install section (fill in per app) ---
# winget install --id OpenJS.NodeJS.LTS -e
# Push-Location "$root\app"; npm install; Pop-Location
Write-Host "Install finished. Next: fill secrets (see secrets\SECRETS-CHECKLIST.md), then run: .\install.ps1 -Check"
