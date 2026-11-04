# 05 Accounts and keys (names only; values live in `secrets/`)

| Service | Name | ID / account | Where used | Secret lives in |
|---|---|---|---|---|
| Google Cloud | Service account key | owner to fill (the `client_email` inside the JSON) | organizer.py | `secrets\*.json`, GitHub secret GOOGLE_SA |
| Google Sheets | Notes sheet | ID in SHEET_ID | organizer.py | `secrets\.env`, GitHub secret |
| AI providers | GEMINI_API_KEY, GROQ_API_KEY, OPENROUTER_API_KEY | owner's accounts | organizer.py | `secrets\.env`, GitHub secrets |
| Figma (optional) | FIGMA_TOKEN | owner's account | organizer.py | `secrets\.env`, GitHub secret |
| GitHub | private repo with `app\` | owner's account | daily run | GitHub Settings > Secrets |

## What is required
| Level | Names |
|---|---|
| Required (secrets) | SHEET_ID, GOOGLE_SA, and at least one of GEMINI_API_KEY, GROQ_API_KEY, OPENROUTER_API_KEY |
| Optional | FIGMA_TOKEN (secret); variables FIGMA_FILE, FIGMA_COMMENT, FIGMA_PAGE, FIGMA_NODE_TYPES, INBOX_TAB, TIMEZONE, RUN_LIMIT, MAX_RUN_MIN, DRY_RUN, GEMINI_MODEL, GROQ_MODEL, OPENROUTER_MODEL |

Several keys of one provider: put them in the same secret separated by commas.

## Where each comes from
1. GOOGLE_SA: console.cloud.google.com > project > enable Google Sheets API > IAM and Admin > Service accounts > Keys > Add key > JSON. Paste the WHOLE file content as the secret. Share the Sheet (Editor) with the client_email inside it.
2. SHEET_ID: the part of the Sheet URL between /d/ and /edit.
3. AI keys: aistudio.google.com (Gemini), console.groq.com/keys (Groq), openrouter.ai/keys (OpenRouter). All have free tiers.
4. FIGMA_TOKEN: Figma > Settings > Security > Personal access tokens, scope file_content:read (add file_comments:write for comments).

## Where the values go
- This PC: secrets\.env plus the Google .json file in secrets\ (install\run.cmd loads them).
- Daily cloud run: GitHub > private repo > Settings > Secrets and variables > Actions.
