# 04 Troubleshooting (symptom > fix)

| Symptom | Cause | Fix |
|---|---|---|
| `healthcheck` / `migrate`: "password authentication failed" or cannot parse URL | Database password rejected, or it contains `@` (and `#`, `/`, `:`) | Reset the password: Supabase > Project Settings > Database > Reset. In `DATABASE_URL` encode special characters: `@` > `%40`, `#` > `%23`, `/` > `%2F`, `:` > `%3A` |
| Engine cannot connect, host unreachable | Direct DB host is IPv6-only on the free plan | Use the **Session pooler** string (Connect > Session pooler, port 5432), as in `.env.example` |
| `create_admin` fails: "invalid API key" / 401 | `SUPABASE_SERVICE_ROLE_KEY` was pasted truncated (the secret key is long, ~40+ chars; a partial copy fails) | Copy again with the Copy button (Project Settings > API Keys > secret), paste on one line, no spaces/quotes |
| Edge Function deploy: "access token not provided" | No `SUPABASE_ACCESS_TOKEN` | Supabase > Account > Access Tokens > generate (`sbp_...`), put in `app\.env` |
| `wrangler deploy`: "not authenticated" / "Workers Scripts Edit" missing | Wrangler not signed in on this PC; the API token in `.env` lacks the Workers permission | `npx wrangler@4.157.0 login` (browser, Allow). Or make a token from the "Edit Cloudflare Workers" template |
| Deploy works but the site shows the old version | Browser cache | Wait for "New version available", click Reload; PWA checks hourly |
| Sheets import: "file not found" / no leads | `GOOGLE_SA_JSON` path wrong (it once pointed to `sheets-reader.json`; the file is `sheet-reader.json`) | Run `install\Install.cmd` (repairs the path), or set the full path in `app\.env`. Then share each lead sheet with the service-account email as Viewer (see 05) |
| Sheets import: 403 "permission" | Sheet not shared with the service account | Sheet > Share > add the service-account email > Viewer, untick Notify |
| Backup to sheet fails | Service account needs **Editor** on the backup sheet, or wrong sheet ID | `app\docs\SHEET-BACKUP.md`; ID = part between `/d/` and `/edit` |
| iPhone: tab bar floats / gap under it | Safari toolbar resizing the viewport with fixed bars | Fixed in commit 77994ce (100dvh column, no `position: fixed`). Needs a real-phone check: `app\web\KNOWN-ISSUES.md` |
| App opens blank, launcher says "Setting up" forever | `node_modules` missing or npm failed | `cd app\web`, `npm install --ignore-scripts`, `npm run build` |
| Launcher: "did not start within 30 seconds" | Port 4180 used by another copy | Close all Outreach windows; end `node.exe` running `vite.js` in Task Manager |
| `winget` not found in installer | Old Windows / no App Installer | Microsoft Store > "App Installer" > Update; or install Node LTS, Python 3.12, uv, Git by hand |
| Tool installed but "not on PATH yet" | PATH changes need a new window | Close and re-run `Install.cmd` |
| `.git/index.lock` exists | A git command is running or crashed | Wait a minute; if no git is running, delete that one file |
| `uv sync` slow/fails on Python | Python 3.12 missing | `winget install Python.Python.3.12`, or let `uv` download it |
| Login locked | 5 wrong passwords (15 min, growing delay) | Wait, or admin: Team > the person > Reset password |
| Real send blocked | Health Check: postal address / opt-out line / TEST_ADDRESSES not set, TEST_MODE on, or PAUSE_ALL | Set them in Settings; `uv run python -m outreach healthcheck` shows which |
