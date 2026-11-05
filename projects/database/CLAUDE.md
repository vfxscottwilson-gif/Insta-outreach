# Database (Level Up VFX lead tracking app)

**Location (2026-11-05):** this is the ONE project folder, `F:\Github Repos\projects\database` (final name, plain "Database": it is not a CRM), next to `levelup-crm` and `email-automation`. For a few hours it was named `projects\database`; that name still works as a Windows junction (link) so absolute paths in older notes and the Flask `.venv` keep working. Delete the `database` link once no note or script uses it. Inside: `app\dashboard` = the working Flask app (data, sync, login, access), `app\web` = the design preview (React, mock data), the docs at the root, `install\` and `GUIDE\` (portable installer, from the packaging chat). The old copy of the Flask app on D: (`D:\All Automations Records\Lead Dashboard`) is a backup only. Caches moved off C: to `F:\caches` (npm, uv) on 2026-11-05.

**Purpose:** one live dashboard for every lead-generation automation. It scans the user's Google Sheets every 1-2 minutes, shows how many leads each automation produced (today / week / month / last month), by country, state, niche and time zone, scores lead quality against the user's ICP, and lets the admin assign sheets and leads to employees. Fail-safe: only the admin can delete data; employees can add, and must request approval to remove.

**Family:** third app next to `projects/levelup-crm` (work OS) and `projects/email-automation` (Outreach). Same theme, shell, login standard (email + password, one active session, reset by code, admin portal). Brand mark: `brand/database-logo.svg` (user's reference in `reference/4.png`, finished in the CRM logo's depth style).

## Docs
| File | What |
|---|---|
| `BRIEF.md` | Goal-first brief, options, pick, red flags + fixes, workstreams, questions (the approval document) |
| `PROGRESS.md` | Workstream tracker |
| `reference/` | The user's reference shots (1-3 dashboards, 4 logo) |
| `preview/` | Clickable UI preview with mock data (no backend) |

## How to run
Preview (mock data, no backend): `cd app/web`, `npm install --ignore-scripts`, then `npm run dev -- --port 4174` or `npm run build` + `npx vite preview --port 4174`. Demo logins: `app/DEMO-LOGINS.md` (gitignored; regenerate with `node scripts/demo-logins.mjs` in `app/web`). Checks (from `app/web`, preview on 4174): `node scripts/preview-tour.mjs`, `a11y-check.mjs`, `mobile-check.mjs <url> chromium`, `consistency.check.mjs`, `screenshots.mjs`. Briefs for screen builders: `app/web/BUILDERS.md` and `V2-BRIEF.md`. Proof: `preview-proof/`.

## Backend decision (2026-11-04)
Supabase Free, lean mirror + log trimming, on a SEPARATE Supabase account (the user's different Gmail) because the main account's 2 free projects are used by the CRM and Outreach (dashboard shows "Level Up VFX, Free, 2 projects"). Do not add the main account as Owner/Admin of that org. See BRIEF section 13 (AUP section 4.2 caveat, mitigations).

## Secrets (only in `.env`, gitignored; never print)
None yet. Later: `SUPABASE_URL`, `SUPABASE_ANON_KEY` (web), `SUPABASE_SERVICE_ROLE_KEY` (Edge Function only), `GOOGLE_SA_JSON` (Sheets + Drive read, same service account style as the CRM).

## Rules
- Plan approved by the user before any backend code. Commit each working step; never push without the user's OK.
- Never write into the bots' sheets: the scanner uses read-only Google scopes; only the app-owned export sheet is ever written (BRIEF.md red flags 3 and 38). Test data: redacted fixtures only, no real company or contact data in the repo, screenshots or proof.

## Status / next step
- **2026-11-04 DECISION (user): the Lead Dashboard (`D:\All Automations Records\Lead Dashboard`, Flask + SQLite, chat "Build: Lead-gen dashboard & database") is the main working app (data, sync, login). The Database BACKEND build (Supabase schema, Edge Function scanner, hosted web app) is FROZEN; do not start those chats. The "Database UI: clickable preview" chat is NOT frozen: the user is steering it directly and it is the DESIGN the Lead Dashboard will be re-skinned to (so its tokens and components must be exportable as plain CSS + HTML). Nothing here is deleted: BRIEF, REDTEAM, UI-SPEC, logo, recon, ICP prompt (`reference/ICP-PROMPT-youtube-creators.md`) stay as reference. Requirements and findings handed over in `HANDOFF-TO-LEAD-DASHBOARD.md`. The Supabase account made with the second Gmail is not needed now.**
- 2026-11-04: BRIEF.md v3 (red-team folded in, `REDTEAM.md`), UI-SPEC.md with amendments, preview chat running (`app/web`, port 4174), storage/data-plan research running (BRIEF section 13). User answered: 2 admins incl. owner, both approve, Approvals folder, employee dashboards. Next: user answers questions A-E, data plan decided, then build chats start (schema, scanner pilot first).
