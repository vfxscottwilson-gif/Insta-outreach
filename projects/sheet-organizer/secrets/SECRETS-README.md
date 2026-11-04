# secrets/ : SECRETS. Do not share, upload or commit.

This folder is gitignored. Files (names only):
- `.env` : NAME=value lines (SHEET_ID, GEMINI_API_KEY, GROQ_API_KEY, OPENROUTER_API_KEY, FIGMA_TOKEN, FIGMA_FILE, DRY_RUN). Created by the installer.
- `*.json` : Google service-account key (read into GOOGLE_SA by `installun.cmd`).
Rules: keep off cloud drives and chat; if a key leaks, rotate it at its service.
