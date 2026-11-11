# Email Draft Generator

**Purpose:** local cold-email draft generator (sheet in, Email/Name/Subject/Body/Follow-up 1-4 out). Rules are in the auto-memory file `feedback_email_framing_v2.md` and in `config/`.
**Run:** `python app\run.py --input X.xlsx --out Y.xlsx` (see START-HERE.md). Tests: `python tests\test_all.py`.
**Secrets:** none.
**Status / next step (2026-11-11):** v1 built, 12/12 tests pass. Not yet tested with Ollama (not installed on this PC). Next: user installs Ollama, runs `--check`, pilots 20 rows on a real sheet with a Niche column, reviews drafts, then approves/edit templates. Smaller niche packs (saas, ecommerce, real estate, showroom, generic) have small pools, some lines exceed 15% share; extend `templates.toml` as needed.
