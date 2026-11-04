# 01 Roadmap: done, open, next

Status date: 2026-11-05. "Tested" means a real run with saved output (see `proof\` and the `sample_*` files in `app\`).

## Done
| Item | Evidence |
|---|---|
| yt-dlp installed; `yt_leads.ps1` wrapper works | `app\yt-dlp\sample_yt_leads.csv`, `sample_search.jsonl`, `sample_channel.json` |
| scrapetube 2.6.0 installed and tested | `app\scrapetube\sample_channels.json` (20 rows) |
| crawl4ai 0.9.5 installed and tested | `app\crawl4ai\sample_site_crawl.json` |
| gosom `gmaps.exe` v1.18.1 downloaded (58 MB) | file present; `install.ps1 -Check` reports it OK |
| One-click installer restores programs, venvs and Chromium | `proof\installer-test-2026-11-05.txt` |
| yt-dlp download is verified against the official SHA2-256SUMS | installer code. The proof file shows the first test run FAILED this check because of a parsing bug; it passed after the fix |
| Folder is portable (copy folder, run INSTALL) | tested in a temporary copy (proof file) |

## Open (honest list)
| Item | Why it is open |
|---|---|
| `gmaps.exe` never executed | An earlier safety check blocked running it. The 36 CSV columns in `docs\INTEGRATION.md` come from the upstream README, not a real run |
| Lead yield estimates (for example 150 to 500 emailed leads a day) | Estimates only, not measured. The one measured fact: a 12-result YouTube test gave 1 channel inside the subscriber range |
| No scheduling | Ideas only (GitHub Actions, Windows Task Scheduler) in `docs\INTEGRATION.md`; nothing is set up |
| Not connected to the lead bot importer | The lead bot owns the importer. Column aliases it should accept are at the end of `docs\INTEGRATION.md`; not checked against the importer code |
| Scripts are test-grade | `site_leads.py` and `test_scrapetube.py` have no error handling, no batch mode and fixed output names (see `03-HOW-TO-CHANGE-THINGS.md`) |
| `app\` git repo | Own git; hub-level commit of the packaged copy is pending (see `PROGRESS.md`) |

## Next, in order
1. Run `gmaps.exe` with 1 query (`00-START-HERE.md` step C4). Check `out.csv` has the columns listed in `docs\INTEGRATION.md`. Save a copy to `proof\`.
2. If good, run 3 queries; then change section 1 of `docs\INTEGRATION.md` from UNTESTED to TESTED.
3. Agree with the lead bot owner which columns it imports. Then add a small combine-and-dedupe step (dedupe on website domain, then phone, as suggested in INTEGRATION.md).
4. Only after step 3: schedule a small daily run and watch for Google blocks before raising volume.
5. Later, optional: email verification with reacher. It needs a VPS because outbound port 25 is blocked on most home and GitHub Actions networks.

## Not planned
instaloader and theHarvester (low value, terms-of-service risk). Anything that needs a login.

## Legal reminder
Scraping Google Maps and YouTube breaks their terms of service; IP blocks are likely. Cold-email rules differ by country; read `docs\INTEGRATION.md` section 1 before any mass send.
