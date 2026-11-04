# Harvey (autonomous AI sales agent)

Third-party open-source tool (github.com/ethanplusai/harvey) that finds businesses, writes cold emails with Claude, sends them from your mailbox, handles replies and shows everything in a local dashboard. It runs fully on this PC (Python + a local SQLite file); the only cloud parts are your Claude subscription and your email provider.

## Start here
1. New PC? Read `SETUP-GUIDE.md` section 10, then double-click `install\INSTALL.cmd`.
2. Just using it? See `SETUP-GUIDE.md` section 7.

## Folder map
| Folder / file | What is inside |
|---|---|
| `SETUP-GUIDE.md` | The 10-section roadmap for a non-expert; links to the chapters in `GUIDE/` |
| `GUIDE/` | 00 start, 01 roadmap, 02 architecture, 03 how to change, 04 troubleshooting, 05 accounts and keys (names only) |
| `install\` | `INSTALL.cmd` (double-click) calls `install.ps1` (`-Check` = dry run, `-Uninstall` = remove shortcuts, `-NoPrompt`, `-WithBrowser`, `-RunTests`). Also `Start Harvey Dashboard.cmd` and `Run Harvey.cmd` |
| `app\` | Full upstream clone with its own `.git` (not edited). Has its own big README.md and CLAUDE.md |
| `database\` | Restore notes for the SQLite file (snapshot kept in `secrets\`) |
| `secrets\` | The ONE secrets folder, gitignored: `.env` + `SECRETS-CHECKLIST.md` (names only) |
| `docs\` | `UPSTREAM.md` (remote URL, commit hash), `FEATURES.md` |
| `notes\`, `reference\`, `archive\` | Notes, read-only snapshots, old files (empty for now) |
| `backups\` | `backup.ps1`: dated zip of the folder (outputs gitignored) |
| `proof\` | Install + test output |
