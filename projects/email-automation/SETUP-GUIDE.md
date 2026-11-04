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
(TODO: `install\INSTALL.cmd` is not written yet.) Until then follow `app\docs\START_HERE.md` parts A to E: Supabase project, Google OAuth client, connect each Gmail account, service account for sheets, pilot.

## 6. Secrets
See `secrets\SECRETS-CHECKLIST.md`. They go in `app\.env` (never committed).

## 7. Run it / use it
- Windows launcher: `app\Start Outreach App.cmd`.
- Web dev: `cd app\web`, `npm install --ignore-scripts`, `npm run dev` (http://localhost:5173).
- Engine: `cd app\engine`, `uv run ...` (see `app\docs\HOW-TO-RUN.md`).

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
1. Copy the whole `email-automation` folder.
2. Recreate `app\.env` from `secrets\SECRETS-CHECKLIST.md` (values from your password manager).
3. Install Node, Python/uv (TODO: `install\INSTALL.cmd`).
4. Data lives in Supabase, so nothing else moves. Keep `database\backups\` current.
