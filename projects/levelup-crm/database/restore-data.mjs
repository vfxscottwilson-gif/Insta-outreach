// Puts a backup made by backup-data.mjs into a NEW Supabase project (schema already created by install -Cloud).
// DRY RUN by default (reads only). Add --apply to write.
// Usage:  node database\restore-data.mjs                         (newest backup, project from app\.env)
//         node database\restore-data.mjs --from 2026-11-05_0108 --ref <new-ref> --apply
// What --apply does, table by table in foreign-key order: deletes the rows already there (seed/default rows),
// then inserts the backup rows. Triggers and FK checks are paused for that session (session_replication_role = replica),
// the same way Supabase's own restore guide does it.
// Login accounts (auth.users) are NOT restored. Create the same people (same emails) first in the new app's
// admin screen (or the install step); this script then moves every old user id over to the new account with that email.
import { existsSync, readdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { randomBytes } from 'node:crypto';
import { DB_DIR, loadConfig, sql, qi, fail } from './lib.mjs';

const BATCH = 500;
const argv = process.argv;
const apply = argv.includes('--apply');
const cfg = loadConfig();
const backups = join(DB_DIR, 'backups');
const fromI = argv.indexOf('--from');
const name = fromI > -1 ? argv[fromI + 1]
  : (existsSync(backups) ? readdirSync(backups).filter((n) => existsSync(join(backups, n, '_manifest.json'))).sort().pop() : '');
const dir = name ? join(backups, name) : '';
if (!dir || !existsSync(join(dir, '_manifest.json'))) fail('No backup found. Run: node database\\backup-data.mjs');
const manifest = JSON.parse(readFileSync(join(dir, '_manifest.json'), 'utf8'));

// Swap old user ids for new ones anywhere in a value (ids are UUIDs, so an exact match is always that user).
const remap = (v, map) => typeof v === 'string' ? (map.get(v) ?? v)
  : Array.isArray(v) ? v.map((x) => remap(x, map))
  : v && typeof v === 'object' ? Object.fromEntries(Object.entries(v).map(([k, x]) => [k, remap(x, map)])) : v;

// Parents before children. Self-references and cycles are fine: checks are paused while writing.
function fkOrder(tables, edges) {
  const done = new Set(), out = [];
  const visit = (t, path = new Set()) => {
    if (done.has(t) || path.has(t) || !tables.includes(t)) return; // auth.* parents are not restored
    path.add(t);
    for (const e of edges) if (e.child === t && e.parent !== t) visit(e.parent, path);
    done.add(t); out.push(t);
  };
  tables.forEach((t) => visit(t));
  return out;
}

try {
  console.log(`${apply ? 'APPLY' : 'DRY RUN (nothing is written; add --apply to write)'}`);
  console.log(`Backup: ${name}   Target project: ${cfg.ref}${cfg.ref === manifest.sourceRef ? '  (SAME project the backup came from)' : ''}\n`);
  if (apply && cfg.ref === manifest.sourceRef) {
    fail('Refusing to overwrite the project this backup came from. Restore only into a NEW project (--ref <new-ref>).');
  }

  const target = (await sql(cfg, `select table_name as t from information_schema.tables
    where table_schema = 'public' and table_type = 'BASE TABLE'`)).map((r) => r.t);
  const files = readdirSync(dir).filter((f) => f.endsWith('.json') && !f.startsWith('_')).map((f) => f.slice(0, -5));
  const missing = files.filter((t) => !target.includes(t));
  if (missing.length) console.log(`WARN  Not in the new project (run install -Cloud migrations first): ${missing.join(', ')}`);
  const edges = await sql(cfg, `select c.conrelid::regclass::text as child, c.confrelid::regclass::text as parent
    from pg_constraint c join pg_namespace n on n.oid = c.connamespace where c.contype = 'f' and n.nspname = 'public'`);
  const strip = (s) => s.replace(/^public\./, '').replace(/"/g, '');
  const order = fkOrder(files.filter((t) => target.includes(t)),
    edges.map((e) => ({ child: strip(e.child), parent: strip(e.parent) })));

  // Old user id -> new user id, matched by email (profiles has id + email).
  const oldProfiles = existsSync(join(dir, 'profiles.json')) ? JSON.parse(readFileSync(join(dir, 'profiles.json'), 'utf8')) : [];
  const newUsers = await sql(cfg, 'select id::text as id, lower(email) as email from auth.users');
  const byEmail = new Map(newUsers.map((u) => [u.email, u.id]));
  const map = new Map(), unmatched = [];
  for (const p of oldProfiles) {
    const id = byEmail.get(String(p.email).toLowerCase());
    if (id) { if (id !== p.id) map.set(p.id, id); } else unmatched.push(p.email);
  }
  console.log(`Accounts: ${oldProfiles.length} in backup, ${oldProfiles.length - unmatched.length} found in the new project, ${unmatched.length} missing.`);
  if (unmatched.length) {
    writeFileSync(join(dir, 'missing-accounts.txt'), unmatched.join('\n') + '\n');
    console.log(`      The missing emails are listed in ${join(dir, 'missing-accounts.txt')}.`);
    console.log('      Create those accounts in the new app (Team page > "Add New Team Member"), then run this again.');
  }

  for (const t of order) {
    const rows = JSON.parse(readFileSync(join(dir, `${t}.json`), 'utf8'));
    const [{ n }] = await sql(cfg, `select count(*)::int as n from public.${qi(t)}`);
    console.log(`${apply ? 'WRITE' : 'PLAN '}  ${t.padEnd(32)} now ${String(n).padStart(5)}  ->  backup ${rows.length}`);
  }
  if (!apply) { console.log('\nDry run finished. Nothing was changed.'); process.exit(0); }
  if (unmatched.length) fail('Some accounts are missing in the new project (see above). Nothing was changed.');

  for (const t of order) {
    const rows = JSON.parse(readFileSync(join(dir, `${t}.json`), 'utf8')).map((r) => remap(r, map));
    // Generated columns are computed by Postgres, so they are left out of the insert.
    const cols = (await sql(cfg, `select column_name as c from information_schema.columns
      where table_schema = 'public' and table_name = '${t.replaceAll("'", "''")}' and is_generated = 'NEVER'
      and coalesce(generation_expression, '') = '' order by ordinal_position`)).map((r) => qi(r.c)).join(', ');
    const pre = 'set session_replication_role = replica;';
    await sql(cfg, `${pre} delete from public.${qi(t)};`);
    for (let i = 0; i < rows.length; i += BATCH) {
      const tag = `$j${randomBytes(6).toString('hex')}$`;
      await sql(cfg, `${pre} insert into public.${qi(t)} (${cols}) overriding system value
        select ${cols} from json_populate_recordset(null::public.${qi(t)}, ${tag}${JSON.stringify(rows.slice(i, i + BATCH))}${tag});`);
    }
    // Identity counters continue after the highest restored id.
    const ids = await sql(cfg, `select a.attname as c from pg_attribute a where a.attrelid = 'public.${qi(t)}'::regclass
      and a.attidentity <> '' and not a.attisdropped`);
    for (const { c } of ids) {
      await sql(cfg, `select setval(pg_get_serial_sequence('public.${qi(t)}', '${c}'),
        greatest(coalesce((select max(${qi(c)}) from public.${qi(t)}), 0), 1))`);
    }
    console.log(`PASS  ${t.padEnd(32)} ${rows.length} rows written`);
  }
  console.log('\nDONE  Restore finished. Open the app and check the data. Stored password copies (private schema) are not');
  console.log('      restored: each person sets a new password once in the new project.');
} catch (e) {
  fail(e.message);
}
