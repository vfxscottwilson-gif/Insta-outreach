# Secrets checklist (names only, never values)

| Secret name | Used by | Where to get it | Done |
|---|---|---|---|
| GOOGLE_SA | generate.py (required) | console.cloud.google.com > IAM > Service accounts > Keys > Add key > JSON; enable Sheets API; save as `secrets\google-sa.json` | [ ] |
| OUTREACH_SHEET_ID | generate.py (required) | New blank Google Sheet, share with the service account as Editor; the ID is in the URL between /d/ and /edit | [ ] |
| SHEET_ID_<COUNTRY> (AU, AU_ONLY, US, CA, GB, IE, NZ, AE, SA, QA, YOUTUBE) | lead sheets (optional) | URL of each lead sheet, share as Viewer | [ ] |
| GEMINI_API_KEY_1..3 | AI (optional) | aistudio.google.com > API keys > Create key in a NEW project each | [ ] |
| GROQ_API_KEY | AI (optional) | console.groq.com/keys | [ ] |
| MISTRAL_API_KEY | AI (optional) | console.mistral.ai > API keys | [ ] |
| OPENROUTER_API_KEY | AI (optional) | openrouter.ai/keys | [ ] |

`Draft Emails API Keys.txt` = old keys file, copied unread; reported dead, replace them.
