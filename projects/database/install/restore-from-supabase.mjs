// Usage: node restore-from-supabase.mjs <backup name | latest> <output .db path> [--local]
// Downloads (and reassembles), decrypts, gunzips, runs a SQLite integrity check. Never overwrites an existing file.
// --local reads backups\ on this PC instead of Supabase (use it when Supabase is unreachable).
import { join, resolve } from 'node:path'
import { ROOT, fsStore, loadKey, loadRemote, restoreBackup, supabaseStore } from './backup-lib.mjs'

const [name, out] = process.argv.slice(2).filter((a) => !a.startsWith('--'))
if (!name || !out) {
  console.error('Usage: node restore-from-supabase.mjs <backup name | latest> <output .db path> [--local]')
  process.exit(2)
}
try {
  const store = process.argv.includes('--local') ? fsStore(join(ROOT, 'backups')) : supabaseStore(loadRemote(join(ROOT, 'secrets', 'supabase-backup.env')))
  const used = await restoreBackup({ store, key: loadKey(join(ROOT, 'secrets', 'backup.key'), false), name, out: resolve(out) })
  console.log(`Restored ${used} -> ${resolve(out)} (SQLite integrity check ok)`)
} catch (e) {
  console.error('Restore FAILED: ' + String(e.message).replace(/\s+/g, ' ').slice(0, 400))
  process.exit(1)
}
