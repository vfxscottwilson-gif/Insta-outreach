# ig-outreach (Instagram Outreach v3)

Reads leads from a Google Sheet, writes short personalised Instagram DMs and schedules them across accounts with follow-ups. A human sends each DM (`send_assist.py` opens the chat and copies the text). Used by the agency owner. Runs daily in the cloud on GitHub Actions, or on this PC.

## Start here
1. New PC? Read `SETUP-GUIDE.md` section 10, then double-click `install\INSTALL.cmd`.
2. Just using it? See `SETUP-GUIDE.md` section 7.

## Folder map
| Folder / file | What is inside |
|---|---|
| `SETUP-GUIDE.md` | The 10-section guide for a non-expert |
| `GUIDE/` | Chapters 00 start, 01 roadmap, 02 architecture, 03 how to change, 04 troubleshooting, 05 accounts and keys |
| `install\` | `INSTALL.cmd` (double-click; `-Check` = dry run), `run.cmd` (runs a script with your keys loaded) |
| `app\` | Source code (own git): `main.py`, `ai.py`, `ig.py`, `rules.py`, `styles.py`, `send_assist.py`, `apps_script.gs`, `.github\workflows\outreach.yml` |
| `database\` | No database (data lives in the Google Sheet); how to back it up |
| `secrets\` | `.env`, Google key, API notes file; gitignored. `SECRETS-CHECKLIST.md` lists names |
| `notes\` | Hand-over notes |
| `backups\` | `backup.ps1` makes a dated zip of this folder |
| `docs\`, `proof\`, `reference\` | Docs, test output, read-only references |
| `archive\` | Old zips (`ig-outreach.zip` older, `ig-outreach-v3.zip`); never use as current |
