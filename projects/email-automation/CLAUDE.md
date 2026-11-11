# Email Automation (Outreach)
Purpose: cold outreach from 14+ Gmail accounts (touch 1 + 4 follow-ups, zero duplicates), dashboard on PC/phone. Online: https://levelup-outreach.outreach-web.workers.dev
Layout and rules: `F:\Github Repos\projects\README.md`. Code: `app\` (own git; do not edit while another chat builds there). Full build log: `app\CLAUDE.md`, `app\PROGRESS.md`.

## Run
- Install: `install\INSTALL.cmd` (`-Check` = preview, `-Uninstall` = shortcuts only). Start: Desktop "Outreach" or `Start Outreach App.cmd`.
- Backup: `powershell -ExecutionPolicy Bypass -File backups\backup.ps1 [-DryRun] [-NoDb]`. Restore: `database\RESTORE.md`.

## Secrets (NAMES only, in `secrets\`, see `secrets\SECRETS-CHECKLIST.md`)
DATABASE_URL, SUPABASE_SERVICE_ROLE_KEY, SUPABASE_ACCESS_TOKEN, GOOGLE_SA_JSON (sheet-reader.json), GOOGLE_OAUTH_CLIENT_ID/SECRET, GEMINI_API_KEY, GROQ_API_KEY, CLOUDFLARE_API_TOKEN/ACCOUNT_ID. Never print values.

## Status / next step
- 2026-11-05 packaged in hub standard; app still being built (see `app\PROGRESS.md`). SETUP-GUIDE.md is marked DRAFT with TODO sections: fill when the build finishes.
