# 04 Troubleshooting (ig-outreach)

## How to read what happened
1. **Run Log tab** in the Sheet: the last row has the time, counts (`synced, followups, new, requeued, private, review, no_handle, ai_notes`) and a `Problems` text. Start here.
2. **GitHub**: repo > Actions > "Daily outreach prep" > the run > step "Run". Last lines: `Done: ...` and `Problems: ...`.
3. **On this PC**: the window of `install\run.cmd main.py`.
4. **Stage / Notes columns** in `Outreach Log` say why a lead was not queued.

## Failure table
| You see | Cause | Fix |
|---|---|---|
| `MISSING SETTING: GOOGLE_SERVICE_ACCOUNT_JSON` | No Google key | Put the `.json` key file in `secrets\` (local) or set the secret (GitHub) |
| `MISSING SETTING: SHEET_ID` / `AI_API_KEYS` / `OFFER` | Empty setting | Fill it in `secrets\.env` or GitHub (OFFER is a Variable; it is needed for full runs, not sync-only) |
| Cannot open sheet / `APIError 403` / `404` | Sheet not shared, or wrong ID | Share (Editor) with the `client_email` inside the JSON; `SHEET_ID` is the part between `/d/` and `/edit` |
| `No accounts. Fill AGENT_ACCOUNTS or the Accounts tab.` | No account rows | Add one in `Accounts` or set `AGENT_ACCOUNTS=acc1,acc2` |
| `Leads tab: no column header containing 'Instagram' / 'Handle' found.` | Wrong tab or no such header | Rename the header to "Instagram Handle" or set `LEADS_TAB` |
| `No working AI key.` + notes | Keys wrong, expired or no credit | Fix `AI_API_KEYS`; notes list which provider failed (`key rejected (401)`, `out of credit`, `could not list models`) |
| `One key in AI_API_KEYS was not recognised` | Typo or extra characters | Re-copy the key (one per line, no quotes) |
| `All AI providers failed: ...` | Every key rate-limited or down | Wait and rerun; add a second provider |
| `Instagram token invalid/expired` | Meta token ran out | Make a new `IG_ACCESS_TOKEN`; the run continues without profile reading |
| `Instagram lookups rate-limited` | Meta limit | Nothing; the run continues, uses sheet Niche/Bio |
| Stage `Needs review`, Notes "No niche/bio" | Nothing to personalise from | Add Niche or Bio in the Leads tab |
| Stage `Needs review`, Notes "AI draft rejected: ..." | Message broke a rule 3 times (too long, spam word, number not in `CASE_STUDIES`, ...) | Write it by hand, or relax the rule in `rules.py` |
| Stage `Private - follow manually` | Personal/private account, nothing to read | Add Niche/Bio or write by hand |
| Follow-up note "write manually" | Follow-up draft rejected | Write by hand |
| Queue is empty | All accounts at cap (warm-up, paused, daily limit) or no new leads | Check `Phase (auto)` in `Accounts`; add leads |
| Rows "late, tomorrow is better" | Suggested time is past `SEND_WINDOW` | Send tomorrow or widen the window |
| `Sent At (auto)` / `Replied At (auto)` stay empty | Apps Script not installed | Sheet > Extensions > Apps Script > paste `apps_script.gs` > Save |
| Follow-ups go to someone who answered | `Replied? = Yes` not set (replies are not tracked automatically) | Set it as soon as someone replies |
| Instagram "Action blocked" | Too many messages, same network, or new account | Set that account to Paused for 3-7 days; reduce limit |
| Scheduled run stops | GitHub pauses scheduled workflows after 60 days without repo activity | Actions tab > re-enable |
| `python` not recognised after install | PATH not refreshed | Close the window, run `install\INSTALL.cmd` again |
| `send_assist.py`: "Chrome not found" | Chrome in a non-standard folder | Set env `CHROME_PATH` |

## Safe habits
- Never delete rows from `Outreach Log`; the bot uses them as its memory.
- Re-running the workflow is safe: today's already-queued items count toward the cap.
- Check the install any time (changes nothing):
```
powershell -ExecutionPolicy Bypass -File install\install.ps1 -Check
```
