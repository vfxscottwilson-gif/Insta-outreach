# 00 Start here: set up local-drafter on a PC

## A. Install
1. Copy the whole `local-drafter` folder (with `secrets\`) to the new PC.
2. Double-click `install\INSTALL.cmd`. Click **Yes** if Windows asks.
3. When asked "Download the AI model qwen3:8b now? (about 5.2 GB)", type `y`. Press Enter to skip and do it later with `ollama pull qwen3:8b`.
4. Expected: a CHECKLIST with OK / SKIP / WARN lines and `242 passed`. FAIL lines point to `04-TROUBLESHOOTING.md`.

## B. Keys
1. Only needed for Google Sheet mode: the Google service-account key and an optional YouTube key. Steps: `05-ACCOUNTS-AND-KEYS.md` and `secrets\SECRETS-CHECKLIST.md`.
2. File mode (CSV/XLSX) needs no key. You can start with the sample data.

## C. Open the app
1. Double-click **Local Drafter** on the Desktop (or `app\run.bat`). A black window opens and runs.
2. First test everything. In PowerShell run:
```
app\run.bat --check
```
You should see PASS lines, including "100% of the model is in GPU memory".
