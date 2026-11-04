# local-drafter (packaged app)
Purpose: local-LLM cold-email body drafter (Ollama qwen3:8b). Reads a leads sheet, writes the Ready to Send tab; never sends. Hub rules: `F:\Github Repos\projects\README.md`. Code + its own CLAUDE.md: `app\`.
Run: `app\run.bat --check` | `--dry-run --limit 5` | `--test-handoff` | `--backend mock` (no model). Tests: `app\.venv\Scripts\python -m pytest -q` (242).
Install: `install\INSTALL.cmd` (`-Check` previews).
Secrets NAMES (in `secrets\.env`): GOOGLE_SERVICE_ACCOUNT_FILE, YOUTUBE_API_KEY, AI_API_KEY.
Original is still edited by chat "local-drafter-build" (`D:\All Automations Records\Local Draft File\local-drafter`). To refresh: robocopy it into `app\` (exclude .venv).
## Status / next step
- 2026-11-05: packaged. Installer tested in a temp copy (-Check, then real install with -SkipModel): 242 tests pass. Ollama and the model were NOT installed by the test (Ollama is not on this PC's PATH).
- Next (needs the user): service-account JSON + share the sheet; `--test-handoff` with the Apps Script; `--dry-run --limit 5` on real leads.
