# 03 How to change things

| I want to... | Do this |
|---|---|
| Change what Harvey sells / who it targets | `harvey train <url>` again, or edit `app\harvey.local.yaml` |
| Change daily limits, quiet hours | `app\harvey.local.yaml` (keys documented in `app\harvey.yaml`) |
| Edit email style rules | `app\skills\email_rules.md` (created by training; gitignored upstream) |
| Switch email provider | Set `channels.email.provider` in `harvey.local.yaml` and fill that option in `secrets\.env` |
| Add or change a key | Edit `secrets\.env`, delete `app\.env`, run `INSTALL.cmd` |
| Pause everything | `harvey sending pause` (resume: `harvey sending resume`) |
| See status / usage | `harvey status`, `harvey usage` |
| Export prospects | `harvey export` |
| Run tests | `install\install.ps1 -RunTests`, or one file: `app\.venv\Scripts\python -m pytest tests\test_config.py` |
| Change Harvey's code | Read `app\CONTRIBUTING.md` first. This is a third-party clone: local code edits will conflict with upstream updates. |
