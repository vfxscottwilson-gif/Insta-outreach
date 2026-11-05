# Restore the database

Everything here is local. The lead data itself can always be rebuilt from the Google Sheets (run a sync); what a restore protects is users, assignments, approvals, audit history and tombstones, which exist only in the SQLite file.

## A. Restore from a backup\ copy (`dash-<date>.db`)
1. Close the dashboard (close the black server window).
2. Keep the current file just in case: rename `app\dashboard\data\dash.db` to `dash.db.old` (if it exists).
3. Copy your backup to `app\dashboard\data\` and rename it to `dash.db`.
4. Make sure `secrets\.env` / `app\dashboard\.env` are the ones used when the backup was made (same `DASH_PASSWORD_KEY`), otherwise employee password copies cannot be revealed (logins still work).
5. Start the dashboard. Expected: you can sign in as before.

## B. Restore from the folder zip (`database-folder-<date>.zip`)
1. Unzip it to a new folder, e.g. `F:\Github Repos\projects\database`.
2. Double-click `install\INSTALL.cmd` (rebuilds the `.venv`, restores keys from `secrets\`).
3. The database file is inside the zip at `app\dashboard\data\dash.db` only if you ran backup.ps1 after the app had a live DB.

## C. New PC, no backup
Run INSTALL.cmd, run `install\create-admin.cmd`, add the sheets again (Sources & sync) and sync. Employees must be re-added.
