# 04 Troubleshooting

How to read a failure: (1) the last lines in the window, (2) `app\run.log` (same lines with times; no addresses or keys), (3) the **Log** tab (or `app\output\Log.csv`): columns `Row | Email | Result | Reason | Words | Retries | Model | Seconds | Tokens | Timestamp`. Messages below are copied from the code.

## Exit codes of `draft_emails.py`
| Code | Meaning |
|---|---|
| 0 | finished (or `--check` all without FAIL) |
| 1 | `--check` had a FAIL, or a setup problem with a message (no email column, file missing, bad sheet settings, model not installed at start) |
| 2 | the model server died during the run; progress up to the last batch is saved |
| 3 | `Another run is already active (PID n)` |
| 130 | you pressed Ctrl+C: `Stopped. Progress up to the last saved batch is kept` |

## A. Installer
| Message | Cause and fix |
|---|---|
| `[WARN] Python/Ollama installed but not on PATH yet: close this window and run INSTALL.cmd again` | Windows has not refreshed PATH. Close the window, run `install\INSTALL.cmd` again |
| `[FAIL] ... missing and winget not available` | Install "App Installer" from the Microsoft Store, run again, or install Python 3.12 / Ollama by hand |
| `[WARN] NVIDIA GPU nvidia-smi not found` | No NVIDIA driver: the model runs on the CPU (very slow). Install the driver or accept the speed |
| `[WARN] Python version ... needs 3.10 or newer` | Install Python 3.12 |
| `[FAIL] Folder layout app\draft_emails.py missing` | You copied only part of the folder. Copy the whole `local-drafter` folder |
| `[FAIL] pytest see output above` | Run `app\.venv\Scripts\python -m pytest -q` and read the first failure |
| `[SKIP] Model qwen3:8b ollama not available yet` | Ollama is not on PATH yet; see the first row |

## B. Model server and GPU
| Message | Cause and fix |
|---|---|
| `Cannot reach the model server at http://localhost:11434. Start Ollama ...` | Ollama is not running. Start menu > Ollama, or run `ollama serve` |
| `Model 'x' is not installed/loaded. Available: ...` | `ollama pull qwen3:8b`, or set `MODEL: ""` |
| `No suitable chat model found. Pull one first` | Nothing installed passes `MODEL_EXCLUDE`. Pull `qwen3:8b` |
| `AI_BACKEND openai_compatible needs BASE_URL` | Set `BASE_URL` in `config.yaml` |
| `The 10-token test call to the model failed: ...` | Server up but the model errors (out of memory, wrong name). Run `ollama run qwen3:8b` once to see the error |
| `x% of the model is on the GPU (slow: pick a smaller model or lower NUM_CTX)` / check shows `WARN` | Model does not fit in GPU memory. Close games and GPU apps, lower `NUM_CTX`, or use a smaller model |
| `Model server not responding; waiting 15s (n/20)` | Waits `AI_WAIT_RETRIES` x `AI_WAIT_SECONDS` (about 5 min), then `The model server stopped responding. Restart it and run again; progress is saved.` (exit 2). Restart Ollama, run again |
| Drafts suddenly 5-10x slower | GPU overheating (88-91 C seen on this PC): check fans and fan curve, clean dust, let it cool |

## C. Input and Google
| Message | Cause and fix |
|---|---|
| `Input file not found: <path>` | Fix `INPUT_FILE` (relative paths start in `app\`) |
| `No email column found. Add a header like 'Email', or set COLUMN_OVERRIDES` | Header not recognised and no column holds email-shaped values. Recipe 3 in `03` |
| `GOOGLE_SERVICE_ACCOUNT_FILE is not set in .env` | Name missing in `secrets\.env`. Add it, re-run the installer to copy it to `app\.env` |
| `The service-account file in .env does not exist: <file>` | Path wrong or file moved |
| `Set INPUT_SHEET (and/or OUTPUT_SHEET) in config.yaml` | Sheet mode with an empty sheet setting |
| `OUTPUT_MODE is sheet but no OUTPUT_SHEET (or INPUT_SHEET)` | Set one of them |
| `SpreadsheetNotFound`, `PERMISSION_DENIED`, `403` | Share the sheet with the service-account e-mail; enable the Google Sheets API |
| `WorksheetNotFound` | `INPUT_TAB` must equal the tab name exactly |
| `Warning: 'Ready to Send' row 1 is not [...]; new rows still go to A-D` | Header differs; harmless |
| `tab 'X' is missing (it will be created on the first real run)` | Seen in `--check` only |
| Google `429` | The tool retries 6 times with waits; if it still fails, wait a minute and run again |

## D. Lock, config and templates
| Message | Cause and fix |
|---|---|
| `Another run is already active (PID n)` | Close the other window. If none is running, delete `app\.lock` |
| `WARNING: unknown setting X ignored` / `has the wrong type` / `outside a-b` | Typo or bad value in `config.yaml`; the default is used |
| `config.yaml unreadable (...)` | YAML syntax error; defaults are used. Fix indentation and quotes |
| `templates.yaml is missing 'x'. Restore it from git` | `git -C "F:\Github Repos\projects\local-drafter\app" checkout templates.yaml` |

## E. Log tab: Result and Reason values
| Result | Reason (start of text) | Meaning and fix |
|---|---|---|
| mapping | `header row 1; email=...` | first row, which columns were used. Check it |
| skipped | `no email`, `non-ASCII address`, `address too long`, `invalid format`, `file name, not an address` | bad cell; fix the sheet |
| skipped | `role or blocked address` | prefix in `SKIP_EMAIL_PREFIXES` (noreply, postmaster...) or domain in `SKIP_EMAIL_DOMAINS`; edit those lists if wrong |
| skipped | `generic address (SKIP_GENERIC_EMAILS)` | set `SKIP_GENERIC_EMAILS: false` |
| skipped | `duplicate address in the sheet` | same address twice; only the first is drafted |
| skipped | `no channel/company name in the sheet, YouTube or website` | add a name column or a URL |
| needs review | `AI draft failed after n repairs, template used: ...` | the AI kept breaking the listed rules; the template draft is in Needs Review. Read the list, tune `rules.md`, or use a bigger model |
| failed | `no draft passed all checks (...)` | AI and template both failed validation; row is retried next run |
| failed | `final check: ...` or `body format: ...` | last validation of the assembled email failed; usually a template or setting conflict (for example word range vs part budgets) |
| failed | `unexpected <ErrorName>: ...` | a bug or odd data in that row; the run continues. Send the line to the builder |

Typical Needs Review messages (from `validate.py`): `do not say "x"`, `opening must contain the exact name "..."`, `the offer must contain the exact wording "..."`, `exactly one question mark ...`, `the question must ask them to reply with a clip or a video link`, `phrase the gap as a possibility`. A few Needs Review per 16 is normal (1 of 16 in the benchmark).

## F. YouTube and websites
| Message | Fix |
|---|---|
| `YouTube facts off (no YOUTUBE_API_KEY in .env)` | Informational. Add the key for channel facts |
| `YouTube API turned off for this run (HTTP 403: key or quota)` | Quota used (resets midnight Pacific) or wrong key. Drafts continue without YouTube |
| `row n: website lookup failed (...)` | That site blocked or timed out; the draft uses other facts |

## G. Still stuck
Run these and read the first failure:
```
app\run.bat --check
```
```
app\.venv\Scripts\python -m pytest -q
```
More detail: `app\START_HERE.md` sections 8 and 12.
