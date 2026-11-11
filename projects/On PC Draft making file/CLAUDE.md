# Email Draft Generator

**Purpose:** local cold-email draft generator (sheet in, Email/Name/Subject/Body/Follow-up 1-4 out). Rules are in the auto-memory file `feedback_email_framing_v2.md` and in `config/`.
**Run:** `python app\run.py --input X.xlsx --out Y.xlsx` (see START-HERE.md). Tests: `python tests\test_all.py`.
**Secrets:** none.
**Status / next step (2026-11-11):** v2 hardened after a full audit. 40/40 tests pass (tests/test_all.py 12, test_errors.py 14, test_v2.py 14). Verified on the real YT and restaurant sheets (300 rows each). Ollama is still not installed, so the model path is untested end to end. Next: user installs Ollama, runs `--check`, pilots 20 rows, reviews templates. Small niche packs (saas, ecommerce, real estate, showroom, generic) still exceed the 15% line-share cap.
