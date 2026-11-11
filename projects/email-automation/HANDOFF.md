# HANDOFF (control room, written 2026-11-11 before the 12:00 a.m. PKT stop)

## 1. Created so far (paths)
- App repo: `app\` (own git, not pushed). `app\web` screens, `app\engine` Python worker, `app\supabase` migrations 0001-0023 + Edge Functions, `app\docs`.
- Specs: `app\docs\BUILD_PROMPT.md`, `SPEC-EMPLOYEES-TRACKING.md`, `SPEC-V2-SHEET-AUTOMATION.md` (newest, commit a4fff0f), `SCHEMA.md`, `ACCESS-RULES.md`, `WORKFLOW.md`, `web\PHONE-REPORT.md`, `web\KNOWN-ISSUES.md`.
- Packaging: `README.md`, `SETUP-GUIDE.md`, `GUIDE\`, `install\INSTALL.cmd`, `backups\`, `secrets\` (gitignored).
- Live: app https://levelup-outreach.outreach-web.workers.dev (Cloudflare Workers `levelup-outreach`), database Supabase project `bnivytzudrpjlscwdxuh`, Google OAuth client in project `outreach-512901`, Sheets service account in `trans-campus-513315-v0`.

## 2. Finished and verified
- Live database with admin login; 14 Gmail accounts connected in tracking mode; scheduled sync on this PC runs (last read 2026-11-11 17:01 UTC; 1,242 first emails, 348 follow-ups recorded).
- Web app live on real data for sign-in, team, accounts, overview, alerts, replies; two devices per login (migration 0023, engine suite 1365 passed per the Engine session).
- Last control-room deploy: Cloudflare version 15ff64aa (commit f309a1d + working tree). Later commits (4ec8bd5, f48e0da, 14f477d, de89f8e) may have been deployed by the Design session: not verified.

## 3. Left to do (all in SPEC-V2)
- A: reply counting is wrong on live (60 of 74 'replies' are mailsuite.com): new rules + recount. Not started (Engine message queued).
- B: Sync button, faster rounds, notification badge count.
- Design list: remove sample data (card shows 'United States -198'), overlaps, theme picker, Niches, 'New' badge.
- C/D: sheet-driven automation, niches. F: zero-cost always-on host decision (Supabase cron vs GitHub Actions).
- iPhone bottom bar: needs the user's `/viewport-debug` screenshot.
- Web OAuth client for the in-app Connect button (`GMAIL_CONNECT_CLIENT_ID/SECRET` missing in `.env`).
- From the user: pilot sheet shared with the service account, niche timing case study, postal address decision, 'free' wording decision. No real sends until the user says go.

## 4. Exact next step
Open the Engine session ("Build: Email app engine") and confirm it picked up the Spec V2 work order (step 1 = section A recount); open the Design session for its Spec V2 list; then deploy what passes and report.
