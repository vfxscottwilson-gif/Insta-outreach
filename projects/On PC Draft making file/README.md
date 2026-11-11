# Email Draft Generator

Local tool: lead sheet in, one row per email out (first email plus four follow-ups), with benchmarks, crash-resume and an optional local model (Ollama).

Start with `START-HERE.md`.

| Path | What |
|---|---|
| `START-HERE.md` | step-by-step guide |
| `config\settings.toml` | ratios, word ranges, model, GPU guard |
| `config\templates.toml` | every sentence per niche (edit freely, then `--lint`) |
| `app\run.py`, `app\draft\` | the program |
| `install\INSTALL.cmd` | installs the Python libraries |
| `proof\` | test outputs and patch scripts |

40 tests: `python tests\test_all.py` (12 behaviour), `python tests\test_errors.py` (14 failure), `python tests\test_v2.py` (14 safeguards).
