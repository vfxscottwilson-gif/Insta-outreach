# 01 Roadmap: done, open, next

Status date: 2026-11-05 (packaging day). Sources: `app\CLAUDE.md` (status section), `CLAUDE.md`, `docs\`. "Not verified" = could not be re-checked while writing this guide.

## Done
| Item | Evidence | Date |
|---|---|---|
| Build the drafter: CLI, column detection, research, local AI, validators, template fallback, sheet/CSV output, resume, lock | `app\drafter\` (13 modules) | 2026-11-03 |
| Automated tests | 242 pytest tests recorded as passing in `app\CLAUDE.md`, and by the installer test noted in `CLAUDE.md`; not re-run now | 2026-11-05 |
| Live test with `qwen3:8b` on the GPU | `--dry-run --limit 5` = 5/5 written (47 s); 16-draft benchmark = 15 written, 1 Needs Review (the model kept writing "saw") | 2026-11-03 |
| Package into `projects\local-drafter` with installer (`-Check`, `-Uninstall`, `-SkipModel`, `-SkipTests`, `-NonInteractive`) | `install\install.ps1`; real install tested in a temp copy with `-SkipModel` | 2026-11-05 |
| Guides 00-05 and SETUP-GUIDE | this folder | 2026-11-05 |

## Open (each needs YOU)
| # | Item | Why it matters | How |
|---|---|---|---|
| 1 | Google service account + share the sheet | Sheet mode cannot start without it | `05-ACCOUNTS-AND-KEYS.md` |
| 2 | Switch `config.yaml` to sheet mode | Out of the box it reads the fake sample file | `03-HOW-TO-CHANGE-THINGS.md` recipe 1 |
| 3 | Apps Script hand-off test | Proves the greeting, sign-off and signature each appear once | `app\run.bat --test-handoff`, then `05` section "Apps Script hand-off" |
| 4 | Pilot: `--dry-run --limit 5`, then `--limit 5`, then `--limit 50`, then all | Pilot before scale | `SETUP-GUIDE.md` section 7 |
| 5 | GPU heat | The RTX 2060 SUPER reached 88-91 C with fans reading 0% and NVIDIA thermal slowdown; drafts slowed from about 5 s to 20-140 s | Check fan curve, dust, airflow before long runs |
| 6 | Ollama and the model on the target PC | The packaging test used `-SkipModel`, so Ollama and `qwen3:8b` were NOT installed by that test | Run `install\INSTALL.cmd`, answer `y` |
| 7 | Where the Apps Script lives | Not recorded in this folder (not verified) | Ask the script owner, write it into `05` |
| 8 | Niches beyond the built-in ones | `templates.yaml` has angles for youtube, real_estate, food, auto, fitness, health and default; other niches use the default angle | `03` recipe 6 |
| 9 | Legal footer | Postal address and opt-out belong in the Apps Script signature, not here. Laws differ by country; this is not legal advice | Check your script's signature |

## Next (in this order)
1. Run the installer on the real PC and pull the model.
2. Create the service account, share the sheet, set sheet mode, run `--check` until input and output both PASS.
3. `--test-handoff`, inspect the 3 Gmail drafts, delete the 3 test rows and drafts.
4. Pilot batches (5, then 50), read the Log tab, then the full run.
5. Try a bigger model (`qwen3:14b`, needs about 16 GB of GPU memory) only if Needs Review stays high.

## Known limits (from the code)
- Writes columns A-D of Ready to Send only; the greeting and signature are not made here.
- The closing question always asks for "a clip or a video link" (`ASK_KEYWORDS`); other niches may want a different ask.
- `CONCURRENCY` is limited to 1 or 2; with one GPU keep 1.
- No sending, no follow-ups, no reply tracking: those belong to the rest of the cycle (`..\full-cycle-emails`).

## Files that define the spec
`docs\LOCAL_DRAFT_GENERATOR_PROMPT.md` (original spec), `docs\AMENDMENTS.md` (amendments win), `docs\UNIVERSAL_PREFLIGHT_PROMPT.md`, `app\PREFLIGHT.md` (decisions).
