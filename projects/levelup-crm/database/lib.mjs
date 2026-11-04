// Shared by backup-data.mjs and restore-data.mjs. Reads the token + project ref; never prints secret values.
import { existsSync, readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

export const DB_DIR = dirname(fileURLToPath(import.meta.url));
export const ROOT = join(DB_DIR, '..');

function readEnvFile(file) {
  if (!existsSync(file)) return {};
  const out = {};
  for (const line of readFileSync(file, 'utf8').split(/\r?\n/)) {
    const m = line.match(/^\s*([A-Z0-9_]+)\s*=\s*(.*)\s*$/);
    if (m) out[m[1]] = m[2].trim().replace(/^["']|["']$/g, '');
  }
  return out;
}

// Order: --ref flag, then app\.env, then secrets\app.env.backup, then secrets\supabase-access-token.txt (token only).
export function loadConfig(argv = process.argv) {
  const appEnv = readEnvFile(join(ROOT, 'app', '.env'));
  const bakEnv = readEnvFile(join(ROOT, 'secrets', 'app.env.backup'));
  const tokFile = join(ROOT, 'secrets', 'supabase-access-token.txt');
  const token = appEnv.SUPABASE_ACCESS_TOKEN || bakEnv.SUPABASE_ACCESS_TOKEN
    || (existsSync(tokFile) ? readFileSync(tokFile, 'utf8').trim() : '');
  const url = appEnv.VITE_SUPABASE_URL || bakEnv.VITE_SUPABASE_URL || '';
  const i = argv.indexOf('--ref');
  const ref = (i > -1 ? argv[i + 1] : '') || url.match(/^https:\/\/([a-z0-9]{20})\.supabase\.co/)?.[1] || '';
  if (!token) fail('SUPABASE_ACCESS_TOKEN not found in app\\.env, secrets\\app.env.backup or secrets\\supabase-access-token.txt.');
  if (!/^[a-z0-9]{20}$/.test(ref)) fail('Project ref not found. Put VITE_SUPABASE_URL in app\\.env or pass --ref <20-letter ref>.');
  return { token, ref };
}

export function fail(msg) {
  console.error(`FAIL  ${msg}`);
  process.exit(1);
}

// Management API SQL endpoint. Returns the rows of the last statement.
export async function sql({ token, ref }, query) {
  const res = await fetch(`https://api.supabase.com/v1/projects/${ref}/database/query`, {
    method: 'POST',
    headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json', 'User-Agent': 'levelup-crm-data-tools/1.0' },
    body: JSON.stringify({ query }),
  });
  const text = await res.text();
  if (!res.ok) throw new Error(`Supabase API ${res.status}: ${text.replaceAll(token, '***').slice(0, 300)}`);
  return text ? JSON.parse(text) : [];
}

export const qi = (name) => `"${String(name).replaceAll('"', '""')}"`; // quote identifier
