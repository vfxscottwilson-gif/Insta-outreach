# Email Automation: packaging progress
Build progress of the app itself: `app\PROGRESS.md` (snapshot: `notes\app-PROGRESS-snapshot.md`).

| Workstream | Session | Status | % | Last update | Blocker | Next step |
|---|---|---|---|---|---|---|
| Folder packaging (hub standard) | packaging chats | Done except items below | 90 | 2026-11-05 | none | Fill SETUP-GUIDE TODO sections when build ends |
| Installer | packaging | `-Check` runs | 90 | 2026-11-05 | real install on a clean PC not verified here | Test on a clean PC |
| Backup (`backups\backup.ps1`) | packaging | `-DryRun` runs; real DB export needs `pg_dump` | 80 | 2026-11-05 | pg_dump not installed | `winget install PostgreSQL.PostgreSQL.17`, run once |
| Database docs | audit chat | `database\RESTORE.md` added | 100 | 2026-11-05 | none | none |
