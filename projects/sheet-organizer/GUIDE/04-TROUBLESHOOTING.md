# 04 Troubleshooting (sheet-organizer)

## How to read what happened
1. **Sheet, tab `_Log`**: one line per run: `new, updated, duplicates, review, waiting, attention items` and, if relevant, `stopped: ...`.
2. **GitHub**: repo > Actions > "Organize my sheet" > the run > step `python organizer.py`. It prints lines like `Gemini: 2 key(s), 4 model(s) found live`, `New notes found: N (processing M now).` and the final `DONE. ...`. A RED run means no AI worked at all.
3. **On this PC**: the window of `install\run.cmd organizer.py`.
4. Notes it could not understand are in `Review Needed` with a reason.

## Failure table
| You see | Cause | Fix |
|---|---|---|
| `GOOGLE_SA secret is missing or is not the full service-account JSON file content` | Empty or cut JSON | Paste the whole file including the braces. Locally keep the `.json` in `secrets\` |
| `SHEET_ID secret is missing` | Not set | Set it (the part of the sheet URL between `/d/` and `/edit`) |
| `Cannot open the sheet (APIError 403/404)` | Wrong ID, Google Sheets API not enabled, or sheet not shared | Enable the Sheets API in Google Cloud; share the sheet with the service-account `client_email` as Editor |
| `No AI key found. Add at least one secret...` | No AI key set | Add `GEMINI_API_KEY`, `GROQ_API_KEY` or `OPENROUTER_API_KEY` |
| `a key was rejected (invalid, disabled or out of credit); switched off` | 401/402/403 from that provider | Make a new key; the others keep working |
| `a model is unavailable; trying the next one` | Model retired or not allowed | Normal; or remove a wrong `*_MODEL` variable |
| `quota hit repeatedly, one key/model switched off for this run` | Free daily limit | Wait a day, or add a second key / provider |
| `all AI providers failed or are out of quota` | Every key dead or spent | Finished notes are saved; check keys; the rest are retried tomorrow |
| `INBOX_TAB 'X' not found. Tabs in the file: ...` | Name differs | Fix the spelling (exact) or delete the variable |
| `INBOX_TAB 'X' is one of the robot's own tabs` | Chose a robot tab | Name your paste tab something else |
| `Tab 'Inbox' not found: using the first tab ...` | No tab called Inbox | Fine, or rename your tab to `Inbox` |
| `Figma skipped: token rejected or lacks 'file_content:read' scope or file access` | Token problem | New token with the scope; make sure the account can open the file |
| `Figma skipped: file key not found` | Wrong link | Fix `FIGMA_FILE` |
| `Figma: 0 text/sticky items read` | Wrong page/types/scope | Check `FIGMA_PAGE`, `FIGMA_NODE_TYPES` |
| `Dashboard rebuild failed (...)` | Sheets hiccup | Data is safe; rerun |
| Note is in `Review Needed` | AI could not classify it | Rewrite the note and paste it again in the Inbox |
| Same note filed twice | Different wording defeats the title match (84%) | Merge by hand. Never delete `_Ledger` |
| Everything re-filed | `_Ledger` was deleted | Duplicates are mostly caught by title; restore `_Ledger` from version history (File > Version history) |
| Notes not picked up | They are in a robot tab, or `RUN_LIMIT` reached | Paste into the Inbox; leftovers show as `waiting` in `_Log` |
| Wrong due dates | Ambiguous date format | Use `dd/mm/yyyy` (read day-first) or `YYYY-MM-DD`; check `TIMEZONE` |
| Daily run stopped appearing | GitHub pauses scheduled workflows after 60 days without repo activity | Actions tab > re-enable, press Run workflow now and then |
| `python` not recognised after install | PATH not refreshed | Close the window, run `install\INSTALL.cmd` again |

## Safe habits
- You may clear the Inbox any time; the ledger remembers what was filed.
- Never edit `Attention Needed` / `Monthly Summary`; they are rebuilt each run.
- Check the install (changes nothing):
```
powershell -ExecutionPolicy Bypass -File install\install.ps1 -Check
```
