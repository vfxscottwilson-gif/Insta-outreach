# sheet-organizer: Setup guide

For a non-expert on Windows 10. Never write secret values in this file. The original long guide (tabs, risks) is `app\SETUP_GUIDE.md`.

## 1. What this app is
You paste notes into the `Inbox` tab of a Google Sheet, one per row. Once a day (or when you press Run) the robot files each note into the right tab (Tasks, Problems & Solutions, Achievements, Ideas, Resources), flags overdue or forgotten items in `Attention Needed` and writes `Monthly Summary` with a manager's report. It can also read FigJam sticky notes into the Sheet. Limit: Figma cannot be rearranged by any program from outside, so the Sheet is the sorted view. Gmail sorting is not included.

## 2. Accounts needed
| Service | Why | Free? | Sign-up link |
|---|---|---|---|
| Google (Sheets + Cloud) | The Sheet is the database; a service account lets the robot edit it | Yes | console.cloud.google.com |
| At least one AI provider | Understands each note | Free tiers (Gemini, Groq, OpenRouter) | aistudio.google.com/apikey, console.groq.com/keys, openrouter.ai/keys |
| GitHub (private repo) | Runs the daily job in the cloud | Yes | github.com |
| Figma (optional) | Reads sticky notes | Yes | figma.com |

Google service-account steps: create a Cloud project, enable the Google Sheets API, create a Service Account, add a JSON key, download it into `secrets\`, then share your Sheet (Editor) with the `client_email` inside that file.

## 3. How it fits together
Cloud: GitHub Actions runs `organizer.py` daily at 02:00 UTC (07:00 Pakistan time). Database: the Google Sheet. Local: the same script via `install\run.cmd`. No web front end.

## 4. Folder map
See `README.md`. Code is in `app\` (own git). The old zip is in `archive\`.

## 5. First-time install
1. To look first without changing anything, open PowerShell in `install\` and run:
```
.\install.ps1 -Check
```
You should see OK and DRY lines (DRY = what it would do).
2. Double-click `install\INSTALL.cmd` (click **Yes** if Windows asks). It installs Python 3.12 if missing, creates `app\.venv`, installs packages, asks for each value (hidden typing; Enter skips), runs an offline health check and adds a "Sheet Organizer test run" Desktop shortcut.
3. You should end with a CHECKLIST of OK / SKIP lines; a WARN about the Google key means the `.json` key still has to be put in `secrets\`.

## 6. Secrets
See `secrets\SECRETS-CHECKLIST.md`. Local values go in `secrets\.env` (NAME=value lines) plus the Google `.json` key in `secrets\`. For the cloud run put them in GitHub: Settings > Secrets and variables > Actions (secrets: SHEET_ID, GOOGLE_SA = whole JSON text, AI keys, FIGMA_TOKEN; variables are optional).

## 7. Run it / use it
1. Test run, writes nothing (default):
```
install\run.cmd organizer.py
```
2. Live run: set `DRY_RUN=no` in `secrets\.env`, set `RUN_LIMIT=10` for the first time, run the same command.
3. Daily use: paste notes into `Inbox`, nothing else. The cloud job files them every morning. To run it now: GitHub > Actions > "Organize my sheet" > Run workflow (`dry_run` = yes first).
4. You may edit Status, Priority, Owner and Due Date by hand in the filing tabs. Never delete `_Ledger`.

## 8. How to change common things
| I want to... | Do this |
|---|---|
| Use another paste tab name | Set `INBOX_TAB` in `secrets\.env` and in GitHub variables |
| Limit notes per run | `RUN_LIMIT` (default 150) |
| Add AI keys | Add to the matching `*_API_KEY`, comma separated |
| Change the timezone | `TIMEZONE` (default Asia/Karachi) |
| Back up | `powershell -ExecutionPolicy Bypass -File backups\backup.ps1` and download the Sheet (`database\README.md`) |

## 9. Troubleshooting
See `GUIDE\04-TROUBLESHOOTING.md`.

## 10. Move to a new PC
1. Copy the whole `sheet-organizer` folder.
2. Put the secrets back in `secrets\` (from your password manager) if they were not copied.
3. Double-click `install\INSTALL.cmd`.
4. Check: open PowerShell in `install\` and run:
```
.\install.ps1 -Check
```
Every line should say OK (or DRY for things already fine).

Not verified: the real Google Sheet, AI keys and Figma flow (they need your logins). The installer, environment setup and script start-up were tested in a temp copy.
