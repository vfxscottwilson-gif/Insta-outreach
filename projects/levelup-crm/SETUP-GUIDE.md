# Level Up VFX CRM: setup guide (roadmap)

Checked against the files on 2026-11-05. Anything marked **not verified** was not tested.

## 1. What this is
A private website for the Level Up VFX team. Staff log in with email + password, clock in and out, see their tasks, write hourly and daily reports. The admin manages people, teams, projects, tasks, duty hours and settings. A copy of the data is written to a Google Sheet every 5 minutes.

Live: https://levelup-vfx-crm-sigma.vercel.app. Owner admin: khizarvfx@gmail.com.

## 2. Map of folders
| Folder | What |
|---|---|
| `README.md` | Start here + folder map |
| `SETUP-GUIDE.md` | This file |
| `DEPLOYMENT.md` | Publishing changes |
| `USER-GUIDE.md` | Daily use (staff + admin) |
| `install\` | `INSTALL.cmd` + `install.ps1` (installer; modes `-Check`, Setup, `-Cloud`, `-Local`) |
| `app\` | Source code, own git repo (branch `upgrade/clickup`) |
| `app\src\` | Website screens (React) |
| `app\supabase\migrations\` | Database tables + security rules (27 SQL files) |
| `app\supabase\functions\` | Server functions: `admin-users`, `sheets-sync`, `login-guard` |
| `app\api\keepalive.ts` | Daily ping so Supabase Free does not pause |
| `app\scripts\` | Admin + test scripts (password reset, secrets, QA) |
| `database\` | `backup-data.mjs`, `restore-data.mjs`, `README.md` (restore steps), `backups\` (saved copies, private) |
| `secrets\` | Keys (gitignored). Names listed in `secrets\SECRETS-CHECKLIST.md` |
| `docs\` | Roadmap, brief, features, prices, UI plan |
| `proof\` | Screenshots / test proof |
| `archive\` | Old CRM + old Vercel links (unused) |

## 3. Architecture
| Layer | Tool | Where | What it does |
|---|---|---|---|
| Frontend | React 18 + Vite + TypeScript + Tailwind | `app\src` → Vercel | The screens in the browser |
| Hosting | Vercel (Hobby), team `vfxscottwilson-gif`, project `levelup-vfx-crm` | vercel.com | Serves the site, security headers, daily keep-alive cron |
| Database | Supabase Postgres (Free, Mumbai, ref `laxxqmtwowitopbqnejs`) | supabase.com | All data. Row Level Security (RLS) decides who sees/edits what |
| Login | Supabase Auth + `login-guard` function + auth hooks | Supabase | Email + password only, one device per account, lockout after 5 wrong tries |
| Server functions | Supabase Edge Functions | `app\supabase\functions` | `admin-users` (add/remove people, set passwords), `sheets-sync` (Sheet mirror), `login-guard` (safe login) |
| Scheduled jobs | pg_cron in Supabase + Vercel cron | DB + `vercel.json` | Sheet sync every 5 min; keep-alive daily 06:00 UTC |
| Google Sheet mirror | Google Sheets API, service account `crm-automation-bot@trans-campus-513315-v0.iam.gserviceaccount.com` | Google Cloud | Writes tasks/staff to the Sheet (Sheet shared with that account as **Editor**) |
| Code storage | GitHub `vfxscottwilson-gif/levelup-vfx-crm` (private) | github.com | `upgrade/clickup` = new CRM, `main` = old CRM |

Backend vs frontend in one line: anything in `app\src` is frontend (what people see); `app\supabase` and `app\api` are backend (data, rules, server jobs).

## 4. Accounts you need
| Account | Login | What for | Cost |
|---|---|---|---|
| GitHub | `vfxscottwilson-gif` | Holds the code (private repo) | Free |
| Vercel | vfx.scottwilson@gmail.com (team `vfxscottwilson-gif`) | Hosts the website | Hobby, free |
| Supabase | the account that owns project `laxxqmtwowitopbqnejs` (**not verified which email**) | Database, login, functions | Free: 500 MB DB, pauses after 7 idle days (keep-alive prevents it) |
| Google Cloud | owner of project `trans-campus-513315-v0` (**not verified which email**) | Service account key for the Sheet | Free |
| Google Sheet | the Sheet owner | The mirror Sheet | Free |
| CRM owner admin | khizarvfx@gmail.com | Full admin inside the CRM | n/a |

## 5. Install on a NEW computer
`install\INSTALL.cmd` does the setup. Modes (type after the file name in Command Prompt):

| Command | What it does |
|---|---|
| `INSTALL.cmd -Check` | Changes nothing. Lists PASS / MISSING for tools, files, settings, internet |
| `INSTALL.cmd` (or double-click) | Setup: installs Git + Node.js if missing, restores `app\.env` from `secrets\app.env.backup`, `npm ci`, `npm run build` |
| `INSTALL.cmd -Local` | Starts the app on this PC (`npm run dev`) |
| `INSTALL.cmd -Cloud` | Puts the app online (Supabase link, migrations, functions, secrets, Vercel). Asks "Type YES" before each cloud change. Only for a new project |

Steps:
1. Copy the whole `levelup-crm` folder (with `secrets\`) to the new PC.
2. In File Explorer open the `install` folder, click the address bar, type `cmd`, press Enter.
3. Run the safe check first:
```
INSTALL.cmd -Check
```
You should see green `PASS` lines. Yellow `MISSING` lines are fine at this point (for example Git or Node.js); the last line says `RESULT: N item(s) need attention`.
4. Run the setup:
```
INSTALL.cmd
```
You should see `Step 1 of 4: tools` to `Step 4 of 4: build the app`, each with `PASS`, ending `RESULT: all good (Setup)`. It takes a few minutes. If it installed Git or Node.js and then stops, close the window and run it again.
5. Start the app on this PC (optional):
```
INSTALL.cmd -Local
```
Open http://localhost:5173 and log in. It uses the real live database.
6. Do the sign-ins below. Use `-Cloud` only when creating a NEW online copy (see `database\README.md`); moving to a new PC does not need it.

The installer never prints secret values. Its log is `install\install.log`.

### What only YOU can do (sign-ins)
1. GitHub: sign in when git asks (browser window) as `vfxscottwilson-gif`.
2. Vercel: `npx vercel login` and sign in as vfx.scottwilson@gmail.com.
3. Supabase: only if `SUPABASE_ACCESS_TOKEN` stopped working: supabase.com → Account → Access Tokens → Generate, copy it, run `powershell -ExecutionPolicy Bypass -File scripts\save-secret.ps1 SUPABASE_ACCESS_TOKEN` in `app\`.

## 6. Move to a new computer / backup
1. **Database backup first** (data lives in Supabase, not in the folder). In Command Prompt, in the `levelup-crm` folder:
```
node database\backup-data.mjs
```
You should see one `PASS` per table and `DONE ... saved to: ...\backups\<date_time>`. It only reads; nothing changes online. Restore into a new Supabase project: see `database\README.md`. Caveats: login accounts must be recreated first (Team > Add New Team Member, same emails), restore replaces the table contents in the new project, and the private schema plus encrypted password copies are not backed up.
2. Copy the whole `levelup-crm` folder (including `secrets\`, `database\backups\` and `app\.git`) to a USB drive or the new PC. `node_modules` can be skipped (the installer rebuilds it).
3. On the new PC follow section 5 (`INSTALL.cmd -Check`, then `INSTALL.cmd`).
4. Nothing on Vercel/Supabase/Google changes when you move PCs.

Keep the copy private: `secrets\` and `app\.env` hold keys that control the live system.

## 7. How to change common things
| Change | Where | Steps |
|---|---|---|
| Add employee | CRM → **Team** | **Add member** → name, email, job title, initial password (or **Generate**) → **Add**. Give them the password yourself |
| Remove access | CRM → Team | **Deactivate** (keeps history). Locked by wrong passwords? **Unlock** |
| Employee forgot password | CRM → Team | **Set new password** on their row (no email is sent) |
| Owner forgot password | `app\.env` | Add `NEW_ADMIN_PASSWORD=...` (8+ chars, upper, lower, number), then in `app\`: `node scripts/set-admin-password.mjs --check`, then `node scripts/set-admin-password.mjs`. It removes the line after success. Then change it in the CRM |
| Duty hours / clock windows | CRM → Settings → **Standard Workday Timings** | Shift start/end, clock-in and clock-out windows (Pakistan time). One person: **Per-employee hours** |
| Task statuses / priorities | CRM → Settings → **Task Statuses** / **Task Priorities** | Add, rename, reorder |
| Project assignment | CRM → **Projects** | Open the project, pick people and/or teams who can see it (exact button names not verified) |
| Teams | CRM → **Teams** | **New team**, add members |
| Branding (name, logo, colour, rail apps) | CRM → Settings → **Branding & apps** | Edit and save |
| Google Sheet | CRM → Settings → Sheets sync → **Sheet URL or ID** | Paste the new Sheet link. Share that Sheet with `crm-automation-bot@trans-campus-513315-v0.iam.gserviceaccount.com` as **Editor** first |
| Rotate Google key | Google Cloud → service account → Keys | Add new JSON key → save as `secrets\google-sa.json` and `app\secrets\google-sa.json` → in `app\`: `node scripts/load-google-secret.mjs` → delete the old key in Google Cloud |
| Rotate Supabase access token | supabase.com → Account → Access Tokens | New token → `save-secret.ps1` (section 5, sign-ins step 3) → revoke the old one → update `secrets\app.env.backup` |
| Vault key backup | `secrets\password-vault-key.txt`: back it up with the other secrets. Re-apply: `node scripts\set-vault-key.mjs --confirm`; rotate only if needed (`--rotate`) | Losing it makes stored passwords unreadable |
| Redeploy site | see `DEPLOYMENT.md` | `git archive` export + `npx vercel --prod` |
| Change code | `app\src` | Edit, `npm run build`, commit, deploy |

## 8. Security rules in force
- Email + password only. No sign-up page, no email reset, no magic links (auth hooks block them).
- One device per account: a new login signs out the old one.
- 5 wrong passwords in 15 min lock the account (15 → 30 → 60 min); too many from one IP block the IP. Admin can **Unlock**.
- Employees can only see their own / their team's tasks and change status. Everything else is admin-only, enforced in the database (RLS).
- One owner admin (khizarvfx@gmail.com) who cannot be demoted, deactivated or deleted.
- Security headers on the site (CSP, HSTS, no framing).
- Keys never in code; `.env` and `secrets\` are gitignored.
- Open items (see `docs/SECURITY-AUDIT.md`): CAPTCHA not on yet; Documents vault still in the browser (don't store real passwords there).

## 9. Troubleshooting
| Symptom | Likely cause | Fix |
|---|---|---|
| Site shows "Signed in elsewhere" | Same account logged in on another device | Log in again; only one device at a time |
| "Account locked" / can't log in after typos | 5 wrong passwords | Wait 15 min or admin clicks **Unlock** in Team |
| Nobody can log in | Auth hook / login-guard problem | Rollback in `DEPLOYMENT.md`; check Supabase → Edge Functions → login-guard logs |
| Site loads but no data, after a long break | Supabase Free paused (7 idle days) | Supabase dashboard → project → **Restore**. Check Vercel cron `/api/keepalive` runs |
| Sheet stops updating | Sheet not shared, key expired, or wrong Sheet ID | Share Sheet as Editor with the bot email; re-run `load-google-secret.mjs`; check Settings → Sheets sync "Last sync" |
| Clock In button greyed out | Outside the clock-in window or already clocked in today | Reason is shown under the button; admin changes hours in Settings |
| `npm install` fails | Node missing or too old | Install Node.js LTS, reopen Command Prompt |
| `npm run build` fails | Code error or missing `.env` | Read the first red line; copy `.env` from `secrets\app.env.backup` |
| Vercel deploy refused (trailer) | Deployed from git with `Co-Authored-By` | Use the `git archive` method in `DEPLOYMENT.md` |
| Scripts say `SUPABASE_ACCESS_TOKEN missing` / 401 | Token missing or revoked | Make a new one (section 5, sign-ins step 3) |
| Login says origin not allowed after domain change | `login-guard` origin list | Set Supabase secret `LOGIN_ALLOWED_ORIGINS` to include the new site |
| Stored passwords show "set a new password once" | `PASSWORD_VAULT_KEY` replaced/lost | Admin sets a new password for that person |

## 10. Glossary
| Word | Meaning |
|---|---|
| Frontend | The part in the browser (screens) |
| Backend | Server side: database, rules, functions |
| Supabase | Hosted database + login service |
| RLS | Row Level Security: database rules that decide who can read/change each row |
| Migration | A numbered SQL file that changes the database structure |
| Edge Function | Small server program run by Supabase |
| Vercel | Website hosting |
| Deploy | Putting a new version live |
| Cron | A job that runs on a schedule |
| Service account | A robot Google account the app uses to write the Sheet |
| `.env` | Hidden file with keys for this PC; never shared |
| Access token | A key that lets scripts control the Supabase project |
| Anon key | Public Supabase key used by the website; safe because RLS protects data |
| Service role key | Super key that bypasses RLS; only inside Supabase |
| Vault key (`PASSWORD_VAULT_KEY`) | Key that encrypts stored password copies |
| Branch | A separate line of code in git (`upgrade/clickup`, `main`) |
