# 04 Troubleshooting

| Problem | Fix |
|---|---|
| `Cannot reach the model server at http://localhost:11434` | Start Ollama from the Start menu, or run `ollama serve` |
| `Model 'x' is not installed` | `ollama pull qwen3:8b` |
| Installer says Ollama or Python is "not on PATH yet" | Close the window, run `install\INSTALL.cmd` again |
| `No email column found` | Add an "Email" header or set `COLUMN_OVERRIDES` in `config.yaml` |
| `GOOGLE_SERVICE_ACCOUNT_FILE is not set` / file does not exist | Fix the path in `secrets\.env`, re-run the installer |
| `SpreadsheetNotFound`, `PERMISSION_DENIED`, `403` | Share the sheet with the service-account e-mail; enable Google Sheets API |
| `WorksheetNotFound` | `INPUT_TAB` must equal the tab name exactly |
| `Another run is already active` | Close the other window, or delete `app\.lock` if none is running |
| `x% of the model is on the GPU` | Close games and GPU apps, or pick a smaller model |
| Drafts 5-10x slower mid-run | GPU overheating: check fans / fan curve, clean dust, let it cool |
| Many drafts in Needs Review | Read the Log "Reason" column; a bigger model (`qwen3:14b`, 16 GB GPU) follows rules better |
| Tests fail after install | Run `app\.venv\Scripts\python -m pytest -q` and read the first failure |

More: `app\START_HERE.md` section 12.
