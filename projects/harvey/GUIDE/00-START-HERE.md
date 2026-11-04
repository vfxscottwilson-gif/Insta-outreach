# 00 Start here: install Harvey and run it the first time

Plain English, Windows 10. Every command goes in PowerShell. Harvey is a third-party app (github.com/ethanplusai/harvey, details in `docs\UPSTREAM.md`). It sends REAL emails once you start it, so go in the order below.

## What you need before you begin
| Need | Why | Where to get it |
|---|---|---|
| Claude Pro or Max account | Harvey's AI brain runs through the Claude CLI, no API key | claude.ai |
| One mailbox on a secondary domain | Sending and reading replies | Gmail/Workspace, any SMTP+IMAP mailbox, Microsoft 365, or Instantly (see `05-ACCOUNTS-AND-KEYS.md`) |
| An email verifier key (Reoon or ZeroBounce) | Without one, found emails stay "guess" and are never sent (upstream `app\CLAUDE.md`, Step 2) | reoon.com, zerobounce.net |

## A. Install (about 2 to 5 minutes)
1. Copy the whole `harvey` folder to the PC (include `secrets\`; `app\.venv` is not needed).
2. Optional dry run that changes nothing. Open PowerShell in the `install` folder and run:
```
.\install.ps1 -Check
```
3. Double-click `install\INSTALL.cmd`. Click **Yes** if Windows asks.
4. The installer: finds Python 3.11+ (installs 3.12 with winget if missing), creates `app\.venv`, runs `pip install -e ".[dev]"`, creates `secrets\.env` from the template and asks for 10 keys (hidden typing, press Enter to skip any), copies it to `app\.env`, runs a health check, and creates the Desktop and Start-menu shortcut "Harvey Dashboard".
5. You should see: `===== CHECKLIST =====`, lines starting `OK` or `SKIP` (a `WARN Claude CLI` line is normal until step C), then `Done.` Any `FAIL` line: see `04-TROUBLESHOOTING.md`.

## B. Keys
1. Pick ONE mailbox option in `secrets\SECRETS-CHECKLIST.md`.
2. Open `secrets\.env` in Notepad and type each value after the `=` for your option. Names only are listed in `05-ACCOUNTS-AND-KEYS.md`.
3. Delete `app\.env`, then double-click `install\INSTALL.cmd` again, so the new keys are copied (the installer never overwrites a different `app\.env`; it only warns).

## C. Log in to Claude (once per PC)
1. If the installer warned that the Claude CLI is missing, install Node.js:
```
winget install OpenJS.NodeJS.LTS
```
2. Close and reopen PowerShell, then:
```
npm install -g @anthropic-ai/claude-code
```
3. Log in. A browser opens; sign in with the Claude Pro/Max account:
```
claude login
```

## D. First run: teach Harvey, find businesses
Open PowerShell in the `app` folder.
1. Activate the environment:
```
.\.venv\Scripts\Activate.ps1
```
If PowerShell blocks scripts, skip this step and write `.\.venv\Scripts\harvey.exe` instead of `harvey` in every command below.
2. Learn your product from your website. This writes `harvey.local.yaml` and files in `skills\`:
```
harvey train https://your-company.com
```
3. Confirm the free signals (facts Harvey may collect). Nothing is collected until you do this:
```
harvey signals --confirm free
```
4. See what discovery would cost, then run the free OpenStreetMap source:
```
harvey discover --estimate
```
```
harvey discover
```
5. Gmail only, once (needs `GMAIL_CLIENT_ID` and `GMAIL_CLIENT_SECRET` set, and `channels.email.provider: gmail`):
```
harvey gmail auth
```
6. Open the dashboard (or double-click the Desktop shortcut). It prints `http://127.0.0.1:5555/#token=...`. Open that full link in your browser and keep it private:
```
harvey dashboard
```
7. Check the state any time:
```
harvey status
```

## E. Start the loop (this is when emails can go out)
1. In the dashboard open **Settings** and confirm limits. Default is approval mode: every email waits in the **Outbox** for your click (`require_approval: true` in `app\harvey.yaml`).
2. Warm up a new mailbox for weeks before cold sending. Check readiness with:
```
harvey warmup
```
3. Start Harvey, or double-click `install\Run Harvey.cmd`. Leave the window open; closing it stops Harvey:
```
harvey run
```
4. What you should see: log lines like `Decision: prospect (...)` or `Decision: write_campaign (...)`, one cycle about every 15 minutes. Stop with Ctrl+C.

Note: if `.env` is missing or the config still says "Your Company", `harvey run` starts the setup wizard instead of the loop (checked in `app\harvey\main.py`, `_needs_setup`).

## Not verified
Steps D2 to E4 need a real Claude login, a mailbox and keys, none of which existed when this folder was packaged. Commands and messages above were checked against the source code only (`app\harvey\cli.py`, `main.py`), not run.
