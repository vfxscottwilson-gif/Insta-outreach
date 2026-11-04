# Secrets checklist (ig-outreach)

Names only. NEVER write values here. Real values live in `secrets\.env` and the key file in this folder (both gitignored), plus the GitHub secrets for the daily cloud run.

| Secret name | Used by | Where to get it | Done |
|---|---|---|---|
| GOOGLE_SERVICE_ACCOUNT_JSON | main.py, send_assist.py (GitHub secret = whole JSON text; on this PC `run.cmd` points it at the `.json` file in this folder) | 1. console.cloud.google.com, new project. 2. Enable Google Sheets API. 3. IAM > Service Accounts > create. 4. Keys > Add key > JSON, save the file in `secrets\`. 5. Share your Sheet (Editor) with the account's `client_email`. | [ ] |
| SHEET_ID | main.py, send_assist.py (GitHub variable) | The text between `/d/` and `/edit` in the Sheet URL | [ ] |
| AI_API_KEYS | ai.py (GitHub secret; comma or one per line; 2+ providers) | Gemini aistudio.google.com/apikey, Groq console.groq.com/keys, OpenRouter openrouter.ai/keys (Mistral, OpenAI, Anthropic also work) | [ ] |
| OFFER | main.py (required for a full run) | Your one-sentence offer | [ ] |
| IG_ACCESS_TOKEN | ig.py (optional) | Meta developer app with an Instagram Professional account + Facebook Page | [ ] |
| IG_USER_ID | ig.py (optional) | Same Meta app | [ ] |
| Optional settings (not secret) | main.py | AGENT_ACCOUNTS, AGENCY_NAME, SENDER_NAME, FREE_SAMPLE, CASE_STUDIES, DAILY_LIMIT_PER_ACCOUNT, SEND_WINDOW, MSG_GAP_MINUTES, FOLLOWUP_GAPS, TIMEZONE, DATE_FORMAT, LEADS_TAB, PROFILES_FILE | [ ] |
| Insta Automation API's.txt | Original notes file with API details (copied from the old Notes folder; contents not reviewed) | Keep private | [x] copied |
| profiles.json (optional) | send_assist.py: maps accounts to Chrome profiles. Put it in `secrets\` (`run.cmd` finds it) | Copy `app\profiles.example.json` and edit | [ ] |
