# Secrets checklist (names only; never write values here)

Real values go in `secrets\.env` (the installer creates it and copies it to `app\.env`).

| Secret name | Used by | Where to get it | Done |
|---|---|---|---|
| GOOGLE_SERVICE_ACCOUNT_FILE (a file path, not a key) | Google Sheet mode (read leads, write Ready to Send) | 1. console.cloud.google.com, make or choose a project. 2. Enable **Google Sheets API** (and Drive API). 3. IAM & Admin > Service Accounts > Create. 4. Keys > Add key > JSON; save the file into `secrets\`. 5. Share your Google Sheet with the service account's e-mail (Editor). | [ ] |
| YOUTUBE_API_KEY (optional) | YouTube facts (channel info) | 1. Same Google Cloud project. 2. Enable **YouTube Data API v3**. 3. Credentials > Create credentials > API key. Free quota. Blank = skip YouTube facts. | [ ] |
| AI_API_KEY (optional) | Only for OpenAI-compatible servers that need a key (Ollama and LM Studio do not) | That server's settings. Leave blank for Ollama. | [ ] |
