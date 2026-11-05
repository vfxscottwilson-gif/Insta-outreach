// Nightly encrypted backup of the Database app. Usage: node backup-to-supabase.mjs [--local-only] [--selftest]
// Writes one line per run to backups\backup.log; exit code 1 on failure. Never prints keys.
import { existsSync, mkdtempSync, rmSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { ROOT, appendLog, checkDb, fsStore, loadKey, loadRemote, logTime, restoreBackup, runBackup, supabaseStore } from './backup-lib.mjs'

const flag = (f) => process.argv.includes(f)

/** Whole pipeline against a temp folder: real app backup command, fake storage, tiny parts, then restore + integrity check. No network, no secrets. */
async function selftest() {
  const root = mkdtempSync(join(tmpdir(), 'dashbk-self-'))
  try {
    const keyFile = join(root, 'secrets', 'backup.key')
    const store = fsStore(join(root, 'fake-storage'))
    const r = await runBackup({
      root, keyFile, getRemote: () => store, partSize: 4096, keep: 2,
      dumpEnv: { DASH_DB: join(root, 'fixture.db'), DASH_SECRET_KEY: 'selftest-only' },
    })
    const parts = (await store.list()).filter((n) => n.includes('.part')).length
    if (parts < 2) throw new Error(`expected a split upload, got ${parts} part(s)`)
    const out = join(root, 'restored.db')
    await restoreBackup({ store, key: loadKey(keyFile, false), name: 'latest', out })
    checkDb(out)
    console.log(`SELFTEST OK name=${r.base} bytes=${r.bytes} parts=${parts}`)
  } finally { rmSync(root, { recursive: true, force: true }) }
}

async function main() {
  if (flag('--selftest')) return selftest()
  // No database file yet (app not set up for real use): skip instead of creating an empty one in the app folder.
  const dbFile = process.env.DASH_DB || join(ROOT, 'app', 'dashboard', 'data', 'dash.db')
  if (!existsSync(dbFile)) { const line = `${logTime()} PKT SKIP no database file yet (${dbFile})`; appendLog(ROOT, line); console.log(line); return }
  try {
    const getRemote = flag('--local-only') ? null : () => supabaseStore(loadRemote(join(ROOT, 'secrets', 'supabase-backup.env')))
    const r = await runBackup({ getRemote })
    const line = `${logTime()} PKT OK name=${r.base} bytes=${r.bytes} local_kept=${r.localKept} remote=${r.remoteKept === null ? 'skipped' : 'kept ' + r.remoteKept}`
    appendLog(ROOT, line); console.log(line)
  } catch (e) {
    const line = `${logTime()} PKT FAIL ${String(e.message).replace(/\s+/g, ' ').slice(0, 400)}`
    appendLog(ROOT, line); console.error(line)
    process.exitCode = 1
  }
}

main().catch((e) => { console.error('SELFTEST FAILED:', e.message); process.exitCode = 1 })
