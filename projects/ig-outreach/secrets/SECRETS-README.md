# secrets/ : SECRETS. Do not share, upload or commit.

This folder is gitignored. Files (names only):
- `.env` : NAME=value lines (SHEET_ID, AI_API_KEYS, OFFER, IG_ACCESS_TOKEN, IG_USER_ID). Created by the installer.
- `*.json` : Google service-account key (GOOGLE_SERVICE_ACCOUNT_JSON). `installun.cmd` points the app at it.
- `profiles.json` (optional) : Chrome profile map for send_assist.py (copy of app\profiles.example.json).
- the old Notes file from the Insta Automation folder (may hold API details).
Rules: keep off cloud drives and chat; if a key leaks, rotate it at its service.
