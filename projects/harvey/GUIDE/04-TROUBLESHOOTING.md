# 04 Troubleshooting

| Problem | Fix |
|---|---|
| `FAIL Python 3.11+` and no winget | Install "App Installer" from the Microsoft Store, or Python 3.12 from python.org (tick "Add to PATH"), then re-run |
| Python installed but "not on PATH yet" | Close the window, run `INSTALL.cmd` again |
| `pip install` fails | Check internet; delete `app\.venv`; run `INSTALL.cmd` again |
| `WARN app\.env differs from secrets\.env` | `secrets\.env` is the master: delete `app\.env`, re-run |
| `Claude CLI not found` | `npm install -g @anthropic-ai/claude-code` (needs Node.js: `winget install OpenJS.NodeJS.LTS`), then `claude login` |
| Dashboard link does not open | Run `harvey dashboard --url` for the link again; use the full link including `#token=` |
| Emails not sending | Check `harvey status`, `harvey sending resume`, quiet hours, and that the mailbox keys are set |
| Playwright / LinkedIn errors | Run `install.ps1 -WithBrowser` |
| Codex errors | Codex is refused on Windows by design; use Claude |
| Tests are slow | The suite is large; run one file: `python -m pytest tests\test_config.py` |

Upstream common issues: `app\CLAUDE.md`, section "Common Issues".
