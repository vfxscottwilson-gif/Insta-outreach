# Database

No database. All data (leads, Outreach Log, Today Queue, Accounts, Run Log) lives in your Google Sheet (cloud, in your Google account).

Backup: open the Sheet > File > Download > Microsoft Excel (.xlsx) and save it in this folder with the date in the name.
Restore: Google Sheets > File > Import > Upload the .xlsx > "Create new spreadsheet". Put the new Sheet ID in `secrets\.env` and in the GitHub variable `SHEET_ID`. Keep tab names and headers as they are (the bot matches columns by header name).
