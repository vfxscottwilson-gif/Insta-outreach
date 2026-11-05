# Owner feedback, round 4 (2026-11-05): MERGE both looks into one. Overrides earlier rounds where they differ.

The owner showed the design chat's **Leads page** (`preview-proof/screens/owner-dark-desktop/leads.png`) and said: "this is the version I meant, I liked it more, it has everything; the only change is the profile pictures must use OUR gradient (purple tints and shades), not the cyan/blue one. The new charts dashboard is also great. I want both merged into one: sleek, minimal, fully workable and fully functional."

## Decision (made by the control room, owner delegated the how)
**Option B+: the working Flask app is restyled to the design chat's look everywhere** (same shell, same screens, same components), and the smooth-chart dashboard from the audit becomes its **second tab "Dashboard"**. Flask keeps all logic, access rules and tests; only templates, CSS and small JS change. One look, one app, no second frontend.

## Target navigation (sidebar groups, as in the design preview)
- **Track:** Overview (home), Dashboard (charts), Leads, Geography (today's Countries + local time), Niches, Quality
- **Sources:** Sheets
- **Team:** Team, Assignments, Approvals (count badge)
- **Insights:** Reports, Activity
- **System:** Settings, Lists, Trash, DNC to-do, Users (admin only; employees see only their allowed items, with My leads as their home)
Top bar: collapse button, page title, search (Ctrl K), Add, Sync, approvals check, "Synced N s ago" pill, bell, theme toggle, sign out. Sidebar footer: welcome card with avatar, "View as" (admin), user chip.

## Leads page (the one the owner liked) must have
- Stat row: Total leads, With email (and email addresses), With phone (and phone numbers), Quality leads (score at or above the threshold, % of all), Waiting (not contacted yet).
- Toolbar: Search (`/` shortcut), Filters (with count), Views, Columns, Sort + direction.
- Period chips: Any date, Today, This week, This month, Last month, with "Counted by: Sheet date" selector (Pakistan time, 12-hour, see round 3) and score chips (Any score, at or above threshold, Below minimum); active filter chips with "Clear all".
- Result line: "707 leads, 881 emails, 643 phone numbers. Added on (sheet date): any."
- Table: select box, Company + person, Location with lead's local time and a badge (Open now / Opens in N h), Niche + group, Tier and score, Status chip, Assigned to (avatar + name), Added on, contact icons; row badges (Also in N sheets, Removal requested, Incomplete, Unclassified niche); pager with "Showing 1 to 8 of N".
- Header buttons: Add lead, Import, Export (admin or allowed people).

## Avatars (again, applies everywhere)
Purple gradient family from the logo (about six variants per person), white initials, soft ring, glow on the signed-in person; no cyan or blue.

## Order of work for the Flask build chat
1. Login (centered brand row with the theme toggle inline, centered card heading, beam). 2. Shell + sidebar groups + top bar + avatars. 3. Overview (home, round 2 and 3 specs). 4. Leads page as above. 5. Dashboard tab (smooth charts, six tiles incl. Clients). 6. Remaining pages in the same style (Geography, Sheets, Team, Assignments, Approvals, Quality, Reports, Activity, Settings/Lists/Trash/DNC). 7. Hosting hardening tasks (docs/HOSTING-BUILD-TASK.md). Commit each step, keep tests green, report with screenshots.

## Order of work for the design chat
Add the charts **Dashboard** page to the preview in the same style (six tiles incl. Clients, Leads per day + Month pace, Automations table, By country/niche/funnel), make sure the avatars are purple, and keep DESIGN-HANDOFF.md complete (shell, Leads page, Overview, Dashboard, avatar and beam CSS) so the Flask templates can copy it.
