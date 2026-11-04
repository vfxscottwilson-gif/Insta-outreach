# 03 How to change common things
| I want to... | Do this |
|---|---|
| Add or change a secret | Edit `secrets\.env` (this PC) AND GitHub repo > Settings > Secrets and variables > Actions (daily run) |
| Change run times | Edit the `cron:` lines in `app\.github\workflows\run-lead-bot.yml` (UTC), commit and push |
| Change niches, locations, scoring rules | Edit the **Rules** tab in the Google Sheet (first-run defaults are in `app\src\defaults.py`) |
| Run it once now on GitHub | GitHub repo > Actions > "Run Lead Bot" > Run workflow |
| Add scraped leads | Put CSV/JSON exports in `app\imports\` or the sheet's **Import** tab (see `app\imports\README.md`) |
| Run the tests | PowerShell inside `app\`: `.venv\Scripts\python.exe src\selftest.py` |
| Back up | `powershell -ExecutionPolicy Bypass -File backups\backup.ps1` |
| Remove the Desktop shortcut | `install\INSTALL.cmd -Uninstall` (only the shortcut) |

Never sort or delete rows in the lead sheet; the bot assumes append-only.
