# 04 Troubleshooting

Full table: `..\SETUP-GUIDE.md` section 9. Most common:

| Symptom | Fix |
|---|---|
| `INSTALL.cmd -Check` shows MISSING Git/Node | Run `INSTALL.cmd` (installs them with winget), then reopen the window |
| MISSING `app\.env` | Run `INSTALL.cmd`: it copies it from `secrets\app.env.backup` |
| Can't log in after typos | Wait 15 minutes or admin clicks Unlock (Team page) |
| Nobody can log in | Roll back the auth hooks (`..\DEPLOYMENT.md`), check the `login-guard` logs in Supabase |
| Site loads but empty after a long break | Supabase Free paused after 7 idle days: Supabase dashboard > project > Restore |
| Sheet not updating | Share the Sheet with the bot email as Editor; re-run `node scripts/load-google-secret.mjs` in `app\` |
| `SUPABASE_ACCESS_TOKEN not found` / API 401 | Make a new token (supabase.com > Account > Access Tokens) and run `scripts\save-secret.ps1` |

Backup problems
| Message | Fix |
|---|---|
| `[TO DO] schema: no DATABASE_URL` | Optional. Add `DATABASE_URL=` to `secrets\.env` (see `..\database\RESTORE.md`) |
| `[TO DO] pg_dump not found` | `winget install PostgreSQL.PostgreSQL.17` (Command Line Tools only) |
| `Supabase API 403` on inventory | Token's account lacks access to the project; make a new token |
| `WARN cron` in inventory | pg_cron schema not readable; harmless |
