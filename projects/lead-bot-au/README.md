# Lead Bot AU
The Australia-only twin of the worldwide bot: finds AU businesses that can pay $500-1,000+ per month (AUD) and AU YouTube creators, with 8 extra AU columns (ABN, entity, GST ...). One Google Sheet. It never writes emails.

**Runs:** automatically twice a day on GitHub Actions (19:00 and 07:00 UTC (`0 19 * * *`, `0 7 * * *`, about 6am/6pm Sydney)), writing to Google Sheets. It can also run on this PC for tests (no Google needed).

## Quick start
1. Double-click `install\INSTALL.cmd` (installs Python packages, makes `secrets\.env`, adds a Desktop shortcut, runs a self-test).
2. Make sure the Google robot key (.json) is in `secrets\` (already there if you copied the whole folder).
3. Follow `SETUP-GUIDE.md` to connect GitHub + Google Sheets (needed only for the daily automatic run).
4. Try it locally: double-click the Desktop shortcut "Lead Bot AU (local test)". Press Ctrl+C to stop.

## Folder map
| Folder / file | What |
|---|---|
| `SETUP-GUIDE.md` | Step-by-step guide (read this) |
| `GUIDE\` | Detailed chapters 00-05 |
| `install\` | `INSTALL.cmd`, `install.ps1` (-Check / -DryRun / -Uninstall), `run-local.ps1` |
| `app\` | The code (own git repo) incl. `.github\workflows` |
| `docs\` | CONTRACT.md (sheet interface for the outreach bot), FREE_TOOLS_RESEARCH.md, HIGH_QUALITY_LEADS_SPEC.md |
| `secrets\` | `.env`, Google key, checklist (gitignored) |
| `archive\` | Old versions and zips (never edit) |
| `backups\` | `backup.ps1` |
| `database\`, `notes\`, `proof\`, `reference\` | small READMEs |
