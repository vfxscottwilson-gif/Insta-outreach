# outreach-bot v2 -> notes for the lead-bot session (from the outreach rebuild session)
- outreach-bot reads tab "All Leads" (fallback: any tab with Personal Email / Generic Email / Email header).
  Columns used: Company Name, First Name, Decision Maker Name, Personal Email, Generic Email, Other Emails,
  Email Verified, Status, ICP Score /10, Niche, City, Suburb, Case Study, Pitch Angle, Social Gap, Email Subject,
  Email Draft, Google Rating, Review Count, Website Summary, Business Type, Instagram/Facebook/TikTok/YouTube.
  "Suggested Pitch AUD/mo" is NEVER used (price).
- It WRITES the Status cell of drafted leads: "Drafted" (later sender: Contacted / Follow-up 1 / Follow-up 2 /
  Replied / Do not contact). Request: if the lead bot rebuilds All Leads, please preserve existing Status values
  (merge by email / Place Id). "Drafted" is not in your STATUS_LIST data validation; please add it.
- Lead-bot Email Draft is reused only if it passes outreach rules; current drafts say "free"/"We do" so they fail
  (template/AI used instead). Optional: drop "free" from the lead bot's subject/body.
- Found: Groq (Cloudflare) answers 403 "error code: 1010" to Python-urllib's default User-Agent. If the lead bot
  calls Groq via urllib, set a custom User-Agent header.

## Update (formula-safe write-back)
- All Leads is now READ-ONLY for outreach-bot (it is a QUERY formula). Status goes to the SOURCE niche tab row,
  matched by "Place Id" (fallback: email), batched (1 batch_get + 1 batch_update per tab, every 200 drafts + at end).
  Needs: every niche tab keeps the "Place Id" and "Status" columns, and "Drafted" is allowed in Status.
