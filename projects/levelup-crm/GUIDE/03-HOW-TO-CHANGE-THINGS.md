# 03 How to change things

Day-to-day changes (add employee, hours, statuses, Sheet, passwords) are tabled in `..\SETUP-GUIDE.md` section 7. Summary and the developer changes:

| Change | How |
|---|---|
| Add / remove / unlock a person, set a password | In the CRM: Team page |
| Work hours, statuses, branding, Sheet link | In the CRM: Settings |
| Owner forgot password | Put `NEW_ADMIN_PASSWORD` in `app\.env`, then in `app\` run `node scripts/set-admin-password.mjs --check` and then the same without `--check` |
| Change screens | Edit `app\src`, run `npm run build`, commit in `app\`, deploy (`..\DEPLOYMENT.md`) |
| Change database | New numbered SQL file in `app\supabase\migrations\`, test with `npm run check:db`, run in the Supabase SQL Editor (`..\DEPLOYMENT.md` section 2) |
| Change a server function | Edit `app\supabase\functions\<name>`, deploy (`..\DEPLOYMENT.md` section 3) |
| Rotate a key | `..\SETUP-GUIDE.md` section 7 (Google key, Supabase token, vault key). Then update `secrets\` |
| Change the cloud backup | Edit `database\cloud-export.ps1` or `database\storage-and-config-inventory.mjs`; test with `backups\backup.ps1 -DryRun` |

Rules: commit in `app\` after each working step; never push to `main` (old CRM); never push or deploy without the owner's OK; no key values in any file except `secrets\`.
