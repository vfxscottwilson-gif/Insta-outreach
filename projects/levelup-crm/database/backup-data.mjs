// READ-ONLY export of every table in the public schema to database\backups\<YYYY-MM-DD_HHmm>\<table>.json
// plus _migrations.json (schema versions) and _manifest.json (row counts). Only SELECT statements are sent.
// Usage:  node database\backup-data.mjs            (project from app\.env or secrets\app.env.backup)
//         node database\backup-data.mjs --ref <ref>
// The files contain personal data: they stay in database\backups\ (gitignored). Never share them.
import { mkdirSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { DB_DIR, loadConfig, sql, qi, fail } from './lib.mjs';

const PAGE = 1000;
const cfg = loadConfig();
const d = new Date();
const p = (n) => String(n).padStart(2, '0');
const stamp = `${d.getFullYear()}-${p(d.getMonth() + 1)}-${p(d.getDate())}_${p(d.getHours())}${p(d.getMinutes())}`;
const out = join(DB_DIR, 'backups', stamp);

try {
  const tables = (await sql(cfg, `select table_name as t from information_schema.tables
    where table_schema = 'public' and table_type = 'BASE TABLE' order by 1`)).map((r) => r.t);
  if (!tables.length) fail('No tables found in the public schema.');
  mkdirSync(out, { recursive: true });

  const counts = {};
  for (const t of tables) {
    const rows = [];
    for (let off = 0; ; off += PAGE) {
      // ctid order = stable physical order for paging inside one export run
      const page = await sql(cfg, `select * from public.${qi(t)} order by ctid limit ${PAGE} offset ${off}`);
      rows.push(...page);
      if (page.length < PAGE) break;
    }
    writeFileSync(join(out, `${t}.json`), JSON.stringify(rows, null, 1));
    counts[t] = rows.length;
    console.log(`PASS  ${t.padEnd(32)} ${rows.length} rows`);
  }

  let migrations = [];
  try {
    migrations = await sql(cfg, 'select version, name from supabase_migrations.schema_migrations order by version');
  } catch { console.log('INFO  No supabase_migrations table found (schema versions not saved).'); }
  writeFileSync(join(out, '_migrations.json'), JSON.stringify(migrations, null, 1));
  writeFileSync(join(out, '_manifest.json'), JSON.stringify(
    { created: d.toISOString(), sourceRef: cfg.ref, tables: counts, migrations: migrations.length }, null, 1));

  console.log(`\nDONE  ${tables.length} tables, ${migrations.length} schema versions saved to:\n      ${out}`);
  console.log('      Login accounts (auth.users) are not in the backup: they are recreated in the new project.');
} catch (e) {
  fail(e.message);
}
