# 03 How to change things

1. Change settings (tab name, run limit, timezone, dry run): edit `secrets\.env` (this PC) and the GitHub variable of the same name (cloud).
2. Add an AI key: add it to `GEMINI_API_KEY`, `GROQ_API_KEY` or `OPENROUTER_API_KEY` (comma separated for several). No model names needed.
3. Change the daily time: edit the `cron` line in `app\.github\workflows\organize.yml`, then re-upload it to GitHub.
4. Tests: no automatic test suite. Run `.\run.cmd organizer.py` (dry run) and read the output.
5. Back up: run `powershell -ExecutionPolicy Bypass -File backups\backup.ps1`, and download the Sheet (`database\README.md`).
6. New PC: `SETUP-GUIDE.md` section 10.
