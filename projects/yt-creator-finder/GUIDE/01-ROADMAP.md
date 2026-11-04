# 01 Roadmap: done, open, next (honest status, 2026-11-05)

Original plan: `docs\MASTER_PROMPT_yt-creator-client-finder.md`. Code status notes: `app\CLAUDE.md`. Sample output of a real run: `docs\SAMPLE_LEADS_live_2026-11-01.csv`.

## Done
| Item | Evidence |
|---|---|
| v1: YTJobs + YouTube search bot | git history in `app\` ("Add detailed setup guide" and earlier) |
| v2: Upwork API, Freelancer.com, LinkedIn Jobs, Remotive; no daily cap; CSV export for dry runs | commits "Add Upwork API, Freelancer.com, LinkedIn Jobs, Remotive; remove daily..." and "Add --export CSV for dry runs..." |
| Offline tests (22 per `app\CLAUDE.md`) | `app\tests\test_core.py`, `test_platforms.py`. The installer runs them. Not re-run in this packaging step (not verified now) |
| Live dry run: LinkedIn 28 + Freelancer 21 real jobs | `docs\SAMPLE_LEADS_live_2026-11-01.csv`, `app\CLAUDE.md` |
| Packaged in the hub: installer, guides, secrets checklist | `install\`, `GUIDE\`, `PROGRESS.md`. Installer `-Check` run 2026-11-05 |
| Safety rules in code | exit code 0 on data errors; no Upwork/Fiverr scraping; secrets masked in logs (`app\src\net.py`, `RunLog.mask`) |

## Open (needs you; nothing here happens by itself)
| Item | Why it is open | Blocker |
|---|---|---|
| Create PRIVATE GitHub repo, push `app\` | never done | your GitHub account |
| Add the 3 required secrets (GOOGLE_SA, SHEET_ID, YOUTUBE_API_KEYS) | never done | your Google account |
| First real write to a Google Sheet | the bot has NEVER run against a real Sheet | the two items above |
| Upwork approval + refresh token | Upwork path untested live | Upwork developer approval |
| Gemini / Groq AI path | not tested with real keys in this package; with no working key every row says `AI_Source = template` | optional keys |

## Next (in this order)
1. Make the YouTube key and the Google service account (`app\SETUP_GUIDE.md` Parts 2 and 3).
2. Local dry run with just the YouTube key (`00-START-HERE.md` section C).
3. Push to GitHub, add secrets, run the workflow with `dry_run` ticked and `max_leads` 10, read the log.
4. Pilot: run again with `dry_run` unticked and `max_leads` 10. Open the Sheet: the tabs should exist and at most 10 new rows appear.
5. Leave the schedule on. After 2-3 days read the `Run Log` and `Master Dashboard` tabs.
6. Tune `app\config.yaml` (`03-HOW-TO-CHANGE-THINGS.md`): minimum subscribers, niches, queries.
7. Later: Upwork approval, then add the three UPWORK_* secrets.

## Known limits (from the code, not guesses)
- DuckDuckGo web search is best effort and is often blocked from GitHub servers (`app\src\sources\web_search.py` raises `Blocked`). The other sources keep working.
- YouTube Data API: 10,000 units per key per day, reset at 00:00 US Pacific (about 12:00 or 13:00 Pakistan time). A search call costs 100 units. 1,500 units stay in reserve (`yt_units_reserve`).
- Upwork and Freelancer rows are pitched only on those platforms (their rules); such rows often have no email.
- Duplicate protection only knows what is in the Sheet (`sheets.seen`). If you delete rows, those leads can return.
- The blacklist is manual: add rows to the `Blacklist` tab.
- Each run stops itself after 40 minutes (`run_max_minutes`); the GitHub job limit is 45.
- `proof\installer-test-2026-11-05.txt` describes the scraper-tools installer (it mentions gosom and yt-dlp), not this app. No proof file exists yet for this app's installer or dry run.
