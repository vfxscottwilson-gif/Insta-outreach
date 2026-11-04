# 03 How to change things

All commands: open Terminal in the folder named. Web = `app\web`, engine = `app\engine`.

## Change the company name / logo
1. Replace the SVG in `app\web\public\` (`level-up-vfx-logo.svg` company mark, `outreach-logo.svg` app mark, `logo.svg` = favicon source).
2. In `web`: `npm run icons` (regenerates PWA icons).
3. The name default lives in `web\src\lib\brand.ts` (and DB setting `APP_COMPANY_NAME` once live: Settings in the app).
4. Rebuild (below). Expected: new logo on the sign-in page.

## Change caps (daily limits)
1. Hard ceilings are code constants: `app\engine\src\outreach\caps.py` (`GMAIL_MAX_PER_DAY = 70`, `DOMAIN_MAX_PER_DAY = 650`) and `app\web\src\lib\caps.ts`.
2. Change both, then `cd app\engine`, `uv run pytest tests/test_caps.py -q` and `cd ..\web`, `node scripts/caps.check.ts`. Expected: pass.
3. Lower per-account caps need no code: edit them in the app (Accounts).

## Change settings (TEST_MODE, pause, address, signature)
Use the app: Settings. The live values are rows in the Supabase table `settings`. `PAUSE_ALL` stops every send at once.

## Add an employee
1. Sign in as admin > **Admin > Team > Add employee**. Enter email, job role, invite or starting password.
2. The password is shown once; give it to them. They choose their own at first sign-in.
3. Needs the `admin-users` Edge Function deployed (roadmap #1).

## Deploy a new web version (Cloudflare)
1. `cd app\web`, `npm run build`. Expected: `dist\` updated, no errors.
2. `npx wrangler@4.157.0 deploy`. Expected: prints the `workers.dev` URL.
3. First time on a PC: `npx wrangler@4.157.0 login` (browser opens, click Allow).
4. Open apps show "New version available > Reload".

## Run tests
| What | Command | Expected |
|---|---|---|
| Engine (all) | `cd app\engine`, `uv run pytest -q` | all pass (first run ~35 s, starts a local Postgres) |
| Web checks | `cd app\web`, `npm run build`, then `node scripts/a11y-check.mjs`, `node scripts/mobile-check.mjs <url> chromium` | 0 violations / 0 failures |
| Database access | `uv run python -m outreach.tools.migrate` | applied list + "nothing readable without login" |

## Database changes
1. Add `app\supabase\migrations\00NN_name.sql`. 2. `cd app\engine`, `uv run python -m outreach.tools.migrate` (uses `DATABASE_URL`). 3. Update `app\docs\SCHEMA.md`.

## Back up and restore
1. Backup: `powershell -ExecutionPolicy Bypass -File backups\backup.ps1`. Gives a dated zip (contains keys: keep private) and, with `pg_dump` installed, schema + data `.sql`.
2. Restore the folder: unzip anywhere, run `install\Install.cmd`.
3. Restore the database: in a new Supabase project run the schema `.sql`, then the data `.sql` with `psql`. The app can also restore from its Google Sheet backup (`app\docs\SHEET-BACKUP.md`, dry run first).

## Move to another PC
Copy the folder (including `private\`), run `install\Install.cmd`. Re-sign in to Cloudflare (`wrangler login`) there.
