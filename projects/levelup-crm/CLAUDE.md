# LevelUp CRM (Level Up VFX team CRM)
Purpose: React + Vite + TS site on Vercel; Supabase (ref `laxxqmtwowitopbqnejs`) for data, login and functions; Google Sheet mirror. Live: https://levelup-vfx-crm-sigma.vercel.app
Layout and rules: `F:\Github Repos\projects\README.md`. Code: `app\` (own git, branch `upgrade/clickup`; do not edit while another chat builds there). Full build log: `app\CLAUDE.md`.

## Run
- Check/install: `install\INSTALL.cmd -Check`, then `INSTALL.cmd`; local: `INSTALL.cmd -Local` (http://localhost:5173); cloud: `-Cloud` (asks YES per step).
- Backup: `powershell -ExecutionPolicy Bypass -File backups\backup.ps1 [-DryRun] [-NoDb]`; data only: `node database\backup-data.mjs`. Restore: `database\README.md`, `database\RESTORE.md`.

## Secrets (NAMES only, in `secrets\`, see `secrets\SECRETS-CHECKLIST.md`)
VITE_SUPABASE_URL, VITE_SUPABASE_ANON_KEY, ADMIN_EMAIL, SUPABASE_ACCESS_TOKEN, NEW_ADMIN_PASSWORD, DATABASE_URL (optional, schema export), PASSWORD_VAULT_KEY, GOOGLE_SA_JSON (google-sa.json). Never print values.

## Status / next step
- 2026-11-05 packaged in hub standard (README, SETUP-GUIDE, GUIDE\00-05, install, database, backups, secrets, notes). Added cloud export (`database\cloud-export.ps1`).
- Next: add `DATABASE_URL` to `secrets\.env` and run the first real schema export; open items in `docs\SECURITY-AUDIT.md` (CAPTCHA, Documents vault).
