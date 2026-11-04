# lead-bot v3 -> notes for the outreach / draft-bot session (from the lead-bot v3 session, 2026-10-31)
- Column rename: "Suggested Pitch AUD/mo" -> "Suggested Pitch /mo" (same position; old tabs renamed in place).
  New columns appended AFTER "Place Id": "Pitch Currency", "Country Code", "YT Last Upload (days)". All other names/positions unchanged.
- "Drafted" added to STATUS_LIST (after "New"); dropdown refreshed on every lead tab each run.
- Lead bot never rewrites Status / My Notes / any existing lead cell: append-only; sorting moves whole rows.
  All Leads is a read-only QUERY view -> write Status to the niche tab, finding the row by Place Id RIGHT BEFORE writing
  (the finish job may re-sort between your read and write).
- Place Id forms: osm:node/123, ChIJ... (Google, Places or gosom import), yt:UC..., gmapscid:..., imp:<hash>, input:<hash>.
  Rare duplicate: imports job + maps job at the same moment can add one business under 2 ids -> dedupe on email before sending.
- Leads are now worldwide (Country / Country Code columns). Email rules differ per country (Playbook tab lists US/UK/IE/CA/NZ/UAE).
- AI calls now send a custom User-Agent (Groq/Cloudflare 1010). Template drafts still contain "free" (kept: it is the offer).
- Full details: D:\All Automations Records\Lead generation\au-lead-bot\au-lead-bot\UPGRADE_V3.md (zip: ..\..\au-lead-bot-v3.zip)
- v3.1 (later): an Australia-only edition exists at D:\All Automations Records\Lead generation\au-only-lead-bot (own repo + own sheet).
  Same columns + 8 AU columns appended at the END: ABN, ABR Entity Name, Entity Type, GST Registered, ABN Active Since,
  Business Age (yrs), Phone Type, AU Timezone. Phone Type = Mobile -> Do Not Call Register check before calls.
  AU Timezone can drive send times (8-10am their time). New optional keys in both editions: SERPER_API_KEY, BRAVE_API_KEY,
  ZENROWS_API_KEY, ABN_LOOKUP_GUID (plus existing APIFY/APOLLO/HUNTER/ZEROBOUNCE).
- v4 (worldwide edition, 2026-10-31): leads now go to 7 Google Sheets (SHEET_ID_US/GB/CA/AU/NZ/IE/YOUTUBE; old single
  SHEET_ID only when none of these exist). Each sheet has its own "All Leads" + Status/Place Id as before -> the outreach
  bot must read each sheet's All Leads (or a list of sheet ids). NEW sheets use a new column order: "Segment" (3rd) and
  "Revenue Band" (6th) near the front; extra columns after Place Id incl. Agency Name, Agency Evidence, Segment Rank.
  Read by header name, not position. Suggested send order: PRIME > PRIME-REVIEW (after manual check) > GROWING;
  never cold-pitch HAS-AGENCY / POLISHED-NO-SIGNAL as new (replacement pitch only). Free-mode rows say
  "free signals (unverified)" in Revenue Est. Basis.

## v5 (2026-11-01): read CONTRACT.md, it is the source of truth
- Contract: D:\All Automations Records\Lead generation\CONTRACT.md (copied into both repos).
- Lead bot NEVER writes email drafts now. New column "Lead Insight" (3-4 lines, newline-separated) replaces Case Study.
  Old tabs may still have Case Study / Email Subject / Email Draft columns: blank on new rows.
- Sheets: SHEET_ID_US/CA/GB(UK)/AU/NZ/IE/AE/SA/QA/YOUTUBE(YT); AU-only edition = SHEET_ID_AU_ONLY (fallback SHEET_ID).
  Lead tab = row 1 has "Place Id" AND "Company Name". Skip Master Dashboard, US Stats, Stats, Meta, Dashboard, All Leads + control tabs.
- Append-only: rows never move. Outreach may write Status only (+ its own "Outreach ..." columns at the end); find row by Place Id.
- All bots share one service account: keep outreach reads <= ~20/min.
