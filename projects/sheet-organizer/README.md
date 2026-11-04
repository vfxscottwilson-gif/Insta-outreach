# sheet-organizer

A "senior manager" robot: files notes you paste into a Google Sheet `Inbox` tab (and optionally FigJam sticky notes) into Tasks, Problems & Solutions, Achievements, Ideas and Resources, flags overdue or forgotten items and writes a monthly report. Used by the agency owner. Runs daily in the cloud on GitHub Actions, or on this PC.

## Start here
1. New PC? Read `SETUP-GUIDE.md` section 10, then double-click `install\INSTALL.cmd`.
2. Just using it? See `SETUP-GUIDE.md` section 7.

## Folder map
| Folder / file | What is inside |
|---|---|
| `SETUP-GUIDE.md` | The 10-section guide for a non-expert |
| `GUIDE/` | Chapters 00 start, 01 roadmap, 02 architecture, 03 how to change, 04 troubleshooting, 05 accounts and keys |
| `install\` | `INSTALL.cmd` (double-click; `-Check` = dry run), `run.cmd` (runs the organizer with your keys loaded; test run by default) |
| `app\` | Source code (own git): `organizer.py`, `requirements.txt`, `.github\workflows\organize.yml`, `SETUP_GUIDE.md` (original detailed guide) |
| `database\` | No database (data lives in the Google Sheet); how to back it up |
| `secrets\` | `.env`, Google key; gitignored. `SECRETS-CHECKLIST.md` lists names |
| `notes\`, `docs\`, `proof\`, `reference\` | Notes, docs, test output, references |
| `backups\` | `backup.ps1` makes a dated zip of this folder |
| `archive\` | `sheet-organizer.zip` old snapshot; never use as current |
