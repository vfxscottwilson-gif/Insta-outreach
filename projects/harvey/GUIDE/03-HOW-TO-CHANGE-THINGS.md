# 03 How to change things

Rules: never edit files in `app\` that git tracks (e.g. `app\harvey.yaml`, `app\prompts\*`): they are upstream. Put your changes in `app\harvey.local.yaml` (wins over `harvey.yaml`) and `secrets\.env`. Where recipes use `harvey`, open PowerShell in `app\` and activate first:
```
.\.venv\Scripts\Activate.ps1
```
(Without activating, use `.\.venv\Scripts\harvey.exe`.) Setting names are documented line by line in `app\harvey.yaml`. Commands below were checked in `app\harvey\cli.py` (not run).

## Quick table
| I want to... | Do this |
|---|---|
| Change what I sell / who I target | Recipe 1 |
| Change daily limits, quiet hours, timezone | Recipe 2 |
| Change email style | Recipe 3 |
| Switch email provider | Recipe 4 |
| Add or change a key | Recipe 5 |
| Stop or restart sending | Recipe 6 |
| Approve or reject emails | Recipe 7 |
| Find more businesses / use a paid source | Recipe 8 |
| Block a company or person | Recipe 9 |
| Get the list without sending | Recipe 10 |
| Back up or restore the database | Recipe 11 |
| Update Harvey | Recipe 12 |

## 1. Product and targeting
1. Re-learn from a website (keeps your other settings; updates product, targeting, company):
```
harvey train https://your-company.com
```
2. Or edit `app\harvey.local.yaml`: `product:`, `icp:` (`industries`, `titles`, `company_size`, `geography`, `hiring_signals`), `persona:`.
3. To make Harvey look in specific cities, add `icp.geo_coordinates` (format shown in `app\CLAUDE.md` Step 5).

## 2. Limits, quiet hours, timezone
Edit `app\harvey.local.yaml`:
- `channels.email.max_daily_sends` (default 50)
- `channels.email.max_bounce_rate` (default 0.05; all sending stops above it)
- `channels.email.warmup.start_date` (`YYYY-MM-DD`), `min_days`, `start_sends`, `daily_increase`
- `usage.max_daily_claude_percent` (default 80), `usage.heartbeat_interval_minutes` (default 15)
- `usage.quiet_hours.start`, `.end`, `.timezone` (default `America/New_York`: change to yours)
- `channels.email.send_window` (office hours per recipient time zone; the block is commented out in `app\harvey.yaml`, copy it and remove the `#` marks)
A running Harvey picks up the approval/autopilot switch next cycle; for other settings stop (Ctrl+C) and start `harvey run` again (not verified for every key).

## 3. Email style
1. Quick: edit nothing, just look at the rules in `app\skills\email_frameworks.md` and `app\prompts\writer.md`.
2. Your own shape: create `app\skills\email_rules.md` (gitignored upstream), then in `harvey.local.yaml` add:
```
writer:
  email_rules: "skills/email_rules.md"
```
3. The send gate still rejects emails over 220 words or with more than one link (comment in `app\harvey.yaml`).
4. Other text lives in `app\skills\` (product, objections, offers) and `app\prompts\` (`writer.md`, `handler.md`, `scout.md`, `system.md`). If you edit tracked files, `git pull` later may conflict.

## 4. Switch email provider
1. In `harvey.local.yaml` set `channels.email.provider` to `gmail`, `microsoft`, `smtp` or `instantly`.
2. Fill that option's key names in `secrets\.env` (list in `05-ACCOUNTS-AND-KEYS.md`), then do Recipe 5.
3. Authorize once: `harvey gmail auth` or `harvey microsoft auth`. Test:
```
harvey gmail test
```
```
harvey microsoft test
```
Microsoft setup details: `app\docs\microsoft365.md`.

## 5. Add or change a key
1. Edit `secrets\.env` in Notepad (this is the master).
2. Delete `app\.env`.
3. Double-click `install\INSTALL.cmd` (it copies `secrets\.env` to `app\.env`). Stop and restart Harvey afterwards.
4. Warmup key shortcut: `harvey trulyinbox connect` (asks for the key in the terminal). Check with `harvey trulyinbox`.

## 6. Pause / resume sending
```
harvey sending pause
```
```
harvey sending resume
```
```
harvey sending status
```
`resume` also resets the bounce counter (`cli.py`, `cmd_sending`). To approve-before-send again, set `channels.email.require_approval: true` or use dashboard Settings, Sending.

## 7. Outbox
```
harvey outbox
```
Then `harvey outbox --approve <ID>`, `--approve-all`, or `--reject <ID>` (use the ID printed by the first command). The dashboard Outbox tab does the same.

## 8. Discovery
```
harvey discover --providers
```
```
harvey discover --estimate
```
Paid example (spend cap 2 dollars; needs `DATAFORSEO_LOGIN` and `DATAFORSEO_PASSWORD`):
```
harvey discover --provider dataforseo_listings --max-spend 2.00
```
Other options: `--city`, `--depth`, `--limit`, `--preset yc|hiring|accelerator|funding`. Always run `--estimate` first.

## 9. Do-not-contact
In `harvey.local.yaml` (it wins over `harvey.yaml`):
```
compliance:
  do_not_contact:
    - "competitor.example"
    - "jane@acme.example"
```
An entry is an address or a domain (covers subdomains). Checked at send time, even for already approved emails.

## 10. List-building only
```
harvey export
```
Writes `prospects.csv` (verified or risky emails only). `harvey export --all` is the raw list; `harvey companies` writes a company register CSV to `data\exports\`. Set `channels.email.enabled: false` to be sure nothing sends.

## 11. Database
File: `app\data\harvey.db`. Stop Harvey first. Restore from the snapshot, per `database\README.md`. Backup: run `backups\backup.ps1` (dated zip of the folder).

## 12. Update and tests
Update: `git -C app pull origin main`, delete `app\.venv`, re-run `install\INSTALL.cmd` (see `docs\UPSTREAM.md`). Tests: one file only, the full suite is very long:
```
.\.venv\Scripts\python.exe -m pytest tests\test_config.py
```
Changing Harvey's code: read `app\CONTRIBUTING.md` first; it is a third-party clone.
