# 04 Troubleshooting
Full table: `app\SETUP_GUIDE.md` Part 7. Most common:
| Problem | Fix |
|---|---|
| Run is red: `[FATAL] Missing required env var(s): X` | Add secret X exactly as spelled (GitHub > Settings > Secrets and variables > Actions) |
| `Upwork API keys not set; skipping` | Normal until you add the three UPWORK_* secrets |
| `AI_Source = template` on every row | No AI key works; check GEMINI_API_KEYS / GROQ_API_KEYS. Leads are still written |
| Nothing is written to the Sheet | Share the Sheet with the service account `client_email` as Editor; check SHEET_ID |
| YouTube quota used up | Normal; quota resets 00:00 Pacific, later runs continue. Add more API keys (comma-separated) |
| Upwork: Run Log says `token refresh failed` | Run `app\tools\upwork_auth.py` again and update UPWORK_REFRESH_TOKEN |
| DuckDuckGo source returns HTTP 202 | Expected (blocked); skipped automatically |
| INSTALL.cmd: Python not on PATH yet | Close the window, run INSTALL.cmd again |
| Schedule stopped after 2 months | GitHub pauses idle repos; the workflow has a keepalive step. Re-enable under the Actions tab |
