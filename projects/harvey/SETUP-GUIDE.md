# Harvey: Setup guide

For a non-expert on Windows 10. Numbered steps. No secret values anywhere.

## 1. What this app is
Harvey is an open-source "AI sales rep". You describe your product (it reads your website), it finds matching businesses, finds the owner's email, writes short personal cold emails with Claude, sends them from YOUR mailbox within safe daily limits, reads replies and answers them. A local web page (the dashboard) shows companies, emails waiting for approval, conversations and usage. Source: github.com/ethanplusai/harvey (see `docs\UPSTREAM.md`).

## 2. Accounts needed
| Service | Why | Free? | Sign-up link |
|---|---|---|---|
| Claude Pro or Max (and the Claude CLI login) | The AI brain. Required. | Paid subscription | claude.ai |
| An email mailbox on a SECONDARY domain (Gmail/Workspace, any SMTP+IMAP, Microsoft 365, or Instantly) | Sending and reading replies. One required. | Mailbox cost only | workspace.google.com or your host |
| Google Cloud project (only for the Gmail option) | Gmail OAuth key | Free | console.cloud.google.com |
| Email verifier: Reoon or ZeroBounce | Avoid bounces. Strongly recommended. | Small free tier / paid | reoon.com, zerobounce.net |
| TrulyInbox (warmup) | Warm a new mailbox. Recommended. | Paid | trulyinbox.com |
| Hunter, Precleared, Cloudflare, LinkedIn, DataForSEO, Serper | Optional extras | Mostly free tiers | see `secrets\SECRETS-CHECKLIST.md` |

No GitHub, Supabase or Google Sheets login is needed. Prices were not re-checked for this guide.

## 3. How it fits together (backend vs frontend)
Everything runs locally: the Python program `harvey` = backend; the dashboard at http://127.0.0.1:5555 = frontend (served by the same program, opened with a private link); database = one SQLite file `app\data\harvey.db`. Cloud = only Claude (via the Claude CLI) and your email provider. See `GUIDE\02-ARCHITECTURE.md`.

## 4. Folder map
See the table in `README.md`. Important: `app\` is a third-party clone; do not edit its files. Your own settings go in `app\harvey.local.yaml` (created by `harvey train`) and `secrets\.env`.

## 5. First-time install
1. Check nothing is missing (changes nothing). Open PowerShell in the `install` folder and run:
```
.\install.ps1 -Check
```
You should see `[OK]` lines; `[DRY]` lines are what the installer will do. A `[WARN] Claude CLI` line means step C of `GUIDE\00-START-HERE.md` is needed later.
2. Double-click `install\INSTALL.cmd`. Click **Yes** if Windows asks.
3. It installs Python 3.12 if missing, creates `app\.venv`, runs `pip install -e`, asks for keys (hidden typing; press Enter to skip any), copies `secrets\.env` to `app\.env`, creates a Desktop shortcut "Harvey Dashboard" and runs a health check.
4. You should end with `===== CHECKLIST =====` and `Done.` (no FAIL lines). It takes about 2 to 5 minutes.

Optional extras (run in PowerShell in the `install` folder):
```
.\install.ps1 -RunTests
```
Runs the upstream test suite (very long). And:
```
.\install.ps1 -WithBrowser
```
Downloads Chromium (only for LinkedIn / deep crawling).

## 6. Secrets
See `secrets\SECRETS-CHECKLIST.md` (required vs optional). Put keys in `secrets\.env`. After editing `secrets\.env`, delete `app\.env` and run `INSTALL.cmd` again so Harvey picks up the change. Also log in to Claude once: `claude login`.

## 7. Run it / use it
Full walk-through in `GUIDE\00-START-HERE.md`. Short version:
1. Double-click **Harvey Dashboard** on the Desktop. A window prints a private link `http://127.0.0.1:5555/#token=...`. Open it in your browser and keep the token private.
2. Train it on your website, confirm signals, discover businesses (commands in the guide).
3. To let it work on its own, double-click `install\Run Harvey.cmd`. It sends real emails: review the Outbox and limits first.

## 8. How to change common things
| I want to... | Do this |
|---|---|
| Change product, targeting, limits, quiet hours | Edit `app\harvey.local.yaml` (or re-run `harvey train <url>`); defaults are in `app\harvey.yaml` |
| Change a key | Edit `secrets\.env`, delete `app\.env`, re-run `INSTALL.cmd` |
| Stop all sending right now | `harvey sending pause` (in the app venv) |
| Approve emails before they go | Dashboard Outbox tab, or `harvey outbox --approve-all` |
| Update Harvey from upstream | `git -C app pull origin main`, delete `app\.venv`, run `INSTALL.cmd` |

More in `GUIDE\03-HOW-TO-CHANGE-THINGS.md`.

## 9. Troubleshooting
| Problem | Fix |
|---|---|
| Installer says Python missing right after installing it | Close the window, double-click `INSTALL.cmd` again |
| `harvey` not recognised | Use `app\.venv\Scripts\harvey.exe` (or the .cmd files in `install\`) |
| Claude CLI not found / not logged in | `npm install -g @anthropic-ai/claude-code`, then `claude login` |
| Codex / ChatGPT brain | Not supported on Windows; use Claude |

More in `GUIDE\04-TROUBLESHOOTING.md`.

## 10. Move to a new PC
1. Copy the whole `harvey` folder (include `secrets\`; `app\.venv` need not be copied).
2. Double-click `install\INSTALL.cmd`.
3. Run `claude login` again (the login does not travel with the folder).
4. Check: open PowerShell in `install\` and run `.\install.ps1 -Check`. Every line should say OK, SKIP or DRY.
