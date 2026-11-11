# Handoff: Email Draft Generator (2026-11-11)

Project folder: `F:\Github Repos\projects\On PC Draft making file\` (was `email-draft-generator`, renamed outside this chat).

## 1. Completed today
- Built a local draft generator: lead sheet in, one row per email out (Email, Name, Subject Line, Body, Follow-up 1 to 4).
- Version 1: template packs per niche, benchmark checker, crash-resume memory, Excel output (row height 21, Title Case headers, Arial 11).
- Hardening: friendly errors, locked output file, Ctrl+C, per-lead failure isolation.
- Version 2 after a full audit: settings mix honoured, safe niche detection (a `Channel` column means YouTube), junk email filter, strict first-name rules (`Team` when unknown), config validation, one-run lock, model circuit breaker, website read only when needed.

## 2. Progress and proof
- 40 of 40 tests pass: `tests\test_all.py` (12), `tests\test_errors.py` (14), `tests\test_v2.py` (14).
- Ran clean on 300 rows from each real sheet: YouTube 297 ready and 3 in review, restaurants 299 ready and 1 in review.
- Zip verified from a clean extraction.
- Last commit: `6a8c63b` (local only, nothing pushed).

## 3. Files
| Path | What |
|---|---|
| `START-HERE.md` | step-by-step guide |
| `config\settings.toml`, `config\templates.toml` | ratios, word ranges, every sentence per niche |
| `app\run.py`, `app\draft\*.py` | the program |
| `tests\*.py` | the three test suites |
| `install\INSTALL.cmd` | installs the libraries |
| `Email Draft Generator.zip` (also in Downloads) | current packaged code |
| `proof\` | test outputs and one-off patch scripts |

## 4. Left to do / pending
- Ollama is not installed, so the model path (niche detection, offence second opinion) is untested end to end.
- No pilot on real leads has been read by Khizar yet; templates are not yet approved by him.
- Small niche packs (software, e-commerce, real estate, showroom, generic) have few lines, so some lines exceed the 15% share cap.
- No independent reviewer has re-read the final wording.
- Release rule (global CLAUDE.md section 14) not yet applied: next delivery must be `Email Draft Generator v3.zip` (current zip counts as v2, move it to `Archive\`), with `Start Here.md` in Title Case and names without hyphens.
- Old output `Canada restaurants - Emails.xlsx` in Downloads uses a scrapped template. Do not send it.

## 5. Exact next step to resume
1. Khizar installs Ollama (ollama.com/download) and runs `ollama pull qwen3:4b`.
2. In the project folder: `python app\run.py --check`
3. Pilot: `python app\run.py --input tests\sample_leads.xlsx --out proof\pilot.xlsx --limit 20 --fresh`
4. Khizar reads `proof\pilot.xlsx` and says which template lines to change in `config\templates.toml`.
5. Apply his edits, run the three test suites, then deliver `Email Draft Generator v3.zip` under the section 14 rule.
