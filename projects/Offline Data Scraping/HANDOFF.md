# Handoff: Offline Data Scraping

Written 2026-11-11 about 22:50 PKT, ahead of the 12:00 a.m. PKT stop. Latest code: `Offline Data Scraping v1.zip` in this folder.

## Created
| Path | What |
|---|---|
| `Start Here.md` | Full walkthrough, flowchart, settings guide, audit, limits, troubleshooting |
| `Run Scraper.cmd`, `Pilot Test.cmd` | Double-click launchers |
| `install\INSTALL.cmd` | One-click install, `-Check` mode |
| `app\run.py` | Runner: Settings to engine, repeated passes, crash isolation, Excel export |
| `app\src\` | Lead Bot Worldwide v6 engine + 4 patches (`ai.py`, `keys.py`, `localsheet.py`, `leadbot.py`) |
| `app\tests\test_offline.py` | 3 tests for the local AI provider |
| `Settings\` | Targets, Niches (38), Benchmarks And Rules, Locations, Sheet Format |
| `docs\Niche Research.md`, `docs\Contract.md` | Niche evidence, sheet contract |
| `secrets\SECRETS-CHECKLIST.md` | Optional key names |
| `proof\Pilot Run 1.txt`, `proof\Pilot Run 2.txt` | Real run output |
| `CLAUDE.md`, `PROGRESS.md` | Project notes and tracker |

## Finished And Verified
- 117 unit tests pass, engine selftest passes, `run.py --check` passes, `INSTALL.cmd -Check` prints `INSTALL OK`.
- Pilot 2 (real internet, US): 325 businesses checked in 12.4 minutes, 1 lead saved, Excel built with tabs `All Leads` and `Boutique Hotels & Luxury Stays`, 75 columns, phone `(212) 703-2001` (no +1).
- Pilot 1: 150 restaurants checked, 0 leads, no crash.
- Local AI provider works against a fake OpenAI-compatible server.

## Not Done / Not Verified
- Local AI with a real model (no model name given, Ollama not found on PATH).
- Instagram "2 posts in 30 days": cannot be measured without `IG_ACCESS_TOKEN` + `IG_USER_ID` or `APIFY_API_TOKEN`. Leads show `?` and are kept.
- Full (non-pilot) run, multi-country run, state-filter run on live data (state logic is covered by the self-test only).
- Windows Task Scheduler task not created.
- openpyxl not yet scanned with SkillSpector or logged in `SKILLS-REGISTRY.md`.
- The three engine copies (this, `lead-bot-worldwide`, `lead-bot-au`) are not synced with the 4 patches.

## Known Issues Seen In The Pilot
- Yield is low in free mode (1 of 325). Main rejections: no website on the map listing (147), chain brand (51), ICP below 7 (44).
- The one lead is a hotel that belongs to a group and its email is a PR agency's: chain detection missed it because the map listing has no brand tag.
- Restaurants rarely reach ICP 7 without review counts.

## Exact Next Step
1. User puts the model name in `Settings\Benchmarks And Rules.csv` (`LOCAL_LLM_MODEL`) and double-clicks `Pilot Test.cmd`; expect `Local AI: on`.
2. User adds an Instagram token or Apify token and, ideally, a Serper or Google Places key to `secrets\.env`.
3. Double-click `Run Scraper.cmd` for the first full run; review `Output\United States Leads.xlsx` and `Output\Run Log.txt`.
