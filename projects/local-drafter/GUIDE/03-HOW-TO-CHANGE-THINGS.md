# 03 How to change things

| I want to... | Do this |
|---|---|
| Change what the AI is told | Edit `app\rules.md` |
| Change enforced limits (word range, banned words, subject length, opt-out line) | Edit `app\config.yaml` |
| Change sample wording, sign-offs, niche angles, fallback drafts | Edit `app\templates.yaml` (if broken, run `git checkout templates.yaml` inside `app\`) |
| Switch to Google Sheet mode | In `config.yaml` set `INPUT_MODE: sheet`, `INPUT_SHEET`, `INPUT_TAB`, `OUTPUT_MODE: sheet` |
| Use a different model | `ollama pull <model>`, then set `MODEL: <model>` in `config.yaml` |
| Fix a doubled sign-off or opt-out | `SIGN_OFF_MODE: none` or `INCLUDE_OPT_OUT: false` in `config.yaml` |
| Refresh `app\` from the original build | Copy `D:\All Automations Records\Local Draft File\local-drafter` over `app\` (skip `.venv`), then run the tests |

Full detail: `app\START_HERE.md` section 11.
