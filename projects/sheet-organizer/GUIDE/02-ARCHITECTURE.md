# 02 Architecture: how sheet-organizer works inside

One Python file, `app\organizer.py` (about 1100 lines), run daily by GitHub Actions (`app\.github\workflows\organize.yml`) or by hand on this PC. No server, no database: your Google Sheet is the storage. All names below were checked against the code.

## 1. Data flow (one run, in order)
1. **Settings** (`main()`): `RUN_LIMIT` (default 150 notes), `MAX_RUN_MIN` (default 35 minutes), `DRY_RUN`. The AI client is built FIRST (`llm_from_env()`), so a missing key fails early with `No AI key found`.
2. **Connect** (`connect()`): `GOOGLE_SA` (the full JSON text) and `SHEET_ID`. Clear exit messages if either is missing or the sheet cannot be opened.
3. **Tabs** (`ensure_tabs()`): finds the paste tab (`INBOX_TAB`; else a tab called `Inbox`; else the first non-robot tab; else it creates an empty `Inbox`). Creates every missing robot tab with its header, dropdowns and formatting and puts them in a sensible order. It refuses an `INBOX_TAB` name that is one of the robot's own tabs.
4. **Read notes** (`read_inbox`, `read_figma`): every non-empty Inbox row becomes one note (cells joined with ` | `, cut at 3000 characters; a first row such as "Inbox" or "Paste here" is treated as a header). If `FIGMA_TOKEN` and `FIGMA_FILE` are set, sticky notes and text from the board are added (types in `FIGMA_NODE_TYPES`, default `STICKY,TEXT,SHAPE_WITH_TEXT`; optional single page `FIGMA_PAGE`). Figma problems never stop the run (`Figma skipped: ...`).
5. **Skip known notes**: each note gets a fingerprint (hash of the normalised text). Hashes already in `_Ledger`, or repeated in this run, are dropped. Only the first `RUN_LIMIT` new notes are processed; the rest wait for the next run.
6. **Classify** (`classify_batch`, AI): 6 notes per call (`BATCH`). The AI returns JSON entries with a type (problem, task, achievement, idea, resource; aliases like bug, todo, win, link are mapped), title, details, solution, status, priority, owner, due date, category, tags, url. One note may become several entries. The prompt marks notes as untrusted data and forbids inventing facts. Missing answers are retried one note at a time.
7. **Validate in code** (`clean_entry`, `norm_status`, `norm_priority`, `parse_date`): status, priority and dates are forced into the allowed values (dates are read day-first, "Friday" resolved with TODAY in `TIMEZONE`). Bad or empty answers go to `Review Needed`.
8. **File** (`route()`): looks for a similar existing title (84% likeness, `SIMILAR`; for resources the same link). Found: a problem/task row is UPDATED if the new note adds a solution/status (`apply_update`), otherwise counted as a duplicate. Not found: a new row with the next ID (`PS-`, `TK-`, `AC-`, `NT-`, `RS-` prefixes). Every note is written to `_Ledger`.
9. **Save**: after each batch the tabs, `Review Needed` and finally `_Ledger` are written (ledger last, so a crash can only cause a harmless re-check). With `DRY_RUN=yes` nothing is written.
10. **Dashboards** (rebuilt every run, by code): `Attention Needed` and `Monthly Summary`. The written "Manager's Report" per month (latest 2 months only) is created by the AI from your real numbers and only when the numbers changed (`Data Signature`).
11. **Finish**: appends a line to `_Log`, prints `DONE. new X, updated X, duplicates X, review X, waiting X, attention X. AI calls: ...`, optionally posts a Figma comment (`FIGMA_COMMENT=yes`). If no AI worked at all it exits with an error so the GitHub run shows red.

## 2. Sheet tabs and columns
| Tab | Columns |
|---|---|
| Inbox (yours) | one note per row, anything goes |
| `Tasks & Progress` | ID, Date Added, Month, Task, Status (Not Started/In Progress/Blocked/Done), Priority (High/Medium/Low), Owner, Due Date, Category, Notes, Source |
| `Problems & Solutions` | ID, Date Added, Month, Category, Problem, Solution, Status (Open/In Progress/Solved), Priority, Owner, Due Date, Tags, Source, Notes |
| `Achievements` | ID, Date Added, Month, Achievement, Category, Impact, Source |
| `Ideas & Notes` | ID, Date Added, Month, Title, Details, Category, Tags, Source |
| `Resources & Links` | ID, Date Added, Month, Title, Link, Category, Description, Source |
| `Attention Needed` | Level, Type, ID, Item, Status, Owner, Due Date, Days, Why it needs attention (rebuilt each run) |
| `Monthly Summary` | Month, Problems, Solved, Still Open, Tasks, Done, In Progress, Blocked, Overdue, Completion %, Achievements, Ideas, Resources, Data Signature, Manager's Report (rebuilt each run) |
| `Review Needed` | Time, Source, Raw Text, Reason |
| `_Ledger` | Hash, Processed, Source, Routed To, Item ID, Preview. The memory. Never delete. |
| `_Log` | Time, Level, Message (one line per run) |

Attention levels (`build_attention`): 1 Overdue, 2 Blocked, 3 Due within 7 days, 4 Open 14+ days with no due date ("Forgotten?"), 5 Problem with no solution after 7 days. Maximum 500 rows.

## 3. AI provider rotation (`class LLM`)
- Providers: Gemini (`GEMINI_API_KEY`), Groq (`GROQ_API_KEY`), OpenRouter (`OPENROUTER_API_KEY`). Several keys per provider: comma separated. Old names `GEMINI_KEY`, `GROQ_KEY`, `OPENROUTER_KEY` also work.
- Models are DISCOVERED live per provider (`discover()`, top 4 ranked). If listing fails, a built-in fallback list is used (`FALLBACK_MODELS`). Optional override variables `GEMINI_MODEL`, `GROQ_MODEL`, `OPENROUTER_MODEL` (comma separated) are tried first.
- Every key x model is a "combo"; the first ready combo in order Gemini, Groq, OpenRouter is used. Errors (`classify()`): 429 -> cool down 60 s, 3 strikes switch it off for the run; 401/402/403 -> that key is switched off; 400/404 -> that model is switched off; 5xx -> wait 20 s, 4 strikes switch it off. Nothing left -> `all AI providers failed or are out of quota`; finished notes are already saved, the rest wait for tomorrow.

## 4. Other facts
- Concurrency lock in the workflow (`organizer`) stops two runs overlapping; job limit 45 minutes.
- Everything is written as plain text (no formulas), so pasted text cannot run as a spreadsheet formula.
- The script never prints note text or keys.
- Figma's web API can only read boards and post comments; it cannot arrange the canvas.
