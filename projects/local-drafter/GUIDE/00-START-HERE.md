# 00 Start here: install local-drafter and do your first run

Plain English. Windows 10. One step at a time. `local-drafter` reads a list of leads, asks an AI model that runs on YOUR PC to write each email body, checks the rules in code and saves the result. **It never sends email.**

## What you need first
| Thing | Needed? | Notes |
|---|---|---|
| Windows 10 + internet | yes | internet is used only by the installer, Google Sheets and the optional YouTube lookups |
| NVIDIA graphics card | strongly advised | without one the model runs on the CPU and is very slow (the installer warns if `nvidia-smi` is missing) |
| About 6 GB free disk | yes | the AI model `qwen3:8b` is about 5.2 GB |
| Google account | only for Google Sheet mode | file mode (CSV/XLSX in, CSV out) needs no account |

## A. Install (once per PC)
1. Copy the whole `local-drafter` folder to the PC (keep `secrets\` inside it).
2. Optional preview, changes nothing. Open PowerShell and run:
```
powershell -ExecutionPolicy Bypass -File "F:\Github Repos\projects\local-drafter\install\install.ps1" -Check
```
   Expect lines starting `[OK]`, `[DRY]`, `[SKIP]` and the last line `FAIL lines: 0`. A `[DRY]` line only means "this would be done".
3. Double-click `install\INSTALL.cmd`. Click **Yes** if Windows asks.
4. It installs Python 3.12 and Ollama with winget if they are missing. If it prints "not on PATH yet", close the window and double-click `INSTALL.cmd` again.
5. When asked "Download the AI model qwen3:8b now? It is about 5.2 GB. (y/N)" type `y` and press Enter. Pressing Enter alone skips it; do it later with:
```
ollama pull qwen3:8b
```
6. It then asks, with hidden typing, for `YOUTUBE_API_KEY` and `AI_API_KEY` (press Enter to skip both) and, if there is no `.json` key in `secrets\`, for the path of your Google service-account key (Enter = skip). Nothing secret is printed. These questions only appear when `secrets\.env` does not exist yet.
7. At the end you should see `=== CHECKLIST ===` with OK / SKIP / WARN lines, a pytest result (the packaging notes record 242 tests passing; not re-run when this guide was written) and `FAIL lines: 0`. Any FAIL: see `04-TROUBLESHOOTING.md`.

What the installer created: `app\.venv` (Python packages), `secrets\.env` (copied to `app\.env`), and a Desktop shortcut **Local Drafter** that runs `app\run.bat`.

## B. First safe run (no Google, no model needed)
Out of the box `app\config.yaml` is in file mode and points at `samples/youtubers_clean.csv`, a fake list.
1. Open PowerShell and go to the app folder:
```
cd "F:\Github Repos\projects\local-drafter\app"
```
2. Rehearse with the fake AI (writes nothing):
```
.\run.bat --dry-run --limit 5 --backend mock
```
3. You should see: `Detected columns: header row 1; email=Email (C); ...`, then `AI: MOCK BACKEND (fake LLM for testing, not a real model)`, printed drafts (To, First Name, Subject, body) and `Finished. ... Repairs: ...`. Some sample rows are skipped on purpose (`role or blocked address`, `no valid email`).
4. `run.bat` ends with "Press any key" because of `pause`; press a key to close.

## C. First real check
1. Health check: model server, model, GPU, input, output.
```
.\run.bat --check
```
2. Good output has `PASS` lines: `model server reachable`, `10-token test call answered`, `100% of the model is in GPU memory`, `input readable: N rows`. `INFO`/`WARN` lines are explained in `04-TROUBLESHOOTING.md`. Exit code 1 means at least one `FAIL`.
3. Real drafts from the sample file with the real model, still writing nothing:
```
.\run.bat --dry-run --limit 5
```
Expect `AI: ollama, model qwen3:8b; 100% of the model is on the GPU.` and roughly 5-20 seconds per draft (measured 2026-11-03 on an RTX 2060 SUPER; speed on your PC: not verified).

## D. Careful with the Desktop shortcut
The shortcut and a plain `run.bat` start a FULL run over every lead in the configured input and WRITE results (CSV files in `app\output\` in file mode, or your Google Sheet tabs in sheet mode). Use the commands above first. The order for the first real use is in `SETUP-GUIDE.md` section 7.

## E. Where things go
| What | Where |
|---|---|
| Results (file mode) | `app\output\Ready_to_Send.csv`, `Needs_Review.csv`, `Log.csv` |
| Run log | `app\run.log` |
| Resume memory | `app\state.json` |
| Your keys | `secrets\.env` (names only in `05-ACCOUNTS-AND-KEYS.md`) |

Next: `01-ROADMAP.md` (what is done and open), `03-HOW-TO-CHANGE-THINGS.md` (settings).
