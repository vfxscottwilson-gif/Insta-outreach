# Lead dashboard: research evidence (checked 2026-11-04; NV = not verified)

Decision: custom Flask + SQLite + gspread app. No off-the-shelf tool meets all four needs (see table). Nothing in the decision depends on a paid price; paid-tier figures below are official-page, single-source.

## Dashboard tools (free self-host)
| Tool | $ for 5 users | Sheets | Assign/edit + write-back to Sheet | Row-level | One session / reset code | Gap |
|---|---|---|---|---|---|---|
| Metabase OSS | $0 (Pro $575/mo) | Cloud only; self-host needs DB copy | Editable tables Pro-only, no Sheets write | Pro | none / emailed link | best charts, no assign |
| NocoDB CE | $0 (Business $24/seat, Scale $45/seat) | CSV/Excel import only | edit yes, no Sheet write-back | Scale | none / needs SMTP | no Sheets link |
| Baserow | $0 core (Premium $10/user/mo) | none (Postgres sync only) | edit yes, no Sheet write-back | RBAC = Enterprise | none / SMTP | no Sheets link |
| Grafana OSS | $0 | read-only plugin | no | Enterprise | Enterprise only / SMTP | charts only |
| Looker Studio | $0 (SaaS) | native | no | NV | Google login only | charts only |
| Appsmith CE | $0 (Business $15/user) | native read/write | yes (you build UI) | Business | session limit likely Business (NV) / SMTP | no charts, you build all |
Common gap: every tool emails a reset LINK, none sends a CODE; none offers "new login signs out old" on free tier.

URLs: metabase.com/pricing, /docs/latest/{cloud/google-sheets, permissions/row-and-column-security, data-modeling/editable-tables, people-and-groups/managing, changing-session-expiration}; nocodb.com/pricing, nocodb.com/docs/{product-docs/sync, self-hosting/environment-variables}; baserow.io/pricing, /user-docs/{data-sync-in-baserow, permissions-overview}, /docs/installation%2Fconfiguration; grafana.com/docs/plugins/grafana-googlesheets-datasource/latest/, github.com/grafana/grafana/issues/33864; docs.cloud.google.com/looker/docs/studio/{what-you-need, connect-to-google-sheets}; appsmith.com/pricing, docs.appsmith.com/connect-data/reference/querying-google-sheets, github.com/appsmithorg/appsmith/issues/23134.

## Hosting
| Option | Cost | Gotcha |
|---|---|---|
| This Windows PC (localhost/LAN) | $0 | PC must be on |
| Cloudflare quick tunnel | $0, no account/domain | new random URL every start, no uptime guarantee |
| Cloudflare named tunnel | $0 (3P sources; CF page did not confirm) | needs a domain on Cloudflare |
| Tailscale Personal | $0, 6 users | pricing FAQ: non-commercial use only -> skip |
| Oracle Always Free | $0 | card required; ARM capacity errors reported 2026; docs say 2 OCPU/12 GB (3P say 4/24) |
| Render free | $0 | sleeps, ephemeral disk (SQLite lost), SMTP ports blocked -> skip |
| Fly.io | no free tier, ~$2.19/mo smallest | trial figure conflicts ($1/7 days official vs $5 3P) |
| Railway | free $1/mo credit or Hobby $5/mo | card required |
| PythonAnywhere free | $0, 1 app, must renew monthly | googleapis.com allowlisted (live test NV) |
| Hetzner CX23 | ~EUR 5.49-5.99/mo ex-VAT | conflict between official page and 3P; official page said "currently unavailable" |
| Contabo VPS | ~$4.40/mo on 24-month term (official) | 1-month price NV |

## Email for reset code (~10/day)
Gmail SMTP + app password: $0, 500/day (support.google.com/mail/answer/22839), needs 2-Step Verification. Brevo free 300/day (fallback). Resend 100/day needs own domain.

## Sheets API (developers.google.com/workspace/sheets/api/limits)
300 reads/min/project, 60/min/user; same for writes; 429 over quota, no daily cap. Google says exceeding quota "is planned to incur charges later in 2026". Per-user quota keys on the principal incl. service accounts, so a separate service account gets its own 60/min bucket (inferred from Cloud docs; Sheets page does not state it).

## Libraries (PyPI, 2026-11-04)
gspread 6.2.1 (May 2025; maintainers seeking help; CI tests Python 3.12), Flask 3.1.3, FastAPI 0.162.0, uvicorn 0.54.0. Python 3.12.10 installed here; none of these are installed yet (use a venv).

## Sheet layouts (from CONTRACT.md v5 + yt-creator-client-finder/sheets_manager.py)
- Lead bots: lead tab = row 1 has `Place Id` AND `Company Name`. Key cols: Niche, Group, Segment, ICP Score /10, Company Name, Country, Country Code, City, Website, emails, Status (New, Drafted, Contacted, Follow-up 1/2, Replied, Call booked, Client, Not interested, Do not contact), My Notes (user-owned, never write), Lead Added On (YYYY-MM-DD), Place Id. Append-only; unknown columns are ignored by the bots (outreach bot prefixes its own with "Outreach ").
- YT finder: tabs `YouTube_Video_Editing_Leads`, `YouTube_Thumbnail_Design_Leads`; key `Lead_ID`; Status New/Contacted/Replied/Call/Won/Lost/Do-Not-Contact; date `Found_At_PKT`; Country; Source_Platform; Score.
- Lead Added On gives free backfill of per-day counts; snapshots still needed for status history and removed rows.
- No local sample lead CSVs exist in the workspace (bots never ran with --local); real pilot needs a shared sheet, or a fixture I generate.
