# Secrets checklist (sheet-organizer)

Names only. NEVER write values here. Local values live in `secrets\.env` and the key file in this folder (gitignored); the daily cloud run uses GitHub secrets.

| Secret name | Used by | Where to get it | Done |
|---|---|---|---|
| SHEET_ID | organizer.py (GitHub secret) | The text between `/d/` and `/edit` in the Sheet URL | [ ] |
| GOOGLE_SA | organizer.py (GitHub secret = whole JSON text; on this PC `run.cmd` reads the `.json` file in this folder) | 1. console.cloud.google.com, new project. 2. Enable Google Sheets API. 3. IAM > Service Accounts > create. 4. Keys > Add key > JSON, save the file in `secrets\`. 5. Share your Sheet (Editor) with the account's `client_email`. | [ ] |
| GEMINI_API_KEY | organizer.py (optional, add at least one AI key) | aistudio.google.com/apikey | [ ] |
| GROQ_API_KEY | organizer.py (optional) | console.groq.com/keys | [ ] |
| OPENROUTER_API_KEY | organizer.py (optional) | openrouter.ai/keys | [ ] |
| FIGMA_TOKEN | organizer.py (optional) | Figma > Settings > Personal access tokens, scope file_content:read | [ ] |
| Optional settings (not secret) | organizer.py | FIGMA_FILE, FIGMA_COMMENT, FIGMA_PAGE, FIGMA_NODE_TYPES, INBOX_TAB, TIMEZONE, RUN_LIMIT, DRY_RUN | [ ] |
