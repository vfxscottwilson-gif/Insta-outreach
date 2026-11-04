# projects/: one folder per app (ONE standard)

**Rule (2026-11-05):** every app lives in ONE self-contained, portable folder `projects\<app-name>\`. Copy the folder to a new PC, double-click `install\INSTALL.cmd`, and the app is back. Start a new app by copying `_TEMPLATE\`. Rules for Claude sessions: `APPS-STANDARD.md`.

## Start here
1. Open an app folder, e.g. `levelup-crm\` or `email-automation\`.
2. Read its `README.md` (what it is, quick start).
3. Follow its `SETUP-GUIDE.md` step by step.
4. To move to another PC: copy the whole folder, then in `install\` run:
```
INSTALL.cmd -Check
```
Fix anything marked MISSING, then run `INSTALL.cmd`.

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

## All apps (one line each)
| Folder | What it is |
|---|---|
| `levelup-crm` | Work OS / CRM (Supabase + Vercel) |
| `email-automation` | Outreach email app (Supabase + Cloudflare) |
| `database` | Flask lead dashboard (packaging pending; another chat is building it) |
| `lead-bot-worldwide` | Worldwide lead bot, GitHub Actions daily, Google Sheets |
| `lead-bot-au` | AU-only lead bot edition |
| `outreach-bot` | Draft-email bot v3 (Google Sheets + AI keys) |
| `local-drafter` | Local AI email drafter (Ollama qwen3:8b) |
| `full-cycle-emails` | Docs only: master spec of the hunt, email and follow-up cycle |
| `ig-outreach` | Instagram lead / DM assist |
| `sheet-organizer` | Figma / sheet organizer |
| `scraper-tools` | gosom, yt-dlp, scrapetube, crawl4ai (manifest of how to re-download) |
| `yt-creator-finder` | YouTube creator client finder (GitHub Actions) |
| `harvey` | Third-party autonomous sales agent (own git, upstream recorded) |

`_shared\` = credentials used by several apps (gitignored). `INSTALL-ALL.cmd` runs every installer (add `-Check` to only check). `PROGRESS.md` = tracker.
