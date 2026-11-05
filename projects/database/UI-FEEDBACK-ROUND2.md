# Owner feedback, round 2 (2026-11-05). Overrides UI-PUNCHLIST.md where they differ.

Images the owner sent are saved in `reference/feedback-2026-11-05/`:
- `7-login-working-app.png`: the working app's login (brand row sits in the top-left corner of the page).
- `8-overview-design-user-prefers.png`: the design chat's Overview (welcome header, action buttons, strips, big stat block, tile cards). **The owner says this is better and what they like.**
- `9-dashboard-layout-preview.png`: the charts dashboard layout (six tiles, Leads per day, Month pace, Automations, By country/niche, funnel). **The owner is happy with it as the SECOND tab, with smoother graphs.**

## What the owner asked for (their words, cleaned)
1. **Login page:** "Level Up VFX" and "Database" are at the top-left; put them both in the CENTER, make them bigger, and center the heading "Connect to Level Up VFX / To open Database, please log in" inside the login box.
2. **Tabs:** the first tab (home) must be the Overview from image 8. The charts dashboard from image 9 (the "742 leads in database" page with the charts) is the second tab. Graphs everywhere smoother (already specified).
3. **Border beam:** in the email automation app a light travelled along the stroke of a box, like a ray moving around the whole border. It looked premium and sleek. Use it in this app.
4. **Whole app:** smooth Apple-style animation so every click feels alive, premium, sleek and satisfying.
5. **Avatars:** the profile picture (for example "DH") must have a background in our gradient colours: tints and shades of the brand purple, so it pops and feels alive. The same gradient behind every profile picture that is added in future.

## Specs

### 1. Login (templates/auth/login.html + app.css)
- One centered column: brand row (Level Up VFX mark + name, link icon, Database mark + name) centered ABOVE the card, marks about 40 px, names about 20 px semibold. Theme toggle stays top-right of the page.
- Inside the card: heading "Connect to Level Up VFX" and the sub line centered (text-align center), heading about 26 px; labels and fields stay left-aligned for usability; button full width. The "Five wrong attempts..." line and the "One active session..." footer stay centered.
- Beam on the login card (see 3). Same treatment on /forgot and /reset.

### 2. Tabs and Overview
- Nav order: **Overview** (route `/`, first, default landing for admins and owner), **Dashboard** (charts page, second), then Leads, Countries, and the rest. Employees keep their own home (`/my`) as first tab.
- Overview content = image 8, from the design chat's source: `app/web/src/features/overview/*`, `preview-proof/screens/owner-dark-desktop/overview.png`, `DESIGN-HANDOFF.md`. Real data, not the mock names: the welcome name, role and date come from the signed-in person (date in Pakistan time).
  - Header: avatar (gradient, see 5), "Welcome back, <first name>", role + date; buttons Sync now, Add sheet, Add country (admin only).
  - Strip row: time-zone note; "Last synced N s ago, next in N s"; "N of M sheets healthy, X late, Y lost access"; "N leads in the last 24 hours"; "N leads in the last hour"; a "N things need you" link (approvals waiting + rows missing + unassigned over 24 h + DNC to-do).
  - Stat block (five cells, tiny bar sparklines, "added this week" chips): Total leads (unique), Total emails (distinct, in how many leads), Total phone numbers (distinct), Total sheets (with "N quality sheets"), Average quality out of 10 (core segments).
  - Tile cards with icons: Leads today, Leads this week, Leads this month, Leads last month, Clients (with sparkline), Reached this month. Every tile has a note that says what it counts, and links to the matching filtered list.
- Dashboard tab = image 9 as already specified (six tiles incl. Clients, Leads per day + Month pace, Automations table, By country, By niche, Status funnel) with the smooth charts. Do not duplicate whole sections between the two tabs: Overview = numbers and health, Dashboard = trends.

### 3. Border beam (port the email app's effect)
Source: `F:\Github Repos\projects\email-automation\app\web\src\styles\index.css`, `@utility beam` (lines about 164-195), used on a panel as `class="panel ... beam"` in `features/overview/today-panel.tsx`. It is a rotating conic gradient behind a 1 px inset, transform only:
```
.beam{position:relative;isolation:isolate;overflow:hidden}
.beam::before{content:"";position:absolute;z-index:-2;left:50%;top:50%;width:160%;aspect-ratio:1;translate:-50% -50%;
  background:conic-gradient(from 0deg,transparent 0 78%,color-mix(in oklab,var(--accent) 85%,transparent) 88%,transparent 96%);
  animation:beam-spin 7s linear infinite}
.beam::after{content:"";position:absolute;z-index:-1;inset:1px;border-radius:inherit;background:var(--card)}
@keyframes beam-spin{to{rotate:360deg}}
```
- Use on a FEW premium spots only: the login card, the Overview stat block, the Overview header card, and the "things need you" chip when the count is above 0. Not on every tile (calm and sleek, and the PC is already busy).
- Pause when off-screen or the tab is hidden (IntersectionObserver / `visibilitychange` sets `animation-play-state:paused`). `prefers-reduced-motion`: no spin, a static soft accent border instead.
- The inner `::after` background must equal the card background in dark AND light.

### 4. Motion (whole app)
Apple-style, transform and opacity only: page content rises in (about 280 ms, ease-out `cubic-bezier(0.23,1,0.32,1)`, capped stagger), navigation between pages with a short cross-fade (`@view-transition{navigation:auto}` with a fallback), sliding pill on the active nav item and on tab/segmented controls, press scale 0.97 (140 ms) on every button, link-card and tile, hover lift only on clickable cards (180 ms), KPI count-up (700 ms), chart draw-in (600 ms), drawers and dialogs spring in, flash/toast slides in and out, bell ring and badge pop, row actions give instant visible feedback (state change + toast), skeleton or fade while sync runs. All of it respects `prefers-reduced-motion`.

### 5. Avatars
- One avatar component/class used everywhere a person appears (header, sidebar chip, Team, assignees, approvals requester, activity, My leads header, comments).
- Background = gradients built from the logo palette (tints and shades of `#846AFF`: for example `#bbadff -> #846aff`, `#846aff -> #5f4bc4`, `#9b7bff -> #6a55cc`, `#6a55cc -> #3d2f8f`, `#b9a9ff -> #7a5cf0`), one of about six variants chosen deterministically from the user id so people are different but on-brand. Initials white, semibold. A faint 1 px light ring; the signed-in person's avatar gets a soft purple glow.
- Alive: a very slow gradient drift (about 10 s, `background-position` or a rotating sheen) that pauses when hidden and is off for reduced motion.
- If a profile photo is added later (`avatar_url`), show it inside the same ring with the gradient behind it (for transparent images). Photo upload itself is NOT built now: ask the owner first (needs size/type validation and re-encoding).
- Replace the cyan/blue avatars in the design preview too.
