# 03 How to change things (sheet-organizer)

Settings are environment variables: GitHub repo Secrets/Variables for the daily run, `secrets\.env` for runs on this PC. After any change, test first (section 8).

## 1. Settings table
| Want | Setting | Default |
|---|---|---|
| Name of the tab you paste into | Variable `INBOX_TAB` | `Inbox`, else the first non-robot tab |
| Notes handled per run | `RUN_LIMIT` | 150 |
| Minutes before the run stops | `MAX_RUN_MIN` | 35 |
| Time zone for dates and stamps | `TIMEZONE` | `Asia/Karachi` |
| Test mode (writes nothing) | `DRY_RUN` = `yes` (manual run input `dry_run`) | `no` |
| Figma board | `FIGMA_TOKEN` (secret), `FIGMA_FILE` (link or key) | off |
| Figma: only one page | `FIGMA_PAGE` | all pages |
| Figma: which items | `FIGMA_NODE_TYPES` | `STICKY,TEXT,SHAPE_WITH_TEXT` |
| Figma comment after sorting | `FIGMA_COMMENT` = `yes` | off |

Extra notes above `RUN_LIMIT` wait for the next day; the free AI tiers cap at roughly 150 notes a run.

## 2. Schedule
Edit `app\.github\workflows\organize.yml`, line `- cron: "0 2 * * *"` (UTC; 02:00 UTC = 07:00 Pakistan). Upload the file to GitHub. Manual run: Actions > "Organize my sheet" > Run workflow (set `dry_run` = `yes` to test).

## 3. Change how notes are understood (the prompt)
Open `app\organizer.py`:
- `SYSTEM` = the instructions to the AI (what counts as problem/task/achievement/idea/resource, field rules, "never invent"). Edit the text, keep the JSON format line at the end unchanged.
- `KIND_ALIAS` = words the AI may use for a type (bug -> problem, todo -> task, ...). Add yours there.
- `REPORT_SYSTEM` = the monthly report prompt (80-140 words, plain text).
- Upload the changed file to GitHub for the daily run to use it.

## 4. Change the sheet layout (tabs, columns, dropdowns)
- `TABS` in `organizer.py` defines each filing tab: name, ID prefix, header list, title column and dropdown values (for example `Status` and `Priority` choices).
- To add a column: add its name to that tab's header list. Existing sheets get the new column on the right automatically (columns are found by name; missing ones are added). To use it, also set it in `make_row()` (new rows) or leave it for manual typing.
- To add a status value: add it to the dropdown list in `TABS` AND to `norm_status()`, or the code will reset it.
- Do not rename robot tab names by hand; the bot would create a new empty one.
- You may move columns around and edit Status / Priority / Owner / Due Date by hand in filing tabs. Do not edit `Attention Needed` or `Monthly Summary` (rebuilt every run).

## 5. Change when something needs attention
`build_attention()` in `organizer.py`: the 7-day "due soon" window, the 14-day "forgotten" age and the 7-day "unsolved problem" age are plain numbers there. The title-match threshold for "same item" is `SIMILAR = 0.84` (higher = stricter, fewer merges).

## 6. Add or change AI keys
1. GitHub > Settings > Secrets and variables > Actions: set `GEMINI_API_KEY`, `GROQ_API_KEY` and/or `OPENROUTER_API_KEY`. Several keys of one provider: separate with commas.
2. No model names needed. To force a model add Variable `GEMINI_MODEL` / `GROQ_MODEL` / `OPENROUTER_MODEL`.
3. A new provider needs code: add it to the list `spec` in `llm_from_env()`, a rank function next to `rank_gemini`, and a call function like `_openai_call` (works for OpenAI-compatible APIs).

## 7. Figma
1. Create a personal access token with scope `file_content:read` (add `file_comments:write` for comments).
2. Set the secret `FIGMA_TOKEN` and the Variable `FIGMA_FILE`.
3. Run once with `dry_run` = `yes` and look for `Figma: N text/sticky items read.` N = 0 means wrong scope, link or `FIGMA_PAGE`.

## 8. Test after a change
1. Put 5-10 notes in the Inbox.
2. Test run (writes nothing; this PC's `run.cmd` defaults to a test run):
```
install\run.cmd organizer.py
```
3. For a real run of 10 notes, set `DRY_RUN=no` and `RUN_LIMIT=10` in `secrets\.env`, then run the same command.
4. Check `Review Needed`, `_Log` (one line per run) and the filing tabs.
