# Progress: Offline Data Scraping

Current version: **v1** (`Offline Data Scraping v1.zip`), 2026-11-11.

| Workstream | Session | Status | % | Last Update | Blocker | Next Step |
|---|---|---|---|---|---|---|
| Engine copy + 4 patches | Lead Bot Worldwide control chat | Done, verified (117 tests) | 100 | 2026-11-11 22:50 PKT | none | Sync future engine fixes across the 3 copies |
| Runner `app\run.py` + Settings | same | Done, verified (self-test + 2 pilots) | 100 | 2026-11-11 22:50 PKT | none | none |
| Excel output | same | Done, verified (1 lead, 75 columns, 2 tabs) | 100 | 2026-11-11 22:47 PKT | none | none |
| Local AI model | same | Code done, tested on a fake server only | 80 | 2026-11-11 22:31 PKT | No real model given yet | User gives model name; run pilot |
| Instagram 2-posts benchmark | same | Rule set (`MIN_POSTS_30D` = 2), not measurable without a key | 50 | 2026-11-11 | Needs `IG_ACCESS_TOKEN` or Apify token | User adds key to `secrets\.env` |
| Lead yield in free mode | same | Low: 1 lead from 325 businesses (pilot 2) | 40 | 2026-11-11 22:46 PKT | Free map has no review counts | Add Serper / Google Places key, or lower `MIN_ICP_SCORE` |
| Start Here guide, installer, docs | same | Done | 100 | 2026-11-11 22:50 PKT | none | none |
| Full (non-pilot) run | same | Not run | 0 | | Time (midnight stop) | User double-clicks `Run Scraper.cmd` |
| Windows scheduled task | same | Not created (steps in Start Here section 9) | 0 | | User's choice | User follows the 5 steps |
