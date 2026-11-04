<#
  Scraper Tools: installer (safe to re-run). Run via install\INSTALL.cmd. Flags:
    -Check / -DryRun   show what would happen; change nothing
    -Uninstall         nothing to remove (there are no shortcuts); prints a note
  Restores: gmaps.exe (gosom), yt-dlp.exe, scrapetube venv, crawl4ai venv + Chromium.
  No secrets are needed by any of these tools. Network use: winget, GitHub release downloads, PyPI, Chromium download.
#>
param([Alias('Check')][switch]$DryRun, [switch]$Uninstall)
$ErrorActionPreference = 'Continue'
$Root = Split-Path -Parent $PSScriptRoot
$App  = Join-Path $Root 'app'
$Results = New-Object System.Collections.ArrayList
$GmapsVer = '1.18.1'; $ScrapetubeVer = '2.6.0'; $Crawl4aiVer = '0.9.5'
$GmapsUrl = "https://github.com/gosom/google-maps-scraper/releases/download/v$GmapsVer/google_maps_scraper-$GmapsVer-windows-amd64.exe"
$YtUrl    = 'https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe'
$YtSums   = 'https://github.com/yt-dlp/yt-dlp/releases/latest/download/SHA2-256SUMS'

function Note($s, $w, $d = '') { [void]$Results.Add([pscustomobject]@{ Status = $s; Step = $w; Detail = $d }); Write-Host ("[{0}] {1} {2}" -f $s, $w, $d) }
function Refresh-Path { $env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User') }
function Have($c) { [bool](Get-Command $c -ErrorAction SilentlyContinue) }
function Run-Step($label, [scriptblock]$act, $would) {
  if ($DryRun) { Note 'DRY' $label "would: $would"; return }
  try { $global:LASTEXITCODE = 0; & $act; if ($LASTEXITCODE -and $LASTEXITCODE -ne 0) { throw "exit code $LASTEXITCODE" }; Note 'OK' $label }
  catch { Note 'FAIL' $label $_.Exception.Message }
}

Write-Host "Scraper Tools installer. Folder: $Root"
if ($DryRun) { Write-Host '*** CHECK / DRY RUN: nothing will be changed ***' }
if ($Uninstall) { Write-Host 'Nothing to uninstall: this app creates no shortcuts. To remove the tools, delete the app\ virtual environments (.venv folders).'; exit 0 }
if (-not (Test-Path $App)) { Note 'FAIL' 'Folder layout' "app\ missing under $Root. Copy the WHOLE scraper-tools folder."; exit 1 }

# 1. Python
Refresh-Path
if (Have 'python') { Note 'OK' 'Python' ((& python --version 2>&1) -join '') }
elseif (Have 'winget') { Run-Step 'Install Python 3.12' { winget install --id Python.Python.3.12 -e --silent --accept-package-agreements --accept-source-agreements; Refresh-Path } 'winget install Python.Python.3.12' }
else { Note 'FAIL' 'Python' 'missing and winget not available; install Python 3.12 from python.org' }
if (-not $DryRun -and -not (Have 'python')) { Note 'WARN' 'Python' 'installed but not on PATH yet: close this window and run INSTALL.cmd again' }

# 2. Binaries
$gm = Join-Path $App 'gosom-google-maps-scraper\gmaps.exe'
if (Test-Path $gm) { Note 'OK' 'gmaps.exe (gosom)' "present, $([int]((Get-Item $gm).Length/1MB)) MB" }
else { Run-Step 'Download gmaps.exe (gosom v1.18.1)' { New-Item -ItemType Directory -Force (Split-Path $gm) | Out-Null; Invoke-WebRequest $GmapsUrl -OutFile $gm -UseBasicParsing } "download $GmapsUrl" }

$yt = Join-Path $App 'yt-dlp\yt-dlp.exe'
if (Test-Path $yt) { Note 'OK' 'yt-dlp.exe' ((& $yt --version 2>&1) -join '') }
else {
  Run-Step 'Download yt-dlp.exe (latest)' {
    New-Item -ItemType Directory -Force (Split-Path $yt) | Out-Null
    Invoke-WebRequest $YtUrl -OutFile $yt -UseBasicParsing
    $raw = (Invoke-WebRequest $YtSums -UseBasicParsing).Content; if ($raw -is [byte[]]) { $raw = [Text.Encoding]::UTF8.GetString($raw) }; $sums = $raw -split "`n"
    $want = ($sums | Where-Object { $_ -match '\s\*?yt-dlp\.exe\s*$' } | Select-Object -First 1) -replace '\s.*', ''
    $got = (Get-FileHash $yt -Algorithm SHA256).Hash
    if (-not $want -or $want -ne $got.ToLower()) { Remove-Item $yt -Force; throw 'SHA-256 mismatch against official SHA2-256SUMS; file deleted' }
  } "download $YtUrl and verify it against SHA2-256SUMS"
}

# 3. Python venvs
function Ensure-Venv($name, $pkg, $folder, $importName) {
  $dir = Join-Path $App $folder; $py = Join-Path $dir '.venv\Scripts\python.exe'
  if (Test-Path $py) { & $py -c "import $importName" 2>$null; if ($LASTEXITCODE -eq 0) { Note 'OK' "$name venv" 'import works'; return } }
  if (-not (Have 'python') -and -not $DryRun) { Note 'FAIL' "$name venv" 'Python not available'; return }
  Run-Step "Create $name venv + pip install $pkg" {
    New-Item -ItemType Directory -Force $dir | Out-Null
    if (-not (Test-Path $py)) { & python -m venv (Join-Path $dir '.venv') }
    & $py -m pip install --quiet $pkg
  } "python -m venv $folder\.venv; pip install $pkg"
}
Ensure-Venv 'scrapetube' "scrapetube==$ScrapetubeVer" 'scrapetube' 'scrapetube'
Ensure-Venv 'crawl4ai' "crawl4ai==$Crawl4aiVer" 'crawl4ai' 'crawl4ai'

# 4. Chromium for crawl4ai (crawl4ai-setup is idempotent)
$setup = Join-Path $App 'crawl4ai\.venv\Scripts\crawl4ai-setup.exe'
if ($DryRun) { Note 'DRY' 'crawl4ai-setup (Chromium)' 'would run crawl4ai-setup once' }
elseif (Test-Path $setup) {
  $mark = Join-Path $App 'crawl4ai\.setup-done'
  if (Test-Path $mark) { Note 'SKIP' 'crawl4ai-setup' 'already done (delete crawl4ai\.setup-done to redo)' }
  else { Run-Step 'crawl4ai-setup (downloads Chromium)' { $env:CRAWL4AI_NO_CLOUD_NOTICE = '1'; & $setup; if ($LASTEXITCODE -eq 0) { New-Item $mark -ItemType File | Out-Null } } 'run crawl4ai-setup' }
} else { Note 'SKIP' 'crawl4ai-setup' 'crawl4ai not installed' }

# 5. Health check (offline, no scraping)
if (-not $DryRun) {
  if (Test-Path $yt) { Note 'OK' 'Health: yt-dlp' ((& $yt --version 2>&1) -join '') }
  if (Test-Path $gm) { Note $(if ((Get-Item $gm).Length -gt 50MB) { 'OK' } else { 'WARN' }) 'Health: gmaps.exe size' "$([int]((Get-Item $gm).Length/1MB)) MB (expected ~58 MB)" }
}

Write-Host "`n===== CHECKLIST ====="
foreach ($r in $Results) { Write-Host ("{0,-5} {1}  {2}" -f $r.Status, $r.Step, $r.Detail) }
$fails = @($Results | Where-Object { $_.Status -eq 'FAIL' }).Count
if ($fails -gt 0) { Write-Host "$fails step(s) FAILED. See GUIDE\04-TROUBLESHOOTING.md."; exit 1 }
Write-Host 'Done. No keys needed. Usage examples: docs\INTEGRATION.md'
