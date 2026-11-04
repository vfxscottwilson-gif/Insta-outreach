# 04 Troubleshooting

Messages below were searched in the source code (`app\src\`) and in `app\SETUP_GUIDE.md` Part 9. The longer click-by-click table is there.

## How to read results
| Where | How |
|---|---|
| Local dry run | The black window prints lines like `[WARN] youtube_api: ...`. Format: `[LEVEL] source: message (channel id)`. Last useful line: `[INFO] leadbot: SUMMARY written N \| processed N \| gated {...} \| yt units N \| ai calls N ...` |
| GitHub run | Repo > Actions > click the run > the step "Run bot" shows the same lines. Artifacts at the bottom: `leadbot-log-<run id>` (kept 14 days) |
| Google Sheet | Tab `Run Log` (one `SUMMARY` row per run + every warning/error) and tab `Master Dashboard` (API health, leads today) |
| Local state | `app\.state_local.json` (dry run), `app\pending_leads.json` (leads waiting for a Sheet write) |

Exit codes: `0` = finished (even if some sources failed). `1` = a required secret is missing or GOOGLE_SA is unreadable; the run goes red. A crash inside the run is caught, printed as `[ERROR] unexpected: ...`, and still exits 0, so a green run does NOT prove the Sheet got rows: read the SUMMARY line (`written N`).

## Failure table
| You see | Cause | Fix |
|---|---|---|
| `[FATAL] Missing required env var(s): YOUTUBE_API_KEYS` | No YouTube key (needed even for a dry run) | Fill it in `secrets\.env`, run `install\INSTALL.cmd` again (copies to `app\.env`). On GitHub add the secret |
| `[FATAL] Missing required env var(s): SHEET_ID, GOOGLE_SA` | Live run without Sheet secrets | Add both secrets with exactly these names |
| `[FATAL] GOOGLE_SA is set but is neither valid JSON nor base64 JSON...` | The key was pasted incompletely | Paste the whole `.json` file from `{` to `}`, or give the installer the file path |
| `[ERROR] sheets: Google Sheet unreachable (check SHEET_ID ...)` | Wrong SHEET_ID, or the Sheet is not shared with the service account | Open the Sheet > Share > add the `client_email` from the key as Editor. Leads are kept in `pending_leads.json` and written next run |
| `write failed; leads buffered to pending_leads.json` | Temporary Google error | Nothing; the next run flushes them (`flushed N buffered leads`) |
| `[WARN] youtube_api: a key is invalid or YouTube Data API v3 is not enabled for its project` | Key typo, key restricted, or API not enabled | Google Cloud > APIs & Services > enable "YouTube Data API v3"; recheck the key |
| `a key hit its quota (N keys left)` / `all YouTube keys are out of quota or invalid` / `daily YouTube unit budget used up` | The 10,000 units per key per day are spent | Normal. Resets 00:00 US Pacific (about 12:00-13:00 PKT). Job platforms still run. Add more keys (comma-separated, one per Google project) |
| `YouTube quota for this Pacific day is spent` | Same | Same |
| `YouTube API 403: ...` / `YouTube API kept failing` | Another API error (not quota) | Read the text after the code; check the key restrictions |
| `[WARN] ai: no working AI key; every lead uses the template generator` / `AI_Source = template` | No Gemini/Groq key, or all rejected | Normal without keys. To fix: new key from aistudio.google.com or console.groq.com |
| `gemini key #1: model list failed (400)` | Wrong or expired AI key | Make a new key, replace it |
| `<provider> key rejected (...); disabled this run` / `rate-limited 3x` | Key bad, or too many requests | Wait; add a second key (comma-separated) |
| `model X unavailable (...); dropped` | Provider retired the model | Nothing; another model is auto-picked. Optional: update `gemini_models` |
| `upwork: Upwork API keys not set; skipping` | The 3 UPWORK_* secrets absent | Normal until Upwork approves you |
| `upwork: token refresh failed (...); re-run tools/upwork_auth.py` | Refresh token expired or revoked | Run `app\tools\upwork_auth.py` (needs the client id/secret), put the new token in `UPWORK_REFRESH_TOKEN`. The bot stores a rotated token in the hidden `_State` tab (key `upwork_refresh_token`) and prefers it (per comment in `upwork.py`); if the new secret seems ignored, delete that row. Not tested live |
| `upwork: API returned N: check the key's scopes` | Key lacks job-search permission | Upwork API Center > edit the key's permissions |
| `upwork: full query rejected ...; retrying minimal query` | Upwork changed a field | Nothing; client stats may be blank |
| `web_search: DuckDuckGo returned 202; skipping web search this run` | DuckDuckGo blocks bots | Normal. Set `use_web_search: false` to silence it |
| `linkedin: HTTP 429; stopping LinkedIn for this run` | LinkedIn slowed us down | Retries next run. If it repeats, lower `linkedin_pages_per_country` |
| `freelancer: API returned N` / `remotive: API returned N` | Temporary site problem | Nothing; next run |
| `5 failures in a row; source marked DOWN for this run` | One source kept failing | Look at the WARN lines just above it. Others keep working |
| `youtube_search: search paused: keeping 1500 units in reserve` | By design | Nothing |
| `optional daily target reached (N/M); nothing to do` | You set `DAILY_LEAD_TARGET` | Set it to `0` for no cap |
| `run time limit reached; stopped cleanly` | 40-minute self-limit | Nothing; next run continues |
| SUMMARY says `written 0`, `gated {...}` | Filters rejected everything. Keys of `gated` explain why (`subs N < 15000`, `last upload Nd ago`, `duplicate email`, `score < 3`) | Loosen settings: `03-HOW-TO-CHANGE-THINGS.md` recipe 1 |
| `[config] could not read config.yaml: ...; using built-in defaults` | Broken YAML (often a tab or bad quote) | Fix the file; defaults are weaker than the real file |
| `[WARN] lead: ...` or `contacts: read failed ...` | One channel or website failed | Ignored; the run continues |

## Install and PC problems
| You see | Fix |
|---|---|
| `[FAIL] Folder layout app\src\leadbot.py missing` | You copied only part of the folder. Copy the whole `yt-creator-finder` folder |
| `[WARN] Python installed but not on PATH yet` | Close the window, run `install\INSTALL.cmd` again |
| `[FAIL] Python missing and winget not available` | Install Python 3.12 from python.org (tick "Add to PATH"), run the installer again |
| `[FAIL] Create venv` / `pip install` | No internet, or a half-made `app\.venv`. Delete the `app\.venv` folder and run the installer again (this deletes only a local, re-creatable folder) |
| `[WARN] Offline tests ...` | Read that line; the bot may still run. Run recipe 9 in `03-HOW-TO-CHANGE-THINGS.md` to see details |
| Desktop shortcut window closes or shows an error | Open it, read the first red line. Usually the YouTube key (first row of the table) |
| Few or no leads | Normal on a first run if filters are strict; see SUMMARY `gated` |
| Schedule stopped | GitHub disables idle schedules after 60 days; a keepalive step prevents it. Re-enable under Actions. Also check that `.github\workflows\run-lead-bot.yml` was pushed |
| No runs at all | Actions disabled in repo Settings > Actions, or the workflow file is missing from the repo |

## Not verified
Messages are from the code; I did not trigger each one. `app\SETUP_GUIDE.md` lists "could not find the poster's YouTube channel; skipped", which is not present in the current source (grep found no match), so it is not listed here.
