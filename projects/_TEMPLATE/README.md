# <App name>

One line: what this app does and who uses it.

## Start here
1. New PC? Read `SETUP-GUIDE.md` section 10, then double-click `install\INSTALL.cmd`.
2. Just using it? See `SETUP-GUIDE.md` section 7.

## Folder map
| Folder / file | What is inside |
|---|---|
| `SETUP-GUIDE.md` | The 10-section roadmap for a non-expert; links to the chapters in `GUIDE/` |
| `GUIDE/` | Detailed chapters: 00 start, 01 roadmap, 02 architecture, 03 how to change, 04 troubleshooting, 05 accounts and keys (names/IDs only) |
| `install\` | `INSTALL.cmd` (double-click) calls `install.ps1` (`-Check` = dry run). `install.example-node-python.ps1` = a full working example (winget prerequisites, npm/uv, build, .env, shortcut, checklist, `-Uninstall`): copy its ideas |
| `app\` | Source code (own git) |
| `database\` | Database notes, `backups\` JSON exports, restore steps |
| `secrets\` | The ONE secrets folder, gitignored: `.env`, key files, account lists + `SECRETS-CHECKLIST.md` (names only) |
| `notes\` | Briefs and copies of every session/hand-over note |
| `reference\` | Read-only snapshots of related code that lives elsewhere |
| `backups\` | `backup.ps1`: dated folder zip + database export (outputs gitignored) |
| `docs\` | Roadmap, brief, features, audit, prices |
| `proof\` | Screenshots and test output |
| `archive\` | Old or unused files (never deleted) |
