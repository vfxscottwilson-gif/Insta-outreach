# Deployment: how a change goes live

Three separate things deploy separately:

| Part | Lives on | Deploy how | Who |
|---|---|---|---|
| Website (frontend + `/api/keepalive`) | Vercel, team `vfxscottwilson-gif`, project `levelup-vfx-crm` | `git archive` export + `npx vercel --prod` (below) | Claude or you |
| Database (tables, security rules, cron) | Supabase `laxxqmtwowitopbqnejs` | Run new file from `app\supabase\migrations\` in the SQL Editor | Claude or you |
| Edge Functions `admin-users`, `sheets-sync`, `login-guard` | Supabase | `npx supabase functions deploy` | Claude or you |

Rules: commit first in `app\` (branch `upgrade/clickup`). Never push `upgrade/clickup` to `main` (`main` = old CRM). Never push or deploy without the owner's OK.

## Why the odd website deploy
Vercel Hobby **refuses deploys whose commits carry a `Co-Authored-By` trailer**. So we deploy a plain copy of the code (no git history) made with `git archive`, plus the `.vercel` link folder. GitHub auto-deploy is **not** connected.

## 1. Website
Before: `app\.vercel\project.json` must exist (links to the right Vercel project; it matches the archived `vfxscottwilson` link). Vercel CLI signed in as a member of team `vfxscottwilson-gif`.

1. Open **Command Prompt** in `app\` and check the build works:
```
npm run build
```
2. Export the committed code to a clean folder:
```
git archive --format=tar -o "%TEMP%\levelup-deploy.tar" HEAD
```
```
mkdir "%TEMP%\levelup-deploy" && tar -xf "%TEMP%\levelup-deploy.tar" -C "%TEMP%\levelup-deploy"
```
3. Copy the Vercel link into it:
```
xcopy /E /I .vercel "%TEMP%\levelup-deploy\.vercel"
```
4. Deploy to production:
```
cd /d "%TEMP%\levelup-deploy" && npx vercel --prod
```
5. Check: open https://levelup-vfx-crm-sigma.vercel.app, log in, see Home. Use a new temp folder name next time (or delete the old one yourself).

Exact commands above: **not verified as written** (the method is from `app\CLAUDE.md`; earlier deploys were done by Claude).

Vercel env vars needed (already set): `VITE_SUPABASE_URL`, `VITE_SUPABASE_ANON_KEY`. Daily cron `/api/keepalive` (06:00 UTC, `vercel.json`) keeps the Free Supabase project from pausing.

## 2. Database change (migration)
The CLI was never linked to the hosted project; migrations have been applied through the SQL Editor.
1. Write the change as a new file in `app\supabase\migrations\` (name starts with date + number, e.g. `20261106000060_x.sql`).
2. Test offline: `npm run check:db` (must end with 0 FAIL).
3. Supabase → SQL Editor → paste the file → Run.
4. Record it so tools know it ran (SQL Editor):
```
insert into supabase_migrations.schema_migrations(version, name) values ('20261106000060','x');
```
(Column list not verified on this project: check the table first.)
5. Live check: run the matching live test script, e.g. `node scripts/security-live-test.mjs`.

## 3. Edge Functions
In `app\`, with `SUPABASE_ACCESS_TOKEN` from `.env` in the environment (PowerShell):
```
$env:SUPABASE_ACCESS_TOKEN = (Select-String -Path .env -Pattern '^SUPABASE_ACCESS_TOKEN=(.+)$').Matches[0].Groups[1].Value
```
```
npx supabase functions deploy admin-users --project-ref laxxqmtwowitopbqnejs
```
```
npx supabase functions deploy sheets-sync --project-ref laxxqmtwowitopbqnejs --no-verify-jwt
```
```
npx supabase functions deploy login-guard --project-ref laxxqmtwowitopbqnejs --no-verify-jwt
```
`sheets-sync` and `login-guard` MUST keep `--no-verify-jwt` (they check callers themselves; set in `config.toml`). Check: `node scripts/guard-login-probe.mjs` (login 200, direct `/token` refused).

## 4. Secrets
| Change | Command (in `app\`) |
|---|---|
| Google key | `node scripts/load-google-secret.mjs` |
| Supabase access token in `.env` | copy token, then `powershell -ExecutionPolicy Bypass -File scripts\save-secret.ps1 SUPABASE_ACCESS_TOKEN` |
| Vault key | `node scripts/set-vault-key.mjs --confirm` (**breaks stored password copies**, read SECRETS-CHECKLIST first) |

## Rollback
| Problem | Undo |
|---|---|
| Bad website deploy | Vercel → project → Deployments → previous one → **Promote to Production** |
| Logins broken after hook change | Supabase Management API PATCH auth config `{"hook_custom_access_token_enabled":false,"hook_send_email_enabled":false}` (from `app\CLAUDE.md`) |
| Bad function | Redeploy the previous commit's function folder |
| Bad migration | Write a new migration that reverses it (never edit an applied file) |
