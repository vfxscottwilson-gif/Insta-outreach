# Email Automation: Setup guide

> Detailed chapters: [00 Start here](GUIDE/00-START-HERE.md) | [01 Roadmap](GUIDE/01-ROADMAP.md) | [02 Architecture](GUIDE/02-ARCHITECTURE.md) | [03 How to change things](GUIDE/03-HOW-TO-CHANGE-THINGS.md) | [04 Troubleshooting](GUIDE/04-TROUBLESHOOTING.md) | [05 Accounts and keys](GUIDE/05-ACCOUNTS-AND-KEYS.md). Installer: `install\INSTALL.cmd` (`-Check` = dry run). Secrets: `secrets\` (gitignored).

DRAFT: app still being built. Sections marked (TODO) are filled in when the build finishes. Source: `app\CLAUDE.md`, `app\docs\START_HERE.md`, `docs\BRIEF.md`. NEVER write secret values here.

## 1. What this app is
Cold outreach from 14+ Gmail accounts: touch 1 plus 4 follow-ups in one thread, zero duplicate sends, replies and bounces classified, and a dashboard (daily/weekly/monthly per account, health, capacity). Admin and employee roles. Windows .exe (Tauri) and phone app (PWA with push).

## 2. Accounts needed
| Service | Why | Free? | Link |
|---|---|---|---|
| Supabase | Database (single source of truth), login, vault for Gmail tokens | Free plan (2 active projects) | https://supabase.com/dashboard |
| Google Cloud | OAuth client so the engine sends from your Gmail accounts; service account to read lead sheets | Free | https://console.cloud.google.com |
| Cloudflare Pages | Hosting the web app (Vercel Hobby is non-commercial) | Free | https://dash.cloudflare.com |
| Small VPS (e.g. Hetzner) | Always-on worker | About 6 EUR/month (verify before buying) | https://www.hetzner.com |
| AI provider (Gemini / Groq / Claude) | Email writing; switch by changing the key | Free tiers vary | per provider |
| GitHub (private repo) | Code, CI | Free | https://github.com |

## 3. Backend vs frontend
- Frontend: `app\web\` (React + Vite, PWA, Tauri wrapper) hosted on Cloudflare Pages.
- Backend: `app\engine\` Python worker (stateless tick every 1-2 min) on the VPS.
- Database: Supabase Postgres; migrations in `app\supabase\`. Google Sheets are read-only lead sources.
- Supabase functions: (TODO, none confirmed yet).

## 4. Folder map
See `README.md`.

## 5. First-time install
`install\INSTALL.cmd` installs the tools (Node.js, Python/uv), runs `npm install` and the build, makes the Desktop shortcut and ends with a checklist (OK / SKIP / WARN / FAIL). Options (type after the file name): `-Check` (same as `-DryRun`: shows what would happen, changes nothing), `-Uninstall` (removes only the Desktop and Start-menu shortcuts), `-SkipHealthcheck` (does not contact the database). Safe to run again.
1. In File Explorer open the `install` folder, click the address bar, type `cmd`, press Enter.
2. Preview first (changes nothing):
```
INSTALL.cmd -Check
```
You should see lines starting `[DRY]` or `[OK]` and no `[FAIL]`.
3. Install for real:
```
INSTALL.cmd
```
If Notepad opens `app\.env`: paste each key after `=`, save, run the same command again. You should end with the checklist and an **Outreach** icon on the Desktop.
4. The accounts and keys (Supabase, Google, AI) are set up by hand: follow `app\docs\START_HERE.md` parts A to E.

## 6. Secrets
See `secrets\SECRETS-CHECKLIST.md`. They go in `app\.env` (never committed).

## 7. Run it / use it
1. Windows launcher: double-click **Outreach** on the Desktop, or:
```
"app\Start Outreach App.cmd"
```
You should see one app window (the local server runs hidden and stops when you close it).
2. Web dev (for changing the screens):
```
cd app\web
npm install --ignore-scripts
npm run dev
```
Open http://localhost:5173.
3. Build and put the online copy up to date (Cloudflare):
```
npm run build
npx wrangler@4.157.0 deploy
```
4. Engine (the sender), from `app\engine`:
```
cd app\engine
uv run python -m outreach healthcheck
```
You should see `can send: False` until setup (START_HERE) is finished. More commands: `app\docs\HOW-TO-RUN.md`.

## 8. How to change common things
| I want to... | Do this |
|---|---|
| Change daily send limits | Caps are code constants (Gmail max 70/day, domain max 650/day); ask Claude to change them |
| Switch AI provider | Put the new provider key in `.env` (TODO exact name) |
| Add a Gmail account | START_HERE part C |
| Change colours | `app\web\src\styles\theme.css` |

## 9. Troubleshooting
| Problem | Fix |
|---|---|
| `.env` not read | File must be named `.env`, not `.env.txt` |
| Supabase will not create a project | Free plan allows 2 active projects; pause an old one |
| Real sends blocked | Health Check blocks sends until sender names are confirmed (TODO detail) |

## 10. Move to a new PC
1. Copy the whole `email-automation` folder (with `secrets\`).
2. Put the secrets back in `secrets\` / `app\.env` if missing (names only in `secrets\SECRETS-CHECKLIST.md`; values from your password manager).
3. In `install\` run `INSTALL.cmd -Check`, then `INSTALL.cmd` (Node.js, Python/uv and the packages are installed for you).
4. Data lives in Supabase, so nothing else moves. Database exports go to `backups\` (run `backups\backup.ps1`; needs `pg_dump`), not into the app folder.
