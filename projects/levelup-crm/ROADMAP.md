# LevelUp VFX CRM → ClickUp-style Work OS: Upgrade Plan

## 1. Where the CRM is today

- **Frontend only.** React 18 + Vite + TypeScript + Tailwind, ~5,300 lines across 11 view folders. No backend, database or API calls.
- **All data lives in the browser.** Every slice is `useState` saved to `localStorage` (`teamlog_*`): per-browser, never shared.
- **Login is a stub.** The password is never read; a "One-Click Direct Sign In" list and a sidebar user switcher let anyone become admin. Logout likely falls back to admin (not verified).
- **No forgot-password, email codes, sessions or hashing.** `resetPassword` only shows a temp password and never stores it.
- **Roles are UI-only.** Nothing enforces `admin`/`employee` (no server).
- **Feature set worth keeping:** dashboard, clock in/out with corrections, tasks with timers, projects, hourly and daily reports with review/comments, My Progress, Performance leaderboard, credential vault (visible to all users today), team management, settings (priorities, statuses, workday), audit log, data cleanup, CSV export. `TeamProgressView` is dead code.
- **No routing, tests, `.gitignore` or `.env`.** Vault secrets are plain text; Google Sheets sync is a stored URL only.
- **Data model gaps:** denormalized names, task `project` is a string, 12-hour time strings, no subtasks/comments/custom fields/hierarchy.
- **No CRM entities.** The repo has no leads, clients or deals (see open questions).

## 2. Target stack

| Layer | Choice | Why (one line) |
|---|---|---|
| Frontend | Keep React 18 + Vite + TypeScript + Tailwind | Works today and deploys to Vercel; add libraries, don't rewrite. |
| Routing, UI | React Router; shadcn/ui + lucide-react; dnd-kit | Deep links (`/t/:id`), accessible primitives, open-source icons, drag and drop. |
| Motion | `motion` + GSAP (scroll/timeline only) | Panels, reorders, hover cards. |
| Table / virtual | TanStack Table + Virtual | Table view, large lists. |
| Calendar / Gantt | FullCalendar (calendar), SVAR Gantt or Frappe Gantt (Gantt/Timeline); custom SVG Gantt as fallback | Avoid hand-rolling; `gantt-task-react` is largely unmaintained, so not used. |
| Docs / charts | Tiptap; Recharts | Docs view, task descriptions; dashboards. |
| Backend | **Supabase** (Postgres + Auth + Realtime + Storage + Edge Functions) | One service covers DB, login, live updates, file uploads, server code; `supabase` + `postgres-best-practices` skills installed. |
| Email | **Resend** via custom SMTP in Supabase, from Phase 0 | Built-in Supabase SMTP only sends to project team members (not verified), so it cannot reach employees; Resend has a free tier (~3,000/month, not verified). |
| Hosting | Vercel (frontend) + Supabase cloud | Existing `vercel.json`. |

**How the app standard is enforced**

| Rule | Mechanism |
|---|---|
| Email + password only | Supabase Auth email/password provider; all other providers and public sign-up disabled. Admin creates users via an Edge Function (`auth.admin.createUser`). |
| One active session per account | After every successful login or recovery `verifyOtp`, the client calls `supabase.auth.signOut({ scope: 'others' })` and upserts `active_sessions(user_id, session_id)` with the `session_id` from the JWT. An RLS helper `is_current_session()` compares `auth.jwt()->>'session_id'` to `active_sessions`, so old access tokens are refused immediately (revoking only kills the refresh token; the access token otherwise lives ~1 hour). A Realtime listener on the user's own row shows "signed in elsewhere" and signs out. Supabase's built-in single-session setting may be Pro-only (not verified). |
| Forgot password with code | `resetPasswordForEmail` → user enters the 6-digit code → `verifyOtp({email, token, type:'recovery'})` → `updateUser({password})`. The recovery email template shows `{{ .Token }}`. The session created by `verifyOtp` goes through the single-session step above. |
| Admin vs employee | `profiles.role` column + Postgres **Row Level Security**. Employees: access rows through ownership, OR task assignees/watchers, OR list/space membership (not just `user_id = auth.uid()`, which would break shared tasks, comments, Inbox, Chat); read shared lists (projects, statuses). Admin: `is_admin()` helper grants full CRUD on every table. Vault secrets use Supabase Vault (`vault.secrets`) or app-level encryption, not `pgsodium` (deprecated). Visibility: see open question. |
| Admin powers | Create/remove employees; create, assign and edit every task field; edit/correct other users' time entries, hourly and daily reports, documents and projects; manage priorities, statuses and workday settings; view the audit log. |
| Audit | `audit_log` written by triggers, not the client. |
| Secrets | Service role key never goes in the app `.env` or any `VITE_` variable; only in Edge Function secrets (`supabase secrets set`). Frontend gets only `VITE_SUPABASE_URL` and `VITE_SUPABASE_ANON_KEY`. |

## 3. Gap table

| ClickUp feature | Plan | Phase |
|---|---|---|
| Auth, sessions, reset, roles, multi-user DB, realtime, encrypted vault | **Build** (Supabase) | 0 |
| Hierarchy, sidebar, Inbox, List, Board, task panel, per-list statuses, Ctrl+K | **Upgrade/Build** (Space=department, Folder=client, List=project) | 1 |
| Table, Calendar, Gantt + dependencies, Timeline, Workload, custom fields | **Build** | 2 |
| Time tracking and hourly/daily reports | **Keep + unify** (`time_entries`, task optional) | 0/2 |
| Docs, Dashboards, Goals, Automations, Inbox, minimal Chat, Forms | **Build** | 3 |
| Whiteboards, Mind Map, AI, formula/rollup fields, 118 integrations, Google Sheets panel | **Later** (CSV import/export + webhook only) | later |
| Guests, SSO, SAML, SCIM | **Skip** | skip |
| Motion, polish, tests, CI, deploy | **Build** | 4 |

## 4. Roadmap

### Phase 0: Foundation (size L, pilot gate)
**Deliverables:** Supabase project; Resend custom SMTP with verified sender domain; schema as committed migrations in `supabase/migrations` (profiles, projects, tasks, time_entries, hourly_reports, daily_reports, report_comments, documents with encrypted vault, priorities, statuses, workday_settings, audit_log, active_sessions, notifications); RLS (ownership, assignee/watcher, list/space membership, `is_admin()`, `is_current_session()`); Edge Function for admin user creation; single-session client step and Realtime "signed in elsewhere" listener; recovery template showing `{{ .Token }}`; React Router; `.env`/`.gitignore`; Supabase data layer replacing localStorage; migration script from `teamlog_*` JSON export; login/forgot/reset screens; admin Team page on real users; demo sign-in list and user switcher removed.
**Done when:** two browsers logged into the same account → first one is signed out within 2 s and its old access token is refused by RLS; employee cannot read another employee's reports via the REST API (tested with pgTAP or curl); reset code email arrives at a real employee address and password changes; all 11 existing views work on Supabase data; `npm run build` passes; migration imports a sample export with zero loss.
### Phase 1: ClickUp shell + hierarchy + List/Board + task panel (size L)
**Deliverables:** Global sidebar (Home/My Tasks, Inbox, Spaces tree, favorites), Ctrl+K palette (cmdk); Space/Folder/List UI; List view with status groups and inline edit; Board view (dnd-kit); task side panel with subtasks, comments, activity, attachments (Supabase Storage), multiple assignees, watchers; per-list statuses; Sonner toasts replacing `confirm()`; own brand mark and lucide icons.
**Done when:** a task is created in a list, dragged across board columns, opened by URL `/t/:id`, commented on, and another user sees it live; `Ctrl+K`, `Esc`, `C` work.

### Phase 2: More views, custom fields, dependencies, unified time (size L)
**Deliverables:** Table, Calendar, Gantt (dependencies), Timeline, Workload; custom fields (JSONB); saved views; unified `time_entries` with timesheet page; reports link to time entries; admin date-range reporting.
**Done when:** every view renders the same list; a dependency blocks Done; a custom "Shot Code" dropdown shows in List/Table/Board; timesheet totals match entries.

### Phase 3: Docs, Dashboards, Automations, Inbox, Chat, Goals, Forms (size L)
**Deliverables:** Docs (Tiptap); dashboard builder (Recharts); automation rules; Inbox with @mentions; task comments as Chat plus simple channels; Goals; public intake form creating tasks.
**Done when:** @mention creates an Inbox item live; one automation runs; an incognito form submission creates a task.

### Phase 4: Polish, motion, performance, tests, deploy (size M)
**Deliverables:** motion pass; shortcut map; virtualized lists; Playwright E2E (auth, single session, reset, admin CRUD, DnD); Lighthouse ≥ 90; Vercel + Supabase deploy.
**Done when:** E2E green in CI; no native `confirm()`; usable at 375 px; production live with real email.

## 5. What I need from you

1. **Required:** Supabase account + new project. Put only the project URL and anon key in the app `.env` (as `VITE_SUPABASE_URL` / `VITE_SUPABASE_ANON_KEY`). The service role key goes only into Edge Function secrets via `supabase secrets set`, never in `.env`, never in a `VITE_` variable, never in chat.
2. **Required:** Resend API key + verified sender domain/address.
3. **Required:** Admin and employee emails + display names.
4. **Required:** Brand name, logo file (SVG/PNG), primary + accent colors (or say "pick for me").
5. **Required:** Migrate localStorage data? If yes, per browser: Settings → Full CSV export plus a JSON dump (I will give a console snippet).
6. **Required:** Vercel account linked to the GitHub repo (or say "local only for now").
7. **Required:** Top 5 ClickUp features (orders phases 2-3).
8. **Optional:** Hierarchy naming, workday timezone/target hours, multiple assignees, OK for a Claude API key later.

## 6. Copy-paste prompt for Claude Code

```text
You are the lead architect and commander for upgrading my CRM into a ClickUp-style work OS.

REPO: https://github.com/vfxscottwilson-gif/levelup-vfx-crm.git (clone to a working folder, init a feature branch `upgrade/clickup`).
FIRST: read README.md, package.json, src/App.tsx, src/context/*, src/types/index.ts, src/utils/initialData.ts and every view under src/components/** before coding. Produce a short inventory confirming every existing feature (dashboard, time clock + corrections, tasks + timers, projects, hourly/daily reports + review/comments, my progress, performance, documents vault, team management, settings incl. priorities/status CRUD and workday settings, audit log, data cleanup, CSV export). ALL must still work at the end; nothing removed, only upgraded. Decide explicitly: the Google Sheets panel moves to Later; TeamProgressView (dead code) gets wired into the admin portal.

APP STANDARD (applies to this and every app I build):
- Login is email + password only. No demo sign-in list, no user switcher, no public sign-up.
- Only ONE active session per account, enforced server-side: after every successful login or recovery verifyOtp the client calls supabase.auth.signOut({ scope: 'others' }) and upserts active_sessions(user_id, session_id from the JWT). An RLS helper is_current_session() compares auth.jwt()->>'session_id' to active_sessions so old access tokens are refused immediately. A Realtime listener on the user's own row shows "signed in elsewhere" and signs out. Do NOT use auth.admin.signOut(sessionId) or triggers on auth.sessions. Check whether Supabase's built-in single-session setting is available on my plan (may be Pro-only, not verified).
- Forgot password: resetPasswordForEmail sends a code (recovery email template shows {{ .Token }}); user enters it -> verifyOtp({ email, token, type: 'recovery' }) -> updateUser({ password }). Do not use signInWithOtp. The verified session goes through the single-session step.
- Admin portal: admin has full access, can add/remove employees, create/assign tasks and edit every task field (title, description, time, deadline, assignee, status, priority, everything), and can edit/correct other users' time entries, hourly and daily reports, documents and projects, manage priorities, statuses and workday settings, and view the audit log.
- Working backend for everything. No localStorage-only or fake data in production paths.

STACK: keep React 18 + Vite + TypeScript + Tailwind. Add React Router, shadcn/ui, lucide-react, motion, dnd-kit, TanStack Table/Virtual, cmdk, Sonner, Tiptap, Recharts, FullCalendar, SVAR Gantt or Frappe Gantt (custom SVG fallback; not gantt-task-react). Backend = Supabase (Postgres + Auth + Realtime + Storage + Edge Functions) with Row Level Security: employees access rows via ownership OR task assignees/watchers OR list/space membership; admin via is_admin(). Vault secrets: Supabase Vault (vault.secrets) or app-level encryption, not pgsodium. Email: custom SMTP via Resend from Phase 0 (built-in Supabase SMTP only reaches project team members). SECRETS: the service role key never goes in the app .env or any VITE_ variable, only in Edge Function secrets (supabase secrets set). The frontend gets only VITE_SUPABASE_URL and VITE_SUPABASE_ANON_KEY. Never print secrets.

DATABASE RULES: all schema, RLS and functions live as SQL in supabase/migrations, committed; never click-build in the dashboard. Test RLS with pgTAP or curl and show the output.

UX GOAL: ClickUp-paid-plan look and behaviour (sidebar, Space > Folder > List > Task > Subtask hierarchy, List/Board/Table/Calendar/Gantt/Timeline/Workload views, task side panel, custom fields, dependencies, Ctrl+K, Docs, Dashboards, Automations, Inbox, Goals, Forms, smooth motion) under MY OWN brand name, logo and colors, using lucide icons. Do NOT copy ClickUp's logo, name or assets.

SKILLS TO USE BY NAME: superpowers (brainstorming, writing-plans, subagent-driven-development, test-driven-development), supabase, supabase-postgres-best-practices, security-review, RedTeam, frontend-design, ui-ux-pro-max, shadcn, web-design-guidelines, react-best-practices, emil-design-eng, animate, gsap-skills, animation-performance, dataviz, webapp-testing, playwright, chrome-devtools, Council.

MULTI-AGENT RULE (mandatory): Haiku subagents for lookups and summaries, Sonnet for coding, research and tests, Opus for architecture, schema, security, hard bugs. The main session only for final decisions, plan approval and verification. Run independent workstreams in parallel with self-contained briefs; verify every subagent result before marking it done.

PHASES: follow Phases 0-4 of the roadmap.

PROCESS:
1. Write the brief (Goal / Done when / Options / Pick / Workstreams / Risks) and the Phase 0 plan. STOP and wait for my approval before writing code.
2. Pilot Phase 0 first: auth + single session + reset + admin + one view (Tasks) on Supabase. Show proof (test output, screenshots, curl showing RLS blocks). STOP for approval before Phase 1.
3. Keep PROGRESS.md and CLAUDE.md (purpose, how to run, secrets needed, status) updated every step so I can resume by clicking Continue.
4. Commit after each working step. NEVER push without my explicit OK: pushing the branch creates a public Vercel preview deploy.
5. NEVER send reset or invite emails to seed or migrated users without my OK.
6. Collect all questions up front, then run without interrupting me unless blocked.
7. Report in tables: done / not done / not verified, with proof.

INPUTS (I fill these in; ask for anything left as a placeholder):
- Admin emails: <...>
- Employee emails + names: <...>
- Brand name / logo path / colors: <... or "pick for me">
- Resend sender (domain/address): <...>
- Top 5 ClickUp features: <...>
- Hierarchy names (Space / Folder / List): <...>
- Migrate localStorage data (yes/no): <...>
- Vault visibility (all employees as today, or admin-only): <...>
- Add real CRM entities (clients, leads, deals pipeline) (yes/no): <...>

Start now with step 1.
```

## 7. Risks and open questions

1. **Supabase free tier pauses after 7 days idle** (not verified); budget Pro for daily use.
2. **Email:** built-in Supabase SMTP only reaches team members, so Resend is needed from Phase 0. No emails to seed/migrated users without your OK.
3. **Single-session enforcement** relies on `signOut({scope:'others'})`, the RLS check and Realtime; test token-refresh edge cases and a failed upsert (must fail closed); RedTeam in Phase 0.
4. **Gantt libraries** may lack dependencies; custom SVG Gantt is the fallback.
5. **Scope is large (4 L phases).** Without the top-5 answer, Phases 2-3 may build low-value views first.
6. **Open question: vault visibility.** Keep the credential vault visible to all employees (today) or admin-only? Not silently changed.
7. **Open question: CRM entities.** The repo has no leads/clients/deals. Do you want real CRM entities (clients, leads, deals pipeline)?

Not verified: prices, quotas, Supabase function signatures and plan limits; repo not re-opened. Risk: recovery template must show `{{ .Token }}` or users get a link, not a code.
