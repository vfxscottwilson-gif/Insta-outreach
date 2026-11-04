# projects/: one folder per app

**Rule (2026-11-05):** every app lives in ONE self-contained, portable folder `projects\<app-name>\`. Copy the folder to a new PC, run `install\Install.cmd`, and the app is back. Start new apps by copying `_TEMPLATE-app\`.

## What goes where
| Path | Goes in it | Git |
|---|---|---|
| `README.md` | What it is, 10-line quick start, map of the folder | hub repo |
| `GUIDE/` | `00-START-HERE` (numbered click-by-click setup), `01-ROADMAP`, `02-ARCHITECTURE`, `03-HOW-TO-CHANGE-THINGS`, `04-TROUBLESHOOTING`, `05-ACCOUNTS-AND-KEYS` (names/IDs only) | hub repo |
| `app/` | The source code with its own git repo (or the code directly if there is no separate repo) | own repo; ignored by the hub repo |
| `notes/` | Briefs and every session/hand-over note, copied here | hub repo |
| `private/` | `.env`, key files, account lists, `SECRETS-README.md` | **gitignored, never committed** |
| `install/` | `Install.cmd` + `install.ps1`: prerequisites (winget), dependencies, build, `.env`, shortcut, checklist. Idempotent, `-DryRun`, `-Uninstall` (shortcuts only) | hub repo |
| `backups/` | `backup.ps1` (folder zip + database export); outputs gitignored | script only |
| `reference/` | Read-only snapshots of related code that lives elsewhere (paths documented) | hub repo (text only) |

## Move or back up
- Move: copy the whole folder (with `private\`), run `install\Install.cmd`.
- Back up: `powershell -ExecutionPolicy Bypass -File <app>\backups\backup.ps1`. The zip contains `private\`: store it safely.

## Before you call an app done (checklist)
- [ ] `README.md` quick start works on a clean read
- [ ] `GUIDE/00..05` filled in (no placeholders left)
- [ ] All app-related notes copied to `notes/`; scattered files (shortcuts, key files, other folders) documented or copied
- [ ] `private/` has `.env`, key files, `SECRETS-README.md`; `git check-ignore -v private/.env` prints a rule
- [ ] `Install.cmd -DryRun` runs clean; real install tested at least on this PC
- [ ] `backup.ps1 -DryRun` runs; database export documented
- [ ] Project `CLAUDE.md` + `PROGRESS.md` current; committed; nothing pushed without approval
- [ ] No secret value in any committed file (grep for keys/tokens)

Apps: `email-automation` (Outreach), `levelup-crm`, `database` (lead dashboard, packaging pending).
