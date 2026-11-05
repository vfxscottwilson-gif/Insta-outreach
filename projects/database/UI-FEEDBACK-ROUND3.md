# Owner feedback, round 3 (2026-11-05). Adds to UI-FEEDBACK-ROUND2.md; overrides it where they differ.

## 1. Login page: theme toggle placement
The brand row is centered above the card: [Level Up VFX mark + name] [link icon] [Database mark + name], then a small gap, then the **theme toggle button in the same row** (not at the far top-right corner of the page). Same on /admin/login, /forgot, /reset.

## 2. Which dashboard is the home (answer to "is this the final one?")
No: the charts page (six tiles + Leads per day + Month pace + Automations + By country/niche/funnel) is the **second** tab, "Dashboard". The **first tab, Overview** (the clean, scannable one the owner liked: image 8 in `reference/feedback-2026-11-05/`) is the home after login, and it is the one that must carry the totals.

## 3. Overview content (home)
- **Totals (always all-time, never change with the period):** Total leads, Total emails, Total phone numbers, Total names found (decision makers), Total sheets with "N quality sheets", Average quality out of 10.
- **Period selector (segmented control at the top): Today | This week | This month | Last month** (also "7 days" if cheap). **Default on every login = Today** (owner: "the daily one shown on the home screen whenever I log in"). The choice is remembered per person after that, but a new login starts on Today.
- **Period numbers** (change with the selector): leads collected, emails found, phone numbers found, names found, with the change against the previous equal period, and the per-country list (leads, emails, phones) for that period.
- **Daily chart:** "Leads collected per day" for **this week** or **this month** (small toggle), one bar per day, smooth style from the audit.
- **Scope ("what to look at and where"):** Source (sheet), Country, Niche/category selects apply to every number and chart on the page; the selection is remembered per person and shown as chips.
- Keep the welcome header, action buttons, status strips and "things need you" from image 8.

## 4. Mobile and narrow screens: sliders, not wrapping
- The period selector and every row of stat tiles become **horizontal slider rows**: `display:flex; overflow-x:auto; scroll-snap-type:x mandatory; scroll-snap-align:start; overscroll-behavior-x:contain; -webkit-overflow-scrolling:touch`, each tile its **own box** with a fixed minimum width (about 150-170 px), no wrapping.
- The slider must **not drift, bounce or float over other content**: no sticky or absolutely positioned slider, no hover-follow effects, no layout shift while scrolling or when the viewport width changes (reserve the height, `contain: layout`). Show a faint edge fade or a partial next tile so it is clear it slides. Works with touch and with mouse drag/trackpad.
- Cards in vertical lists stay stacked normally.

## 5. Time and date: Pakistan time, 12-hour
- All "today / this week / this month" boundaries, the daily chart days, "last synced" and every clock time use **Pakistan time (Asia/Karachi, PKT)** in **12-hour format with AM/PM** (for example "09:05 PM PKT"). Dates read "05 Nov 2026".
- "Collected" for a lead = the moment the scanner first saw it, converted to PKT, for leads discovered live after the first import. For history rows imported at the first sync (and rows that only have the sheet's date) use the sheet's `Lead Added On` date as the PKT date, and label the figure "history uses the sheet date". Do not count the first import as "today".
- Week = Monday to Sunday in PKT.

## 6. Hosting notes that touch the app (details in docs/HOSTING-PLAN.md)
- The dashboard will be reached through a Cloudflare Worker proxy at a free workers.dev address, so the app must trust `X-Forwarded-Proto/Host` from 127.0.0.1 (waitress trusted_proxy) and read the visitor IP from the `X-Client-IP` header (the proxy sets it).
- The free Worker allows 100,000 requests per day: make the live `/api/pulse` poll every **60 s**, only while the tab is visible.
