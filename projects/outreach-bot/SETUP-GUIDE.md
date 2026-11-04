# outreach-bot: Setup guide

For a non-expert on Windows 10. No secret values are written anywhere in this folder.

## 1. What this app is
A Python script (`app\generate.py`) that reads all your lead sheets (one per country, plus YouTube and AU-only), removes duplicates, and asks free AI models (Gemini, Groq, Mistral, OpenRouter) to write one email per lead. Drafts go into the "Emails" tab of one Outreach sheet. Sending is OFF; you send by hand. It runs daily in the cloud (GitHub Actions) and can be test-run on this PC.

## 2. Accounts needed
| Service | Why | Free? | Sign-up link |
|---|---|---|---|
| Google (Cloud + Sheets) | Service account that reads lead sheets and writes the Outreach sheet | Yes | console.cloud.google.com |
| GitHub | Runs the bot daily (Actions), holds the cloud secrets | Yes | github.com |
| Google AI Studio | Gemini keys (one project per key) | Yes, small daily quota | aistudio.google.com |
| Groq | AI keys | Yes | console.groq.com |
| Mistral (optional) | AI keys | Yes, limited | console.mistral.ai |
| OpenRouter (optional) | AI keys | Yes, 50 requests/day | openrouter.ai |

## 3. How it fits together
- Frontend: none (you work in Google Sheets).
- Backend: `app\generate.py`, run by GitHub Actions (daily 10:00 UTC) or by `install\run-bot.ps1` on this PC.
- Database: Google Sheets only (see `database\README.md`).
- Cloud vs local: the daily run is cloud (needs the GitHub repo and its secrets). This folder only needs Python 3.12 for local tests.

## 4. Folder map
See `README.md`.

## 5. First-time install
1. Optional: check what is missing, nothing is changed.
```
install\INSTALL.cmd -Check
```
You should see `[OK]` lines; `[DRY]` lines show what the installer would add.
2. Double-click `install\INSTALL.cmd`. It installs Python 3.12 if missing (winget), makes `app\.venv`, installs `gspread`, creates `secrets\.env`, asks for each secret with hidden typing (press Enter to skip any), adds a Desktop shortcut "Outreach Bot (dry run)" and runs the offline self-test.
3. You should end with `[OK] Self-test passed`, plus `[TODO]` lines for any key still empty.

## 6. Secrets
See `secrets\SECRETS-CHECKLIST.md` (names only). Local file: `secrets\.env`; the Google JSON key goes in `secrets\google-sa.json`. For the daily cloud run the same names are GitHub repo secrets (GitHub > repo > Settings > Secrets and variables > Actions). `secrets\Draft Emails API Keys.txt` is the old keys file, copied unread; the bot's own notes say those keys were dead (401), so create new ones.

## 7. Run it / use it
1. Safe test (writes nothing):
```
powershell -ExecutionPolicy Bypass -File install\run-bot.ps1
```
2. Real run (writes drafts), 10 leads:
```
powershell -ExecutionPolicy Bypass -File install\run-bot.ps1 -Live -Limit 10
```
3. Offline tests only:
```
powershell -ExecutionPolicy Bypass -File install\run-bot.ps1 -SelfTest
```
4. Daily cloud run: GitHub > Actions > `generate-emails` (manual inputs `limit`, `dry_run`). Key check: Actions > `diagnose-keys`.

## 8. How to change common things
| I want to... | Do this |
|---|---|
| Change writing rules | Edit the "Email Rules" tab in the Outreach sheet (base rules: `app\rules.md`) |
| Change daily target / switches | "Options" tab in the Outreach sheet |
| Add a country sheet | Add secret `SHEET_ID_<COUNTRY>`, share the sheet with the service account (Viewer) |
| Add an AI key | Add `GEMINI_API_KEY_n` / `GROQ_API_KEY` etc., then run `diagnose-keys` |
| Turn on sending | Do not. `app\phase2_parked\` is parked on purpose |

## 9. Troubleshooting
| Problem | Fix |
|---|---|
| `python` not found after install | Close the window and run `INSTALL.cmd` again |
| "GOOGLE_SA secret is missing" | Save the service-account JSON as `secrets\google-sa.json` |
| Keys rejected (401/403) | See `app\DIAGNOSIS.md`; make new keys, each Gemini key in its own project |
| "running scripts is disabled" | Use the `-ExecutionPolicy Bypass` commands above |

## 10. Move to a new PC
1. Copy the whole `outreach-bot` folder.
2. Put the secrets back in `secrets\` (from your password manager).
3. Double-click `install\INSTALL.cmd`.
4. Check: open PowerShell in `install\` and run `.\install.ps1 -Check`. Every line should say OK (DRY lines mean "already planned/not needed yet").
The GitHub repo and its secrets live in the cloud; copying this folder does not move them.

Not verified: a live run against Google Sheets and the AI APIs (needs your logins). Only the offline self-test (58 checks) was run.

## 11. Deeper chapters (read these when you need detail)
| Question | Chapter |
|---|---|
| What happens in one run, which tabs and columns exist, how the AI keys rotate | `GUIDE\02-ARCHITECTURE.md` |
| Exact settings, files and tabs for each change (rules, limits, schedule, countries, keys, models) | `GUIDE\03-HOW-TO-CHANGE-THINGS.md` |
| Error messages and fixes (dead keys 401, quota, sheet sharing, how to read the log) | `GUIDE\04-TROUBLESHOOTING.md` |
| Order of work and what is parked | `GUIDE\01-ROADMAP.md` |

Key facts to remember:
- Option priority: GitHub Variable > Options tab > default.
- Targets: DAILY_TARGET 400, RUN_LIMIT 700, MAX_RUN_MIN 50. Real output is limited by the free AI quota (about 400-700 drafts a day).
- The Outreach sheet must be a separate, new sheet. The bot never writes to lead sheets and refuses to start if both are the same.
- Local install check (changes nothing):
```
powershell -ExecutionPolicy Bypass -File install\install.ps1 -Check
```
