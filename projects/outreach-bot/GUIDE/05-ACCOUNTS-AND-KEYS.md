# 05 Accounts and keys (names only; values live in `secrets/` and GitHub secrets)

| Service | Name | Where used | Secret lives in |
|---|---|---|---|
| Google | GOOGLE_SA (whole service-account JSON) | generate.py | `secrets\google-sa.json`; GitHub secret |
| Google Sheets | OUTREACH_SHEET_ID | generate.py | `secrets\.env`; GitHub secret |
| Google Sheets | SHEET_ID_AU, _AU_ONLY, _US, _CA, _GB (or _UK), _IE, _NZ, _AE, _SA, _QA, _YOUTUBE, EXTRA_LEAD_SHEET_IDS | lead sheets (optional) | same |
| Google AI Studio | GEMINI_API_KEY_1..5 | AI drafts | same |
| Groq | GROQ_API_KEY, GROQ_API_KEY_2 | AI drafts | same |
| Mistral | MISTRAL_API_KEY | AI drafts | same |
| OpenRouter | OPENROUTER_API_KEY | AI drafts | same |
| Legacy names | SHEET_ID, LEADS_SHEET_ID, GEMINI_KEY(S), GROQ_KEY, OPENROUTER_KEY, AI_KEYS | still read as fallback | same |
| Variables | RUN_LIMIT, DRY_RUN, DAILY_TARGET, TEMPLATE_FALLBACK, *_MODELS, MAX_RUN_MIN | overrides | GitHub variables / Options tab |

Full table with formats and limits: `app\SECRETS_GUIDE.md`.

## What is required
| Level | Names |
|---|---|
| Required | GOOGLE_SA, OUTREACH_SHEET_ID, and at least one AI key (or set option TEMPLATE_FALLBACK to On) |
| Optional | every SHEET_ID_<COUNTRY> (a missing one is skipped), EXTRA_LEAD_SHEET_IDS, the other AI keys |

## Where each comes from (links are the provider sites, no values here)
1. GOOGLE_SA: console.cloud.google.com > create a project > enable the Google Sheets API > IAM and Admin > Service accounts > create > Keys > Add key > JSON. Share the Outreach sheet (Editor) and each lead sheet (Viewer) with the client_email inside the JSON.
2. OUTREACH_SHEET_ID: the part of the Outreach sheet URL between /d/ and /edit (the full URL also works). Must be a NEW sheet, not a lead sheet.
3. Gemini: aistudio.google.com > API keys > create the key in a NEW project each time (keys in one project share one quota).
4. Groq: console.groq.com/keys. Mistral: console.mistral.ai. OpenRouter: openrouter.ai/keys.

## Where the values go
- This PC: secrets\.env (names above, one NAME=value per line) and secrets\google-sa.json. Both are gitignored.
- Daily cloud run: GitHub > repo > Settings > Secrets and variables > Actions. Secrets tab for keys and sheet IDs, Variables tab for settings (RUN_LIMIT, DAILY_TARGET and so on).
- secrets\Draft Emails API Keys.txt is the old keys file, copied unread. Its keys were dead (401) on 2026-10-31; do not reuse them.

Key check: GitHub > Actions > diagnose-keys > Run workflow. It prints status per key with only the last 4 characters.
