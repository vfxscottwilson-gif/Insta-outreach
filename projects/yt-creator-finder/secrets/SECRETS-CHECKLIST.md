# Secrets checklist (names only, never values)

Real values live in `secrets\.env` (this PC, gitignored; the installer asks for them with hidden input) AND in GitHub: repo > Settings > Secrets and variables > Actions > Secrets (for the scheduled run). The same NAME is used in both places. No `.env` or key file existed in the original folder, so `secrets\` starts empty.

| Secret name | Required? | Used by | Where to get it |
|---|---|---|---|
| GOOGLE_SA | yes | Sheets writer (service account) | Google Cloud > IAM > Service accounts > create > Keys > Add key > JSON. The whole JSON (or its base64) is the value. Share the Sheet with its `client_email` as Editor |
| SHEET_ID | yes | Sheets writer | The long ID in the Sheet URL between `/d/` and `/edit` |
| YOUTUBE_API_KEYS | yes | YouTube search + channel enrichment | Google Cloud > APIs & Services > Credentials > API key (enable YouTube Data API v3). Several keys: comma-separated |
| GEMINI_API_KEYS | optional | AI insight and pitch | aistudio.google.com > Get API key (comma-separated for rotation) |
| GROQ_API_KEYS | optional | AI fallback | console.groq.com > API Keys |
| JINA_API_KEY | optional | YTJobs reading (Jina Reader), higher limits | jina.ai free key; works without it, slower |
| UPWORK_CLIENT_ID | optional | Upwork source | upwork.com/developer/keys/apply (needs approval) |
| UPWORK_CLIENT_SECRET | optional | Upwork source | same page |
| UPWORK_REFRESH_TOKEN | optional | Upwork source | run `python tools\upwork_auth.py` in `app\` after approval |

GitHub Variables (not secrets, optional): DAILY_LEAD_TARGET, MIN_SUBS, MAX_DAYS_SINCE_UPLOAD, YT_SEARCH_BUDGET.
Sources with no key at all: Freelancer.com, LinkedIn Jobs (guest listings), Remotive, YTJobs (works without the Jina key).

| Done on this PC | Done on GitHub |
|---|---|
| [ ] secrets\.env filled (INSTALL.cmd asks) | [ ] repo created and code pushed, 3 required secrets added |
