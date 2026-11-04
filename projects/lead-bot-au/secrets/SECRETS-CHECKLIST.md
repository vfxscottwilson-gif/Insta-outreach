    # Secrets checklist: Lead Bot AU
    Names only. NEVER write values here. Real values live in `secrets\.env` (this PC) and in **GitHub > your repo > Settings > Secrets and variables > Actions** (the daily run).
    Full detail per key (format, free limit): `app\SECRETS_GUIDE.md`.

    ## A. Required
    | Secret name | What it is | Needed? | Done |
    |---|---|---|---|
    | GOOGLE_SA | Google service-account key (robot login for Sheets). Local: path to the .json in secrets\ (installer sets it). GitHub: paste the whole JSON text | Yes | [ ] |
    | SHEET_ID_AU_ONLY | Leads - Australia (one sheet, with ABN columns) | Yes | [ ] |

    ## B. Optional keys (missing = skipped, the bot never crashes)
    | Secret name | Used for | Where to get it | Cost | Done |
    |---|---|---|---|---|
    | GEMINI_API_KEY_1 / _2 / _3 | Optional AI for the Lead Insight text (without it: fact-only insights) | aistudio.google.com > Get API key | free tier | [ ] |
| GROQ_API_KEY | Optional AI fallback | console.groq.com > API Keys | free tier | [ ] |
| CEREBRAS_API_KEY | Optional AI fallback | cloud.cerebras.ai > API Keys | free tier | [ ] |
| OPENROUTER_API_KEY | Optional AI fallback | openrouter.ai > Keys | free models | [ ] |
| MISTRAL_API_KEY | Optional AI fallback | console.mistral.ai > API keys | free tier | [ ] |
| SERPER_API_KEY | Optional: Google search results (more leads / decision makers) | serper.dev > API key | free credits | [ ] |
| HUNTER_API_KEY | Optional: email finder | hunter.io > API | free tier | [ ] |
| GOOGLE_PLACES_API_KEY | Optional: Google Places (needs billing on the Google project) | Google Cloud Console > APIs > Places API > Credentials | paid | [ ] |
| YOUTUBE_API_KEY_1 / _2 | Optional: YouTube Data API (bot also works without) | Google Cloud Console > YouTube Data API v3 > Credentials | free quota | [ ] |
| APIFY_API_TOKEN | Optional: scraper actors | console.apify.com > Settings > Integrations | free credit | [ ] |
| BRAVE_API_KEY | Optional: Brave search | brave.com/search/api | free tier | [ ] |
| ABN_GUID | Optional: Australian ABN Lookup (old name ABN_LOOKUP_GUID also works) | abr.business.gov.au > Web services > register for a GUID | free | [ ] |
| ZENROWS_API_KEY, JINA_API_KEY, APOLLO_API_KEY, PROSPEO_API_KEY, SNOV_CLIENT_ID, SNOV_CLIENT_SECRET, NZBN_API_KEY, ZEROBOUNCE_API_KEY, REACHER_URL, REACHER_SECRET | Optional helpers (website reading, email finding/verifying); a missing key is skipped | app\SECRETS_GUIDE.md (one section per key) | mixed | [ ] |

    ## C. GitHub "Variables" (Settings > Secrets and variables > Actions > Variables tab)
    | Name | Meaning |
    |---|---|
    | KEY_CHECK | turn on the key check report |
    | LEAD_MATRIX | which jobs run |
    | TIMEZONE | e.g. Australia/Sydney |
    | USE_JINA, IG_USER_ID | optional |
    The workflow also reads these optional secrets: IG_ACCESS_TOKEN, AI_API_KEYS, PLACES_API_KEYS, YOUTUBE_API_KEYS (comma lists), SHEET_ID (old fallback).

    ## D. Files kept in this folder
    - `outreach-512901-101a0b58215d.json` : a Google service-account key file (copied from `Lead generation\All Needed Files\Json FIle`). Its contents were NOT opened. Check in Google Cloud which project/robot it belongs to before relying on it.
    - `AUS Lead Gen all info.txt` : notes file with keys/ids (copied unread; keep private).
