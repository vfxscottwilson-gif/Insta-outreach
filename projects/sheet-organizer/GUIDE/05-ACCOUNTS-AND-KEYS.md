# 05 Accounts and keys (names only; values live in `secrets/`)

| Service | Name | ID / account | Where used | Secret lives in |
|---|---|---|---|---|
| Google Cloud | Service account key | owner to fill (the `client_email` inside the JSON) | organizer.py | `secrets\*.json`, GitHub secret GOOGLE_SA |
| Google Sheets | Notes sheet | ID in SHEET_ID | organizer.py | `secrets\.env`, GitHub secret |
| AI providers | GEMINI_API_KEY, GROQ_API_KEY, OPENROUTER_API_KEY | owner's accounts | organizer.py | `secrets\.env`, GitHub secrets |
| Figma (optional) | FIGMA_TOKEN | owner's account | organizer.py | `secrets\.env`, GitHub secret |
| GitHub | private repo with `app\` | owner's account | daily run | GitHub Settings > Secrets |
