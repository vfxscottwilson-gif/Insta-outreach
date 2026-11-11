# Database: export and restore (Supabase `haroonvfx-outreach`, ref `bnivytzudrpjlscwdxuh`)

Schema = `app\supabase\migrations\` (the source of truth). Data lives only in Supabase. Supabase also keeps its own daily backups (Dashboard > Database > Backups; plan limits not verified here).

## Export
1. Install the PostgreSQL command line tools once (pick only "Command Line Tools"):
```
winget install PostgreSQL.PostgreSQL.17
```
2. Preview (changes nothing):
```
powershell -ExecutionPolicy Bypass -File backups\backup.ps1 -DryRun
```
3. Real run (needs `DATABASE_URL` in `app\.env`; the installer copies it there from `secrets\.env`):
```
powershell -ExecutionPolicy Bypass -File backups\backup.ps1
```
You get `outreach-folder-<date>.zip`, `db-<date>-schema.sql`, `db-<date>-data.sql` in `backups\`. They hold keys and real data: keep private.

## Restore into a new Supabase project
1. Create the project at https://supabase.com/dashboard/new (needs you, in the browser).
2. Put its connection string in `secrets\.env` as `DATABASE_URL`, and update `SUPABASE_SERVICE_ROLE_KEY`, then copy to `app\.env`.
3. Run the schema file in the Supabase SQL Editor (or apply `app\supabase\migrations\` in order), then the data file.
4. Gmail tokens are stored in Supabase Vault: they may not survive a move; reconnect the Gmail accounts in the app if senders show as disconnected.
5. Run `install\INSTALL.cmd -Check` and the app health check.

Not verified: a real `pg_dump` / restore run (pg_dump not installed on this PC when this was written).
