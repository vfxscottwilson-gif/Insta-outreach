# 05 Accounts and keys (names only; values live in `secrets/`)

| Service | Name | ID / account | Where used | Secret lives in |
|---|---|---|---|---|
| Google Cloud | Service account key | owner to fill (the `client_email` inside the JSON) | main.py, send_assist.py | `secrets\*.json`, GitHub secret GOOGLE_SERVICE_ACCOUNT_JSON |
| Google Sheets | Leads sheet | ID in SHEET_ID | all | `secrets\.env`, GitHub variable |
| AI providers | AI_API_KEYS | Gemini, Groq, OpenRouter, others | ai.py | `secrets\.env`, GitHub secret |
| Meta (optional) | IG_ACCESS_TOKEN, IG_USER_ID | Instagram Professional + Facebook Page | ig.py | `secrets\.env`, GitHub secret |
| GitHub | private repo with `app\` | owner's account | daily run | GitHub Settings > Secrets |
| Instagram | the sending accounts | listed in the Sheet's Accounts tab | send_assist.py | Chrome profiles (not stored here) |

## What is required
| Level | Names |
|---|---|
| Required (secrets) | GOOGLE_SERVICE_ACCOUNT_JSON, AI_API_KEYS |
| Required (variables) | SHEET_ID, OFFER (full runs), AGENT_ACCOUNTS on the first run (later the Accounts tab) |
| Optional | IG_ACCESS_TOKEN, IG_USER_ID, AGENCY_NAME, SENDER_NAME, FREE_SAMPLE, CASE_STUDIES, DAILY_LIMIT_PER_ACCOUNT, SEND_WINDOW, MSG_GAP_MINUTES, FOLLOWUP_GAPS, TIMEZONE, DATE_FORMAT, LEADS_TAB, GRAPH_VERSION |
| Local helper only | PROFILES_FILE (path to profiles.json), CHROME_PATH |

## Where each comes from
1. GOOGLE_SERVICE_ACCOUNT_JSON: console.cloud.google.com > project > enable Google Sheets API > Service accounts > Keys > Add key > JSON. Share the Sheet (Editor) with the client_email inside it. Locally the setting may be the path to the file; on GitHub it is the whole JSON text.
2. AI_API_KEYS: one key per line. Gemini aistudio.google.com/apikey, Groq console.groq.com/keys, OpenRouter openrouter.ai/keys, plus Mistral, OpenAI or Anthropic if you have them. Use at least 2 providers.
3. SHEET_ID: the part of the Sheet URL between /d/ and /edit.
4. IG_ACCESS_TOKEN and IG_USER_ID: Meta developer app, Instagram Professional account linked to a Facebook Page. Optional.

## Where the values go
- This PC: secrets\.env plus the Google .json file in secrets\ (install\run.cmd loads them).
- Daily cloud run: GitHub > private repo > Settings > Secrets and variables > Actions (Secrets: GOOGLE_SERVICE_ACCOUNT_JSON, AI_API_KEYS, IG_ACCESS_TOKEN. Variables: everything else).
- Instagram account passwords are never stored here; sending uses your own Chrome profiles.
