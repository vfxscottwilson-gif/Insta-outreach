# 03 How to change things

1. Change the offer, limits, accounts or window: edit the value in `secrets\.env` (this PC) and the GitHub variable of the same name (cloud). Then run `.\run.cmd main.py --sync-only` from `install\`.
2. Change a message angle: edit `app\styles.py`, then run a small test (3 to 10 leads).
3. Add an AI key: add it to `AI_API_KEYS`, comma separated. No model name needed.
4. Pause an account: Sheet, Accounts tab, Status = Paused.
5. Tests: there is no automatic test suite. Run `main.py --sync-only` and read the Sheet's Run Log.
6. Back up: run `powershell -ExecutionPolicy Bypass -File backups\backup.ps1`, and download the Sheet (see `database\README.md`).
7. New PC: `SETUP-GUIDE.md` section 10.
