# Database

Harvey uses ONE local SQLite file: `app\data\harvey.db` (created on first run; gitignored upstream). No cloud database.

- `secrets\harvey-db-snapshot-2026-11-05.db` = copy of the original database at packaging time (272 KB). Kept in secrets\ because it holds prospect data and is gitignored.
- Restore: close Harvey, then copy the snapshot over `app\data\harvey.db`:
```
copy secrets\harvey-db-snapshot-2026-11-05.db app\data\harvey.db
```
- Backup: `backups\backup.ps1` zips the whole folder (including the database).
