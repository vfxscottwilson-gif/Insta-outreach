# 03 How to change things (recipes)

Three files control behaviour. All are in `app\`:
| File | Controls |
|---|---|
| `config.yaml` | every setting and every enforced limit |
| `rules.md` | the instructions the AI is given |
| `templates.yaml` | wording: sample offers, sign-offs, fallback subjects, niche angles, template fallback drafts |

Rules for editing: use Notepad or VS Code, keep the `KEY: value` layout, save, then test with `--dry-run --limit 5`. A wrong value never crashes `config.yaml`: you get a `WARNING:` line (`unknown setting X ignored`, `setting X has the wrong type`, `X=... outside a-b; using ...`) and the default is used. A broken `templates.yaml` does crash: restore it with (in PowerShell):
```
git -C "F:\Github Repos\projects\local-drafter\app" checkout templates.yaml
```
Do not edit anything else in `app\` (it is the packaged code).

## Recipe 1: switch from the sample file to your Google Sheet
1. Finish `05-ACCOUNTS-AND-KEYS.md` (service account, shared sheet).
2. In `app\config.yaml` set:
   - `INPUT_MODE: sheet`
   - `INPUT_SHEET: "https://docs.google.com/spreadsheets/d/..."` (URL or ID)
   - `INPUT_TAB: Leads` (exact tab name)
   - `OUTPUT_MODE: sheet`
   - `OUTPUT_SHEET: ""` (blank = same spreadsheet; or another URL)
3. Check:
```
app\run.bat --check
```
Input readable and output sheet opened must both say PASS. Missing tabs are created on the first real run.

## Recipe 2: use your own CSV/XLSX once, without editing config
```
app\run.bat --input "C:\path\leads.xlsx" --dry-run --limit 5
```
`--input` forces file mode for that run. Permanent: `INPUT_MODE: file` and `INPUT_FILE`.

## Recipe 3: the wrong column was picked
1. Read the `Detected columns:` line printed at the start (also the first Log row).
2. In `config.yaml` set `COLUMN_OVERRIDES`, using a header name or a column letter:
   `COLUMN_OVERRIDES: {email: "E-mail", org: "Business Name", niche: "D"}`
   Roles you may force: email, person, org, youtube, website, socials, social_handle, social_name, latest_video, niche, country, state, city, bio, notes.
3. A plain "Notes" column is never sent to the AI unless `SEND_NOTES_TO_AI: true`.

## Recipe 4: change the model or the AI program
| Goal | Do |
|---|---|
| Bigger model (about 16 GB GPU) | `ollama pull qwen3:14b`, then `MODEL: qwen3:14b` |
| Let the tool choose | `MODEL: ""` (picks by `MODEL_PREFERENCE`, skips names matching `MODEL_EXCLUDE`) |
| LM Studio | start its server, `AI_BACKEND: lmstudio` |
| Other OpenAI-style server | `AI_BACKEND: openai_compatible` and `BASE_URL: "http://localhost:8080/v1"`; key in `secrets\.env` as `AI_API_KEY` if required |
| Fake AI to rehearse | `app\run.bat --backend mock --dry-run --limit 5` |
| Model too slow or not fully on GPU | lower `NUM_CTX` (default 4096) or pick a smaller model |
After a model change run `app\run.bat --check`.

## Recipe 5: change what the emails say
| Want | Edit |
|---|---|
| Different instructions to the AI | `rules.md` |
| Longer or shorter email | `WORD_MIN`, `WORD_MAX`, `PART_WORDS`, `PART_BUDGET` in `config.yaml` (budget numbers should add up to about the middle of the range) |
| Banned words / verbs | `BANNED_WORDS`, `BANNED_VERBS` |
| Opt-out line | `OPT_OUT_LINE`, or `INCLUDE_OPT_OUT: false` |
| Sign-off | weights under `sign_offs` in `templates.yaml`; country boosts under `sign_off_country_weights`; `SIGN_OFF_MODE: none` removes it |
| Offer wording ("at no cost", "on me"...) | `sample_wording` in `templates.yaml`; the phrase list is `SAMPLE_PHRASES` and every key in `sample_wording` should be listed there |
| Subject | `SUBJECT_WORDS`, `SUBJECT_MAX_CHARS`; fallback subjects under `subjects` |
| Closing question | `fallback > ask` in `templates.yaml` and `ASK_KEYWORDS` in `config.yaml` (the question must contain one of them) |

## Recipe 6: add a niche
1. Open `templates.yaml`, section `niches`.
2. Copy an existing block. Set a new `key`, list `match` words (the first block whose word appears in the lead's niche text wins), then `pain` and `missed` sentences.
3. Keep each sentence under 20 words and phrase it as a possibility (could, can, often, many). They are validated like AI output.
4. Test: `app\run.bat --dry-run --limit 5`.

## Recipe 7: fix a doubled sign-off or opt-out in Gmail
After `app\run.bat --test-handoff`: sign-off twice = `SIGN_OFF_MODE: none`; opt-out twice = `INCLUDE_OPT_OUT: false`.

## Recipe 8: re-draft leads that are already done
Resume skips any address found in Ready to Send, Needs Review, the Log (written / needs review) or `app\state.json`. To redo one lead: delete its rows from those three tabs (or CSVs in `app\output\`) AND stop the run from using memory by deleting `app\state.json`. Rows that ended `failed` are retried automatically.

## Recipe 9: turn research off or limit it
| Goal | Do |
|---|---|
| Skip all lookups for one run | `--no-research` |
| No YouTube | `USE_YOUTUBE: false` (or leave `YOUTUBE_API_KEY` empty) |
| No websites | `USE_WEBSITE: false` |
| Fresh facts | delete `app\.cache\` or set `CACHE_DAYS: 0` |
| Allow `/c/name` YouTube URLs | `YT_ALLOW_SEARCH: true` (uses the 100 calls/day search bucket) |

## Recipe 10: stop or pace a run
- `--limit 50` stops after 50 drafts. Press Ctrl+C once to finish the current draft and save; twice to quit at once.
- `BATCH_SIZE` (default 10) is how many drafts are written together; a crash loses at most that many.
- Another settings file for a trial: `--config path\other.yaml`.

## Recipe 11: refresh `app\` from the original build
Copy `D:\All Automations Records\Local Draft File\local-drafter` over `app\` except `.venv`, `.env`, `state.json`, `output\`, `.cache\`; then run the tests with `app\.venv\Scripts\python -m pytest -q`. Only do this when no other session is editing there. Not verified: the original folder may have changed since packaging (commit `7ad603c`).
