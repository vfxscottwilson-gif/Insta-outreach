# 02 How it fits together
| Part | Where | Notes |
|---|---|---|
| Code (Python 3.12) | `app\src\` | `leadbot.py` main program; `enrich.py` reads websites; `quality.py`/`score.py` segments + ICP score; `insight.py` Lead Insight; `ai.py` AI key failover |
| Daily automation | GitHub Actions, `app\.github\workflows\run-lead-bot.yml`, workflow "Run AU Lead Bot", 19:00 and 07:00 UTC (`0 19 * * *`, `0 7 * * *`, about 6am/6pm Sydney), plus manual "Run workflow" | cloud (needs a GitHub repo) |
| Data | Google Sheets, written through the Google robot (service account) | cloud |
| Local test | `install\run-local.ps1` | this PC, writes CSV, no Google |
| Next step in the pipeline | `docs\CONTRACT.md` | the outreach bot reads the sheets; keep the contract stable |

Flow: the GitHub schedule starts the workflow, which runs the self-test and unit tests, then collects leads (free map data, websites, YouTube, optional APIs), scores them and appends rows to the sheet(s). Nothing is ever deleted or re-sorted.
