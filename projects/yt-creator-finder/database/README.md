# Database

No database. The "database" is your Google Sheet (tabs for leads, a hidden `_State` tab for quota counters and the Upwork token, a Run Log). It lives in your Google account.

## Back up
1. Open the Sheet > File > Download > Microsoft Excel (.xlsx). Save it in this folder.
2. Or File > Make a copy.

## Restore / new Sheet
1. Create an empty Google Sheet (or copy the backup).
2. Share it with the service account `client_email` (from the GOOGLE_SA key) as Editor.
3. Put the new Sheet ID in `SHEET_ID` (secrets\.env and the GitHub secret). The bot creates missing tabs itself. Duplicate protection only knows leads present in the Sheet, so restoring an old copy avoids re-adding old leads.
