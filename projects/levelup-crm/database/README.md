# Database: backup and restore

The app's data lives in Supabase (a hosted Postgres database). These tools copy the data to this folder and back.

| File | What it does |
|---|---|
| `backup-data.mjs` | **Read-only.** Saves every table of the `public` schema to `backups\<date_time>\<table>.json`, plus `_migrations.json` (schema versions) and `_manifest.json` (row counts). |
| `restore-data.mjs` | Puts a backup into a **new** Supabase project. Dry run by default; writes only with `--apply`. |
| `lib.mjs` | Shared helper (reads the token and project, talks to the Supabase Management API). |
| `backups\` | The saved copies. **Contains personal data. Never share, never commit** (ignored by git: `projects/*/database/backups/`). |

Both tools read `SUPABASE_ACCESS_TOKEN` and `VITE_SUPABASE_URL` from `app\.env` (or `secrets\app.env.backup`). They never print secret values.

## Make a backup

1. Open a terminal in the `levelup-crm` folder (in File Explorer: click the address bar, type `cmd`, press Enter).
2. Run:
   ```
   node database\backup-data.mjs
   ```
3. You should see one `PASS` line per table and `DONE ... saved to: ...\backups\2026-11-05_0108`.

## Restore into a NEW Supabase project (moving house)

1. Create the new project in the browser: https://supabase.com/dashboard/new (this needs you; it cannot be done from here).
2. Put the new project's URL and anon key in `app\.env` (`VITE_SUPABASE_URL`, `VITE_SUPABASE_ANON_KEY`).
3. Run `install\INSTALL.cmd -Cloud` and answer `YES` to link, migrations, functions and secrets. This builds the empty tables.
4. Sign in to the new app as admin and **create the same people with the same emails** (Team page > "Add New Team Member").
   Login accounts (`auth.users`) are not in the backup: passwords cannot be copied, so each person gets a new one.
5. Dry run (changes nothing; shows what would be written and if any accounts are still missing):
   ```
   node database\restore-data.mjs
   ```
   Use `--from 2026-11-05_0108` to pick a backup (default: newest) and `--ref <new-ref>` to pick the project.
6. When it says `Accounts: ... 0 missing`, write the data:
   ```
   node database\restore-data.mjs --apply
   ```
7. Open the app and check tasks, teams and time entries.

How `--apply` works: tables are written parents-first (foreign-key order). For each table it deletes the rows the
new project already has (seed/default rows), then inserts the backup rows. Old user ids are swapped for the new
accounts' ids by matching email. Triggers and FK checks are paused for that session only (`session_replication_role = replica`).
It **refuses** to write into the project the backup came from, so the live project cannot be overwritten by mistake.

## Not included (be aware)

- `auth.users` (login accounts): recreated by hand, step 4.
- `private` schema (login lock counters, stored password copies): not copied. Stored password copies are encrypted with
  the old project's `PASSWORD_VAULT_KEY`, so they could not be opened in a new project anyway.
- Files in Supabase Storage: the app does not use Storage today.
- Server secrets (Edge Function secrets): set again by `install\INSTALL.cmd -Cloud`.

## Troubleshooting

| Message | Fix |
|---|---|
| `SUPABASE_ACCESS_TOKEN not found` | Add it to `app\.env`. Make one at https://supabase.com/dashboard/account/tokens |
| `Supabase API 401` | Token wrong or expired: make a new one. |
| `Supabase API 403` / `404` | Token's account has no access to that project, or the ref is wrong. |
| `Refusing to overwrite the project this backup came from` | Working as intended. Pass `--ref <new-ref>` for the new project. |
| `Some accounts are missing` | Create the emails listed in `backups\<date>\missing-accounts.txt`, then run again. |
