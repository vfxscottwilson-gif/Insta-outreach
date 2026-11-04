# 04 Troubleshooting
| Problem | Fix |
|---|---|
| Installer says Python missing even after installing it | Close the window, open a new one, run `INSTALL.cmd` again (PATH refresh) |
| "running scripts is disabled" | Start with `INSTALL.cmd` (it bypasses the policy for that run only) |
| `MISSING secrets\.env` | Normal before install; the installer creates it |
| Run says `MISSING CORE SETTING: GOOGLE_SA and SHEET_ID` | Put the .json key in `secrets\`, run `INSTALL.cmd`, fill `SHEET_ID_AU_ONLY` in `secrets\.env` (or run with `--local`) |
| GitHub run: sheet permission error | Share the sheet with the robot's email (the `client_email` inside the .json) as **Editor** |
| A job prints `SKIP <country>: no SHEET_ID...` | That sheet secret is not set; harmless |
| AI insight is "fact-only" | Free AI limit hit (429) or no AI key; expected, not an error |
| Self-test fails after install | Re-run `INSTALL.cmd` (reinstalls packages), then `install\install.ps1 -Check` |

More: `app\00_START_HERE_SETUP_GUIDE.md`, `app\SECRETS_GUIDE.md`.
