# local-drafter: Setup guide
For a non-expert on Windows 10. No secret values appear here.

## 1. What this app is
It reads your leads (a CSV/XLSX file, or a Google Sheet tab), finds public facts (YouTube, the lead's website), asks an AI model **on your own PC** to write each email body, checks every rule in code and writes `Email | First Name | Subject | Body` into the **Ready to Send** tab. Weak drafts go to **Needs Review**. It never sends email. Your Apps Script adds the greeting and signature and creates Gmail drafts.

## 2. Accounts needed
| Service | Why | Free? | Sign-up link |
|---|---|---|---|
| Google (Cloud project + Sheets) | Sheet mode only: a service account reads/writes your sheet | Yes | https://console.cloud.google.com |
| Google Apps Script (your existing one) | Turns Ready to Send rows into Gmail drafts | Yes | https://script.google.com |
| YouTube Data API key (optional) | Channel facts | Yes (free quota) | same Google Cloud project |
| Ollama | Runs the AI model locally (no account) | Yes | https://ollama.com |

File mode (CSV/XLSX in, CSV out) needs no account at all.

## 3. How it fits together
All local: a Python program (`app\`) plus an Ollama server on this PC using the GPU. Cloud: only Google Sheets (and YouTube if you add a key). No frontend, no hosted backend, no database.

## 4. Folder map
See `README.md`.

## 5. First-time install
1. Open the `install\` folder and double-click `INSTALL.cmd`. Click **Yes** if Windows asks.
2. To preview first, open PowerShell in `install\` and run:
```
.\install.ps1 -Check
```
You should see `[OK]`, `[DRY]` (would be done) and `[SKIP]` lines, no `FAIL`.
3. The real install adds Python 3.12 and Ollama if missing (via winget), then **asks before downloading the 5.2 GB model** `qwen3:8b`. Type `y` to download.
4. It creates `app\.venv`, installs the packages, asks for the optional keys (hidden typing, Enter = skip), makes a Desktop shortcut "Local Drafter" and runs the 242 tests. Expect `242 passed` and a CHECKLIST with no FAIL.
5. If a line says "not on PATH yet" (Python or Ollama was just installed), close the window and run `INSTALL.cmd` again.

## 6. Secrets
See `secrets\SECRETS-CHECKLIST.md` (names and steps). Real values live only in `secrets\.env`; the installer copies it to `app\.env`. After editing `secrets\.env`, re-run the installer to refresh.

## 7. Run it
1. Check everything (GPU, model, sheet access). Expect all PASS, including "100% of the model is in GPU memory":
```
app\run.bat --check
```
2. Safe trial with 5 leads:
```
app\run.bat --dry-run --limit 5
```
3. Test the Apps Script hand-off (writes 3 sample rows, see GUIDE\05):
```
app\run.bat --test-handoff
```
4. Real run on all leads:
```
app\run.bat
```
No model installed? Add `--backend mock` to rehearse with a fake AI (output is labelled MOCK).

## 8. How to change common things
| I want to... | Do this |
|---|---|
| Switch file/sheet input or output, sheet URL, tab names, model | Edit `app\config.yaml` (INPUT_MODE, INPUT_SHEET, INPUT_TAB, OUTPUT_MODE, MODEL, AI_BACKEND) |
| Change email wording or structures | Edit `app\templates.yaml` |
| Change the writing rules | Edit `app\rules.md` (also enforced in `app\drafter\validate.py`) |
| Use a bigger model (16 GB GPU) | `ollama pull qwen3:14b`, set `MODEL: qwen3:14b` |
| Use LM Studio | Set `AI_BACKEND: lmstudio` in `config.yaml` |

## 9. Troubleshooting
See `GUIDE\04-TROUBLESHOOTING.md`.

## 10. Move to a new PC
1. Copy the whole `local-drafter` folder (with `secrets\`).
2. Double-click `install\INSTALL.cmd`.
3. Check: open PowerShell in `install\` and run:
```
.\install.ps1 -Check
```
Every line should say OK, SKIP or DRY.
4. The AI model is not stored in the folder: the installer downloads it again (5.2 GB).
