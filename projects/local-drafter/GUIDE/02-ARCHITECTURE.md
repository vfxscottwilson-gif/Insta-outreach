# 02 Architecture

Everything is local except Google Sheets (and YouTube if a key is set).

| Part | What | Where |
|---|---|---|
| CLI | `draft_emails.py` | `app\` |
| Pipeline | run, `--check`, `--test-handoff` | `app\drafter\pipeline.py` |
| Input | Google Sheet tab (service account) or CSV/XLSX; columns auto-detected | `columns.py`, `sinks.py` |
| Facts | YouTube Data API + the lead's website, cached in `.cache\` | `research.py`, `facts.py` |
| Writing | Local LLM via Ollama (default), LM Studio or any OpenAI-compatible server; `mock` backend for tests | `ai.py` |
| Rules | Every rule checked in code; weak drafts get a template fallback or go to Needs Review | `validate.py`, `compose.py` |
| Output | `Ready to Send` (columns A-D only), `Log`, `Needs Review` tabs, or CSVs in `output\` | `sinks.py` |
| Settings | `config.yaml`, `templates.yaml`, `rules.md` | `app\` |
| Hand-off | Your Apps Script reads Ready to Send, adds "Hi {First Name}," + signature, creates Gmail drafts | Google (not in this folder) |

It never sends email. Backend = Python on this PC + Ollama (GPU). Frontend = none (command line). Database = none.
