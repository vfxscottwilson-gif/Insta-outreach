# 02 Architecture

| Layer | Tool | Code | Cloud or local |
|---|---|---|---|
| Frontend (screens) | React 18 + Vite + TypeScript + Tailwind | `app\src` | Built locally, served by Vercel (cloud) |
| Hosting | Vercel Hobby, project `levelup-vfx-crm` | `app\vercel.json` | Cloud |
| Database + RLS | Supabase Postgres, ref `laxxqmtwowitopbqnejs` | `app\supabase\migrations` (27 files) | Cloud |
| Login | Supabase Auth + `login-guard` function + auth hooks | `app\supabase\functions\login-guard` | Cloud |
| Server functions | Edge Functions `admin-users`, `sheets-sync`, `login-guard` | `app\supabase\functions` | Cloud |
| Scheduled jobs | pg_cron (Sheet sync every 5 min), Vercel cron (`/api/keepalive`, 06:00 UTC) | migrations, `app\api\keepalive.ts` | Cloud |
| Sheet mirror | Google Sheets API, service account | `secrets\google-sa.json` | Cloud |
| Admin / test scripts | Node scripts | `app\scripts` | Local |
| Backup / restore | Node + PowerShell | `database\`, `backups\` | Local, reads cloud |

Flow: browser -> Vercel (static site) -> Supabase (login via login-guard, data protected by Row Level Security). Rule of thumb: anything in `app\src` is frontend; `app\supabase` and `app\api` are backend.

Rules that matter: employees see only their own/team tasks; everything else is admin-only, enforced in the database, not in the screens. The service-role key never leaves Supabase.
