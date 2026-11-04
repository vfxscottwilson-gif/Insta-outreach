# 02 Architecture: how local-drafter works inside

Everything runs on this PC except Google Sheets (sheet mode) and YouTube (only with a key) and the websites of your leads. Backend = Python in `app\` + Ollama (GPU). Frontend = none (command line, `run.bat`). Database = none (files). It never sends email.

## Data flow, step by step
1. **Start.** `app\draft_emails.py` reads the flags, loads `app\.env`, then `config.yaml` (bad values fall back to defaults with a `WARNING:` line), `templates.yaml` and `rules.md`. Then it calls `drafter\pipeline.py`.
2. **Lock.** `.lock` holds the PID of the running copy. A second run stops with exit code 3. A lock left by a crashed run (dead PID) is taken over.
3. **Input.** `INPUT_MODE: file` reads a CSV/XLSX (`INPUT_FILE`; CSV tries utf-8-sig, cp1252, latin-1); `sheet` opens `INPUT_SHEET` with the service account and reads tab `INPUT_TAB`. Google calls retry up to 6 times on 429/5xx with growing waits.
4. **Column detection** (`columns.py`). Finds the header row within the first 10 rows, maps roles (email, person, org, youtube, website, niche, country, bio...) by name, fuzzy match and by content (email-shaped values, links). Headers with price, quote, score, subscribers, views, revenue, budget, "my notes" are never read. `COLUMN_OVERRIDES` wins. No email column = stop with "No email column found". The mapping is printed and saved as the first Log row.
5. **Address planning** (`emails.py`, `pipeline.plan`). One cell may hold several addresses (`MULTI_EMAIL_MODE: split`); each becomes a task. Bad ones are logged `skipped` with a reason: no email, non-ASCII address, address too long, invalid format, file name, role or blocked address (`SKIP_EMAIL_PREFIXES`, `SKIP_EMAIL_DOMAINS`), generic address (only if `SKIP_GENERIC_EMAILS: true`). Addresses already in the output tabs/CSVs, the Log or `state.json` are skipped silently (resume).
6. **Research** (`research.py`). Per lead, never fatal: YouTube Data API (channel, latest `YT_RECENT` uploads; needs `YOUTUBE_API_KEY`) and the lead's website (home page plus an About page; honours robots.txt; text capped by `WEB_CHARS`/`ABOUT_CHARS`; sentences that look like instructions are dropped). Results are cached as JSON in `app\.cache\` for `CACHE_DAYS` days (14).
7. **First name** (`names.py`). From the name column, social handles, YouTube/website text, or a clean `first.last@` address. Titles and brand words are stripped. Else `FIRST_NAME_FALLBACK` ("Team"). Used only for the Apps Script greeting, never inside the body.
8. **Facts** (`facts.py`). Builds the LEAD DATA block, picks a niche angle (`templates.yaml > niches`) and a gap statement. No name from sheet, YouTube or website = `skipped` ("no channel/company name ..."). No video/bio/site data = LOW_DATA (the AI may only talk about the niche).
9. **Draft** (`ai.py`). Prompt = `rules.md` + LEAD DATA + a sentence plan + an example. Backends: `ollama` (`/api/chat`, thinking off, JSON schema), `lmstudio` and `openai_compatible` (`/v1`), `mock` (fake, for tests). Four JSON parts: opening, missing, offer, ask (+ subject).
10. **Validate and repair** (`validate.py`). Every rule is checked in code: word totals (`WORD_MIN`-`WORD_MAX`), per-part words, sentence length, banned words/verbs, hedge words, exact name, exact sample wording once, one question mark, no greeting, no repeat of recent openings (`NO_REPEAT_LAST`). Failing parts are re-asked up to `MAX_RETRIES` times with the exact problems listed.
11. **Fallback** (`compose.py`). Still failing = a template draft from `templates.yaml > fallback`, marked `needs review`. If even that fails the row is `failed`.
12. **Assemble.** Parts become the body; sign-off added when `SIGN_OFF_MODE: in_body` (weighted pick, country weights); opt-out line when `INCLUDE_OPT_OUT: true`. One last validation; any problem = `failed`.
13. **Sink** (`sinks.py`). Every `BATCH_SIZE` drafts: one write to **Ready to Send** (`Email | First Name | Subject | Body`, columns A-D only), **Needs Review** (adds `Problems`) and **Log**. Writes are RAW (no formulas run); cells are capped at 49,000 characters. File mode writes `Ready_to_Send.csv`, `Needs_Review.csv`, `Log.csv` in `OUTPUT_DIR`. Then `state.json` is saved (sheet first, state second, so a crash never makes duplicates).
14. **Finish.** Prints `Finished. written: N, ... Repairs: N.` and the YouTube units used.

## Modules (`app\drafter\`)
| File | Job |
|---|---|
| `config.py` | defaults, type/range checks, loads yaml and rules |
| `columns.py` | header row and column mapping, lead extraction |
| `emails.py` | split cells, validate addresses |
| `names.py` | first-name rules |
| `research.py` | YouTube client, website fetch, cache, robots.txt |
| `facts.py` | LEAD DATA, niche angle, gap, low-data flag |
| `ai.py` | backends, prompt, JSON parsing, repair loop, waiting when the server is down |
| `validate.py` | all rule checks (body and subject) |
| `compose.py` | sign-off, body assembly, subject, template fallback |
| `sinks.py` | file/sheet reading and writing, retry on Google errors |
| `state.py` | `state.json`, `.lock`, keep Windows awake |
| `pipeline.py` | the run loop, `--check`, `--test-handoff` |
| `textutil.py` | small text helpers |

## Files created at run time (all in `app\`, git-ignored)
| File | Meaning |
|---|---|
| `state.json` | per address status (written / needs review / skipped), recent openings, draft counter. Not written in `--dry-run`. Safe to delete only if the output tabs still hold the rows (they are re-read as the source of truth) |
| `.lock` | one run at a time |
| `.cache\` | YouTube and website answers, 14 days |
| `run.log` | timestamped log, no addresses or keys |
| `output\` | CSV results in file mode |

## Network calls
Ollama `http://localhost:11434` (`/api/tags`, `/api/chat`, `/api/ps`); LM Studio `http://localhost:1234/v1`; `www.googleapis.com/youtube/v3`; Google Sheets API; the lead websites. Nothing else.

## Hand-off
Your Apps Script (in Google, not in this folder) reads Ready to Send, adds "Hi {First Name}," and the signature, and makes the Gmail drafts.
