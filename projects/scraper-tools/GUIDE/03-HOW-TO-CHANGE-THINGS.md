# 03 How to change things

Recipes with exact files and settings. Run commands from the `scraper-tools` folder in PowerShell. Files in `app\` are the tools' own scripts: edit them only when no other session is building there, and note `app\` has its own git (commit there, not in the hub).

## Run settings (no file edits)

### Find more or fewer YouTube channels
1. Raise `-Max` (videos searched; default 30) and widen `-MinSubs` / `-MaxSubs` (defaults 5000 / 500000).
```
powershell -ExecutionPolicy Bypass -File app\yt-dlp\yt_leads.ps1 -Query "realtor vlog" -Max 50 -MinSubs 1000 -MaxSubs 1000000 -Out realtors.csv
```
2. Use a different `-Out` name each run so you do not overwrite the previous CSV.

### Slow down to avoid blocks
1. yt-dlp wrapper: `-DelayMs 4000` (default 2000, waits between channels).
```
powershell -ExecutionPolicy Bypass -File app\yt-dlp\yt_leads.ps1 -Query "gym tour" -DelayMs 4000 -Out gym.csv
```
2. gmaps: add `-c 1` (one at a time) to the command.

### Google Maps variations (flags from the upstream README, not run here)
| Want | Add to the gmaps command |
|---|---|
| More results per query | `-depth 10` |
| Emails from websites | `-email` |
| JSON instead of CSV | `-json` |
| Faster, fewer fields, no email | `-fast-mode` |
| Search around a point | `-geo "30.27,-97.74" -radius 5000` |
| Stop when idle | `-exit-on-inactivity 3m` |
Add more lines to `queries.txt` for more searches, for example `independent real estate agency in Leeds UK`. See all flags: run `app\gosom-google-maps-scraper\gmaps.exe -h`.

### Crawl many websites
`site_leads.py` takes one URL. Use a loop (it overwrites its JSON each time, so read the screen output or copy the file):
```
foreach ($u in Get-Content urls.txt) { app\crawl4ai\.venv\Scripts\python.exe app\crawl4ai\site_leads.py $u }
```

## Edit a script

### Change the scrapetube search phrase or count
1. Open `app\scrapetube\test_scrapetube.py` in Notepad.
2. Change `"gym owner vlog"` and `limit=20` (also the number in `islice(..., 20)`).
3. Run it:
```
app\scrapetube\.venv\Scripts\python.exe app\scrapetube\test_scrapetube.py
```

### Change which pages site_leads.py reads
In `app\crawl4ai\site_leads.py` the line `for u in [url, url.rstrip('/')+'/contact']:` is the page list. Add for example `url.rstrip('/')+'/about'`.

### Change the output file name of the Python scripts
The names `sample_site_crawl.json` and `sample_channels.json` are written in the last lines of each script (`json.dump(... open("..."))`). Edit that text.

## Installer settings (`install\install.ps1`, top of file)
| Want | Edit |
|---|---|
| Newer gosom | `$GmapsVer = '1.18.1'` to the new version (the download URL uses it). Delete `app\gosom-google-maps-scraper\gmaps.exe`, run `INSTALL.cmd`. Test with 1 query. Update `docs\TOOLS-MANIFEST.md`. The step label still says v1.18.1 (cosmetic) |
| Other scrapetube / crawl4ai | `$ScrapetubeVer` / `$Crawl4aiVer`. Delete that tool's `.venv` folder, run `INSTALL.cmd` |
| Redo the Chromium setup | Delete `app\crawl4ai\.setup-done`, run `INSTALL.cmd` |
| Update yt-dlp | The installer downloads "latest" only when the file is missing. To update an existing one: |
```
app\yt-dlp\yt-dlp.exe -U
```

## Add a new tool
1. Put it in a new folder under `app\`, for example `app\mytool\`.
2. Add install steps to `install\install.ps1` (use `Run-Step` so `-Check` stays a dry run) and a row to `docs\TOOLS-MANIFEST.md`.
3. Add its binaries/venvs to `app\.gitignore`.
4. Test `install\install.ps1 -Check`, then update `docs\INTEGRATION.md` and `02-ARCHITECTURE.md`.

## Back up
```
powershell -ExecutionPolicy Bypass -File backups\backup.ps1
```
Writes `backups\scraper-folder-DATE.zip` (no `.venv`; the installer rebuilds those). Add `-DryRun` to preview.
