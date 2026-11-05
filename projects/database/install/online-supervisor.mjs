// Keeps the free Cloudflare quick tunnel alive and tells the Worker (through KV) where it currently is,
// so visitors always use the same workers.dev address. Usage: node online-supervisor.mjs <app port, default 8080>
import { spawn, execFile } from 'node:child_process'
import { readdirSync, statSync } from 'node:fs'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'

const here = dirname(fileURLToPath(import.meta.url))
const PORT = process.argv[2] || process.env.APP_PORT || '8080'
const CF = join(here, 'bin', process.platform === 'win32' ? 'cloudflared.exe' : 'cloudflared')
const WORKER = join(here, 'worker')
const log = (...a) => console.log(new Date().toTimeString().slice(0, 8), ...a)

const put = (url) => new Promise((resolve) => execFile('npx', ['--yes', 'wrangler@4.157.0', 'kv', 'key', 'put', 'origin', url, '--binding', 'ORIGIN_KV', '--remote'],
  { cwd: WORKER, shell: true }, (e, _so, se) => { log(e ? 'KV update FAILED: ' + String(se || e.message).slice(0, 200) : 'KV updated: ' + url); resolve(!e) }))

let child = null, current = '', failures = 0
function run() {
  child = spawn(CF, ['tunnel', '--url', `http://127.0.0.1:${PORT}`, '--no-autoupdate'], { stdio: ['ignore', 'pipe', 'pipe'] })
  const onData = async (d) => {
    const m = String(d).match(/https:\/\/[a-z0-9-]+\.trycloudflare\.com/)
    if (!m || m[0] === current) return
    current = m[0]
    for (let i = 0; i < 3; i++) if (await put(current)) break
  }
  child.stdout.on('data', onData); child.stderr.on('data', onData)
  child.on('exit', (code) => { log('tunnel exited', code, '- restarting in 5 s'); current = ''; failures = 0; setTimeout(run, 5000) })
}
run()

// Health check: the app answers locally but the public tunnel address does not -> restart the tunnel.
setInterval(async () => {
  if (!current) return
  try {
    const r = await fetch(current + '/login', { signal: AbortSignal.timeout(10000) })
    if (r.status >= 500) throw new Error('HTTP ' + r.status)
    failures = 0
  } catch (e) {
    if (++failures >= 3) { log('tunnel unhealthy (' + e.message + '), restarting it'); failures = 0; child?.kill() }
  }
}, 60000)

// Nightly encrypted backup at 03:00 Pakistan time (child process, so a failure can never take the supervisor down).
// Also once 2 minutes after start when the newest backup file in backups\ is older than 24 h (or there is none).
const BACKUP = join(here, 'backup-to-supabase.mjs'), BACKUPS = join(here, '..', 'backups')
let backingUp = false
function backup(why) {
  if (backingUp) return
  backingUp = true
  try {
    execFile(process.execPath, [BACKUP], { timeout: 15 * 60000, windowsHide: true }, (e, so, se) => {
      backingUp = false
      const out = String(e ? se || so || e.message : so).trim().split('\n').slice(-2).join(' | ').slice(0, 300)
      log(`backup (${why}) ${e ? 'FAILED' : 'done'}: ${out}`)
    })
  } catch (e) { backingUp = false; log('backup could not start: ' + e.message) }
}

const karachi = () => {
  const p = Object.fromEntries(new Intl.DateTimeFormat('en-GB', { timeZone: 'Asia/Karachi', hourCycle: 'h23', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit' })
    .formatToParts().map((x) => [x.type, x.value]))
  return { day: `${p.year}-${p.month}-${p.day}`, hour: +p.hour }
}
// Run on the first tick at/after 03:00 each day (also fires after a sleep/wake at 03:20). Started after 03:00 -> today counts as handled; the 2-minute check below covers it.
let lastDay = karachi().hour >= 3 ? karachi().day : ''
setInterval(() => {
  try { const k = karachi(); if (k.hour >= 3 && k.day !== lastDay) { lastDay = k.day; backup('03:00 Karachi') } } catch (e) { log('backup timer error: ' + e.message) }
}, 30000)

setTimeout(() => {
  let newest = 0
  try { newest = Math.max(0, ...readdirSync(BACKUPS).filter((f) => /^dash-.*\.enc$/.test(f)).map((f) => statSync(join(BACKUPS, f)).mtimeMs)) } catch {}
  if (Date.now() - newest > 24 * 3600 * 1000) backup('catch-up after start')
}, 120000)
