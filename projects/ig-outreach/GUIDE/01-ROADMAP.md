# 01 Roadmap (ig-outreach)

## Where it stands
v3 code is finished (v2 bugs fixed: daily-limit overrun, lost queue rows, header overwrite, 429 crashes). It needs your accounts and a small live test before scaling.

## Steps
| # | Step | Who | Blocker | Done |
|---|---|---|---|---|
| 1 | Create a Google service account; share the Sheet (Editor) with its `client_email` | Owner | Google login | [ ] |
| 2 | Add AI keys to `AI_API_KEYS` (2+ providers, one per line) | Owner | Provider accounts | [ ] |
| 3 | Paste `app\apps_script.gs` into the Sheet (Extensions > Apps Script) | Owner | none | [ ] |
| 4 | Upload `app\` to a PRIVATE GitHub repo; add secrets and variables (list in `05`) | Owner | GitHub login | [ ] |
| 5 | Fill the `Accounts` tab (Start Date per account); accounts under 14 days old send nothing, under 28 days max 5 a day | Owner | account ages | [ ] |
| 6 | Test: 3-10 leads, 1 account (Start Date older than 28 days), run the workflow, check all tabs and `Run Log` | Owner | steps 1-5 | [ ] |
| 7 | Run `send_assist.py` once for a real send; set up `profiles.json` first | Owner | Chrome profiles | [ ] |
| 8 | Add real `CASE_STUDIES` (real results only) | Owner | real results | [ ] |
| 9 | 20-lead test, then scale; after 100 sends compare reply rate by `Style`, delete losing angles in `styles.py` | Owner | step 6 | [ ] |
| 10 | Optional: Instagram profile reading (Meta developer app) | Owner | Meta setup | [ ] |

## Known limits (by design)
- Reply tracking is manual (`Replied?`).
- No auto-sender: it would break Instagram's terms and risk every account.
- Same network for many accounts risks linked bans; stagger or use separate networks.
- Expect low DM reply rates (2-5% is the guide's own estimate, not measured here).

## How to know it works
`Today Queue` fills each morning, `Outreach Log` Stage moves Queued -> Message sent -> Follow-up N, and `Run Log` shows no `CRASH`.
