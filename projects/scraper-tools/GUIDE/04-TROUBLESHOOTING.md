# 04 Troubleshooting

How to read results first, then problems by where they appear. Messages below are copied from `install\install.ps1` and the scripts.

## How to read what happened
1. Installer: the black window ends with `===== CHECKLIST =====`. Each line starts `OK`, `SKIP`, `WARN`, `DRY` (check mode) or `FAIL`. If any FAIL, the last line is `N step(s) FAILED. See GUIDE\04-TROUBLESHOOTING.md.` and the exit code is 1. The window stays open ("pause") so you can read it. A past full output is in `proof\installer-test-2026-11-05.txt`.
2. There are no log files. To keep the installer output, run it in PowerShell and save it:
```
powershell -ExecutionPolicy Bypass -File install\install.ps1 *> install-log.txt
```
3. `yt_leads.ps1` hides yt-dlp's errors (`2>$null`). If it prints `0 channels written`, test yt-dlp directly (see below).
4. `site_leads.py` and `test_scrapetube.py` have no error handling: a failure shows a Python "Traceback"; the last line says what went wrong.
5. Quick health check, which downloads nothing:
```
powershell -ExecutionPolicy Bypass -File install\install.ps1 -Check
```

## Installer messages
| Message | Cause | Fix |
|---|---|---|
| `FAIL Folder layout app\ missing under ...` | Folder copied without `app\` | Copy the WHOLE `scraper-tools` folder again |
| `FAIL Python missing and winget not available; install Python 3.12 from python.org` | No Python and no winget | Install Python 3.12 from python.org (tick "Add to PATH"), or "App Installer" from the Microsoft Store, then re-run |
| `WARN Python installed but not on PATH yet: close this window and run INSTALL.cmd again` | New PATH is not seen by the open window | Close the window, run `INSTALL.cmd` again |
| `FAIL Python not available` (under a venv step) | Python missing at venv time | Fix Python as above, re-run |
| `FAIL Download yt-dlp.exe ... SHA-256 mismatch against official SHA2-256SUMS; file deleted` | Download damaged, or a proxy changed it, or the checksum list could not be matched | Re-run. If repeated, do the manual steps in `docs\TOOLS-MANIFEST.md` section 2. Do not use a file that fails the check |
| `FAIL Download ...` with a web error | No internet, firewall, or GitHub down | Check internet, re-run |
| `FAIL ... exit code N` | A command inside the step returned an error code | Scroll up in the window for the real message; re-run |
| `WARN Health: gmaps.exe size` | `gmaps.exe` under 50 MB: partial download | Delete `app\gosom-google-maps-scraper\gmaps.exe`, re-run |
| `SKIP crawl4ai-setup already done (delete crawl4ai\.setup-done to redo)` | Normal | Only delete the marker if the browser is broken |
| crawl4ai-setup very slow or looks stuck | Large Chromium download on a slow link (an earlier pip run stalled once) | Wait; else close and re-run. No marker is written until setup succeeds, so it retries |
| `[notice] A new release of pip is available` | Harmless | Ignore |

## Tool problems
| Problem | Cause | Fix |
|---|---|---|
| "running scripts is disabled on this system" | PowerShell policy | Start with `powershell -ExecutionPolicy Bypass -File ...` as in the guides |
| `yt_leads.ps1` prints `0 channels written` | yt-dlp outdated or blocked, or all channels outside the subscriber range | See "Test yt-dlp directly" below |
| `yt_leads.ps1` finds no emails | Most About texts have none (10 to 20 percent is the estimate, unmeasured). The hidden "business email" on the About tab is not collected | Expected |
| CSV opens with strange characters | File is UTF-8 | In Excel use Data > From Text/CSV and choose UTF-8 |
| `site_leads.py`: `IndexError: list index out of range` | No URL given | Add a URL, with `https://` |
| `site_leads.py` shows few or no emails; `/contact` blocked | Some sites block crawlers; script does not stop the run for a blocked page (not verified for every case) | Expected for some sites |
| `site_leads.py` socials contain `facebook.com/tr?` links | Tracking pixels | Filter them out in the next step |
| crawl4ai or scrapetube: `ModuleNotFoundError` | venv broken or wrong python used | Use the `python.exe` inside that tool's own `.venv\Scripts` folder (`app\scrapetube` or `app\crawl4ai`); or delete `.venv` and re-run `INSTALL.cmd` |
| `test_scrapetube.py` returns 0 or errors | YouTube changed or blocked | Retry later; try `pip install -U scrapetube` in its venv only if you accept leaving the pinned version (update `$ScrapetubeVer` too) |
| gmaps: Google blocks, CAPTCHA, empty CSV | IP flagged | Add `-c 1`, fewer queries, home IP not a cloud IP, wait. Scraping Google Maps breaks Google's terms |
| gmaps won't start or antivirus quarantines it | Unsigned download; upstream publishes no checksum | Check the URL in `docs\TOOLS-MANIFEST.md`; compare to the SHA-256 recorded there (detects change only); then allow it |
| Antivirus flags `yt-dlp.exe` | Unsigned program | The installer already verified its checksum; allow it |
| gmaps first start hangs | Downloading its Chromium | Wait. Not verified (never run here) |

## Test yt-dlp directly (when the wrapper says 0 channels)
1. Update yt-dlp (YouTube changes often; an old version is the first suspect):
```
app\yt-dlp\yt-dlp.exe -U
```
2. Search by hand:
```
app\yt-dlp\yt-dlp.exe "ytsearch3:gym owner vlog" --flat-playlist --dump-json
```
3. If JSON lines print, the search works and your `-MinSubs` / `-MaxSubs` filter removed every channel: widen it. If an error prints, that error is the real cause (the wrapper hides it).
