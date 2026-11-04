# 02 Architecture

- Front end: none; you use Google Sheets.
- Back end: `app\generate.py` (Python 3.12, only dependency `gspread`).
- Hosting: GitHub Actions (`generate-emails` daily 10:00 UTC, `diagnose-keys` manual).
- Data flow: lead sheets (read-only) -> dedupe by Place Id/email -> AI batches of 5 -> legal footer -> Outreach sheet tabs Leads, Emails, Options, Email Rules, Inboxes, AI Usage.
- Sending: parked in `app\phase2_parked\`, OFF.

| Want to change | File |
|---|---|
| Bot logic | `app\generate.py` |
| Tests | `app\selftest.py` |
| Base writing rules | `app\rules.md` |
| Key tester | `app\tools\diag_keys.py` |
| Schedule and env passed to the bot | `app\.github\workflows\generate.yml` |
