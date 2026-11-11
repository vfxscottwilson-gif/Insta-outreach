# LevelUp CRM (upgrade/clickup)

**Purpose:** Upgrade the TeamLog / LevelUp VFX CRM (React 18 + Vite + TS + Tailwind, today localStorage-only with fake login) into a ClickUp-style work OS on Supabase, keeping every existing feature.

**Plan docs (outside this repo):** `F:\Github Repos\projects\levelup-crm\` — `ROADMAP.md` (phases), `BRIEF.md` (brief + Phase 0 plan + feature inventory), `INPUTS.md` (what the user must provide), `FACTS-CHECKED.md`, `PROGRESS.md` (tracker).

## How to run
```
npm install
npm run dev      # http://localhost:5173
npm run build    # tsc && vite build
npx supabase start   # local Supabase in Docker (Studio :54323, Mailpit :54324)
npx supabase test db # pgTAP tests (needs Docker)
npm run check:db # applies supabase/migrations to PGlite (Supabase stubs) and runs RLS assertions; no Docker needed
```

## Secrets
- `.env` (gitignored): `VITE_SUPABASE_URL`, `VITE_SUPABASE_ANON_KEY` only.
- `.env` also holds `ADMIN_EMAIL`, `ADMIN_INITIAL_PASSWORD` (server-side only, never VITE_, never seed.sql/logs). Password was pasted in chat → treat as exposed: create the admin via Supabase admin API (one-off Node script or Edge Function reading .env) with role=admin and forced_password_change=true; put the real admin email on the user record then, not in committed code (repo is public).
- Password recovery: no email, no codes. Employees ask the admin (Team -> Set new password). Owner/admin: put `NEW_ADMIN_PASSWORD` in `.env`, run `node scripts/set-admin-password.mjs` (8+, upper, lower, digit; `--check` is a dry run), then change it in the portal. Supabase built-in SMTP cannot be turned off (rate_limit_email_sent min 1 needs custom SMTP); /auth/v1/recover returns a generic 200 either way.
- Service role key + Resend key: never in `.env` or code; only `supabase secrets set`.

## Rules
- Branch `upgrade/clickup`. Commit each working step. **Never push without the user's OK** (push = public Vercel preview).
- No reset/invite emails to real users without the user's OK.
- All schema/RLS as SQL in `supabase/migrations`.

## Status / next step
- 2026-11-05 PRODUCTION = app `1debebb` (login via login-guard, Show password, Create task + allowed statuses, projects per person, delete account, lock/unlock, themed Select). LIVE: migrations 21, 22, 40, 50, 51, 52; PASSWORD_VAULT_KEY set; functions admin-users, sheets-sync, login-guard deployed; auth hooks ON (custom access token = login_guard_access_token_hook, send email = login_guard_send_email_hook). ROLLBACK if logins break: PATCH auth config `{"hook_custom_access_token_enabled":false,"hook_send_email_enabled":false}`. Proof: guard login 200 + direct /token refused (`node scripts/guard-login-probe.mjs`), security-live-test 233 PASS (3 late FAILs = GoTrue per-IP limit exhausted by the test's own ~40 logins: all logins share the guard's IP bucket, ~30/5 min). Scripts that call signInWithPassword directly (pw-reset-live-test, role-live-test, accounts-live-test) now fail by design: switch them to login-guard. Open: CAPTCHA (Turnstile, free) for the direct-REST password oracle; Documents vault still localStorage.
- 2026-11-04 PRODUCTION = app `957bb33` (legacy webhook field removed; Sheets sync LIVE, sheet set, first sync ok, every 5 min) on top of `dbb41c5` (adds Sheets sync, one-admin rule, owner protection, admin set-password UI; migrations 17-20 live; GOOGLE_SA_JSON secret set; live tests role/owner 17/17, password 13/13). Previous: app `6dc5442` on https://levelup-vfx-crm-sigma.vercel.app (Vercel team vfxscottwilson-gif, project levelup-vfx-crm; Supabase Site URL points there). Live: login (email+password only), single session, clock in/out rules, teams + team-only tasks, admin-only writes, job titles, admin set-password (`set_password` action, revokes sessions), mobile pass (648/648 WebKit + Chromium), Apple-like motion, link preview (og-image). Repo commits as vfxscottwilson-gif <vfx.scottwilson@gmail.com> (Vercel team member). Tests: check-db 192, hosted pgTAP 65, unit 15, QA scripts in scripts/ (qa-accounts, qa-logged-in, qa-mobile, pw-reset-live-test, pw-dialog-ui-test; all use throwaway *.test accounts and delete them). Password recovery is admin-driven (no email). QUEUED pending user yes: low-data/slow Wi-Fi mode + offline PWA. Never push upgrade/clickup to main (Vercel prod branch = main = old CRM).
- 2026-11-04 Hosting moved: old Vercel project (vfxscottwilson-gif) deleted by the user. New project `khizarvfx-8915/levelup-vfx-crm` (CLI login khizarvfx@gmail.com), VITE_SUPABASE_URL/ANON_KEY set for Preview + Production (type config). Deploy from `git archive HEAD` into a plain folder + copy `.vercel` (Hobby blocks commits with Co-Authored-By trailers). GitHub auto-deploy not connected (repo is under vfxscottwilson-gif). Supabase Free: 500 MB DB limit, pauses after 7 idle days -> daily Vercel cron `/api/keepalive` calls `public.keepalive()` (migration 0014).
- 2026-11-04 Admin bootstrapped (role admin, forced change); admin-users deployed (role fix `d050281`,`91e9f13`). Recovery by email dropped (2026-11-04). Owner recovery: NEW_ADMIN_PASSWORD in .env + `node scripts/set-admin-password.mjs`. Secrets saved via `scripts/save-secret.ps1` (clipboard). Vercel BLOCKS deploys whose commits carry a Co-Authored-By trailer (Hobby): deploy from `git archive HEAD` into a plain folder + copied `.vercel`. Preview: https://levelup-vfx-4lg5q573q-vfxscottwilson-gif.vercel.app (app `af6d55f`). Guide: ../GUIDE.html.
- 2026-11-04 P0.4-P0.6 built (not verified with a real user): Supabase Auth login/change-password (forgot/reset pages removed 2026-11-04), claim_session fail-closed, Realtime kick; Edge Function `supabase/functions/admin-users` written, NOT deployed; tasks/priorities/statuses/projects on Supabase (other slices still localStorage, `// shortcut:` in DataContext, P0.8). `npm test` (vitest). Next: deploy function + bootstrap admin, then real-user proof (P0.7).
- 2026-11-04 Hosted Supabase live: ref `laxxqmtwowitopbqnejs` (Mumbai, Free). 9 migrations + seed applied through the SQL Editor (CLI has no token; schema_migrations filled by hand), pgTAP 54/54 pass on real DB, sign-up off, min password 8. URL + anon key in .env and Vercel Preview (not Production). Repo is now PRIVATE. CLI not logged in: SUPABASE_ACCESS_TOKEN never reached .env.
- 2026-11-03 UI: U1 shell (`1c922c4`), U2 tasks List/Board/Calendar/side panel (`19f1e2b`), branding 'Level Up VFX' + admin Branding & apps settings (`984dcaa`), workspace_settings migration 0009; check:db 112 PASS. Pushed → branch preview. Next: user review → U3 (Home dashboard, Inbox, My Tasks) → U4 → U5. Plan: ../UI-PLAN.md, features: ../FEATURES.md.
- 2026-11-03: P0.1-P0.3 + hardening + 6 review fixes (`bb39cf2`..`7bfa622`); check:db 101 PASS / 0 FAIL; pgTAP plan(48) not yet run (Docker needs PC restart).
- Old CRM (`main`) is LIVE: https://levelup-vfx-crm.vercel.app (Vercel project levelup-vfx-crm, deployed from worktree `../app-main`, prod branch main). Branch pushed; preview: https://levelup-vfx-crm-git-upgrade-clickup-vfxscottwilson-gif.vercel.app. Old app opens straight into Admin (no real login) until Phase 0 ships. `upgrade/clickup` = preview only until Supabase live, login built, views switched.
- Docker skipped (no restart possible): run pgTAP against the hosted project once it exists (`npx supabase test db --linked` needs a container runtime, so fall back to running rls.test.sql via psql/SQL editor); P0.4 auth UI must call `rpc('claim_session')` (not a direct active_sessions upsert).
- Hosted dashboard must mirror config.toml: signup off, min password 8. Re-check: postgres may delete auth.sessions / triggers on auth.users / vault on hosted.
