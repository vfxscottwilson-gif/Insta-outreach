# Cloud configuration notes (what lives online, and how to recreate it)

Checked against the repo files on 2026-11-05. No secret values here (names only).

## Supabase (project ref `laxxqmtwowitopbqnejs`, Mumbai, Free plan)
| Item | Where it is defined | Exported by |
|---|---|---|
| Tables, RLS, cron jobs, auth hooks | `app\supabase\migrations\` (27 files) | `database\cloud-export.ps1` writes `schema-<date>.sql` (needs `DATABASE_URL`) |
| Table data | database | `database\backup-data.mjs` (JSON per table) |
| Edge Functions `admin-users`, `sheets-sync`, `login-guard` | `app\supabase\functions\` | list + versions in `cloud-<date>\functions.json` |
| Edge Function secret NAMES | Supabase > Edge Functions > Secrets | `cloud-<date>\secret-names.json` (values can never be read back; see `secrets\SECRETS-CHECKLIST.md`) |
| Storage buckets | Supabase > Storage | `cloud-<date>\storage.json` (bucket list + file counts; the app uses no Storage today, so expect 0 buckets or 0 files) |
| Auth settings (sign-up off, min password 8, hooks ON) | Supabase > Authentication; mirrored in `app\supabase\config.toml` | **Not exported.** Re-set by hand from `app\CLAUDE.md` "Status" (hooks: `login_guard_access_token_hook`, `login_guard_send_email_hook`) |
| Auth users (logins) | `auth.users` | **Not exported** (passwords cannot be copied). Recreate people in the app: Team > Add New Team Member |

## Vercel (team `vfxscottwilson-gif`, project `levelup-vfx-crm`)
| Item | Where | How to recreate |
|---|---|---|
| Build + headers + daily cron | `app\vercel.json` (in the repo) | Comes with the code |
| Env vars `VITE_SUPABASE_URL`, `VITE_SUPABASE_ANON_KEY` (Production + Preview) | Vercel > Project > Settings > Environment Variables | Values are in `secrets\app.env.backup`; add them again in a new project |
| Project link | `app\.vercel\project.json` | `npx vercel link` (sign in first) |
| Address `levelup-vfx-crm-sigma.vercel.app` | Vercel > Domains | A new project gets a new address: update the Supabase Site URL and the `LOGIN_ALLOWED_ORIGINS` secret |

Optional snapshot of project settings (needs Vercel sign-in, not run by the backup script; prints variable NAMES and environments only):
```
npx vercel env ls
```

## Cloudflare
Not used by this app (hosting is Vercel). If a Cloudflare Turnstile CAPTCHA is added later (open item in `docs\SECURITY-AUDIT.md`), note its site key name here.

## Google
Service account `crm-automation-bot@trans-campus-513315-v0.iam.gserviceaccount.com` (key file `secrets\google-sa.json`). The mirror Sheet must be shared with it as Editor. The Sheet ID is stored in the app (Settings > Sheets sync).
