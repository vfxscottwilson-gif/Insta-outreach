# 05 Accounts and keys (names and IDs only; values live in `secrets/`)

| Service | Name | ID / account email | Where used | Secret lives in |
|---|---|---|---|---|
| Google Cloud | project (suggested name `local-drafter`) | your Google account | Sheets API (+ YouTube Data API v3 optional) | cloud |
| Google service account | any name (no roles needed) | `...@...iam.gserviceaccount.com`, shown on its page | Reads the leads tab, writes Ready to Send / Log / Needs Review | JSON key file in `secrets\`; path in `GOOGLE_SERVICE_ACCOUNT_FILE` |
| YouTube Data API v3 (optional) | API key | same project | Channel facts | `YOUTUBE_API_KEY` in `secrets\.env` |
| Ollama | none (no account) | - | Local AI | model `qwen3:8b` stored by Ollama, not in this folder |
| AI server key (optional) | - | - | Only for OpenAI-compatible servers | `AI_API_KEY` |

## Secret NAMES (values are never written in any guide)
| Name | Required? | Read by | Behaviour if missing |
|---|---|---|---|
| `GOOGLE_SERVICE_ACCOUNT_FILE` (a file path, not a key) | only in sheet mode | `sinks.py` | `GOOGLE_SERVICE_ACCOUNT_FILE is not set in .env`; relative paths start in `app\`; surrounding quotes are removed |
| `YOUTUBE_API_KEY` | optional | `pipeline.py`, `research.py` | `YouTube facts off (no YOUTUBE_API_KEY in .env)`; drafting continues |
| `AI_API_KEY` | optional | OpenAI-compatible backend only | Ollama and LM Studio need none |

How they get to the app: you (or the installer, on a first install) fill `secrets\.env`; the installer copies it to `app\.env`; `draft_emails.py` loads `app\.env`. After editing `secrets\.env`, re-run `install\INSTALL.cmd` to copy it again (an existing `secrets\.env` is never overwritten). Template: `app\.env.example`. Per-secret steps: `secrets\SECRETS-CHECKLIST.md`.

## Free tiers and limits
| Service | Limit | Source / date |
|---|---|---|
| YouTube Data API | 10,000 units per day, about 3 units per YouTube lead; `search.list` has its own bucket (100 calls/day) used only if `YT_ALLOW_SEARCH: true` | `app\START_HERE.md` "Facts checked" (checked 2026-11-03); not re-checked for this guide |
| Google Sheets API | 300 read and 300 write requests per minute per project; this tool writes about once per 10 drafts | same table, 2026-11-03; Google said exceeding quotas is planned to incur charges later: not re-verified |
| Ollama, `qwen3:8b` | free, local, no account | ollama.com |

## Checking that access works
1. Sheet and key: `app\run.bat --check` must show `input readable` and `output sheet opened`.
2. YouTube key: the same check shows `YouTube API key answers (1 quota unit)`.
3. Rotate a key: create the new key in Google Cloud, change the value in `secrets\.env`, re-run the installer, delete the old key in Google Cloud. If a key was ever shown in chat or committed, rotate it.

## Google service account (once)
1. Go to https://console.cloud.google.com and create a project.
2. APIs & Services > Library: enable **Google Sheets API** (and **YouTube Data API v3** for the optional key).
3. IAM & Admin > Service Accounts > Create service account (any name, no roles) > Done.
4. Open it > Keys > Add key > Create new key > JSON. Save the file into `secrets\`.
5. Copy the service account e-mail (ends `iam.gserviceaccount.com`). In Google Sheets press **Share** and add it: Viewer on the leads sheet, Editor on the output sheet (Editor if it is the same file).
6. Re-run `install\INSTALL.cmd` (or put the file path in `secrets\.env`), then:
```
app\run.bat --check
```
Input and output must show PASS.

## Apps Script hand-off (your existing script, lives in Google)
1. The drafter writes columns A-D of the **Ready to Send** tab: `Email | First Name | Subject | Body`. It never touches column E onward.
2. Your Apps Script reads those rows, adds "Hi {First Name}," and your signature (postal address, opt-out) and creates the Gmail drafts. The drafter's body has no greeting, name or signature.
3. Test before the first real run. This writes 3 sample rows:
```
app\run.bat --test-handoff
```
4. Press your Apps Script draft button and open the 3 drafts (`handoff-test-1..3@example.com`). Check: greeting once, sign-off once, signature once, no blank line at the top. Doubled sign-off: set `SIGN_OFF_MODE: none`. Doubled opt-out: `INCLUDE_OPT_OUT: false`. Then delete the 3 test rows and drafts.
5. The Apps Script is not stored in this folder, and its name and location are not recorded here (not verified: ask the owner of the script).
