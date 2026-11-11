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

## Engine session handoff (written 2026-11-11 ~17:40 UTC)

**Created this round (all committed in `app\`, not pushed; live migrations 0024, 0025 applied):**
- `app\supabase\migrations\0024_counting_rules.sql`, `0025_sync_requests.sql`
- `app\engine\src\outreach\mailbox\classify.py`, `sync.py`, `events.py` (counting rules), `reclassify.py` (new)
- `app\engine\src\outreach\worker.py` (new), `__main__.py` (`worker` command), `mailbox\phase.py`, `settings.py`
- `app\engine\tools\run-tick.vbs`, `worker-task.ps1` (now a long-running worker, starts at logon)
- Tests: `app\engine\tests\test_counting_rules.py`, `test_worker.py`
- Commits: 3a44c3a (section A), beb695b + dff6053 (section B)

**Finished and verified:**
- Section A: live replies 74 -> 11; 63 moved to `other_inbound`; rerun changes nothing. 95 targeted tests pass.
- Section B (database + engine): `request_sync()`, `sync_requests`, `open_alert_count()`, worker loop (30 s poll, 3 min rounds), `MAILBOX_SYNC_MINUTES` = 3 live. 16 targeted tests pass. All 14 accounts synced within 8 minutes after the change.
- Design has the names (message queued to its session).

**Not done / not verified:**
- Full engine suite NOT run since 0024/0025 (last full run: 1365 passed before these). Run `uv run pytest -q` in `app\engine` first.
- `worker-task.ps1` must be run once more by the user (Claude is not allowed to create scheduled tasks) so the task starts at logon with no 10-minute time limit. Until then the old task restarts the worker every 10 minutes: it works, but less cleanly.
- New-thread replies older than today appear only after a 30-day re-read (not run). Auto Reply label: not checked per account.
- Section F (zero-cost always-on research): NOT started. Web tools in the Engine session are redirected by the context-mode hook; use `ctx_fetch_and_index` or a subagent. Facts needed: Supabase Free pg_cron + Edge Function limits, GitHub Actions private minutes and cron delays, Cloudflare Workers Free cron.
- Sections C and D (sheet-driven sending, niches): NOT started.

**Exact next step (Engine):** run the full suite; then section F research and report; then C/D per `app\docs\SPEC-V2-SHEET-AUTOMATION.md`. Nothing sends until the user approves a pilot.

## 4. Exact next step
Open the Engine session ("Build: Email app engine") and confirm it picked up the Spec V2 work order (step 1 = section A recount); open the Design session for its Spec V2 list; then deploy what passes and report.

## 5. Rule added 2026-11-11 (section 14 of the user's CLAUDE.md): release packaging
Next time code is delivered: a zip named `Email Automation v<N>.zip` (Title Case, lowercase v, number +1 each delivery) in this folder, complete and deployable with `install\` and `Start Here.md`, no secrets/.env/key files/.venv/.git/caches (names only in SECRETS-CHECKLIST.md), older zips moved to `Archive\`, contents checked before saying done. Title Case, no hyphens or underscores, for every name the user sees (folders, files, zips, Google Sheet and tab names). Not yet delivered: no zip exists, and the app's folder names (`app`, `install`, `email-automation`) are tool or project names still to be reviewed against this rule.
