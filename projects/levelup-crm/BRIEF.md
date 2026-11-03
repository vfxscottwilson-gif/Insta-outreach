# LevelUp CRM upgrade: Brief + Phase 0 plan (for approval)

Written 2026-11-03 by the lead architect session. Sources: `ROADMAP.md` §6 (the brief this follows), the app inventory (Sonnet subagent, spot-checked), and `FACTS-CHECKED.md`.

## 1. Brief

| Section | Content |
|---|---|
| **Goal** | Turn the localStorage-only, fake-login TeamLog CRM into a real multi-user ClickUp-style work OS on Supabase, under your brand, losing no feature. |
| **Done when** | Phases 0-4 "Done when" lines in ROADMAP §4 all pass with proof. Phase 0 gate: single session proven in 2 browsers + RLS curl/pgTAP output + real reset-code email + all 11 views on Supabase + `npm run build` green. |
| **Options** | (a) Supabase (Postgres+Auth+Realtime+Storage+Edge) · (b) Firebase · (c) Own Node/Express + Postgres + Lucia auth · (d) PocketBase · (e) Fork an open-source ClickUp clone (Plane, Huly, Focalboard) and port features in |
| **Pick + why** | **(a) Supabase**, keeping the React/Vite app. RLS gives server-enforced roles; Auth has recovery OTP; Realtime powers "signed in elsewhere" and live boards; `supabase` + `postgres-best-practices` skills are installed. (e) was rejected: Plane/Huly are huge AGPL codebases, and porting your time clock, reports and vault into them costs more than adding views to your own app. |
| **Workstreams** | See §3 (Phase 0) and ROADMAP §4 (Phases 1-4). |
| **Risks** | See §5. |

## 2. Inventory: every existing feature (must all still work)

| Feature | Today | Phase 0 action |
|---|---|---|
| Dashboard | DashboardView | Same view, Supabase data |
| Time clock + corrections | TimeView, `correctSession` (UI-gated only) | `time_entries`; admin-only correction enforced by RLS; **fix UTC shift bug** in corrected times |
| Tasks + timers | TasksView, `toggleTaskTimer` | **Pilot view.** `tasks` + `task_assignees`; timer start stored server-side |
| Projects | ProjectsView | `projects`; remove hard-coded `2026-11-15` default deadline |
| Hourly reports | HourlyReportsView (admin sees today only) | `hourly_reports` (FK project); add a date filter for admin |
| Daily reports + review/comments | DailyReportsView | `daily_reports` + `report_comments` table |
| My Progress | MyProgressView | Same view |
| Performance leaderboard | PerformanceView | Same view |
| Documents / credential vault | DocumentsView; secrets readable by all; seed secrets in public repo | Values in Supabase Vault; visibility per your answer (INPUTS #7) |
| Team management | TeamManagementView (fake reset) | Real users via Edge Function `admin-users`; reset = sends real code email (only with your OK) |
| Settings: priorities, statuses, workday | SettingsView | Tables `priorities`, `statuses`, `workday_settings`; admin-only writes via RLS |
| Audit log | Written only by `correctSession`, **no UI** | Postgres triggers on all key tables + **new admin Audit Log page** |
| Data cleanup | `cleanupOldData` exists, **never called, no UI** | Admin-only RPC + a button in Settings (confirm dialog) |
| CSV export | `downloadCsv` in 5 views | Keep as is |
| Google Sheets panel | Stores a URL, never calls it | **Moves to Later** (panel hidden; CSV export stays) |
| TeamProgressView | Dead code (confirmed: imported nowhere) | **Wired into the admin portal** as "Team Progress" |
| Theme toggle | `teamlog_theme` | Stays in localStorage (per-device preference is fine) |

Known bugs fixed in Phase 0 because they break the app standard: password ignored at login; one-click login list and "Active Persona" switcher let anyone become admin; logout falls back to `users[0]` (confirmed `AuthContext.tsx:38`), so it never really logs out; `forcedPasswordChange` never enforced; `Date.now()` ids collide (→ uuid).

## 3. Phase 0 plan: Foundation (pilot first)

Order matters: the **pilot (P0.1-P0.7)** is auth + single session + reset + admin + **Tasks** on Supabase. Then **STOP for your approval**. Then P0.8-P0.9 move the other 10 views.

| Step | What | Owner (model) | Skills | Output | Done when |
|---|---|---|---|---|---|
| P0.1 | Scaffold: `.gitignore`, `.env.example`, `supabase init`, add `@supabase/supabase-js`, `react-router-dom`; app CLAUDE.md | Sonnet subagent | supabase | commit | `npm run build` green, `.env` ignored |
| P0.2 | Schema migration: profiles, projects, tasks, task_assignees, task_watchers, time_entries, hourly_reports, daily_reports, report_comments, documents, priorities, statuses, workday_settings, audit_log, active_sessions, notifications. uuid PKs, FKs instead of copied names, `timestamptz`/`time` instead of 12h strings, indexes on FKs | **Opus** designs, Sonnet writes SQL | supabase-postgres-best-practices | `supabase/migrations/0001_schema.sql` | `supabase db reset` runs clean locally |
| P0.3 | RLS + helpers `is_admin()`, `is_current_session()` on every table (ownership OR assignee/watcher OR membership; admin full) | **Opus** | supabase, security-review | `0002_rls.sql` + pgTAP tests | pgTAP green: employee can't read another's reports; old session token refused |
| P0.4 | Auth UI: email+password login, forgot → 6-digit code → new password, single-session step (`signOut({scope:'others'})` + upsert `active_sessions`), Realtime "signed in elsewhere", forced password change on first login; remove demo list + persona switcher; fix logout | Sonnet subagent (TDD) | superpowers:test-driven-development, frontend-design | `src/auth/*`, routes `/login`, `/forgot`, `/reset` | Playwright: login, wrong password, reset by code, 2nd login kicks 1st ≤ 2 s |
| P0.5 | Edge Function `admin-users` (create/delete/role/reset-email), checks caller `is_admin()`; service role key only via `supabase secrets set` | Sonnet writes, **Opus** reviews | supabase, security-review | `supabase/functions/admin-users` | curl as employee → 403; as admin → user created |
| P0.6 | Data layer: `useData()`/`useAuth()` keep their names, internals call Supabase (async). **Tasks view first.** | Sonnet subagent | react-best-practices | Tasks on Supabase | Admin creates task → employee sees it live; employee can't see others' tasks via REST |
| P0.7 | **Pilot proof + RedTeam** on auth/RLS; Fable go/no-go summary | Sonnet (Playwright), Opus (RedTeam), **Fable** (verdict) | webapp-testing, playwright, RedTeam | `proof/phase0-pilot/` (test output, curl output, screenshots) | → **STOP for your approval** |
| P0.8 | Remaining 10 views on Supabase; audit triggers + Audit Log page; cleanup RPC + button; vault via Supabase Vault; Team Progress in admin; hide Sheets panel | 2-3 Sonnet sessions in parallel (split by view files, no overlap) | supabase, react-best-practices | each view on Supabase | each view smoke-tested by Playwright |
| P0.9 | Migration script `scripts/import-localstorage.ts` from your `teamlog_*` JSON export (only if INPUTS #6 = yes) | Sonnet | — | script + dry-run report | sample export imported with zero loss (row counts match) |

Every step: commit on `upgrade/clickup`, update `PROGRESS.md` + app `CLAUDE.md`. **No push, no emails to real users without your OK.**

Single-session design (Free plan, because the built-in setting is Pro-only and lags up to 1 h):
- `is_current_session()` = `auth.jwt()->>'session_id'` matches `active_sessions.session_id` for `auth.uid()`.
- Fails closed. If the upsert fails, the new session is not current, so data is refused and the user sees "sign in again".
- Access-token expiry is lowered (for example to 10 min) as defence in depth. That setting may vary by plan (not verified).

## 4. Then (outline only, each gets its own plan + approval)
Phase 1 shell + hierarchy + List/Board + task panel → Phase 2 views/custom fields/time → Phase 3 Docs/Dashboards/Automations/Inbox/Chat/Goals/Forms → Phase 4 polish/tests/deploy. Order in 2-3 follows your top-5 (INPUTS #4).

## 5. Risks / unknowns

| Risk | Mitigation |
|---|---|
| Reset-by-code (`verifyOtp` type `recovery` with email+token) isn't shown verbatim in Supabase docs | Prove it first in P0.4 against your project. Fallback: same 6-digit `{{ .Token }}` via `verifyOtp` type `email` after admin-controlled check |
| No verified email domain → employees get no codes | INPUTS §C; build/test with your own address meanwhile |
| Public repo already holds seed vault values | INPUTS §E: rotate if real; Phase 0 removes them from code |
| Supabase Free pauses after 7 days idle | Pro at go-live (INPUTS #12) |
| Vercel Hobby is non-commercial | Vercel Pro or other host (INPUTS #11) |
| All context calls become async → many callers change | Keep same function names; P0.6 pilots on Tasks before touching other views |
| Scope (4 large phases) | Phase gates; your top-5 orders Phases 2-3 |
