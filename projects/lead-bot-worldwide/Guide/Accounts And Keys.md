# 05 Accounts and keys (names only; values live in `secrets\` and in GitHub, never here)

Names below were taken from the `env:` block of `app\.github\workflows\run-lead-bot.yml`. Per-key format and free limits: `app\Secrets Guide.md`. Free-tier sizes change; check each vendor page (not verified).

## 1. Accounts you need

| Service | Account | Required? | Used for |
|---|---|---|---|
| Google (Gmail) | your Google account | yes | owns the Sheets |
| Google Cloud Console | same Google account | yes | the "robot" (service account) and its key file; APIs to enable: Google Sheets API, Google Drive API |
| GitHub | your GitHub account | for the daily run | repo, Actions, secrets |
| AI and data services | one account per vendor | no | see sections 3 and 4 |

Not verified: the GitHub repo URL and the Google project name (no remote is set in `app\.git`, and the key file was not opened). Write them into `secrets\SECRETS-CHECKLIST.md` once known.

## 2. Required secrets

| Name | Holds |
|---|---|
| `GOOGLE_SA` | the whole text of the service-account .json key file |
| `SHEET_ID_US` | id (or full URL) of the US sheet; the only sheet id you must have (it also holds the Master Dashboard) |

## 3. Sheet ids (each optional; missing = that job is skipped)

`SHEET_ID_CA`, `SHEET_ID_GB` (alias `SHEET_ID_UK`), `SHEET_ID_AU`, `SHEET_ID_NZ`, `SHEET_ID_IE`, `SHEET_ID_AE`, `SHEET_ID_SA`, `SHEET_ID_QA`, `SHEET_ID_YOUTUBE` (alias `SHEET_ID_YT`). Old single-sheet fallback: `SHEET_ID`. Every sheet must be shared with the robot's email as Editor.

## 4. Optional keys (one secret per key)

| Group | Names |
|---|---|
| AI for Lead Insight | `GEMINI_API_KEY_1`, `GEMINI_API_KEY_2`, `GEMINI_API_KEY_3`, `GROQ_API_KEY`, `OPENROUTER_API_KEY`, `MISTRAL_API_KEY`, `CEREBRAS_API_KEY` |
| Finding businesses | `GOOGLE_PLACES_API_KEY`, `YOUTUBE_API_KEY_1`, `YOUTUBE_API_KEY_2`, `SERPER_API_KEY`, `BRAVE_API_KEY`, `APIFY_API_TOKEN` |
| Emails and people | `HUNTER_API_KEY`, `ZEROBOUNCE_API_KEY`, `APOLLO_API_KEY`, `PROSPEO_API_KEY`, `SNOV_CLIENT_ID`, `SNOV_CLIENT_SECRET`, `REACHER_URL`, `REACHER_SECRET` |
| Website reading | `ZENROWS_API_KEY`, `JINA_API_KEY` |
| Company registers | `ABN_GUID` (Australia; old name `ABN_LOOKUP_GUID` works), `NZBN_API_KEY` (New Zealand) |
| Instagram stats | `IG_ACCESS_TOKEN` (secret), `IG_USER_ID` (a Variable) |
| Old combined secrets (still read as a fallback) | `AI_API_KEYS`, `YOUTUBE_API_KEYS`, `PLACES_API_KEYS`, `ABN_LOOKUP_GUID` |

Most optional keys can also be typed into a sheet's `Options` tab. A GitHub secret wins over the Options tab. Prefer GitHub secrets: the Options tab is a visible sheet cell.

## 5. GitHub Variables (Settings > Secrets and variables > Actions > Variables tab)

| Name | Meaning |
|---|---|
| `LEAD_MATRIX` | overrides which collect jobs run (JSON) |
| `TIMEZONE` | timezone for Master Dashboard dates, for example `Asia/Karachi` |
| `KEY_CHECK` | `warn` = keep a key whose format looks unusual |
| `USE_JINA` | switch for the Jina reader |
| `IG_USER_ID` | Instagram user id |

## 6. Where values live

| Where | What |
|---|---|
| `secrets\.env` (this PC, gitignored) | values for local test runs; created by `install\INSTALL.cmd` |
| `secrets\*.json` | the robot's key file (one file is present; its contents were never opened) |
| GitHub repo secrets | values for the daily run |
| Sheet `Options` tab | optional alternative for keys |

Never paste a value into chat, a document or a commit.
