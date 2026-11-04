# Lead bot → outreach bot: interface contract (v5)

This is the only thing the outreach (draft) bot may rely on. The lead bot keeps it stable. Any change gets a new
version line at the bottom.

## 1. Which Google Sheets

Each sheet id is its own GitHub secret. A missing secret means that sheet doesn't exist: skip it and don't fail.

| Edition | Secret | Sheet |
|---|---|---|
| Worldwide | `SHEET_ID_US` | United States leads (also holds `Master Dashboard` and `US Stats`) |
| Worldwide | `SHEET_ID_CA` | Canada |
| Worldwide | `SHEET_ID_GB` (alias `SHEET_ID_UK`) | United Kingdom |
| Worldwide | `SHEET_ID_AU` | Australia (worldwide edition) |
| Worldwide | `SHEET_ID_NZ` | New Zealand |
| Worldwide | `SHEET_ID_IE` | Ireland |
| Worldwide | `SHEET_ID_AE` | United Arab Emirates (optional) |
| Worldwide | `SHEET_ID_SA` | Saudi Arabia (optional) |
| Worldwide | `SHEET_ID_QA` | Qatar (optional) |
| Worldwide | `SHEET_ID_YOUTUBE` (alias `SHEET_ID_YT`) | YouTube creators, all countries |
| AU-only | `SHEET_ID_AU_ONLY` (fallback `SHEET_ID`) | Australia-only edition: one sheet |

- **Legacy single-sheet setups:** only `SHEET_ID` is set. Every niche tab is in that one sheet.
- **Value format:** the lead bot accepts either the bare id or the full sheet URL in these secrets, and the outreach
  bot should accept both too. The id is the part between `/d/` and `/edit`.

## 2. Which tabs are lead tabs

A tab is a **lead tab** when its row 1 contains **both** `Place Id` and `Company Name`. Ignore every other tab.

- **Lead tab names:** one tab per niche, named after the niche text in the `Niches` tab. Characters `[ ] * ? : / \`
  become spaces, and names are cut to 90 characters. If a niche name collides with a control-tab name below,
  " Leads" is added.
  - Examples: `Dentists (Cosmetic, Implants, Ortho)`, `Boutique Fitness Studios & Gyms (Owner-operated)`.
  - YouTube sheet: one tab per YouTube niche, for example `YouTube Creators: Finance & Business`.
- **Never lead tabs:**
  - `Master Dashboard`, `US Stats`, `Stats`, `Meta` (hidden), `Dashboard` (old v4)
  - `All Leads` (old v4, no longer updated)
  - `Rules`, `Niches`, `Locations`, `Options`, `Leads Input`, `Import`, `Seen`, `Searches`, `Snapshots`
  - `Blacklist`, `Run Log`, `Playbook`, and any tab starting with `OLD `
- **Tab names can change:** users may rename tabs, so find lead tabs by their header row, not by a hard-coded name.

## 3. Columns the outreach bot reads (always by header name, never by position)

Users can reorder columns or add their own. Read row 1, then map each header to its column index.

| Header | Content | Can be blank? |
|---|---|---|
| `Place Id` | Unique, stable lead key. Google place id, `osm:node/123`, `yt:UC…`, `input:…`, or `import:…`. Never changes, never reused. | never blank |
| `Company Name` | Business or channel name, as listed | never blank |
| `Decision Maker Name` | Full name of the owner, founder, director or principal, **facts only**: printed on their site, in a LinkedIn result title, in Hunter data, or in a YouTube description. Never guessed. | often blank |
| `First Name` | First word of that name, without the title (blank when there's no name) | blank with no name |
| `Personal Email` | A named person's mailbox on their own domain | often blank |
| `Generic Email` | info@, hello@, bookings@, and similar | may be blank |
| `Other Emails` | Remaining public emails, comma-separated | may be blank |
| `Niche` | Same text as the tab's niche | never blank |
| `Country` | Full country name, e.g. `United States`. **Blank is allowed on YouTube rows** (unknown country). | YouTube only |
| `Country Code` | ISO-2 code (`US`, `GB`, `AU`, `AE`…) | YouTube only |
| `City` | Search city, e.g. `Chicago` | may be blank |
| `Website` | `https://…`, or the channel URL for YouTube | may be blank |
| `Instagram`, `Facebook`, `LinkedIn`, `TikTok`, `YouTube`, `Twitter / X` | Profile URLs | may be blank |
| `Other Socials` | `Label: url` pairs separated by ` \| ` | may be blank |
| `Lead Insight` | 3-4 short lines: who they are and their likely pains or struggles. Lines are separated by newlines. Inferences start with "Likely". It is either AI text built from facts or a fact-only summary. **It is not an email.** | never blank on v5 rows |
| `Segment` | One of `PRIME`, `PRIME-REVIEW`, `GROWING`, `HAS-AGENCY`, `POLISHED-NO-SIGNAL` | blank on pre-v4 rows |
| `ICP Score /10` | Number with one decimal, e.g. `7.4` | never blank |
| `Lead Added On` | `YYYY-MM-DD`, in the sheet's Rules › `TIMEZONE` (default UTC) | never blank |

**Also useful (optional to read):**
- `Phone`
- `Decision Maker Role`
- `Pitch Angle`
- `Social Gap`
- `Suggested Pitch /mo` with `Pitch Currency`
- `Tier`
- `Revenue Band`
- `Agency Name` and `Agency Evidence` (HAS-AGENCY rows)
- `Email Verified`
- `Status`
- `My Notes`

**Old rows:**
- Rows written before v5 have no `Lead Insight`. Fall back to the old `Case Study` column if it exists, or else use
  `Pitch Angle`.
- Old tabs may still contain the `Email Subject` / `Email Draft` columns. The lead bot **leaves them blank on every new
  row**, so ignore them.

## 4. Rules both bots keep

1. **The lead bot never writes an email draft.** Drafting is entirely the outreach bot's job.
2. **The lead bot is append-only:**
   - New rows always go below the last existing row.
   - It never sorts, inserts above, deletes, or rewrites an existing lead row. That includes `Status` and
     `My Notes`.
   - So a row's position never changes after it's written. Still, find a row by `Place Id` right before writing to it.
3. **New rows:**
   - The lead bot writes `Status` = `New` once, when the row is created.
   - The lead bot dedupes by `Place Id` across the whole sheet before appending, so a `Place Id` appears once per
     sheet.
4. **What the outreach bot may write back:**
   - **`Status`:** only these values: `New`, `Drafted`, `Contacted`, `Follow-up 1`, `Follow-up 2`, `Replied`,
     `Call booked`, `Client`, `Not interested`, `Do not contact`.
   - **Its own columns:** it may add columns at the end of the header row. Prefix the header with `Outreach `, for
     example `Outreach Drafted On`. The lead bot ignores unknown columns and never overwrites them.
   - It must never write to `My Notes`, which belongs to the user.
5. **Skip these rows:** `Status` = `Do not contact` or `Not interested`. Also skip any row whose email or domain is in
   that sheet's `Blacklist` tab (column A).
6. **Quota:** both bots use the same Google service account. Keep the outreach bot under about 20 reads per minute,
   because the lead bot's jobs share the 60 reads/min/user limit.

## Version

- v5 (2026-11-01): first version. Adds `Lead Insight`; removes drafting from the lead bot; sheets for
  AE/SA/QA/AU_ONLY; append-only.
