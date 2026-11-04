# Security audit 2026-11-04 (full adversarial pass)

Scope: app `upgrade/clickup` (React/Vite on Vercel), Supabase `laxxqmtwowitopbqnejs` (RLS, Auth, Realtime, Storage, Edge Functions
`admin-users`, `sheets-sync`), Vercel `api/keepalive.ts`. Live tests used only throwaway `*@levelup-sec.test` accounts, all deleted (0 left).
Real users were touched only by attempts that had to be refused (owner DB probes ran inside rolled-back transactions).

Proof (in `app/`): `npm run check:db` 265 PASS / 0 FAIL | `node scripts/security-live-test.mjs` 225 PASS / 3 FAIL (the 3 = rollout pending:
migrations 21-22, login-guard, hook) / 0 accounts left; rerunnable, `... cleanup` removes leftovers | `npm audit` 0 vulnerabilities |
`npm run build` green | CSP: `vite preview` + Playwright with the vercel.json headers: 0 violations on /login.
Commits (app repo): `15bff8e` migrations 21-22 + tests, `acfba29` login-guard, `638ab2c` headers, `53b6ca9` live test.

## Findings

| # | Item | Result | Proof / fix |
|---|---|---|---|
| a | Public sign-up: supabase-js, raw `/signup`, existing e-mail, `/otp` create, `/magiclink`, `/invite` without service role, anonymous | PASS: all refused, no account created, victim password unchanged | live a.* |
| a2 | `/otp` `create_user:false`: unknown e-mail 422 `otp_disabled`, existing 200 / 429 | **OPEN (low): account-existence oracle; not closable on Free.** The Send Email hook drops the mail but GoTrue still answers 422 vs 200. Throttled by `rate_limit_otp` 30/5 min/IP. The access-token hook makes any OTP / magic-link / recovery code useless for login | live; migration 22 |
| b | Only admin creates accounts; works only with the admin-set password; new accounts are employees | PASS (forced-change flag now off by default: product choice in `cc19d10`) | live b.* |
| c | Employee A vs B: select/insert/update/delete on 23 tables, embeds, `or=` filters | PASS: 0 rows / refused; B's rows, settings and owner row md5-identical after ~90 attempts | live c.* |
| c2 | RPCs (vault get/set, cleanup, admin_revoke_sessions, sheets_cron_secret_ok) as employee + anon; claim/clock/list_team as anon | PASS refused; `keepalive` anon by design (boolean) | live |
| c3 | `clock_in` race, 6 parallel | PASS: exactly 1 row | live |
| c4 | Unbounded employee text could fill the 500 MB Free DB | **FIXED, migration 21** (notes 2 000, report text 10 000, comments 4 000, 500 task ids) | check-db |
| c5 | OpenAPI root, `private` / `auth` schemas, GraphQL (anon + employee) | PASS (pg_graphql not installed) | live |
| c6 | Storage: list / create bucket / upload / download, anon + employee | PASS: no buckets, all refused | live |
| c7 | Realtime postgres_changes: A subscribed to tasks/comments while B's changed | PASS: A got nothing, B (control) got the events | live |
| c8 | Realtime public broadcast: anon can send on any topic | INFO (low): app has no broadcast/presence listeners. Recommend Realtime "Allow public access" off | live INFO |
| c9 | admin-users (all actions) and sheets-sync (all actions) without JWT / anon key / as employee / forged `x-cron-secret`; bootstrap wrong token | PASS: 401/403, settings unchanged | live |
| d | Owner: second admin set_role / set_password via function; DB demote / deactivate / re-email / owner flag | PASS refused | live d.*, check-db |
| d2 | Owner deletable via `auth.admin.deleteUser` (FK cascade runs as postgres; `protect_owner` skips postgres) | **FIXED, migration 21** (`protect_owner_auth_user`). Not reachable today (no delete action) | check-db |
| d3 | One-admin rule | PASS offline only (live would touch the real admin) | check-db |
| e | Single session; superseded admin token at admin-users; deactivated and password-reset accounts' old access + refresh tokens; old password | PASS all refused | live e.* |
| f | Login error generic (wrong password = unknown e-mail) | PASS | live |
| f2 | Rate limit | PASS: GoTrue 429 per IP | live |
| f3 | JWT lifetime | PASS: 600 s | live |
| f4 | `user_metadata` / `app_metadata` self-edit | PASS: grants nothing (role from profiles) | live |
| f5 | **Brute force per account**: Free has only per-IP limits; the Password Verification hook is Team/Enterprise only (docs 2026-11-04); leaked-password check is Pro+ | **FIX WRITTEN, rollout pending**: migration 22 + `login-guard` + Custom Access Token hook (Free). 5 fails / 15 min lock the e-mail 15 -> 30 -> 60 min; 20 fails / IP block the IP; identical answers for unknown e-mails; audit `LOGIN_LOCKED` + admin notification; `admin_login_unlock`. Without a guard ticket direct `/auth/v1/token` gets no session even with the right password | check-db (45 rows); live bf.* FAIL until rolled out |
| f6 | Residual after f5: direct `/auth/v1/token` answers differently for right vs wrong password (hook error vs `invalid_credentials`) = oracle limited only by GoTrue's per-IP limit | **OPEN (medium) until CAPTCHA**: Attack Protection CAPTCHA (Cloudflare Turnstile, free) + pass `captcha_token` through login-guard (already supported) | live INFO row after rollout |
| t1 | Takeover via self e-mail change | **FIXED, migration 21**: `email_change` blocked; admin e-mail changes copied to profile; profile e-mail must equal login e-mail | check-db; live t.* after apply |
| t2 | Employees reading `auth.users` | PASS refused | live |
| t3 | `list_team` gives employees colleagues' e-mails | ACCEPTED for a small studio (work e-mails for the directory); optional patch below | live INFO |
| t4 | E-mail recovery / OTP / magic link as login paths | Closed by the access-token hook (refuses every method except password-with-ticket and token_refresh) + Send Email hook (drops all auth mail); rollout pending | migration 22 |
| t5 | Password change without reauth | INFO: needs e-mail to turn on (mail is dropped); single session + 10 min JWT limit the risk | auth config |
| g | Secrets in git (112 commits: `sbp_`, service-role JWTs, `PRIVATE KEY`, `GOCSPX`) and `dist/` | PASS: only `.env.example` tracked; only JWT is the anon key; the `PRIVATE KEY` hit is generated inside `sheetsMapper.test.ts`. `dist/` holds the Google service-account e-mail (shown on purpose in Sheets settings, not a secret), no key | report |
| g2 | `.vercelignore` misses `secrets/` and `.env.test` | **OPEN (low)**: patch below (deploys use `git archive`, which already excludes them) | |
| g3 | Passwords in logs | PASS: functions log counts / errors only | grep |
| h | Security headers | **FIXED** (`vercel.json`): CSP (self, Supabase https + wss, Google Fonts, img data/blob/https, no unsafe-eval; style `unsafe-inline` for sonner/motion), frame-ancestors none + XFO DENY, HSTS preload, nosniff, Referrer-Policy, Permissions-Policy, COOP | Playwright: 0 violations, fonts load, login reaches Supabase |
| i | `npm audit` | PASS: 0 | |
| r1 | Documents vault kept in browser `localStorage` in plain text (`DataContext`, `valueOrPassword`), not Supabase Vault | **OPEN (medium)**: move to `documents` + `set/get_document_secret` (built, tested); until then no real secrets there | code review |
| r2 | Google Sheet formula injection | PASS in Sheets (`RAW`). Residual: a CSV export opened in Excel can run `=` cells from employee text | code review |
| r3 | `forced_password_change` is UI-only | INFO | code review |

## Rollout (not done by the audit)
1. Apply `20261104000021_security_hardening.sql`, then `20261104000022_login_guard.sql`.
2. `supabase functions deploy login-guard --no-verify-jwt` (+ `[functions.login-guard] verify_jwt = false` in config.toml).
3. Ship the AuthContext login patch (login-guard -> `setSession` -> `claim_session`).
4. Enable hooks (PATCH `/v1/projects/{ref}/config/auth`):
   `{"hook_custom_access_token_enabled":true,"hook_custom_access_token_uri":"pg-functions://postgres/public/login_guard_access_token_hook","hook_send_email_enabled":true,"hook_send_email_uri":"pg-functions://postgres/public/login_guard_send_email_hook"}`
   Rollback: `{"hook_custom_access_token_enabled":false,"hook_send_email_enabled":false}`.
5. Switch scripts that sign in directly to login-guard: `accounts-live-test.mjs`, `pw-reset-live-test.mjs`, `role-live-test.mjs` (security-live-test already does; UI scripts follow the app).
6. Rerun `node scripts/security-live-test.mjs`: expect 0 FAIL.

## Patches for files outside the audit
- `.vercelignore`: add `secrets/` and `.env.test`.
- Optional, hide colleagues' e-mails in `list_team`: `case when private.is_admin() or p.id = auth.uid() then p.email end`.

---

# Who can write what (audit 2026-11-04)

Enforced in Postgres (RLS policies + guard triggers), migrations `20261104000010` and `20261104000011`.
Proof: `npm run check:db` 156 PASS / 0 FAIL (offline); pgTAP on the hosted project 59 ran / 0 failed (rolled back).

## Tables

| Table | Employee could write before | Employee can write now |
|---|---|---|
| profiles | own name, avatar | nothing (only the server clears forced_password_change after a password change) |
| profiles.role / is_active / job_title | no | no. Admin only; the last active admin can't be demoted or deactivated (also blocks server code) |
| active_sessions | own row | own row (needed for one-session-per-account) |
| tasks: insert | yes (own tasks) | **no** |
| tasks: update | creator: everything; assignee: status, progress, notes, time taken, image | **assignee: status only** |
| tasks: delete | creator | **no** |
| task_assignees: add/remove | task creator | **no** |
| task_watchers: add/remove | self, task creator | **no** |
| projects, statuses, priorities | no | no |
| workday_settings, duty_overrides, workspace_settings | no | no |
| time_entries: clock in/out | insert/stop own, any time, many per day | **clock in/out only (RPC or direct), once a day, inside the duty window** |
| time_entries: task timers | start/stop own | **no** |
| time_entries: corrections, delete | no | no (admin; corrections are flagged and audited) |
| hourly_reports / daily_reports: create, edit draft, submit | yes | yes (own only; locked once submitted) |
| hourly_reports / daily_reports: delete | own drafts | **no** |
| report_comments: add | on own daily reports | on own daily reports |
| report_comments: edit, delete | own comments | **no** |
| notifications: create | no | no |
| notifications: update | own rows, any column | **own rows, read_at only** |
| notifications: delete | own rows | **no** |
| documents (vault) | no | no |
| audit_log | no | no |

## RPCs (functions an employee can call)

| Function | Runs as | Employee result |
|---|---|---|
| claim_session() | definer | claims own session (single-session rule) |
| clock_in(), clock_out() | invoker | same rules as the table: once a day, inside the window |
| clock_status() | invoker | reads own status only |
| list_team() | definer | read-only team directory (id, name, email, role, job title) |
| get_document_secret(id) | definer | refused unless the admin turned on vault_visible_to_all |
| set_document_secret(id, value) | definer | refused (admin check) |
| cleanup_old_data(months, types) | definer | refused (admin check) |
| private.* helpers and triggers | definer | not callable directly to change data |

Admin Edge Function `admin-users` (create, deactivate, set_role, send_reset): verifies the caller's JWT and `profiles.role = 'admin'` before using the service role.

## Decision taken by default (say if you want it changed)
- Employees can no longer start task timers; only the clock counts their time. Reversible in one policy.
- Employees can no longer edit their own name; the admin does it.
