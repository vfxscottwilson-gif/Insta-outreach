# projects/: one folder per app (ONE standard)

**Rule (2026-11-05):** every app lives in ONE self-contained, portable folder `projects\<app-name>\`. Copy the folder to a new PC, double-click `install\INSTALL.cmd`, and the app is back. Start a new app by copying `_TEMPLATE\`. Rules for Claude sessions: `APPS-STANDARD.md`.

## Standard layout
| Path | Goes in it | Git |
|---|---|---|
| `README.md` | What it is, quick start, folder map | hub repo |
| `SETUP-GUIDE.md` | 10-section roadmap for a non-expert (numbered steps); links to `GUIDE/` | hub repo |
| `GUIDE/` | Detailed chapters: `00-START-HERE`, `01-ROADMAP`, `02-ARCHITECTURE`, `03-HOW-TO-CHANGE-THINGS`, `04-TROUBLESHOOTING`, `05-ACCOUNTS-AND-KEYS` (names/IDs only) | hub repo |
| `install/` | `INSTALL.cmd` (entry point, double-click) calls `install.ps1` (`-Check` / `-DryRun`, `-Uninstall` = shortcuts only). Idempotent | hub repo |
| `app/` | Source with its own git repo | own repo; ignored by hub |
| `database/` | DB notes, restore method, export scripts | hub repo |
| `docs/` | Brief, roadmap, features, audit, prices | hub repo |
| `notes/` | Copies of every session / hand-over note | hub repo |
| `proof/` | Screenshots, test output | hub repo |
| `reference/` | Read-only snapshots of related code that lives elsewhere | hub repo (text only) |
| `archive/` | Old or unused files (never delete, move here) | ignored |
| `backups/` | `backup.ps1` (folder zip + DB export); outputs gitignored | script only |
| `secrets/` | The ONE secrets folder: `.env`, key files, account lists, `SECRETS-CHECKLIST.md` (names only) | **gitignored** (`projects/*/secrets/`) |

## Move or back up
- Move: copy the whole folder (with `secrets\`), run `install\INSTALL.cmd`.
- Back up: `powershell -ExecutionPolicy Bypass -File <app>\backups\backup.ps1` (the zip contains `secrets\`: store it safely).

## Before you call an app done
- [ ] `README.md` quick start works on a clean read; `SETUP-GUIDE.md` + `GUIDE/00..05` have no placeholders
- [ ] App notes copied to `notes/`; scattered files (shortcuts, key files, other folders) documented or copied
- [ ] `secrets/` has `.env`, key files, checklist; `git check-ignore -v secrets/.env` prints a rule
- [ ] `INSTALL.cmd -Check` runs clean; a real install tested at least on this PC
- [ ] `backup.ps1 -DryRun` runs; DB export documented in `database/`
- [ ] Project `CLAUDE.md` + `PROGRESS.md` current; committed; nothing pushed without approval
- [ ] No secret value in any committed file

Apps: `email-automation` (Outreach), `levelup-crm` (CRM), `database` (lead dashboard, packaging pending).
