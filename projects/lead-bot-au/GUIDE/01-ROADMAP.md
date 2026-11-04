# 01 Roadmap: from zero to the daily run

Owner: **You** = needs your login or decision. **Installer** = the script does it. **Claude** = an assistant on this PC can do it. "Done" = verified on 2026-11-05 from files; "Not verified" = needs your accounts.

## Status now

| Step | State |
|---|---|
| Bot code v5 (append-only sheet, Lead Insight, Stats, one secret per key, 8 AU columns) | done; the worldwide twin's `app\CLAUDE.md` records 60 self-test checks and 92 unit tests (same code; not re-run here because system Python lacks the packages, the installer's venv has them) |
| Packaged in this standard folder, installer, guides | done |
| `install\install.ps1 -Check` | passes; only `app\.venv` and `secrets\.env` show MISSING until the first install |
| Google robot key file present in `secrets\` | present (contents not opened) |
| GitHub repo, secrets, first green run | **not verified** (no git remote is set in `app\`) |
| Google Sheet created and shared | **not verified** |

## Steps

| # | Step | Owner | Time | Done when |
|---|---|---|---|---|
| 1 | Install on this PC: double-click `install\INSTALL.cmd`; skip all key prompts for now | You (click) + Installer | 5-10 min | `install.ps1 -Check` shows only `OK` |
| 2 | Local trial: Desktop shortcut "Lead Bot AU (local test)" | You | 5 min | CSV files appear in `app\local_sheet\` |
| 3 | Google robot: Google Cloud Console, new project, enable **Google Sheets API** and **Google Drive API**, Service Accounts, create, Keys, Add key, JSON. (A key file may already be in `secrets\`.) Copy its `client_email` | You | 10 min | you have the .json and the robot email |
| 4 | Create ONE Google Sheet (sheets.new), name it for example `Leads - Australia`, share it with the robot email as **Editor**, copy its id (between `/d/` and `/edit`). Leave it empty | You | 5 min | id noted |
| 5 | Create a NEW GitHub repository (not the worldwide one) and push `app\` (commands in `SETUP-GUIDE.md` section 6). Make it PUBLIC: no secrets are stored in the repo, and two daily runs of six jobs need more free minutes than a private repo has (per the workflow comment) | You | 10 min | code visible on GitHub |
| 6 | Add GitHub secrets (Settings > Secrets and variables > Actions): `GOOGLE_SA` (whole .json text) and `SHEET_ID_AU_ONLY` | You | 5 min | both listed (values hidden) |
| 7 | First run: Actions > "Run AU Lead Bot" > Run workflow. The six collect jobs run one at a time, so allow a few hours. Read each log: registration report, then `Done: ...` | You | hours (waiting) | green ticks; `Run Log` rows; new rows in the niche tabs |
| 8 | Register the free ABN Lookup GUID (abr.business.gov.au, Web Services) and add secret `ABN_GUID`; add `GEMINI_API_KEY_1`; re-run | You | 15 min | ABN columns and Lead Insight text fill in |
| 9 | Review leads, tune `Rules` / `Niches` / `Locations` in the sheet (`GUIDE\03`) | You (+ Claude) | ongoing | leads look right after 2-3 days |
| 10 | Connect the outreach bot using `docs\CONTRACT.md` | Claude | separate project | outreach bot reads the sheet by header name |

## Known limits (from the worldwide `app\CLAUDE.md` and `app\AU_EDITION.md`)

| Limit | What it means |
|---|---|
| Free AI limits | a 429 gives fact-only insights |
| Decision-maker / personal email coverage | only about 20-35% on free sources |
| Free map data | many OpenStreetMap businesses have no website listed, so they are skipped by default (`REQUIRE_WEBSITE_OSM`) |
| ABN | without `ABN_GUID` only ABNs printed on the website are filled |
| `Seen` tab | nears Google's 10M-cell limit in about a year; the one-sheet design fills faster than per-country sheets |

More ideas: `docs\HIGH_QUALITY_LEADS_SPEC.md`, `docs\FREE_TOOLS_RESEARCH.md`, `app\AU_EDITION.md`.
