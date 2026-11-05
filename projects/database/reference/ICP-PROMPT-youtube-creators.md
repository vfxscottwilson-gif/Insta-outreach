# The user's ICP prompt (YouTube creator leads). Saved 2026-11-04.

The user pasted this prompt into the "Database UI: clickable preview" chat as the reference for **what their ideal customer (ICP) looks like and how leads are rated out of 10**. They said: use it only to understand the ICP and the scoring idea for the dashboard's quality numbers. **Do NOT use it to build any email automation**; that purpose lives elsewhere. Most of their sheets already carry a score out of 10.

Key facts for the dashboard (extracted; the full prompt follows):
- ICP: YouTubers, mostly talking-head creators (coaches, educators, consultants, finance, business, fitness, commentary, personal brands) with a real business behind the channel. A 10/10 lead can pay about $1,000 a month; the user only wants leads scoring **6.5/10 or higher** (the lead bot's own gate is 7).
- Score (out of 10, steps of 0.5): Business behind the channel 0-3; Ability to pay $500-1,000/month 0-3; How much the services would help 0-2; Activity and reachability 0-2. Facts from the sheet only, one-line "Why this score".
- Hard filters: a business behind the channel (website, course, coaching, products, booking link, sponsors, business email); active Instagram with posts; last Instagram post within 3-4 months. If the sheet lacks the data to check a filter, mark the lead **"unverified"**, never guess.
- Cleaning: duplicate emails, invalid emails, no-reply/system addresses removed.
- Name rules (First Name column): never guess; `Team` when unclear; initials -> Team; Singh/Kaur are not first names; Muhammad/Md as first part -> use the next name; business-style names -> extract the person.
- Mentions Harvey's `skills/lead_qualification.md` as the base idea.

---

# Prompt: Filter, Score and Write Cold Emails for YouTube Creator Leads (verbatim from the user)

## Who I am and what I sell
I run social media services for creators and businesses. I handle everything myself and I have a team behind me. My services: paid ads, SEO, branding, brand handling and brand management, reels, short-form and long-form video, and websites.

## My target customer (ICP)
YouTubers, mainly talking-head creators (face-to-camera: coaches, educators, consultants, finance, business, fitness, commentary, personal brands) who have a real business behind the channel.
A 10/10 lead can easily pay $1,000 a month for my services. I only want leads that score 6.5/10 or higher.

## The job
I am uploading a sheet of about 16,000-17,000 leads. Do this:
1. Look at the sheet first. Tell me which columns exist, how many rows there are, and which of my rules can actually be checked with that data.
2. Clean the data with code: remove duplicate emails, invalid emails, and no-reply/system addresses.
3. Apply the hard filters. Tell me how many leads pass each step.
4. Extract a first name for each lead using the name rules.
5. Score every lead that passes, using the scoring rubric. Keep only 6.5 and above.
6. Write a personalized email for every lead that is kept. (Email part: out of scope for the dashboard.)
7. Give back a spreadsheet: Tab 1 original data with pass/fail + reason; Tab 2 final output.

## Hard filters (a lead must pass all)
- Running a business, not only a hobby channel (website, course, coaching, consulting, products, services, booking link, sponsors or brand deals, or a business email).
- An active Instagram account with a few posts.
- Last Instagram post no older than 3-4 months.
If the sheet does not contain the data to check a filter, do not guess: mark those leads "unverified".

## Name rules (column: First Name)
Never invent, guess or misspell a name. "Team" is always safe. Use the real first name if clear in the sheet (or in email address, channel name, Instagram handle, website); otherwise `Team`. Initials/abbreviations/two-letter names -> `Team`. Sikh names: Singh and Kaur are not first names ("Harpreet Singh" -> `Harpreet`). Muhammad/Mohammad/Mohammed/Muhammed/Md as first part -> next name. Business-style names: pull out the person ("Fitness with Sarah" -> `Sarah`). No person's name in the brand -> `Team`. Proper capitalization. Unsure -> `Team`.

## Scoring rubric (column: Score, out of 10)
Question: can this person afford $500-1,000 a month for social media services, and how much would those services help them? Base it only on facts in the sheet.
| Area | Points | What to look for |
|---|---|---|
| Business behind the channel | 0-3 | 3 = clear paid offer (course, coaching, agency, product, service). 2 = some monetization (sponsors, affiliates, merch). 1 = weak signs. 0 = none. |
| Ability to pay $500-1,000/month | 0-3 | Audience size, number of offers, website, team, sponsors, how established they look. |
| How much my services would help | 0-2 | Visible gaps: inconsistent posting, no Shorts/Reels, weak Instagram, no website, weak branding. |
| Activity and reachability | 0-2 | 2 = active in the last 3 months and a personal/business email. 1 = one of these. 0 = neither. |
Score in steps of 0.5. Keep only 6.5 or higher. Add a short "Why this score" note (one line, facts only).

## Email rules (summary; not used by the dashboard)
Written as one person ("I"), 90-100 words, plain text, no greeting, opens with a pain point, one easy question at the end, only facts from the sheet, banned words (guarantee, discount, limited time, no obligation, act now, risk-free), subject 40 characters or fewer. Final output columns: Email, First Name, Subject, Body, Score (+ optional "Why this score"). Reminder: send from several separate warmed-up domains.
