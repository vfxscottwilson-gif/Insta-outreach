# Restore: from backup files to a working system

Use after `backups\backup.ps1` or `database\cloud-export.ps1`. Moving the app to a NEW Supabase project: follow `database\README.md` (steps 1-7). This page adds the extra files.

| Backup file (in `database\backups\`) | Restore it with |
|---|---|
| `<date_time>\*.json` (table data) | `node database\restore-data.mjs` (dry run) then `--apply` (see README.md) |
| `schema-<date>.sql` (full schema, only if `DATABASE_URL` was set) | Only needed if `app\supabase\migrations\` is lost: Supabase > SQL Editor > paste and Run in an EMPTY project. Normally `INSTALL.cmd -Cloud` rebuilds the schema from the migrations instead |
| `cloud-<date>\functions.json`, `secret-names.json` | Checklist only: after `INSTALL.cmd -Cloud` compare the function list and secret names with these |
| `cloud-<date>\storage.json` | Shows which buckets/files existed. Files are not downloaded. The app uses no Storage today |
| `backups\levelup-crm-folder-<date>.zip` | Unzip on the new PC, then run `install\INSTALL.cmd -Check` and `INSTALL.cmd` |

## Run an export
Preview first (changes nothing):
```
powershell -ExecutionPolicy Bypass -File backups\backup.ps1 -DryRun
```
Real run (remove `-DryRun`; add `-NoDb` for the folder zip only).

## One-time setup for the schema file (optional)
1. Supabase dashboard > Project Settings > Database > Connection string > URI (Session pooler).
2. Add one line `DATABASE_URL=...` to `secrets\.env` (create the file if missing). Never paste it in chat.
3. Install the PostgreSQL command line tools once (pick only "Command Line Tools"):
```
winget install PostgreSQL.PostgreSQL.17
```

Not verified: a real `pg_dump` run and the storage/functions inventory run (no `DATABASE_URL` is stored yet; the inventory was only dry-run). Table-data export and restore were verified earlier (see `database\README.md`).
