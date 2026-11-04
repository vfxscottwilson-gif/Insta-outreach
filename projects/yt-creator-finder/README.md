# YT Creator Finder

Finds YouTube channel owners who are hiring (or likely to need) a video editor or thumbnail designer, scores them, adds an AI pitch angle and appends them to a Google Sheet. Sources: Upwork (official API), Freelancer.com, LinkedIn Jobs, Remotive, YTJobs, YouTube search. It runs free and automatically on GitHub Actions.

## Start here
1. New PC or first time? Read `SETUP-GUIDE.md` section 5, then double-click `install\INSTALL.cmd`.
2. Going live (cloud schedule)? `SETUP-GUIDE.md` sections 5-7.
3. Just checking results? Open your Google Sheet.

## Folder map
| Folder / file | What is inside |
|---|---|
| `SETUP-GUIDE.md` | The 10-section roadmap for a non-expert; links to `GUIDE/` |
| `GUIDE/` | 00 start, 01 roadmap, 02 architecture, 03 how to change, 04 troubleshooting, 05 accounts and keys (names only) |
| `install\` | `INSTALL.cmd` runs `install.ps1` (`-Check` = dry run, `-Uninstall` = shortcut only). Sets up a local test copy |
| `app\` | The bot (original git history). Runs in GitHub Actions: `app\.github\workflows\run-lead-bot.yml`. Its own long guide: `app\SETUP_GUIDE.md` |
| `database\` | "No database, it is a Google Sheet" + backup/restore |
| `secrets\` | `.env` (gitignored) + `SECRETS-CHECKLIST.md` (names only) |
| `docs\` | Master prompt, sample leads CSV (2026-11-01) |
| `archive\` | Old zip snapshots (never edit) |
| `backups\` | `backup.ps1` (folder zip) |
| `reference\` | Notes from the old D:\ folder |
| `notes\`, `proof\` | Hand-over notes, test output |
