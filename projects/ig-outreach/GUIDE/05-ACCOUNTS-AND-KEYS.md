# 05 Accounts and keys (names only; values live in `secrets/`)

| Service | Name | ID / account | Where used | Secret lives in |
|---|---|---|---|---|
| Google Cloud | Service account key | owner to fill (the `client_email` inside the JSON) | main.py, send_assist.py | `secrets\*.json`, GitHub secret GOOGLE_SERVICE_ACCOUNT_JSON |
| Google Sheets | Leads sheet | ID in SHEET_ID | all | `secrets\.env`, GitHub variable |
| AI providers | AI_API_KEYS | Gemini, Groq, OpenRouter, others | ai.py | `secrets\.env`, GitHub secret |
| Meta (optional) | IG_ACCESS_TOKEN, IG_USER_ID | Instagram Professional + Facebook Page | ig.py | `secrets\.env`, GitHub secret |
| GitHub | private repo with `app\` | owner's account | daily run | GitHub Settings > Secrets |
| Instagram | the sending accounts | listed in the Sheet's Accounts tab | send_assist.py | Chrome profiles (not stored here) |
