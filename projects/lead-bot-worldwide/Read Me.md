# Lead Bot Worldwide
Finds local businesses in the US, Canada, UK, Australia, New Zealand and Ireland (optional UAE, Saudi Arabia, Qatar) that can pay $500-1,000+ per month, plus YouTube creators. It writes facts-only contact data, a Segment, an ICP score and a short Lead Insight into one Google Sheet per country. It never writes emails (the outreach bot does).

**Runs:** automatically twice a day on GitHub Actions (20:00 and 08:00 UTC (`0 20 * * *`, `0 8 * * *`)), writing to Google Sheets. It can also run on this PC for tests (no Google needed).

## Quick start
1. Double-click `install\INSTALL.cmd` (installs Python packages, makes `secrets\.env`, adds a Desktop shortcut, runs a self-test).
2. Make sure the Google robot key (.json) is in `secrets\` (already there if you copied the whole folder).
3. Follow `Setup Guide.md` to connect GitHub + Google Sheets (needed only for the daily automatic run).
4. Try it locally: double-click the Desktop shortcut "Lead Bot Worldwide (local test)". Press Ctrl+C to stop.

## Folder map
| Folder / file | What |
|---|---|
| `Setup Guide.md` | Step-by-step guide (read this) |
| `Guide\` | Detailed chapters 00-05 |
| `install\` | `INSTALL.cmd`, `install.ps1` (-Check / -DryRun / -Uninstall), `run-local.ps1` |
| `app\` | The code (own git repo) incl. `.github\workflows` |
| `docs\` | CONTRACT.md (sheet interface for the outreach bot), Free Tools Research.md, High Quality Leads Spec.md |
| `secrets\` | `.env`, Google key, checklist (gitignored) |
| `archive\` | Old versions and zips (never edit) |
| `backups\` | `backup.ps1` |
| `database\`, `notes\`, `proof\`, `reference\` | small READMEs |
