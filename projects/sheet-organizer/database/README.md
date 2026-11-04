# Database

No database. All data (Inbox, Tasks & Progress, Problems & Solutions, Achievements, Ideas & Notes, Resources & Links, Review Needed, Attention Needed, Monthly Summary, `_Ledger`, `_Log`) lives in your Google Sheet (cloud, in your Google account).

Backup: Google Sheets > File > Download > Microsoft Excel (.xlsx), saved in this folder with the date in the name.
Restore: File > Import > Upload the .xlsx > "Create new spreadsheet", then use the new Sheet ID in `secrets\.env` and the GitHub secret `SHEET_ID`. Keep `_Ledger` (it remembers which notes were already filed).
