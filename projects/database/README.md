# Database (Lead Dashboard)

A local Flask + SQLite dashboard over the agency's lead Google Sheets: counts per day/month, by country/niche/source/status, duplicates, and assigning leads to team members. It is NOT an email tool. Runs on this PC at http://127.0.0.1:8080.

## Start here
1. New PC? Read `SETUP-GUIDE.md` section 10, then double-click `install\INSTALL.cmd`.
2. First login: double-click `install\create-admin.cmd` once, then the **Database Dashboard** Desktop shortcut.
3. Just want to look around on fake data? `SETUP-GUIDE.md` section 7 ("Demo mode").
4. Safety: never point tests or the demo at the real Sheets. The tests and the demo use fixture files only.

## Folder map
| Folder / file | What is inside |
|---|---|
| `SETUP-GUIDE.md` | 10-section roadmap for a non-expert; links to `GUIDE/` |
| `GUIDE/` | 00 start, 01 roadmap, 02 architecture, 03 how to change things, 04 troubleshooting, 05 accounts and keys (names only) |
| `install\` | `INSTALL.cmd` (double-click; `-Check` = dry run, `-Uninstall` = shortcuts only, `-WithPreview`, `-RunTests`), `install.ps1`, `start-dashboard.cmd`, `create-admin.cmd` |
| `app\dashboard\` | THE app (Flask + SQLite; `manage.py`, `dash\`, `tests\`). Own git |
| `app\web\` | Optional Vite design preview with mock data. Not the real app |
| `database\` | `README.md` (where the SQLite file is) + `RESTORE.md` |
| `backups\` | `backup.ps1` (`-DryRun`): dated folder zip + SQLite copy; outputs gitignored |
| `secrets\` | The ONE secrets folder (gitignored): `.env`, `service_account.json`, `sources.yaml`, demo logins + `SECRETS-CHECKLIST.md` (names only) |
| `docs\` | Copies of START_HERE, HANDOFF-GAPS (40 gaps + decisions), DESIGN-SPEC, MOTION |
| `notes\` | Copies of the original briefs (BRIEF, USER-REQUEST, UI-SPEC, REDTEAM, hand-overs) |
| `reference\`, `brand\`, `recon\`, `preview-proof\`, `lead-dashboard-preview\` | Original reference images, logo, preview proofs (untouched) |
| `proof\`, `archive\` | Test output / screenshots; old files (never deleted) |
| `CLAUDE.md`, `PROGRESS.md`, `PACKAGING-STATUS.md` | Project status; packaging status + next steps |
