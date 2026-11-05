# Design handoff: re-skin the Flask dashboard to the Database design

**Goal:** `app/dashboard` (Flask + Jinja) looks and moves exactly like the Database preview (`app/web`). Everything needed is plain CSS, HTML and a small JS file in **`app/design-export/`**. Start with its `README.md` (copy steps, base layout, class map, data attributes) and open `components.html` by double-click to see every piece.

| Need | Where |
|---|---|
| Tokens, light and dark | `app/design-export/tokens.css` |
| Components | `app/design-export/components.css` (prefix `db-`) |
| Motion | `motion.css`, `motion.js` |
| Reference screens | `dashboard.html`, `leads.html`, `login.html`, `components.html` |
| Jinja macros | `macros.jinja` |
| Proof screenshots | `app/design-export/proof/` (compare with `preview-proof/screens/`) |

## 1. Tokens (as the app resolves them)

Dark is the default (`.dark` on `<html>`), light is the toggle. Never hard-code a hex in a template: use the variable.

| Token | Light | Dark | Use |
|---|---|---|---|
| `--background` | `#f4f4f6` | `#1b1b1f` | Page |
| `--foreground` | `#1f1f24` | `#ececef` | Text |
| `--card` | `#ffffff` | `#232328` | Panels |
| `--raised` | `#f8f8fa` | `#2a2a30` | Rows inside panels |
| `--popover` | `#ffffff` | `#27272c` | Menus, dialogs, drawers |
| `--primary` | `#775fe6` | `#775fe6` | Accent fill (white text) |
| `--brand-text` | `#6f59d6` | `#9a85ff` | Accent as text or thin line |
| `--secondary` / `--muted` | `#f0f0f3` | `#2a2a30` | Tiles, segmented track |
| `--muted-foreground` | `#6b6b76` | `#a5a5b0` | Secondary text |
| `--accent` | `#efeff3` | `#2f2f36` | Hover fill |
| `--border` | `#e6e6ea` | `#33333a` | Hairlines |
| `--input` | `#8b8b96` | `#73737e` | Input border |
| `--ring` | `#846aff` | `#846aff` | Focus |
| `--destructive` / `--danger` | `#c8323f` / `#b52532` | `#ff6b7a` | Errors |
| `--ok` | `#0b7a54` | `#34d399` | Good |
| `--warn` | `#8f5805` | `#fbbf24` | Attention |
| `--series-1..6` | `#846aff #8e8e9a #0b6fa8 #0f766e #a21caf #c2410c` | `#846aff #7a7a85 #4db8ff #5eead4 #f0abfc #fb923c` | Charts |
| `--grid` | `#eeeef1` | `#2d2d33` | Chart grid |
| `--sidebar` | `#f8f8fa` | `#17171a` | Sidebar |
| `--sidebar-accent` | `#efeff3` | `#26262b` | Active pill |
| `--sidebar-border` | `#e6e6ea` | `#2a2a30` | Sidebar hairline |
| `--shadow-panel` | soft 2-layer | inner top highlight only | Panels |
| `--shadow-overlay` | `0 24px 48px -16px rgb(10 16 24 / .22)` + hairline | `0 24px 64px -12px rgb(0 0 0 / .7)` + hairline | Dialogs, menus |

Tints are the accent or tone at **6 to 7 percent** over the card (chips, circles, active states), borders at **25 to 30 percent**. Admin Branding overrides only `--primary`, `--brand-text`, `--ring`, `--sidebar-primary`, `--series-1`, `--heat-1`, `--company` and the dark neutrals.

**Type** (Geist Variable; Inter only for the "Level Up VFX" name): caption 12/16, small 13/20, body 14/22, title 22/28 (tracking -0.015em; page title 28/36 from 768px), KPI 30/34 (tracking -0.025em), display 60/60 (tracking -0.04em). Headings are semibold with tracking -0.025em. Every number is tabular (`font-variant-numeric: tabular-nums`).
**Radii:** `--radius` 10px. Controls 8 to 10px, panels and folder cards 14px, welcome and user card and auth card 16px, pills and avatars full.
**Spacing:** 4px base. Screen blocks are 20px apart (24px from 768px). Panel padding 20px (24px from 768px). Toolbars 16px (20px).

## 2. Shell sizes

| Part | Size |
|---|---|
| Sidebar | 16rem open, 3rem icon-only, 18rem as the phone drawer (max 85 percent of the screen) |
| Header | 3.5rem tall, sticky, frosted (`db-material`), search field 17rem |
| Content | max-width 1480px, padding 16px (24px from 768px), bottom padding 7rem on phones for the tab bar |
| Tab bar | 3.5rem + safe area, below 1024px |
| Breakpoints | below 1024px: sidebar becomes a drawer, tab bar appears, tables become card lists. 640px: folder grid and chips grow. 1280px: 12-column rows (`db-cols`). 1060px container: automations table instead of cards |
| Tap area | 44px minimum on touch screens, without changing how controls look (`@media (pointer: coarse)` rule in `components.css`) |

## 3. Component inventory (HTML structure and classes)

Full markup is in the reference pages; macros in `macros.jinja`.

- **Shell:** `.db-app > .db-sidebar + .db-scrim + .db-inset(.db-backdrop, .db-header, .db-main) + .db-tabbar`.
- **Sidebar:** `.db-sidebar__head .db-brand`, `.db-welcome` (avatar with ring, "Welcome back" and name), `.db-navgroup` (toggle button with chevron, folding `__items`), `.db-navitem.is-active` (icon tile, label, `.db-badge`, `.db-navitem__edge`), foot: `.db-sample`, `.db-usercard`.
- **Header:** sidebar toggle, title, `.db-search`, quick actions (add lead, sync now, approvals with `.db-count`), `.db-syncpill` with `.db-live-dot`, bell with `.db-dot-new`, theme toggle, sign out.
- **Page header:** `.db-pagehead` (title, one-line purpose, actions on the right).
- **Panel:** `.db-panel.db-card` with `.db-panelhead` (title, description, action).
- **KPI tile:** tinted-circle layout (`.db-kpi.db-tone-*` > `.db-circle` + number + label, foot with `.db-delta`) or plain layout with sparkline. Inline metric row: `.db-metrics > .db-metric` with `.db-minibars`.
- **Pills and chips:** `.db-pill` (tone, icon, label; status colour is never alone), tier pills, lead status, sheet status, `.db-delta`, `.db-badge`, `.db-counter`, `.db-chip`, `.db-chipinfo`.
- **Controls:** `.db-btn` variants and sizes, `.db-input`, `.db-select`, `.db-switch`, `.db-check`, `.db-seg` (sliding thumb), `.db-field`.
- **Tables:** `.db-table` (sortable `th[data-sort]` with `aria-sort`, sticky header, sticky first column), card list for phones, `.db-pager`, `.db-bulk` floating bar.
- **People:** `.db-avatar` (initials, hue from the name, optional ring), `.db-avatars`, `.db-person`.
- **Charts:** `.db-gauge` arc and ring, `.db-area` smooth line chart (crosshair and tooltip card), `.db-cols-chart`, `.db-spark`, `.db-minibars`, `.db-progress`.
- **Overlays:** `.db-menu`, `.db-pop`, `.db-tooltip`, `.db-overlay` > `.db-dialog` (blurred backdrop) or `.db-drawer` (right drawer, bottom sheet on phones), `.db-toast`.
- **States:** `.db-empty`, `.db-skeleton.db-shimmer`.
- **Auth:** `.db-auth` with company and product logos, glow, card (sign in, forgot password, new password with rules).
- **Geography and niches:** country folder cards (`.db-folder`, closed, open, add) that fold open to `.db-folder-detail` with a state filter; niche tree `.db-tree`; four-number rows `.db-statrow`.
- **Lists:** needs you, activity feed, notification popover.

## 4. Motion rules

| Thing | Rule |
|---|---|
| What animates | Transform and opacity only (heights only through `DB.fold`) |
| Easings | `--ease-out cubic-bezier(.23,1,.32,1)` entrances and hover, `--ease-in-out cubic-bezier(.77,0,.175,1)` shimmer, `--ease-drawer cubic-bezier(.32,.72,0,1)` drawers, dialogs, lift, gauge, line draw, `--ease-spring` (critically damped `linear()`) folds, segmented thumb, bulk bar |
| Durations | press 140ms, hover 150ms, menus 160 to 200ms, dialog 340ms (close 200ms), drawer 380ms (close 200ms), lift 340ms, rise 520ms, bars 700ms, gauge 1000ms, line draw 1100ms, fold 440ms, theme crossfade 280ms, toasts 320ms |
| Entrance | `.db-rise` with `style="--i:n"`: 10px up and fade, 45ms stagger, 60ms base |
| Press | `.db-press` scales to .97 |
| Lift | `.db-lift` rises 2px with an accent shadow on hover, settles at .985 on press |
| Folds and moving highlights | Spring, no bounce, interruptible (cancel and restart from the current height) |
| Count-up | 900ms ease-out quartic from 0 |
| Dialog, drawer, menu | CSS transitions on `data-state`, so closing mid-open reverses smoothly. Esc closes. Focus is trapped and returned |
| Reduced motion | Global rule in `motion.css`: 1ms durations, no delays, no live-dot or shimmer. State still changes. `motion.js` skips count-up and folds animations |
| Reduced transparency | `.db-material` and overlays become opaque |
| Phones | Header and tab bar are opaque (no blur) |

## 5. Accessibility rules

- Every icon-only button has `aria-label` and a tooltip (`data-db-tip`). Targets at least 24px, 44px on touch.
- Status colour never alone: icon and label (`status_chip`, `tier_pill`).
- Focus: 2px `--ring` outline, 2px offset, on everything. Skip link first in the body.
- Toggle buttons use `aria-pressed`, folds use `aria-expanded` and `aria-controls`, the active nav item has `aria-current="page"`, sortable headers have `aria-sort`, switches are `role="switch"` with `aria-checked`.
- Charts: `role="group"` or `role="img"` with a label, plus an `.db-sr-only` table (the line chart builds it).
- Inputs are 16px on phones so iOS does not zoom. No `100vh` (use `100svh`). Fixed and sticky bars are opaque on phones.
- Keyboard: everything reachable by Tab, Esc closes overlays, arrow keys move in menus, `/` focuses search, Ctrl or Cmd K opens search.
- Contrast is checked for every token pair in the React app (`scripts/appearance.check.ts`); keep to the tokens.

## 6. Copy rules (from `app/web/DESIGN.md`)

- Sentence case, plain verbs, no ALL CAPS labels, **no middle dots** (`A · B`), no trailing arrows. Buttons say what happens ("Pause account").
- **Every number has its own label**: "41 of 58 sent", not "41 / 58"; "3 times", not "x3". A date stands alone, then the sentence starts.
- **Every clock time says whose it is**: PKT, or the lead's zone with "lead's time" nearby ("10:43 AM EST" and "Pakistan time: 08:43 PM PKT"). Calendar-day totals say "Pakistan time" somewhere on the screen. Relative times ("3 h ago") are fine.
- Totals say their scope ("Automation sent today", not a bare "Sent today").
- Dates: `03 Nov 2026`, `03 Nov`, `Tue 03 Nov`, `03 Nov 2026 02:30 PM PKT`.
- Plain words: "Business ID (Google place)", "First seen (Pakistan time)", "Missing in its sheet", "Quality score out of 10", "Moved to Trash", "Permanently remove", "Last synced 41 s ago". Keep the bot's own words where they are data (PRIME, Follow-up 1, Tier A).
- Errors say what to do next. Destructive actions confirm in a dialog and toast the outcome with the same verb.

## 7. Re-skin order (suggested)

1. Base layout and theme script (README steps 1 to 4). 2. Login and password pages. 3. Overview. 4. Leads and the lead drawer. 5. The remaining screens with the same panels, tables and chips. Each step: compare against `preview-proof/screens` at 1440 dark, 1440 light and 390 dark.


---

## Update 2026-11-05: minimal, rounded, glanceable (the user's latest direction)

Rule for every element: it must answer one question about progress, or it is removed. Questions the dashboard answers: How is this week and month against last? Are the sheets alive? What needs my approval? Who works what? How good are the leads?

### Radius scale (`--radius` is 0.875rem; everything derives from it)
| Token | Value | Used for |
|---|---|---|
| `--radius-sm` | 10px | chips inside tables, small inputs |
| `--radius-md` | 12px | buttons, inputs, menu items |
| `--radius-lg` | 14px | cards inside panels, drawers' inner blocks |
| `--radius-xl` | 18px | panels, KPI tiles, dialogs |
| full | 9999px | pills, avatars, switches, icon circles, bar tops, ring ends |
No square corners anywhere: charts use rounded bar tops (10px radius), round line joins and caps, and round ends on rings.

### Chart spec
| Chart | Spec |
|---|---|
| Line / area | Monotone cubic curve (control points clamped between neighbours, so no dips below zero or overshoot), 2.25px stroke with round caps, area fill = same colour from 28% to 0% opacity top to bottom, light dotted grid, no axis lines except the baseline |
| Bars | Rounded tops (10px), 4px gaps, grow from the baseline with `transform: scaleY` |
| Ring / arc | 16px stroke, round caps, 1.2% gap between stacked parts, track = `--secondary` |
| Hover | Vertical dashed crosshair, a dot per series with a card-coloured fill, tooltip card (title row, one row per series with swatch, label, tabular value) |
| Draw-in | Line draws once, 600 to 1100 ms, `--ease-drawer`; bars 700 ms `--ease-out`; rings 1000 ms |
| KPI number | Counts up from 0 to the value (NumberFlow-style tween, about 800 ms); no tween under reduced motion |
| Colours | Series 1 accent purple, 2 neutral, 3 blue, 4 teal, 5 pink, 6 orange; never colour alone (labels and tooltips carry the meaning) |

### Motion table (transform and opacity only)
| Interaction | Property | Duration | Easing |
|---|---|---|---|
| Page content enters | opacity, translateY 8px to 0 | 320 ms (cards stagger 45 ms) | `cubic-bezier(0.23, 1, 0.32, 1)` |
| Press (button, tile, nav item) | scale to .97 (cards .985) | 110 to 140 ms | `--ease-out` |
| Hover on a clickable card | translateY -2px + soft shadow | 340 ms | `cubic-bezier(0.32, 0.72, 0, 1)` |
| Active nav pill and accent edge | position (shared layout) | 420 ms | spring, no bounce (damping 1) |
| Group / row fold | height, opacity | 380 ms | spring, no bounce |
| Dialog opens / closes | opacity, scale .95 to 1, backdrop blur 3px | 340 / 200 ms | `cubic-bezier(0.32, 0.72, 0, 1)` |
| Drawer opens / closes | translateX | 380 / 200 ms | same iOS curve |
| Menu / popover | opacity, scale .95 from the trigger | 200 ms | same iOS curve |
| Tooltip on a chart | opacity, scale .95 | 150 ms | ease-out |
| Toast | opacity, translateY | 250 ms | ease-out |
Reduced motion: every duration collapses to 1 ms, loops stop, count-ups and draw-ins show the final state. Reduced transparency: frosted surfaces become solid.

### Minimal dashboard layout (above the fold, desktop 1440)
1. Welcome row: name, role, date in Pakistan time, Sync now, and one chip row (last synced, sheets healthy, new leads in the last 24 hours, things that need you).
2. Metric row (5 cells): total leads, emails, phone numbers, sheets (quality sheets), average quality out of 10. Each has a change chip and a mini bar.
3. Period cards (4): today, this week, this month, last month with change against the same days before.
4. Trend (8 columns) and quality gauge (4 columns).
Below the fold, in this order: Needs you (approvals, late or lost sheets, missing rows) beside niche-wise totals, countries as folders with states, then the automations table. Removed as decorative: the arrivals-by-hour chart and the activity feed (Activity has its own page).

---

## Audit alignment (control-room note, 2026-11-05)
The Flask audit rules below are adopted as guidance for the re-skin; where they differ from the preview, the preview keeps the user's own words.
| Audit rule | Status in the preview |
|---|---|
| Monotone cubic curves, round caps, gradient area, pill bars, round-capped ring | Done (AreaChart, Gauge, rounded bar tops) |
| Motion: rise 280 ms, hover 180 ms, press 140 ms, draw-in 600 ms, count-up 700 ms, transform and opacity only | Close: rise 320 ms, hover 340 ms, press 110 to 140 ms, draw-in 600 to 1100 ms, count-up about 800 ms. Use the audit numbers in Flask |
| Radii 12 card / 8 control | Differs: the user asked for softer corners, so the preview uses 18 panels, 14 controls. Flask may use either; keep one scale |
| No hero card, no 9-colour donut, no stacked workload | Followed |
| Five linked KPI tiles, Leads per day beside Month pace, By country and By niche below the fold | Partly: the preview shows five metrics, four period cards, trend and quality gauge; Month pace and status funnel are not built |
| Employee home three tiles and Contact-now list; Leads four filters plus More filters | Not applied to the preview yet |

### Six tiles (control-room change, 2026-11-05)
The overview shows six linked KPI tiles under the metric row: Leads today, this week, this month, last month, **Clients** (client count, "x% of all leads", 14-day cumulative sparkline, links to Leads filtered to clients) and Reached this month. Grid: 3 by 2 from 1100 px, 2 columns below (phone included). The funnel in Flask should end in Clients.


---

## Round 2 pieces to copy (owner feedback 2026-11-05)

Tabs: **Overview** first (this design), **Dashboard** (charts, six tiles, Leads per day + Month pace, Automations, By country / niche, funnel) second. Employees keep their own home first.

### Avatars (one component everywhere a person appears)
Six gradients of the brand purple, picked from the person id (`n = hash(id) % 6 + 1`), white semibold initials, faint light ring, slow drift, glow on the signed-in person. A photo, if added later, sits inside the same circle with the gradient behind it (`<img class="db-avatar__img">`, `object-fit: cover`). Photo upload is not built; ask the owner first (size and type checks, re-encode).
```html
<span class="db-avatar db-avatar--v3" data-me aria-hidden="true" style="--size:38px">{{ initials }}</span>
```
```css
.db-avatar{display:grid;place-items:center;width:var(--size,32px);height:var(--size,32px);border-radius:9999px;color:#fff;font-weight:600;
  font-size:calc(var(--size,32px)*.38);text-shadow:0 1px 2px rgb(0 0 0/.25);background-size:220% 220%;
  animation:db-avatar-drift 10s ease-in-out infinite alternate;box-shadow:inset 0 0 0 1px rgb(255 255 255/.28)}
.db-avatar[data-me]{box-shadow:inset 0 0 0 1px rgb(255 255 255/.32),0 0 0 2px color-mix(in oklab,var(--primary) 45%,transparent),0 4px 16px -2px color-mix(in oklab,var(--primary) 70%,transparent)}
@keyframes db-avatar-drift{to{background-position:100% 100%}}
.db-avatar--v1{background-image:linear-gradient(135deg,color-mix(in srgb,var(--primary) 45%,white),var(--primary),color-mix(in srgb,var(--primary) 45%,white))}
.db-avatar--v2{background-image:linear-gradient(135deg,var(--primary),color-mix(in srgb,var(--primary) 75%,black),var(--primary))}
.db-avatar--v3{background-image:linear-gradient(135deg,color-mix(in srgb,var(--primary) 85%,white),color-mix(in srgb,var(--primary) 70%,black),color-mix(in srgb,var(--primary) 85%,white))}
.db-avatar--v4{background-image:linear-gradient(135deg,color-mix(in srgb,var(--primary) 70%,black),color-mix(in srgb,var(--primary) 45%,black),color-mix(in srgb,var(--primary) 70%,black))}
.db-avatar--v5{background-image:linear-gradient(135deg,color-mix(in srgb,var(--primary) 55%,white),color-mix(in srgb,var(--primary) 90%,black),color-mix(in srgb,var(--primary) 55%,white))}
.db-avatar--v6{background-image:linear-gradient(135deg,color-mix(in srgb,var(--primary) 35%,white),color-mix(in srgb,var(--primary) 80%,white),var(--primary))}
@media (prefers-reduced-motion:reduce){.db-avatar{animation:none}}
html[data-hidden] .db-avatar{animation-play-state:paused}
```

### Border beam (only on: Overview stat block, Overview header card, login card, the "things need you" chip when above 0)
```css
.db-beam{position:relative;isolation:isolate;overflow:hidden}
.db-beam::before{content:"";position:absolute;z-index:-2;left:50%;top:50%;width:160%;aspect-ratio:1;translate:-50% -50%;
  background:conic-gradient(from 0deg,transparent 0 78%,color-mix(in oklab,var(--primary) 85%,transparent) 88%,transparent 96%);
  animation:db-beam-spin 7s linear infinite}
.db-beam::after{content:"";position:absolute;z-index:-1;inset:1px;border-radius:inherit;background:var(--beam-bg,var(--card))}  /* must equal the surface, dark and light */
@keyframes db-beam-spin{to{rotate:360deg}}
.db-beam[data-paused]::before,html[data-hidden] .db-beam::before{animation-play-state:paused}
@media (prefers-reduced-motion:reduce){.db-beam::before{animation:none;width:100%;aspect-ratio:auto;height:100%;background:color-mix(in oklab,var(--primary) 35%,transparent)}}
```
```js
// pause off-screen and when the tab is hidden
document.addEventListener('visibilitychange',()=>document.documentElement.toggleAttribute('data-hidden',document.hidden))
const io=new IntersectionObserver(es=>es.forEach(e=>e.target.toggleAttribute('data-paused',!e.isIntersecting)))
document.querySelectorAll('.db-beam').forEach(el=>io.observe(el))
```

### Login (centered)
```html
<main class="db-auth">
  <header class="db-auth__brand"><img src="level-up-vfx-logo.svg" alt=""><span class="db-auth__company">Level Up VFX</span><svg class="db-auth__link"/> <img src="database-logo.svg" alt=""><span class="db-auth__app">Database</span></header>
  <section class="db-auth__card db-beam"><h1>Connect to Level Up VFX</h1><p>To open <strong>Database</strong>, please log in:</p> <!-- form: labels and fields left-aligned, button full width --></section>
  <p class="db-auth__foot">One active session per account. Logging in here signs out your other devices.</p>
</main>
```
```css
.db-auth{display:flex;flex-direction:column;align-items:center;min-height:100svh;padding:0 1rem 3rem}
.db-auth__brand{display:flex;align-items:center;justify-content:center;gap:.75rem;padding:2rem 0}
.db-auth__brand img{width:3rem;height:3rem}                      /* 40px on phones */
.db-auth__company,.db-auth__app{font-size:1.5rem;font-weight:600;letter-spacing:-.01em}  /* 20px on phones; company name in Inter */
.db-auth__card{width:100%;max-width:400px;border-radius:var(--radius-2xl);border:1px solid var(--border);padding:1.75rem}
.db-auth__card h1,.db-auth__card>p{text-align:center}
.db-auth__card h1{font-size:1.625rem}
.db-auth__foot{max-width:400px;text-align:center;font-size:var(--text-caption);color:var(--muted-foreground)}
```

### Overview structure (copy with real data; the greeting uses the signed-in person's name token, never a mock name)
```
.db-page
  .db-welcome            avatar (v-variant, ring) + h2 "Welcome back, {{ user.first_name }}" + "{{ user.role_label }}, {{ today_pkt }} in Pakistan time"
                         + actions: Sync now (primary), Add sheet, Add country (admin only)
  .db-chiprow            time-zone note, last synced + next in, "N of M sheets healthy" + trouble, N leads in last 24 h, N in last hour,
                         .db-chip--beam "N things need you" (only when N > 0; gets .db-beam)
  .db-statblock.db-beam  five .db-stat cells in a 1px-gap grid (2 columns on phones, 5 from 1280): label, number, delta chip ("+33 added this week"),
                         explanation line, 14-bar mini chart (last bar accent)
                         cells: Total leads (unique) / Total emails (distinct, in how many leads) / Total phone numbers (distinct) /
                         Total sheets ("N quality sheets") / Average quality out of 10 (core segments)
  .db-tilegrid           six .db-kpi tiles, 3 by 2 from 1100px, 2 columns below: Leads today (no delta, "each sheet's own date"), this week and
                         this month (delta vs the same days before), last month, Clients (count, "x% of all leads", 14-day cumulative sparkline,
                         links to Leads filtered to clients), Reached this month. Each tile: tinted icon circle, number, label, note, links to the matching filtered list
  .db-grid-8-4           Leads per day area chart (30 days, three series) + Quality gauge card (arc, average out of 10, "kept at 6.5 and up")
  .db-grid-5-7           Needs you list (approvals, late or lost sheets, missing rows, unassigned over 24 h, DNC to-do) + By niche (group > niche rows)
  .db-folders            Countries as folder cards that open to states with a state filter
  .db-table              Automations table with status chips, quality out of 10, quality sheet chip, worked-by avatars
```
Class names and markup for each block are in `app/design-export/dashboard.html` and `components.html` (same `db-` prefix); the React source is `app/web/src/features/overview/`.


---

## Round 4: one merged design. Dashboard, Leads and shell, with class names

Source of truth for markup and CSS: `app/design-export/` (`dashboard.html`, `leads.html`, `components.html`, `components.css`, `round2.css`); React source in `app/web/src`. Avatars: every person uses the six purple variants (`.db-avatar--v1..v6`, no cyan or blue; checked, none left in the preview).

### Shell and sidebar groups
`.db-app` > `.db-sidebar` (16rem; icon-only 3rem) + `.db-main` > `.db-header` + `.db-content`.
Sidebar, top to bottom: `.db-brand` (mark, "Database", "Level Up VFX"), `.db-welcome` (avatar with ring, "Welcome back", name), foldable groups `.db-navgroup` (button label + chevron, items fold with a spring), `.db-navitem` (icon tile `.db-navitem__icon`, label, optional `.db-badge`; active = `.is-active`: pill + accent edge bar + filled icon tile), footer: sample-data note, "View as" select (admin), `.db-userchip`.
Groups: **Track** Overview, Dashboard, Leads, Geography, Niches, Quality / **Sources** Sheets / **Team** Team, Assignments, Approvals (count badge) / **Insights** Reports, Activity / **System** Lists, Settings (Trash, DNC to-do and Users are Flask-only items, admin only). Employees see Overview as "My work", Leads, Geography, Approvals as "My requests".
Top bar `.db-header` (3.5rem, frosted): collapse button, page title, search field (Ctrl K), then Add, Sync, approvals check with count, "Synced N s ago" pill, bell, theme toggle, sign out.

### Dashboard page (second tab, admin)
```
.db-page
  .db-pagehead            h2 "Dashboard", "{{ n }} leads in database. Trends and rankings; the numbers and health are on Overview."
  .db-tilegrid            the same six .db-kpi tiles as Overview (today, week, month, last month, Clients with sparkline, Reached)
  .db-grid-7-5
    .db-panel             "Leads per day": 30-day area chart + grey dashed 7-day average
    .db-panel             "Month pace": cumulative leads this month vs last month by day of month; subtitle says ahead of / behind by N on the same day
  .db-panel               Automations table (period chips Today / This week / This month / Last month)
  .db-grid-2
    .db-panel             "By country": .db-rank rows (label, pill bar, value + "8.0 of 10")
    .db-panel             "By niche": the eight biggest niches, same rows
  .db-panel               "Status funnel": New > Drafted > Contacted > Follow-up 1 > Follow-up 2 > Replied > Call booked > Client; each row = bar of leads that reached the step or further + "N% of the step before"; Not interested and Do not contact left out
```
```css
.db-rank{display:grid;gap:.75rem;list-style:none;padding:0;margin:0}
.db-rank li{display:grid;grid-template-columns:minmax(0,9rem) 1fr auto;align-items:center;gap:.75rem;font-size:var(--text-small)}
.db-rank__bar{height:.5rem;border-radius:9999px;background:var(--secondary);overflow:hidden}
.db-rank__bar>span{display:block;height:100%;border-radius:9999px;background:var(--series-1);transform-origin:left;animation:db-grow-x .8s var(--ease-out) both}
.db-funnel li{display:grid;grid-template-columns:8rem 1fr 9rem;gap:.75rem;align-items:center}
.db-funnel .db-rank__bar{height:.75rem}
```
Charts use the smooth monotone curves, gradient area, round caps and the hover crosshair + tooltip in this file's earlier chart spec (also `docs/ui-audit/charts-smooth.*`).

### Leads page anatomy (copy from `leads.html`)
```
.db-pagehead + actions     Add lead (primary), Import, Export (admin or allowed)
.db-statrow                five .db-kpi: Total leads / With email (+ distinct addresses) / With phone (+ numbers) / Quality leads (at or above the threshold, % of all) / Waiting
.db-panel
  .db-toolbar              search ("/" shortcut), Filters (count badge), Views, Columns, Sort + direction
  .db-periodchips          Any date, Today, This week, This month, Last month + "Counted by" select (Sheet date / Pakistan time) + score chips (Any score, at or above minimum, Below minimum)
  .db-activefilters        removable chips + "Clear all"
  .db-resultline           "707 leads, 881 emails, 643 phone numbers. Added on (sheet date): any."
  table.db-table           select box | Company + person | Location + lead's local time + business-hours badge | Niche + group | Tier + score | Status chip | Assigned (avatar + name) | Added on | contact icons (masked until Reveal)
                           row badges: Also in N sheets, Removal requested, Incomplete, Unclassified niche; click a row = right drawer
  .db-pager                "Showing 1 to 8 of N" + pages
  .db-bulkbar              only while rows are ticked: Assign, Tag, Mark contacted, Do not contact, Export, Request removal or Move to Trash
```
Keep the scroll position and place after a row action (no full reload).
