# 05 Accounts and keys (names only)
Full table with steps: `secrets\SECRETS-CHECKLIST.md`. Click-by-click: `app\SETUP_GUIDE.md` Part 4.

| Name | Required | From | Put it in |
|---|---|---|---|
| GOOGLE_SA | yes | Google Cloud service account JSON key | secrets\.env + GitHub secret |
| SHEET_ID | yes | Google Sheet URL | both |
| YOUTUBE_API_KEYS | yes | Google Cloud API key (YouTube Data API v3) | both |
| GEMINI_API_KEYS | no | aistudio.google.com | both |
| GROQ_API_KEYS | no | console.groq.com | both |
| JINA_API_KEY | no | jina.ai | both |
| UPWORK_CLIENT_ID / UPWORK_CLIENT_SECRET / UPWORK_REFRESH_TOKEN | no | Upwork developer key + `app\tools\upwork_auth.py` | both |

Accounts: Google (Cloud, Sheets), GitHub. Optional: Gemini, Groq, Jina, Upwork developer. Freelancer.com, LinkedIn Jobs, Remotive and YTJobs need none.
Variables (GitHub Variables tab, not secrets): DAILY_LEAD_TARGET, MIN_SUBS, MAX_DAYS_SINCE_UPLOAD, YT_SEARCH_BUDGET.
