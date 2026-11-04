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
