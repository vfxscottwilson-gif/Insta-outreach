# Database
No database. The data lives in Google Sheet(s) in your Google account (see `Guide\Accounts And Keys.md`). Sheets are append-only. To back one up: Google Sheets > File > Make a copy (or File > Download > Excel).
The bot's own state (the "Seen" tab and the Rules tab) is inside the sheet, so a new run with the same sheet continues where the last one stopped.
