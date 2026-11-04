# Tools manifest: Scraper Tools

Checked 2026-11-05 against the official GitHub releases API and PyPI (URLs below returned HTTP 200). `install\install.ps1` uses exactly these sources.

| Tool | Version here | Licence | What it is | Source (official) | Where it lives in `app\` |
|---|---|---|---|---|---|
| gosom google-maps-scraper | v1.18.1 | MIT | Google Maps listings to CSV (name, website, phone, emails) | https://github.com/gosom/google-maps-scraper | `gosom-google-maps-scraper\gmaps.exe` |
| yt-dlp | 2026.10.26 | Unlicense | YouTube search and channel facts (no API key) | https://github.com/yt-dlp/yt-dlp | `yt-dlp\yt-dlp.exe` (+ `yt_leads.ps1` wrapper) |
| scrapetube | 2.6.0 | MIT | YouTube channel search with subscriber text (no API key) | https://pypi.org/project/scrapetube/ | `scrapetube\.venv` + `test_scrapetube.py` |
| crawl4ai | 0.9.5 | Apache-2.0 (per upstream README; PyPI metadata field is blank) | Website crawler: emails and social links | https://github.com/unclecode/crawl4ai | `crawl4ai\.venv` + `site_leads.py` |

Detected versions: `yt-dlp.exe --version` printed 2026.10.26; gmaps.exe version taken from the release file name it was downloaded as (1.18.1); scrapetube and crawl4ai from the `.dist-info` folders in each venv (2.6.0 and 0.9.5). Python in the venvs: 3.12.10.

## Re-download / reinstall (the installer does all of this; manual steps if it fails)

### 1. gosom gmaps.exe (stable release URL: the installer downloads it)
1. Open PowerShell in the `app\gosom-google-maps-scraper` folder.
2. Download the pinned release:
```
Invoke-WebRequest "https://github.com/gosom/google-maps-scraper/releases/download/v1.18.1/google_maps_scraper-1.18.1-windows-amd64.exe" -OutFile gmaps.exe
```
3. Expected size: 61,168,128 bytes (about 58 MB). SHA-256 of the copy on this PC (upstream publishes no checksum, so this only detects a changed or damaged file, it is not an upstream proof): `c124fab30f12e4aae25ef52f38eb2bea5422ece708b3171ca0f34be56cf7848f`
```
Get-FileHash gmaps.exe -Algorithm SHA256
```
4. Other platforms on the same release page: `-linux-amd64`, `-darwin-amd64`. Newer versions: https://github.com/gosom/google-maps-scraper/releases (change the version number in the URL; test with 1 query first).
5. First start downloads its own Chromium (Playwright). Not run during packaging (see Not verified).

### 2. yt-dlp.exe (stable "latest" URL: the installer downloads and verifies it)
1. Open PowerShell in `app\yt-dlp`.
```
Invoke-WebRequest "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe" -OutFile yt-dlp.exe
```
2. Verify against the official checksum list:
```
(Invoke-WebRequest "https://github.com/yt-dlp/yt-dlp/releases/latest/download/SHA2-256SUMS").Content -split "`n" | Select-String "yt-dlp.exe"
```
```
Get-FileHash yt-dlp.exe -Algorithm SHA256
```
The two hashes must match. For the version on this PC (2026.10.26) the hash is `f5389d3698ecde4ef06f4e6b1ce0294fe9ac1396228c8990b8d3416d6d177a7d` (copy of the official list is in `app\yt-dlp\SHA2-256SUMS`).
3. Update later: `yt-dlp.exe -U`. YouTube changes often, so an old yt-dlp is the first suspect if it stops working.

### 3. scrapetube (PyPI, pinned)
```
python -m venv app\scrapetube\.venv
```
```
app\scrapetube\.venv\Scripts\python.exe -m pip install scrapetube==2.6.0
```
Test: `app\scrapetube\.venv\Scripts\python.exe app\scrapetube\test_scrapetube.py` (needs internet; writes `sample_channels.json` next to the script).

### 4. crawl4ai (PyPI, pinned; needs Python 3.10+)
```
python -m venv app\crawl4ai\.venv
```
```
app\crawl4ai\.venv\Scripts\python.exe -m pip install crawl4ai==0.9.5
```
```
app\crawl4ai\.venv\Scripts\crawl4ai-setup.exe
```
The last command downloads Chromium (large, can be slow). Test: `app\crawl4ai\.venv\Scripts\python.exe app\crawl4ai\site_leads.py https://example.com` (set `CRAWL4AI_NO_CLOUD_NOTICE=1` to hide a notice). Upstream install docs: https://docs.crawl4ai.com/core/installation/

## Not installed on purpose
theHarvester and instaloader (low value, ToS risk). reacher / check-if-email-exists v0.11.11: no Windows binary, needs outbound port 25 (see `INTEGRATION.md`).

## Not verified
- gmaps.exe was never executed (an earlier session's safety check blocked it). Run it once yourself with 1 query: command in `INTEGRATION.md` section 1.
- Download URLs verified by HTTP 200 on the real URLs; the full 61 MB gosom download and yt-dlp download are exercised by the installer test (result in `proof\`).
