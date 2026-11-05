// Shared code for backup-to-supabase.mjs and restore-from-supabase.mjs. Only node: built-ins.
// File format of a backup: "DASHBK01" (8 bytes) + IV (12) + AES-256-GCM ciphertext of gzip(sqlite copy) + tag (16).
import { createCipheriv, createDecipheriv, randomBytes } from 'node:crypto'
import { gzipSync, gunzipSync } from 'node:zlib'
import { execFileSync } from 'node:child_process'
import { appendFileSync, existsSync, mkdirSync, mkdtempSync, readFileSync, readdirSync, renameSync, rmSync, writeFileSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { dirname, join, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

const here = dirname(fileURLToPath(import.meta.url))
const REAL_ROOT = resolve(here, '..')
export const ROOT = process.env.BACKUP_ROOT ? resolve(process.env.BACKUP_ROOT) : REAL_ROOT // BACKUP_ROOT is for tests
export const APP_DIR = process.env.BACKUP_APP_DIR || join(REAL_ROOT, 'app', 'dashboard')
export const KEEP = 14
export const PART_SIZE = 40 * 1024 * 1024 // Supabase free plan: 50 MB per file
const MAGIC = Buffer.from('DASHBK01')
const NAME_RE = /^dash-\d{8}-\d{6}\.db\.gz\.enc(\.part\d{3})?$/
const BASE_RE = /^dash-\d{8}-\d{6}\.db\.gz\.enc$/

// ---- time (Pakistan) ----
const pk = (d = new Date()) => Object.fromEntries(new Intl.DateTimeFormat('en-GB', {
  timeZone: 'Asia/Karachi', hourCycle: 'h23', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit',
}).formatToParts(d).map((x) => [x.type, x.value]))
export const stamp = (d) => { const p = pk(d); return `${p.year}${p.month}${p.day}-${p.hour}${p.minute}${p.second}` }
export const logTime = (d) => { const p = pk(d); return `${p.year}-${p.month}-${p.day} ${p.hour}:${p.minute}:${p.second}` }

// ---- crypto ----
export function encrypt(plain, key) {
  const iv = randomBytes(12)
  const c = createCipheriv('aes-256-gcm', key, iv)
  c.setAAD(MAGIC)
  return Buffer.concat([MAGIC, iv, c.update(plain), c.final(), c.getAuthTag()])
}

export function decrypt(blob, key) {
  if (blob.length < MAGIC.length + 12 + 16 || !blob.subarray(0, MAGIC.length).equals(MAGIC)) throw new Error('not a Database backup file (bad header)')
  const d = createDecipheriv('aes-256-gcm', key, blob.subarray(8, 20))
  d.setAAD(MAGIC)
  d.setAuthTag(blob.subarray(-16))
  try { return Buffer.concat([d.update(blob.subarray(20, -16)), d.final()]) } catch { throw new Error('decryption failed: wrong key or the file was changed') }
}

export function loadKey(file, create) {
  if (!existsSync(file)) {
    if (!create) throw new Error(`encryption key not found: ${file}`)
    mkdirSync(dirname(file), { recursive: true })
    writeFileSync(file, randomBytes(32).toString('hex') + '\n', { flag: 'wx', mode: 0o600 })
    console.log(`NOTICE: a new backup encryption key was created at ${file}. Save a copy OFF this PC now (password manager). Without it no backup can be restored.`)
  }
  const hex = readFileSync(file, 'utf8').trim()
  if (!/^[0-9a-f]{64}$/i.test(hex)) throw new Error(`${file} must contain exactly 64 hex characters`)
  return Buffer.from(hex, 'hex')
}

// ---- splitting, naming, rotation ----
export const splitParts = (buf, size = PART_SIZE) =>
  buf.length <= size ? [buf] : Array.from({ length: Math.ceil(buf.length / size) }, (_, i) => buf.subarray(i * size, (i + 1) * size))
export const partNames = (base, n) => (n === 1 ? [base] : Array.from({ length: n }, (_, i) => `${base}.part${String(i + 1).padStart(3, '0')}`))

/** Map base name -> sorted object names (single file or its parts). Ignores anything not named dash-*.enc. */
export function groupBackups(names) {
  const g = new Map()
  for (const n of names.filter((x) => NAME_RE.test(x)).sort()) {
    const b = n.replace(/\.part\d{3}$/, '')
    g.set(b, [...(g.get(b) ?? []), n])
  }
  return g
}

export async function putBackup(store, base, enc, partSize = PART_SIZE) {
  const parts = splitParts(enc, partSize)
  const names = partNames(base, parts.length)
  try { for (let i = 0; i < parts.length; i++) await store.put(names[i], parts[i]) } catch (e) { await store.del(names).catch(() => {}); throw e }
  return names
}

export async function fetchBackup(store, base) {
  if (!BASE_RE.test(base)) throw new Error(`not a backup name: ${base} (expected dash-YYYYMMDD-HHMMSS.db.gz.enc)`)
  const names = groupBackups(await store.list()).get(base)
  if (!names) throw new Error(`backup not found: ${base}`)
  if (names.length === 1 && names[0] === base) return store.get(base)
  const want = partNames(base, names.length)
  if (names.some((n, i) => n !== want[i])) throw new Error(`backup ${base} is incomplete (missing or mixed parts: ${names.join(', ')})`)
  const bufs = []
  for (const n of names) bufs.push(await store.get(n))
  return Buffer.concat(bufs)
}

/** Keep the newest `keep` backups (all their parts), delete the rest. Returns how many backups remain. */
export async function rotate(store, keep = KEEP) {
  const g = groupBackups(await store.list())
  const doomed = [...g.keys()].sort().reverse().slice(keep).flatMap((b) => g.get(b))
  if (doomed.length) await store.del(doomed)
  return Math.min(g.size, keep)
}

// ---- storages: { list(): names, put(name, buf), del(names), get(name): Buffer } ----
export function fsStore(dir) {
  mkdirSync(dir, { recursive: true })
  return {
    list: async () => readdirSync(dir),
    put: async (name, buf) => { const t = join(dir, name + '.tmp'); writeFileSync(t, buf); renameSync(t, join(dir, name)) },
    del: async (names) => names.forEach((n) => rmSync(join(dir, n), { force: true })),
    get: async (name) => readFileSync(join(dir, name)),
  }
}

export function loadRemote(file) {
  if (!existsSync(file)) throw new Error(`Supabase settings file not found: ${file} (needs SUPABASE_URL, SUPABASE_SECRET_KEY, SUPABASE_BUCKET=database-backups)`)
  const env = {}
  for (const l of readFileSync(file, 'utf8').split(/\r?\n/)) {
    const m = l.match(/^\s*([A-Z_]+)\s*=\s*(.*?)\s*$/)
    if (m) env[m[1]] = m[2].replace(/^["']|["']$/g, '')
  }
  const missing = ['SUPABASE_URL', 'SUPABASE_SECRET_KEY'].filter((k) => !env[k])
  if (missing.length) throw new Error(`${file} is missing ${missing.join(' and ')}`)
  if (!/^https:\/\//.test(env.SUPABASE_URL)) throw new Error('SUPABASE_URL must start with https://')
  return { url: env.SUPABASE_URL, key: env.SUPABASE_SECRET_KEY, bucket: env.SUPABASE_BUCKET || 'database-backups' }
}

export function supabaseStore({ url, key, bucket }) {
  const root = `${url.replace(/\/+$/, '')}/storage/v1/object`
  // New sb_secret_ keys are not JWTs and go on the apikey header only; legacy service_role JWTs (eyJ...) also go on Authorization.
  const auth = { apikey: key, ...(key.startsWith('eyJ') ? { Authorization: `Bearer ${key}` } : {}) }
  const b = encodeURIComponent(bucket)
  const redact = (s) => String(s).replaceAll(key, '***')
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms))

  async function call(method, path, { json, body } = {}) {
    for (let i = 0; ; i++) { // 3 tries on network errors / 5xx; uploads use x-upsert so a retry is safe
      let r
      try {
        r = await fetch(root + path, {
          method, body: json ? JSON.stringify(json) : body, signal: AbortSignal.timeout(120000),
          headers: { ...auth, ...(json ? { 'content-type': 'application/json' } : body ? { 'content-type': 'application/octet-stream', 'x-upsert': 'true' } : {}) },
        })
      } catch (e) {
        if (i < 2) { await sleep(1000 * (i + 1)); continue }
        throw new Error(redact(`${method} ${path}: ${e.cause?.code ?? e.message}`))
      }
      if (r.status >= 500 && i < 2) { await sleep(1000 * (i + 1)); continue }
      if (!r.ok) throw new Error(redact(`${method} ${path} -> HTTP ${r.status} ${(await r.text()).slice(0, 200)}`))
      return r
    }
  }

  return {
    async list() {
      const out = []
      for (let offset = 0; ; offset += 100) {
        const r = await call('POST', `/list/${b}`, { json: { prefix: '', limit: 100, offset, sortBy: { column: 'name', order: 'desc' } } })
        const page = await r.json()
        out.push(...page.map((o) => o.name))
        if (page.length < 100) return out
      }
    },
    put: async (name, buf) => { await call('POST', `/${b}/${encodeURIComponent(name)}`, { body: buf }) },
    async del(names) {
      for (let i = 0; i < names.length; i += 100) await call('DELETE', `/${b}`, { json: { prefixes: names.slice(i, i + 100) } })
    },
    get: async (name) => Buffer.from(await (await call('GET', `/authenticated/${b}/${encodeURIComponent(name)}`)).arrayBuffer()),
  }
}

// ---- app database ----
export function pythonPath() {
  return process.env.BACKUP_PYTHON || [join(APP_DIR, '.venv', 'Scripts', 'python.exe'), join(APP_DIR, '.venv', 'bin', 'python')].find(existsSync) || 'python'
}

/** Safe copy made by the app itself (no password vault, no sessions). */
function dump(appDir, out, env) {
  try {
    execFileSync(pythonPath(), [join(appDir, 'manage.py'), 'backup', '--to', out], { cwd: appDir, env: { ...process.env, ...env }, stdio: 'pipe', timeout: 300000 })
  } catch (e) {
    throw new Error(`the app's backup command failed: ${String(e.stderr || e.message).trim().split('\n').slice(-2).join(' ').slice(0, 300)}`)
  }
  if (!existsSync(out)) throw new Error("the app's backup command produced no file")
}

export function checkDb(file) {
  const code = "import sqlite3,sys; r=sqlite3.connect(sys.argv[1]).execute('PRAGMA integrity_check').fetchall(); sys.exit(0 if r==[('ok',)] else 1)"
  try { execFileSync(pythonPath(), ['-I', '-c', code, file], { stdio: 'pipe', timeout: 120000 }) } catch { throw new Error('the restored file failed the SQLite integrity check') }
}

// ---- the two jobs ----
/** dump -> gzip -> encrypt -> local copy (+rotate) -> optional upload (+rotate). Whole file lives in memory (shortcut: fine up to a few hundred MB). */
export async function runBackup({ root = ROOT, appDir = APP_DIR, keyFile = join(root, 'secrets', 'backup.key'), getRemote = null, keep = KEEP, partSize = PART_SIZE, dumpEnv = {}, now = new Date() }) {
  const key = loadKey(keyFile, true)
  const tmp = mkdtempSync(join(tmpdir(), 'dashbk-'))
  try {
    const raw = join(tmp, 'dump.db')
    dump(appDir, raw, dumpEnv)
    const enc = encrypt(gzipSync(readFileSync(raw)), key)
    const base = `dash-${stamp(now)}.db.gz.enc`
    const local = fsStore(join(root, 'backups'))
    await putBackup(local, base, enc, Infinity)
    const res = { base, bytes: enc.length, localKept: await rotate(local, keep), remoteKept: null }
    if (getRemote) {
      try {
        const remote = getRemote()
        await putBackup(remote, base, enc, partSize)
        res.remoteKept = await rotate(remote, keep)
      } catch (e) { throw new Error(`upload to Supabase failed (local copy kept): ${e.message}`) }
    }
    return res
  } finally { rmSync(tmp, { recursive: true, force: true }) }
}

/** name = a backup name or "latest" (newest that can be fetched and decrypted). Refuses to overwrite `out`. */
export async function restoreBackup({ store, key, name, out }) {
  if (existsSync(out)) throw new Error(`refusing to overwrite an existing file: ${out}`)
  const bases = name === 'latest' ? [...groupBackups(await store.list()).keys()].sort().reverse() : [name]
  if (!bases.length) throw new Error('no backups found')
  let plain, used, first
  for (const b of bases) {
    try { plain = gunzipSync(decrypt(await fetchBackup(store, b), key)); used = b; break } catch (e) { first ??= e; if (name !== 'latest') throw e }
  }
  if (!used) throw first
  mkdirSync(dirname(out), { recursive: true })
  const part = out + '.restoring'
  writeFileSync(part, plain)
  try {
    checkDb(part)
    if (existsSync(out)) throw new Error(`refusing to overwrite an existing file: ${out}`)
    renameSync(part, out)
  } catch (e) { rmSync(part, { force: true }); throw e }
  return used
}

export function appendLog(root, line) {
  try { mkdirSync(join(root, 'backups'), { recursive: true }); appendFileSync(join(root, 'backups', 'backup.log'), line + '\n') } catch (e) { console.error('could not write backup.log:', e.message) }
}
