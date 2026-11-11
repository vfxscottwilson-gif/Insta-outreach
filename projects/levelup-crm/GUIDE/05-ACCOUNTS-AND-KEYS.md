# 05 Accounts and keys (names and IDs only; values live in `secrets\`)

| Service | What | ID / account | Secret lives in |
|---|---|---|---|
| Supabase | Project, Mumbai, Free | ref `laxxqmtwowitopbqnejs`; owner account email not verified | `SUPABASE_ACCESS_TOKEN` in `secrets\app.env.backup` + `secrets\supabase-access-token.txt`; optional `DATABASE_URL` in `secrets\.env` |
| Vercel | Team `vfxscottwilson-gif`, project `levelup-vfx-crm` | login vfx.scottwilson@gmail.com (also CLI login khizarvfx@gmail.com on project `khizarvfx-8915/levelup-vfx-crm` per `app\CLAUDE.md`) | env vars `VITE_SUPABASE_URL`, `VITE_SUPABASE_ANON_KEY` |
| GitHub | Private repo `vfxscottwilson-gif/levelup-vfx-crm` | branch `upgrade/clickup` = new CRM, `main` = old CRM | browser sign-in |
| Google Cloud | Project `trans-campus-513315-v0`, service account `crm-automation-bot@...iam.gserviceaccount.com` | owner email not verified | `secrets\google-sa.json` |
| CRM owner admin | In-app admin | khizarvfx@gmail.com | `NEW_ADMIN_PASSWORD` (temporary, only for resets) |
| Vault key | Encrypts stored password copies | n/a | `secrets\password-vault-key.txt` (back it up) |

Complete list with where each name is used and how to get it: `..\secrets\SECRETS-CHECKLIST.md`. File inventory: `..\secrets\SECRETS-README.md`. Cloud settings: `..\database\CLOUD-CONFIG.md`.
