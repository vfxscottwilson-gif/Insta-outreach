# 05 Accounts and keys (names only, never values)

Full table with steps: `secrets\SECRETS-CHECKLIST.md`. Click-by-click: `app\SETUP_GUIDE.md` Parts 2 to 4. Template of all names: `app\.env.example`.

Where values live: `secrets\.env` on your PC (gitignored; the installer asks for them with hidden typing and copies the file to `app\.env`) and GitHub repo > Settings > Secrets and variables > Actions > Secrets (for the scheduled run). The same NAME is used in both places. Never paste a value into a guide, chat or commit.

## Secrets
| Name | Required | What it is | Where to get it | Used by (code) |
|---|---|---|---|---|
| GOOGLE_SA | yes for live runs (not for dry run) | Service-account key: the whole JSON, or its base64 | Google Cloud > IAM > Service accounts > Keys > Add key > JSON. Then share the Sheet with its `client_email` as Editor | `config.service_account()`, `sheets_manager.py` |
| SHEET_ID | yes for live runs | The long id in the Sheet URL between `/d/` and `/edit` | The Sheet's address bar | `sheets_manager.py` |
| YOUTUBE_API_KEYS | yes, always | One or more YouTube Data API v3 keys, comma-separated | Google Cloud > APIs & Services > Credentials > API key; enable "YouTube Data API v3" | `enrichment\youtube.py` |
| GEMINI_API_KEYS | no | AI pitch (first choice) | aistudio.google.com > Get API key | `ai_insight.py` |
| GROQ_API_KEYS | no | AI pitch (second choice) | console.groq.com > API Keys | `ai_insight.py` |
| JINA_API_KEY | no | Faster website/YTJobs reading | jina.ai | `net.py` (Jina) |
| UPWORK_CLIENT_ID | no | Upwork API key | upwork.com/developer/keys/apply (needs approval) | `sources\upwork.py` |
| UPWORK_CLIENT_SECRET | no | Upwork API secret | same page | `sources\upwork.py` |
| UPWORK_REFRESH_TOKEN | no | Login token for the Upwork API | run `app\tools\upwork_auth.py` after approval | `sources\upwork.py` |
| AI_API_KEYS | no | Extra AI keys; the code reads it but `.env.example`, the workflow and the installer do not list it | not needed | `config.py` (not verified how it is used) |

Missing optional keys switch that feature off; they never crash the run.

## Variables (GitHub > Settings > Secrets and variables > Actions > Variables tab; not secrets)
DAILY_LEAD_TARGET, MIN_SUBS, MAX_DAYS_SINCE_UPLOAD, YT_SEARCH_BUDGET. These four are passed to the run by the workflow. Other names in `.env.example` comments (GEMINI_MODELS, GROQ_MODELS, DRY_RUN) work on your PC; on GitHub only the four above plus `dry_run` (a run input) are wired in the workflow file.

## Accounts
| Account | Why | Cost |
|---|---|---|
| Google (Cloud project + Sheets) | YouTube key, service account, the Sheet | free |
| GitHub | Runs the schedule, stores secrets | free |
| Google AI Studio, Groq, Jina | Optional AI and reading | free tiers |
| Upwork developer | Optional Upwork jobs | free, approval needed |

No account needed: Freelancer.com, LinkedIn Jobs (public listings), Remotive, YTJobs, DuckDuckGo. Prices and quotas of these services were not re-checked in this step; the free-tier claims come from the app's own guide (not verified today).

## Rotating or losing a key
1. Make a new key at the provider.
2. Replace the line in `secrets\.env` and the GitHub secret with the same NAME.
3. Run `install\INSTALL.cmd` again (it copies `secrets\.env` to `app\.env`).
4. Delete the old key at the provider.

## Checklist
- [ ] YOUTUBE_API_KEYS in `secrets\.env` (enough for a dry run)
- [ ] GOOGLE_SA and SHEET_ID in `secrets\.env`, Sheet shared with the service account
- [ ] The same three as GitHub secrets (before the first cloud run)
- [ ] Optional keys added when you want AI pitches or Upwork
