# <APP NAME>

<One sentence: what it is and who uses it.> **This folder is the whole app: copy it to a new PC and run the installer.**

## Quick start (new PC)
1. Copy this whole folder to the new PC.
2. Double-click `install\Install.cmd` (`-DryRun` first for a preview).
3. If Notepad opens a `.env`: paste each key after `=`, save, run `Install.cmd` again.
4. Read the checklist at the end.
5. Open the app: <how>.
6. Problems: `GUIDE\04-TROUBLESHOOTING.md`. Backup: `backups\backup.ps1`.

## Where everything is
| Folder / file | What |
|---|---|
| `app/` | Source code + its git repo (gitignored by the hub repo) |
| `GUIDE/` | 00 start, 01 roadmap, 02 architecture, 03 how to change, 04 troubleshooting, 05 accounts and keys |
| `notes/` | Brief + every session note |
| `private/` | Secrets (gitignored): `.env`, key files, `SECRETS-README.md` |
| `install/` | `Install.cmd` + `install.ps1` |
| `backups/` | `backup.ps1` |
| `reference/` | Snapshots of related code that lives elsewhere |
