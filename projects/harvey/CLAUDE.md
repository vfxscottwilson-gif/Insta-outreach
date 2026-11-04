# Harvey (third-party autonomous AI sales agent)
Purpose: find businesses, write and send cold emails with Claude, handle replies; local dashboard. Upstream: github.com/ethanplusai/harvey (commit in `docs\UPSTREAM.md`).
Run: `install\INSTALL.cmd` once; then `app\.venv\Scripts\harvey.exe dashboard` / `run` (or the .cmd files in `install\`).
Secrets (names only): see `secrets\SECRETS-CHECKLIST.md`. Needs Claude CLI login + one email provider. Master env file `secrets\.env`, copied to `app\.env`.
`app\` = untouched upstream clone with its own .git and its own large CLAUDE.md (read it before changing code). Layout/rules: `F:\Github Repos\projects\README.md`.

## Status / next step
- 2026-11-05 packaged: copy verified, installer tested in a temp copy (venv + pip install + import + tests). No real `.env` existed, so no keys are stored. Next: user adds Claude login + mailbox keys, runs `harvey train`.
