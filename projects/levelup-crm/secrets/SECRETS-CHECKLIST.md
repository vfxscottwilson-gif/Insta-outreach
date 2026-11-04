# Secrets checklist (names only, NEVER values)

Rules: values live only in `secrets\`, `app\.env`, `app\.env.test`, Supabase secrets, Supabase Vault or Vercel env vars. Never paste a value into a guide, chat, commit or screenshot. This folder is gitignored (`projects/*/secrets/` in the hub `.gitignore`).

Status checked 2026-11-05 by reading key NAMES only.

## 1. Files on this PC
| Secret name | Where it is | Used by | How to get / replace it | Present? |
|---|---|---|---|---|
| `VITE_SUPABASE_URL` | `app\.env` (+ copy `secrets\app.env.backup`) | Frontend, `npm run dev`, keep-alive | Supabase → Project Settings → API → Project URL | Yes |
| `VITE_SUPABASE_ANON_KEY` | `app\.env` (+ backup) | Frontend (public by design, RLS protects data) | Supabase → Project Settings → API → anon public key | Yes |
| `ADMIN_EMAIL` | `app\.env` (+ backup) | `scripts\set-admin-password.mjs` | Owner email (khizarvfx@gmail.com) | Yes |
| `SUPABASE_ACCESS_TOKEN` | `app\.env` (+ backup, + `secrets\supabase-access-token.txt`) | All admin scripts, `supabase` CLI (deploy functions, set secrets, run SQL) | supabase.com → Account → Access Tokens → Generate (starts `sbp_`). Save with `scripts\save-secret.ps1` (reads clipboard, never shows it). **Full control of the project: guard it** | Yes (the .txt file's content not verified) |
| `NEW_ADMIN_PASSWORD` | `app\.env` (+ backup) | `scripts\set-admin-password.mjs` (owner password reset) | You type it. The script deletes it from `app\.env` after success | **Has a value now in both files: run the reset or delete the line, then delete it from `app.env.backup` too** |
| `QA_ADMIN_EMAIL`, `QA_ADMIN_PASSWORD`, `QA_EMPLOYEE_EMAIL`, `QA_EMPLOYEE_PASSWORD` | `app\.env.test` | QA/Playwright scripts | Throwaway `*.test` accounts made per test run | Yes (names) |
| Google service-account key | `secrets\google-sa.json` (+ copy `app\secrets\google-sa.json`) | Pushed into Supabase secret `GOOGLE_SA_JSON` by `node scripts\load-google-secret.mjs` | Google Cloud Console → project `trans-campus-513315-v0` → IAM → Service Accounts → `crm-automation-bot@trans-campus-513315-v0.iam.gserviceaccount.com` → Keys → Add key → JSON | Yes |

## 2. Supabase Edge Function secrets (project `laxxqmtwowitopbqnejs`)
See names: Supabase → Edge Functions → Secrets (values cannot be read back, only replaced).

| Secret name | Used by | How set | Notes |
|---|---|---|---|
| `SUPABASE_URL`, `SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY` | all functions | Auto-injected by Supabase | Service role key never goes in `.env` or code |
| `GOOGLE_SA_JSON` | `sheets-sync` | `node scripts\load-google-secret.mjs` | From `secrets\google-sa.json` |
| `PASSWORD_VAULT_KEY` | `admin-users` (stored password copies, AES) | `node scripts\set-vault-key.mjs --confirm` | **See warning below** |
| `BOOTSTRAP_TOKEN` | `admin-users` (one-time first-admin setup) | `npx supabase secrets set` | Set: not verified |
| `ADMIN_EMAIL`, `ADMIN_INITIAL_PASSWORD` | `admin-users` bootstrap | `npx supabase secrets set` | Only for first admin; set: not verified |
| `LOGIN_ALLOWED_ORIGINS` | `login-guard` (which websites may log in) | optional | Default already includes the live site + localhost. Set it if the site address changes |

## 3. Inside the database (Supabase Vault)
| Name | Used by | Notes |
|---|---|---|
| `sheets_sync_cron_secret` | pg_cron job → `sheets-sync` every 5 min (`x-cron-secret` header) | Created by migration `20261104000017/18`. Lives in the DB, travels with it |

## 4. Vercel env vars (project `levelup-vfx-crm`, team `vfxscottwilson-gif`)
| Name | Environments | Notes |
|---|---|---|
| `VITE_SUPABASE_URL`, `VITE_SUPABASE_ANON_KEY` | Production + Preview | Also used by `/api/keepalive` daily cron |

## 5. Account logins (keep in your password manager, NOT here)
GitHub (`vfxscottwilson-gif`), Vercel (vfx.scottwilson@gmail.com), Supabase dashboard, Google Cloud (owner of the service account), the Google Sheet owner, CRM owner admin (khizarvfx@gmail.com).

## WARNING: PASSWORD_VAULT_KEY
- **Back up `secrets\password-vault-key.txt`. Losing it makes every stored password copy unreadable** (each person then needs a new password once).
- Rotated 2026-11-05 to a key with this backup file (no stored copies existed, so nobody lost anything).
- `node scripts\set-vault-key.mjs --confirm` re-applies the key from the file (e.g. after moving to a new Supabase project); `--rotate` makes a new key (old file kept as `.old`). The installer's `-Cloud` mode uses the file when present and never makes a second key.

## After copying to a new PC: check
1. `secrets\` contains `app.env.backup`, `google-sa.json`, `supabase-access-token.txt`, `password-vault-key.txt`.
2. `app\.env` exists (installer copies it from `secrets\app.env.backup`; or copy by hand and rename to `.env`).
3. `app\secrets\google-sa.json` exists (copy from `secrets\`).
