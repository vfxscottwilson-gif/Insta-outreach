# 05 Accounts and keys

Names only. This app has no secret values.

## Secret names
| Name | Used by | Where to get it |
|---|---|---|
| (none) | No tool needs an API key, token, password or login | n/a |

Checked: `app\` has no `.env` or `.env.example`, and the four scripts and `install\install.ps1` read no key variables. `secrets\` holds only `SECRETS-CHECKLIST.md` and `SECRETS-README.md`.

## Settings that are not secrets
| Name | Meaning |
|---|---|
| `CRAWL4AI_NO_CLOUD_NOTICE=1` | Hides a crawl4ai notice. The installer sets it for its own run. Optional when you run `site_leads.py` by hand |

## Accounts
| Service | Needed? | Why |
|---|---|---|
| Google, YouTube | No | Public pages only; do not log in |
| GitHub | Only for downloads (public releases, no sign-in) and, optionally, a future scheduled run on GitHub Actions | Free |
| Microsoft Store / winget | Only if Python is missing | Free |
| Lead bot (other project) | Reads your CSV files; its own keys live in its own project | Not part of this app |

## If you add a tool that needs a key
1. Write its NAME (never the value) in `secrets\SECRETS-CHECKLIST.md`.
2. Put the value in `secrets\.env` (the hub ignores `secrets\` in git).
3. Never paste a key into a guide, chat or commit.

## Legal note
Cold-email rules differ by country; see `docs\INTEGRATION.md` section 1. Scraping Google Maps and YouTube breaks their terms of service.
