# full-cycle-emails is a docs-only app: there is nothing to install. Supports -Check.
param([switch]$Check)
$root = Split-Path -Parent $PSScriptRoot
$spec = Join-Path $root 'docs\CLAUDE_MAX_BUILD_PROMPT.md'
if (Test-Path $spec) { Write-Host 'OK      docs only: master spec found (docs\CLAUDE_MAX_BUILD_PROMPT.md). Nothing to install.'; exit 0 }
Write-Host 'MISSING docs\CLAUDE_MAX_BUILD_PROMPT.md'; exit 1
