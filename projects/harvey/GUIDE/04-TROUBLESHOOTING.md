# 04 Troubleshooting

Upstream's own list: `app\CLAUDE.md`, section "Common Issues". Below: installer problems first, then run-time problems. Messages in quotes were taken from `install\install.ps1` and the source in `app\harvey\`.

## How to read what Harvey is doing
| Where | What you see |
|---|---|
| The `harvey run` window | The log. Harvey writes NO log file; the window is the log (`main.py` logs to the console only). Lines look like `2026-11-05 10:00:00 [harvey] INFO: Decision: prospect (...)`. Copy the last 30 lines when asking for help. |
| `harvey status` | Pipeline counts and flags: `Sending: HELD`, `Sending: NOT SENDING (...)`, `Prospecting: PAUSED`, `Writing: STOPPED`, `Postal address: MISSING`, `Brain: ... PAUSED since ...` |
| `harvey status --check` | Same, plus a brain check; exits with an error if something is wrong (cli.py) |
| `harvey sending status` | `active` or `PAUSED - reason` |
| Dashboard **Today**, **Activity**, **Usage** tabs | What waits for you, what Harvey did, Claude usage |
| Installer window | A CHECKLIST of OK / SKIP / WARN / FAIL lines at the end |
| `proof\install-temp-copy-2026-11-05.log` | A known-good install log to compare with |

## Installer problems
| Message | Cause | Fix |
|---|---|---|
| `FAIL Python 3.11+ ... winget not available` | No Python 3.11+ and no winget (Windows 10 may lack App Installer) | Install "App Installer" from the Microsoft Store, or Python 3.12 from python.org with "Add to PATH" ticked, then run `INSTALL.cmd` again |
| `WARN Python ... installed but not on PATH yet` | Windows has not refreshed PATH | Close the window, run `INSTALL.cmd` again |
| `FAIL Create venv` / `no Python` | Python missing or only the Microsoft Store stub (paths containing `WindowsApps` are skipped) | Install real Python as above |
| `FAIL pip install -e ".[dev]"` | No internet, or a half-made venv | Check internet, delete the folder `app\.venv`, run `INSTALL.cmd` again |
| `FAIL Health check: import harvey` | Broken install | Delete `app\.venv`, re-run |
| `FAIL Folder layout` | `app\pyproject.toml` or `app\harvey` missing | Copy the WHOLE `harvey` folder again |
| `WARN app\.env differs from secrets\.env` | You edited one of them | `secrets\.env` is the master: delete `app\.env`, re-run. Not overwritten automatically |
| `WARN Claude CLI not found` | Not installed (needed to RUN Harvey, not to install) | `00-START-HERE.md`, step C |
| Window closes instantly | Script policy or a crash | Open PowerShell in `install\` and run `.\install.ps1`; read the message |
| `Playwright / LinkedIn errors` | Chromium not downloaded | Only needed for LinkedIn or deep crawling: `.\install.ps1 -WithBrowser` |

## Run-time problems
| Symptom | Cause | Fix |
|---|---|---|
| `harvey` not recognised | venv not active | `.\.venv\Scripts\Activate.ps1`, or use `.\.venv\Scripts\harvey.exe` |
| "Harvey is already running (pid N). Stop it first..." | A second `harvey run` (only one loop is allowed, so two do not drain the same Outbox) | Press Ctrl+C in the first window; if none is open, end the python process in Task Manager |
| "Harvey isn't set up yet. Run `harvey setup`" or the wizard appears | `app\.env` missing, or config company still "Your Company" | `harvey train <url>` and make sure `app\.env` exists (run `INSTALL.cmd`) |
| "Harvey is paused: ... Nothing was sent or changed" | Brain not usable, e.g. Claude not logged in | `claude login`, then wait up to 15 min or restart. Message mentions "Run 'claude login' and restart Harvey." |
| "usage limit reached (80% of quota ...). Sleeping 1h" | You hit `usage.max_daily_claude_percent` | Wait, or raise it in `harvey.local.yaml` |
| "Cannot start - configuration error" | Bad yaml (tabs, typo, wrong type) | Fix the line shown. Compare with `app\harvey.yaml` |
| Nothing sends, emails stay in Outbox | Approval mode (default) | Approve in the Outbox (`03`, recipe 7) |
| Emails approved but not sent | Sending paused, quiet hours, warmup ramp, daily cap, a gate hold, Precleared hold, or replies unreadable (`Sending: NOT SENDING`) | `harvey status` names the reason; `harvey sending resume` if paused |
| Prospects found but no email ever sent | Email tagged "guess": no verifier key | Add `REOON_API_KEY` or `ZEROBOUNCE_API_KEY` (`03`, recipe 5) |
| Everything stopped after bounces | Bounce rate passed `max_bounce_rate` (global kill switch) | Find why (bad list, unwarmed mailbox), then `harvey sending resume` (resets the counter) |
| "Quiet hours. Sleeping for N minutes." | Normal. Default quiet hours 22:00-07:00 in `America/New_York` | Set your timezone (`03`, recipe 2) |
| "Prospecting: PAUSED" | A day's worth of prospects have no usable email | Add a verifier key, or run discovery with a better source |
| Dashboard link does not open | Token missing from the link or Harvey not running | `harvey dashboard --url` prints the link again; use the whole link including `#token=` |
| "Dashboard not started: ... is a symbolic link / readable by other users / owned by another user" | The token file `app\data\dashboard-token` is unsafe | Delete that file and run `harvey dashboard` again (a new token is made) |
| "Refusing to listen on ..." | You passed `--host` other than this PC | Remove `--host`; the dashboard is local only |
| Gmail "not authorised" or auth errors | `harvey gmail auth` not done or wrong client | Re-run `harvey gmail auth`, then `harvey gmail test` |
| Instantly API 401 | Wrong key, or plan without API access (Growth plan or higher, per upstream) | Fix `INSTANTLY_API_KEY` |
| Google search rate limiting | Normal; Harvey falls back to DuckDuckGo and Bing | Optional `SERPER_API_KEY` |
| Codex errors / "Codex is refused" | Codex is not supported on Windows | Keep `brain.provider` as claude |
| `ModuleNotFoundError: harvey` | Upstream macOS issue; on Windows usually a broken venv | Delete `app\.venv`, re-run installer |
| Tests very slow | Large suite | Run one file (`03`, recipe 12) |

## Last resorts
1. `proof\` and `database\README.md` show the known-good state and the DB restore.
2. Nuclear reset of code only: delete `app\.venv` and re-run `INSTALL.cmd`. Data (`app\data\`) and keys (`secrets\`) are untouched.
3. Remove shortcuts only: `.\install.ps1 -Uninstall` (folder, venv, data and keys stay).

## Not verified
All entries come from reading source and installer text. None were reproduced on a live Harvey (no Claude login or mailbox was available).
