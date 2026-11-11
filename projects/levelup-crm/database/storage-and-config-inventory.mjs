// READ-ONLY cloud inventory of the Supabase project -> database\backups\cloud-<date_time>\
//   storage.json    buckets + object counts (files themselves are NOT downloaded)
//   functions.json  deployed Edge Functions (slug, version, status)
//   secret-names.json  Edge Function secret NAMES only (values are never read or written)
//   cron.json       scheduled jobs (pg_cron) if the extension is on
// Usage: node database\storage-and-config-inventory.mjs [--dry-run] [--ref <ref>]
// --dry-run: checks token + project ref are found and prints what it would do. Sends nothing. Never prints secret values.
import { mkdirSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { DB_DIR, loadConfig, sql } from './lib.mjs';

const cfg = loadConfig();
const dry = process.argv.includes('--dry-run');
const d = new Date();
const p = (n) => String(n).padStart(2, '0');
const out = join(DB_DIR, 'backups', `cloud-${d.getFullYear()}-${p(d.getMonth() + 1)}-${p(d.getDate())}_${p(d.getHours())}${p(d.getMinutes())}`);

if (dry) {
  console.log(`[DRY] token found, project ref ${cfg.ref}. Would write storage.json, functions.json, secret-names.json, cron.json to ${out}`);
  process.exit(0);
}

async function api(path) {
  const res = await fetch(`https://api.supabase.com/v1/projects/${cfg.ref}${path}`, {
    headers: { Authorization: `Bearer ${cfg.token}`, 'User-Agent': 'levelup-crm-data-tools/1.0' },
  });
  if (!res.ok) throw new Error(`Supabase API ${res.status} on ${path}`);
  return res.json();
}
const safe = async (label, fn) => { try { return await fn(); } catch (e) { console.log(`WARN  ${label}: ${String(e.message).replaceAll(cfg.token, '***')}`); return { error: String(e.message).replaceAll(cfg.token, '***') }; } };

mkdirSync(out, { recursive: true });
const save = (name, data) => { writeFileSync(join(out, name), JSON.stringify(data, null, 2)); console.log(`PASS  ${name}`); };

save('storage.json', await safe('storage', () => sql(cfg,
  `select b.id, b.name, b.public, count(o.id) as objects from storage.buckets b left join storage.objects o on o.bucket_id = b.id group by 1,2,3 order by 1`)));
save('functions.json', await safe('functions', async () => (await api('/functions')).map(({ slug, name, version, status, updated_at }) => ({ slug, name, version, status, updated_at }))));
save('secret-names.json', await safe('secrets', async () => (await api('/secrets')).map((s) => s.name)));
save('cron.json', await safe('cron', () => sql(cfg, `select jobid, jobname, schedule, active from cron.job order by 1`)));
console.log(`DONE  saved to: ${out}`);
