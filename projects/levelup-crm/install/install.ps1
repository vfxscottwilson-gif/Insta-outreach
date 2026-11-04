<#
  LevelUp CRM installer. Windows 10, PowerShell 5.1, no extra modules. Safe to run again (idempotent).

  Modes:
    -Check   Changes nothing. Reports PASS / MISSING for every tool, file and setting.
    (none)   Setup: installs missing Git / Node, restores app\.env from secrets, npm ci, npm run build.
    -Cloud   Puts the app online: Supabase link, migrations, functions, secrets, Vercel deploy.
             Asks "Type YES" before every step that changes anything in the cloud.
    -Local   Starts the app on this PC (npm run dev).

  Secret VALUES are never printed or written to install\install.log. Only key NAMES are shown.
#>
param([switch]$Check, [switch]$Cloud, [switch]$Local)

$ErrorActionPreference = 'Continue'
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$Install = $PSScriptRoot
$Root    = Split-Path $Install -Parent
$App     = Join-Path $Root 'app'
$Secrets = Join-Path $Root 'secrets'
$EnvFile = Join-Path $App '.env'
$EnvBak  = Join-Path $Secrets 'app.env.backup'
$GoogleSa = Join-Path $Secrets 'google-sa.json'
$LogFile = Join-Path $Install 'install.log'
$Functions = @('admin-users', 'sheets-sync', 'login-guard')
$script:Problems = 0

# ---------- output helpers (screen + log; never pass secret values to these) ----------
function Log([string]$t) { Add-Content -Path $LogFile -Value ("{0}  {1}" -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $t) }
function Say([string]$t)     { Write-Host $t; Log $t }
function Pass([string]$t)    { Write-Host "  PASS     $t" -ForegroundColor Green; Log "PASS     $t" }
function Missing([string]$t) { Write-Host "  MISSING  $t" -ForegroundColor Yellow; Log "MISSING  $t"; $script:Problems++ }
function Fail([string]$t)    { Write-Host "  FAIL     $t" -ForegroundColor Red; Log "FAIL     $t"; $script:Problems++ }
function Info([string]$t)    { Write-Host "  INFO     $t" -ForegroundColor Cyan; Log "INFO     $t" }
function Title([string]$t)   { Write-Host ""; Write-Host "== $t ==" -ForegroundColor White; Log "== $t ==" }

function Ask-Yes([string]$what) {
  Write-Host ""
  Write-Host "  NEXT: $what" -ForegroundColor Magenta
  $a = Read-Host "  Type YES to do this (anything else skips it)"
  $ok = ($a -ceq 'YES')
  Log ("ASK      {0} -> {1}" -f $what, $(if ($ok) { 'YES' } else { 'skipped' }))
  return $ok
}

function Refresh-Path {
  $env:Path = [Environment]::GetEnvironmentVariable('Path', 'Machine') + ';' + [Environment]::GetEnvironmentVariable('Path', 'User')
}

# Reads KEY=VALUE lines into a hashtable. Values stay in memory only.
function Read-EnvFile([string]$file) {
  $h = @{}
  if (Test-Path $file) {
    foreach ($line in Get-Content $file) {
      if ($line -match '^\s*([A-Z0-9_]+)\s*=\s*(.*)$') { $h[$Matches[1]] = $Matches[2].Trim().Trim('"').Trim("'") }
    }
  }
  return $h
}

function Get-Ref($envh) {
  if ($envh['VITE_SUPABASE_URL'] -match '^https://([a-z0-9]{20})\.supabase\.co') { return $Matches[1] }
  return $null
}

function Get-NodeMajor {
  if (-not (Get-Command node -ErrorAction SilentlyContinue)) { return 0 }
  $v = (& node -v) 2>$null
  if ($v -match '^v(\d+)\.') { return [int]$Matches[1] }
  return 0
}

# Runs a program in a folder; returns its exit code. Output goes to the screen only (never to the log).
function Run([string]$dir, [string]$exe, [string[]]$argList) {
  Log ("RUN      {0} {1}  (in {2})" -f $exe, ($argList -join ' '), $dir)
  Push-Location $dir
  try { & $exe @argList | Out-Host; $code = $LASTEXITCODE } finally { Pop-Location }  # Out-Host: keep output out of the return value
  Log "EXIT     $code"
  return $code
}

function Test-Url([string]$url) {
  try { Invoke-WebRequest -Uri $url -Method Head -UseBasicParsing -TimeoutSec 15 | Out-Null; return $true }
  catch { return ($null -ne $_.Exception.Response) }  # any HTTP answer (even 403/404) means the site is reachable
}

$RequiredKeys = @('VITE_SUPABASE_URL', 'VITE_SUPABASE_ANON_KEY')
$CloudKeys    = @('SUPABASE_ACCESS_TOKEN', 'ADMIN_EMAIL')

# ---------------------------------- CHECK ----------------------------------
function Invoke-Check {
  Title 'Tools'
  if (Get-Command git -ErrorAction SilentlyContinue) { Pass ("Git " + ((& git --version) -replace 'git version ', '')) }
  else { Missing 'Git (Setup installs it with winget)' }

  $major = Get-NodeMajor
  if ($major -ge 20) { Pass ("Node.js " + (& node -v)) }
  elseif ($major -gt 0) { Missing ("Node.js 20 or newer (found " + (& node -v) + ")") }
  else { Missing 'Node.js 20 or newer (Setup installs Node LTS with winget)' }

  if (Get-Command npm -ErrorAction SilentlyContinue) { Pass ("npm " + (& npm -v)) } else { Missing 'npm (comes with Node.js)' }

  if (Get-Command winget -ErrorAction SilentlyContinue) { Pass 'winget (used by Setup to install tools)' }
  else { Info 'winget not found: install Git and Node.js by hand from git-scm.com and nodejs.org' }

  $sbCmd = Join-Path $App 'node_modules\.bin\supabase.cmd'
  if ((Test-Path $sbCmd) -and (Get-Command npx -ErrorAction SilentlyContinue)) {
    Push-Location $App; $v = (& npx --no-install supabase --version) 2>$null; Pop-Location
    if ($LASTEXITCODE -eq 0) { Pass "Supabase CLI $v (npx, from app\node_modules)" } else { Missing 'Supabase CLI (run Setup: npm ci installs it)' }
  } else { Missing 'Supabase CLI (run Setup: npm ci installs it into app\node_modules)' }

  if (Get-Command vercel -ErrorAction SilentlyContinue) { Pass ("Vercel CLI " + ((& vercel --version) 2>$null | Select-Object -Last 1)) }
  else { Info 'Vercel CLI not installed globally: -Cloud will use "npx vercel" instead' }

  Title 'Files'
  foreach ($f in @(
      @{ p = $App;      n = 'app\ (source code)' },
      @{ p = (Join-Path $App '.git'); n = 'app\.git (code history)' },
      @{ p = $EnvBak;   n = 'secrets\app.env.backup' },
      @{ p = $GoogleSa; n = 'secrets\google-sa.json (Google Sheet access)' },
      @{ p = $EnvFile;  n = 'app\.env (Setup copies it from secrets\app.env.backup)' },
      @{ p = (Join-Path $App '.vercel\project.json'); n = 'app\.vercel\project.json (link to the Vercel project)' },
      @{ p = (Join-Path $App 'node_modules'); n = 'app\node_modules (Setup creates it with npm ci)' })) {
    if (Test-Path $f.p) { Pass $f.n } else { Missing $f.n }
  }

  Title 'Settings in app\.env (names only, values are never shown)'
  $envh = Read-EnvFile $(if (Test-Path $EnvFile) { $EnvFile } else { $EnvBak })
  foreach ($k in $RequiredKeys) { if ($envh[$k]) { Pass "$k (needed to run the app)" } else { Missing "$k (needed to run the app)" } }
  foreach ($k in $CloudKeys)    { if ($envh[$k]) { Pass "$k (needed for -Cloud)" } else { Missing "$k (needed for -Cloud)" } }
  if (Get-Ref $envh) { Pass 'Supabase project ref found in VITE_SUPABASE_URL' } else { Missing 'Supabase project ref (VITE_SUPABASE_URL must look like https://<ref>.supabase.co)' }

  Title 'Internet'
  foreach ($u in @('https://supabase.com', 'https://api.supabase.com', 'https://vercel.com', 'https://registry.npmjs.org')) {
    if (Test-Url $u) { Pass "can reach $u" } else { Fail "cannot reach $u (check the internet connection or firewall)" }
  }
}

# ---------------------------------- SETUP ----------------------------------
function Invoke-Setup {
  Title 'Step 1 of 4: tools'
  $hasWinget = [bool](Get-Command winget -ErrorAction SilentlyContinue)
  if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    if ($hasWinget) {
      Say '  Installing Git (a window may ask for permission: click Yes)...'
      & winget install --id Git.Git -e --scope user --silent --accept-package-agreements --accept-source-agreements
      if ($LASTEXITCODE -ne 0) { & winget install --id Git.Git -e --silent --accept-package-agreements --accept-source-agreements }
      Refresh-Path
    }
    if (Get-Command git -ErrorAction SilentlyContinue) { Pass 'Git installed' } else { Fail 'Git missing: install it from https://git-scm.com/download/win, then run INSTALL again' }
  } else { Pass 'Git already installed' }

  if ((Get-NodeMajor) -lt 20) {
    if ($hasWinget) {
      Say '  Installing Node.js LTS (a window may ask for permission: click Yes)...'
      & winget install --id OpenJS.NodeJS.LTS -e --scope user --silent --accept-package-agreements --accept-source-agreements
      if ($LASTEXITCODE -ne 0) { & winget install --id OpenJS.NodeJS.LTS -e --silent --accept-package-agreements --accept-source-agreements }
      Refresh-Path
    }
    if ((Get-NodeMajor) -ge 20) { Pass ("Node.js " + (& node -v) + " installed") }
    else { Fail 'Node.js 20+ missing: install the LTS version from https://nodejs.org, CLOSE this window, then run INSTALL again'; return }
  } else { Pass ("Node.js " + (& node -v) + " already installed") }

  Title 'Step 2 of 4: settings file'
  if (Test-Path $EnvFile) { Pass 'app\.env already there (left as it is)' }
  elseif (Test-Path $EnvBak) { Copy-Item $EnvBak $EnvFile; Pass 'app\.env restored from secrets\app.env.backup' }
  else { Fail 'No app\.env and no secrets\app.env.backup: see secrets\SECRETS-CHECKLIST.md'; return }

  Title 'Step 3 of 4: app packages (npm ci, takes a few minutes)'
  if ((Run $App 'npm' @('ci')) -ne 0) { Fail 'npm ci failed (read the red text above; often the internet dropped: run INSTALL again)'; return }
  Pass 'packages installed'

  Title 'Step 4 of 4: build the app'
  if ((Run $App 'npm' @('run', 'build')) -ne 0) { Fail 'build failed (read the text above)'; return }
  Pass 'app built into app\dist'

  Title 'Next steps (you do these)'
  Say '  1. To open the app on this PC:   double-click INSTALL.cmd with -Local, or run:  install\install.ps1 -Local'
  Say '  2. To put it online (Supabase + Vercel):  run  install\install.ps1 -Cloud'
  Say '     It needs a browser sign-in to Vercel once ("vercel login") and SUPABASE_ACCESS_TOKEN in app\.env.'
  Say '  3. To move the data to a NEW Supabase project: see database\README.md'
}

# ---------------------------------- CLOUD ----------------------------------
function Invoke-Cloud {
  $envh = Read-EnvFile $EnvFile
  $ref = Get-Ref $envh
  Title 'Cloud: checks first'
  if (-not (Test-Path (Join-Path $App 'node_modules\.bin\supabase.cmd'))) { Fail 'Run Setup first (double-click INSTALL.cmd)'; return }
  if (-not $ref) {
    Fail 'No Supabase project in app\.env (VITE_SUPABASE_URL).'
    Say  '  A brand-new Supabase project is made in the browser: https://supabase.com/dashboard/new'
    Say  '  Then copy its Project URL and anon key into app\.env (VITE_SUPABASE_URL, VITE_SUPABASE_ANON_KEY) and run -Cloud again.'
    return
  }
  if (-not $envh['SUPABASE_ACCESS_TOKEN']) {
    Fail 'SUPABASE_ACCESS_TOKEN missing in app\.env. Make one at https://supabase.com/dashboard/account/tokens (see secrets\SECRETS-CHECKLIST.md)'
    return
  }
  $env:SUPABASE_ACCESS_TOKEN = $envh['SUPABASE_ACCESS_TOKEN']  # this window only, never printed
  Pass "Supabase project ref found (ends in ...$($ref.Substring(16)))"

  if (Ask-Yes 'Link this folder to the Supabase project (press Enter if it asks for a database password)') {
    if ((Run $App 'npx' @('supabase', 'link', '--project-ref', $ref)) -eq 0) { Pass 'linked' } else { Fail 'link failed' }
  }

  if (Ask-Yes 'Apply database migrations (supabase db push --include-all). Changes the cloud database structure.') {
    if ((Run $App 'npx' @('supabase', 'db', 'push', '--include-all')) -eq 0) { Pass 'migrations applied' } else { Fail 'db push failed' }
  }

  if (Ask-Yes ("Deploy server functions: " + ($Functions -join ', '))) {
    foreach ($fn in $Functions) {
      if ((Run $App 'npx' @('supabase', 'functions', 'deploy', $fn, '--project-ref', $ref)) -eq 0) { Pass "function $fn deployed" } else { Fail "function $fn failed" }
    }
  }

  if (Ask-Yes 'Set server secrets (ADMIN_EMAIL, GOOGLE_SA_JSON, and PASSWORD_VAULT_KEY only if the project has none yet). Values are not shown.') {
    $lines = @()
    foreach ($k in @('ADMIN_EMAIL', 'LOGIN_ALLOWED_ORIGINS', 'BOOTSTRAP_TOKEN', 'ADMIN_INITIAL_PASSWORD')) {
      if ($envh[$k]) { $lines += "$k=$($envh[$k])"; Info "will set $k" }
    }
    if (Test-Path $GoogleSa) {
      $sa = (Get-Content $GoogleSa -Raw | ConvertFrom-Json | ConvertTo-Json -Compress -Depth 5)
      $lines += "GOOGLE_SA_JSON=$sa"; Info 'will set GOOGLE_SA_JSON (from secrets\google-sa.json)'
    } else { Info 'secrets\google-sa.json missing: Google Sheet sync will not work until it is added' }
    Push-Location $App
    $existing = (& npx supabase secrets list --project-ref $ref) 2>$null | Out-String
    Pop-Location
    # PASSWORD_VAULT_KEY: the backup file in secrets\ is the source of truth. Never generate a second key while it exists.
    $vaultFile = Join-Path $Root 'secrets\password-vault-key.txt'
    if (Test-Path $vaultFile) {
      $vk = (Get-Content $vaultFile -Raw).Trim()
      if ($vk -match '^[A-Za-z0-9+/]{43}=$') { $lines += "PASSWORD_VAULT_KEY=$vk"; Info 'will set PASSWORD_VAULT_KEY from secrets\password-vault-key.txt' }
      else { Fail 'secrets\password-vault-key.txt is not a valid key: fix it before continuing'; return }
    } elseif ($existing -notmatch 'PASSWORD_VAULT_KEY') {
      # New project, no backup yet: make one key, save the backup FIRST, then set it.
      $bytes = New-Object byte[] 32; [Security.Cryptography.RandomNumberGenerator]::Create().GetBytes($bytes)
      $vk = [Convert]::ToBase64String($bytes)
      Set-Content -Path $vaultFile -Value $vk -NoNewline -Encoding ascii
      $lines += "PASSWORD_VAULT_KEY=$vk"; Info 'will set a new PASSWORD_VAULT_KEY (backup written to secrets\password-vault-key.txt: back it up)'
    } else { Info 'WARNING: PASSWORD_VAULT_KEY is set in the project but secrets\password-vault-key.txt is missing: left as it is (no backup!)' }
    $tmpDir = Join-Path $env:TEMP ("lvl-" + [guid]::NewGuid().ToString('N'))
    New-Item -ItemType Directory -Path $tmpDir | Out-Null
    $tmp = Join-Path $tmpDir 'secret.env'
    try {
      [IO.File]::WriteAllText($tmp, ($lines -join "`n") + "`n")
      Push-Location $App
      & npx supabase secrets set --env-file $tmp --project-ref $ref *> $null   # output hidden: it could echo values
      $code = $LASTEXITCODE
      Pop-Location
      Log "EXIT     supabase secrets set -> $code"
      if ($code -eq 0) { Pass 'server secrets set' } else { Fail 'secrets set failed (check the token and run -Cloud again)' }
    } finally { Remove-Item -LiteralPath $tmpDir -Recurse -Force -ErrorAction SilentlyContinue }
  }

  Title 'Build'
  if ((Run $App 'npm' @('run', 'build')) -ne 0) { Fail 'build failed: fix it before deploying'; return }
  Pass 'build ok'

  Title 'Vercel (website hosting)'
  $vercelLink = Join-Path $App '.vercel'
  if (-not (Test-Path (Join-Path $vercelLink 'project.json'))) {
    Fail 'app\.vercel is missing. Run these once in a terminal inside the app folder:  npx vercel login   then   npx vercel link'
    return
  }
  $dirty = (& git -C $App status --porcelain) | Out-String
  if ($dirty.Trim()) { Info 'app\ has changes that are not committed: they are NOT deployed (only the last commit is).' }
  if (Ask-Yes 'Deploy the last commit to Vercel PRODUCTION (the live website changes)') {
    $tmpDir = Join-Path $env:TEMP ("lvl-deploy-" + [guid]::NewGuid().ToString('N'))
    New-Item -ItemType Directory -Path $tmpDir | Out-Null
    try {
      $zip = "$tmpDir.zip"
      & git -C $App archive --format=zip -o $zip HEAD
      Expand-Archive -Path $zip -DestinationPath $tmpDir
      Remove-Item -LiteralPath $zip -Force
      Copy-Item $vercelLink (Join-Path $tmpDir '.vercel') -Recurse
      $vercel = $(if (Get-Command vercel -ErrorAction SilentlyContinue) { 'vercel' } else { 'npx' })
      $pre = $(if ($vercel -eq 'npx') { @('vercel') } else { @() })
      if ((Run $tmpDir $vercel ($pre + @('whoami'))) -ne 0) { Fail 'Not signed in to Vercel. Run:  npx vercel login   (opens the browser), then -Cloud again'; return }
      Push-Location $tmpDir
      $names = (& $vercel @($pre + @('env', 'ls', 'production'))) 2>$null | Out-String
      foreach ($k in $RequiredKeys) {
        if ($names -match $k) { Pass "Vercel has $k" }
        # shortcut: value piped on stdin (not verified on a fresh Vercel project); if the site shows a blank page, add it in Vercel > Settings > Environment Variables
        elseif ($envh[$k]) { $envh[$k] | & $vercel @($pre + @('env', 'add', $k, 'production')) *> $null; Info "added $k to Vercel (value not shown)" }
      }
      Pop-Location
      if ((Run $tmpDir $vercel ($pre + @('deploy', '--prod', '--yes'))) -eq 0) { Pass 'deployed to Vercel (the address is printed above)' } else { Fail 'Vercel deploy failed' }
    } finally { Remove-Item -LiteralPath $tmpDir -Recurse -Force -ErrorAction SilentlyContinue }
  }

  Title 'Things only you can do'
  Say '  - Login accounts are not copied between projects. Create people in the app: Team page > "Add New Team Member".'
  Say '  - To copy the data into a NEW project: database\README.md (backup, then restore --apply).'
  Say '  - In the Supabase dashboard (Authentication > URL Configuration) set the Site URL to the Vercel address.'
  Say '  - Auth hooks (login guard) are switched on in the Supabase dashboard: Authentication > Hooks. See SETUP-GUIDE.md.'
}

# ---------------------------------- MAIN ----------------------------------
$mode = $(if ($Check) { 'Check' } elseif ($Cloud) { 'Cloud' } elseif ($Local) { 'Local' } else { 'Setup' })
Log "========== install.ps1 -$mode =========="
Write-Host "LevelUp CRM installer  (mode: $mode)   folder: $Root" -ForegroundColor White

switch ($mode) {
  'Check' { Invoke-Check }
  'Setup' { Invoke-Setup }
  'Cloud' { Invoke-Cloud }
  'Local' {
    if (-not (Test-Path (Join-Path $App 'node_modules'))) { Fail 'Run Setup first (double-click INSTALL.cmd)' }
    else { Say 'Starting the app. Open the address shown below (usually http://localhost:5173). Press Ctrl+C to stop.'; Run $App 'npm' @('run', 'dev') | Out-Null }
  }
}

Write-Host ""
if ($script:Problems -eq 0) { Write-Host "RESULT: all good ($mode)" -ForegroundColor Green; Log "RESULT ok"; exit 0 }
Write-Host "RESULT: $($script:Problems) item(s) need attention (see MISSING / FAIL above). Log: install\install.log" -ForegroundColor Yellow
Log "RESULT $($script:Problems) problem(s)"
exit 1
