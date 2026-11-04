# Outreach (email-automation)

Cold-outreach app for Level Up VFX / Haroon VFX: 14+ Gmail accounts, touch 1 + 4 follow-ups in one thread, zero duplicate sends, employee tracking, dashboard on PC and phone. **This folder is the whole app: copy it to a new PC and run the installer.**

## Quick start (new PC)
1. Copy this whole folder to the new PC (any path, e.g. `C:\Apps\email-automation`).
2. Double-click `install\INSTALL.cmd` (add `-DryRun` first if you only want a preview).
3. If Notepad opens `app\.env`: paste each key after `=`, save, run `INSTALL.cmd` again.
4. Read the checklist it prints at the end (OK / SKIP / WARN / FAIL).
5. Double-click **Outreach** on the Desktop (or `Start Outreach App.cmd`).
6. Online version: https://levelup-outreach.outreach-web.workers.dev
7. Problems: `GUIDE\04-TROUBLESHOOTING.md`. Backup: `backups\backup.ps1`.

## Where everything is
| Folder / file | What |
|---|---|
| `app/` | The code and its git repo (name kept as `app` on purpose; do not rename). `web/` front end, `engine/` Python worker, `supabase/` database + edge functions, `docs/` technical docs |
| `GUIDE/` | Setup, roadmap, architecture, how-to, troubleshooting, accounts table |
| `notes/` | Brief + every build-session note (`session-notes/`), desktop shortcut details |
| `secrets/` | **Secrets** (`.env`, Google key, account list). Gitignored. Never share. See `secrets/SECRETS-README.md` |
| `install/` | `INSTALL.cmd` + `install.ps1` (one-time installer, uninstall = shortcuts only) |
| `backups/` | `backup.ps1` (folder zip + database export) |
| `reference/` | Read-only copies of the related bots in `D:\All Automations Records\` (docs and the draft generator; not the originals) |
| `SETUP-GUIDE.md` | The 10-section roadmap (start here if new); links to the detailed chapters in `GUIDE/` |
| `docs/` | Brief and other planning docs (`BRIEF.md`; a copy is in `notes/`) |
| `database/` | Database notes: schema is `app/supabase/migrations/`; exports go to `backups/` (see `backups/backup.ps1`) |
| `proof/`, `archive/` | Screenshots / test output; old files (never deleted) |
| `Start Outreach App.cmd` | Opens the app (calls `app\Start Outreach App.vbs`) |

Rule for all apps: `F:\Github Repos\projects\README.md`. Status: `app\PROGRESS.md`.
