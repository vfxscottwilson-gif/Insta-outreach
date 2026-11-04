# outreach-bot (v3)

Writes personalised cold-email DRAFTS from your lead Google Sheets into one "Outreach" Google Sheet. It sends nothing: you copy and send by hand.

## Start here
1. New PC? Read `SETUP-GUIDE.md` section 10, then double-click `install\INSTALL.cmd`.
2. Just using it? See `SETUP-GUIDE.md` section 7. Daily runs happen in the cloud on GitHub Actions; this folder holds the source, a local test runner and the keys.

## Folder map
| Folder / file | What is inside |
|---|---|
| `SETUP-GUIDE.md` | The 10-section roadmap for a non-expert |
| `GUIDE\` | 00 start, 01 roadmap, 02 architecture, 03 how to change, 04 troubleshooting, 05 accounts and keys (names only) |
| `install\` | `INSTALL.cmd` calls `install.ps1` (`-Check`, `-Uninstall`); `run-bot.ps1` (local dry run / live / selftest); `env.example` |
| `app\` | Bot source with its own git (generate.py, selftest.py, tools\, .github\workflows, phase2_parked\) |
| `database\` | No database: data lives in Google Sheets (see its README) |
| `secrets\` | Gitignored: old `Draft Emails API Keys.txt` (copied unread), `.env` after install, `SECRETS-CHECKLIST.md` |
| `archive\` | Old zips (v2, v3, "fixed") and the superseded `outreach-bot-v2` folder |
| `backups\` | `backup.ps1` folder zip |
| `notes\`, `docs\`, `proof\`, `reference\` | Notes, copies of the setup docs, test output |
