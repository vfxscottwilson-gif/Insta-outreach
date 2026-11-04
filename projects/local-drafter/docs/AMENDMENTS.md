# Amendments to LOCAL_DRAFT_GENERATOR_PROMPT.md (user, 2026-11-03)

These override the build prompt wherever they conflict.

1. **Multiple emails in one cell → split, one email per row.** (Replaces §2 "take the first valid one".)
   - A cell with N emails (separated by commas, semicolons, spaces, slashes, new lines, " or ", etc.) becomes N rows in `Ready to Send`, one email per cell in column A.
   - Each row gets its own First Name, Subject and Body (A–D). Drafts for addresses of the same lead must differ (different STYLE/opening, subject and sign-off).
   - Each address is validated and de-duplicated on its own (invalid, role/blocked, already in output/Log/state → skipped and logged).
   - Config: `MULTI_EMAIL_MODE = split | first` (default `split`).

2. **First Name sources, in order:**
   1. Name column.
   2. Owner/contact name found in the lead's socials data: Instagram/TikTok/X handle or display-name columns in the sheet, YouTube channel title/description (e.g. "I'm Sarah"), website About text already fetched.
   3. Clean `first.last` pattern in that row's email local part.
   - Same trust rules as spec §3: reject brands, handles that aren't clean names, multi-word titles; strip Dr/Mr/Muhammad/Mohammed etc.; capitalise properly.
   - Do not scrape Instagram or other social sites (they block scrapers). Use only what is in the sheet or already fetched (YouTube API, website).
   - For split emails, prefer the name from that specific address's local part (e.g. `john.smith@` → John) when it is clean; otherwise the lead's name.

3. **Fallback name:** `FIRST_NAME_FALLBACK`, default `Team` (Apps Script writes "Hi Team,"). `There` (capital T, gives "Hi There,") is the documented alternative; both are fine.

4. **Resume after credits run out:** keep the project `CLAUDE.md` "Status / next step" and the workspace `PROGRESS.md` row current, and commit after each working step, so when the user clicks Continue the work resumes exactly where it stopped.

5. **Scope now:** code only (plus tests and docs). The user shares the real lead sheet later; no real-sheet run yet.
