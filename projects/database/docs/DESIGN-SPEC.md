# DESIGN-SPEC: Lead Dashboard restyle (extracted 2026-11-04, read-only research)

Roots. CRM = `F:\Github Repos\projects\levelup-crm\app\` (current; `app-main\` is the OLD blue/slate CRM, ignore). EA = `F:\Github Repos\projects\email-automation\app\web\` (built React UI on sample data; its rulebook is `DESIGN.md`) plus `F:\Github Repos\projects\email-automation\BRIEF.md`. Paths below are relative to these roots.

## 0. Read first (surprises / owner decisions)
- Neither app is literally black-and-white: both are cool neutral greys (faint violet tint) plus ONE purple accent (`#6E4CF5` light / `#846AFF` dark). For strict B&W use the mono-accent option in §5.
- EA `BRIEF.md` and `CLAUDE.md` say "blue/black `#07090D` / `#0E131B` / `#4DB8FF`". Superseded: built `src/styles/theme.css` is purple on soft grey; EA `PROGRESS.md` (WS5a) says "admin colours (purple default)".
- The two apps' greys differ (dark bg CRM `#141416`, EA `#1B1B1F`). This spec uses CRM (owner's ask) and borrows EA's contrast-checked status colours.
- CRM status colours as TEXT on white fail WCAG (computed: review `#F59E0B` 2.15:1, done `#22C55E` 2.28:1). Use them for dots/bars only; text uses the EA variants.
- Possible CRM bug: `src/index.css` declares `--rail` twice (colour channels, then `--rail: 60px`). The unlayered 60px wins, so `bg-rail` is likely invalid/transparent. Not verified in a browser. Use separate names (`--rail-w`).
- CRM has NO pre-paint theme script (`index.html` hard-codes `class="dark"`, React swaps it in an effect), so light-mode users probably see a dark flash (inferred, not verified). EA does it right (§1).
- EA shell scrolls the window (sticky header, fixed bottom tab bar); `KNOWN-ISSUES.md` lists an iOS Safari bug where that tab bar floats mid-screen. CRM scrolls an inner `<main>` inside an `h-dvh` shell. Copy the CRM approach for a truly fixed shell.

## 1. Theme tokens (CRM `src/index.css`, `tailwind.config.js`, `src/context/ThemeContext.tsx`, `BrandingContext.tsx`, `index.html`)
- Colour values: see the annotated block in §5 (each line names its CRM token; light = `:root` lines 8-24, dark = `.dark` lines 31-43). Status tokens `--st-*` are not overridden in dark.
- EA deltas worth copying (`src/styles/theme.css`): text-safe status light `ok #0B7A54 / warn #8F5805 / danger #C8323F` (5.35 / 5.89 / 5.27:1), dark `ok #34D399 / warn #FBBF24 / danger #FF6B7A`; accent-as-text `brand-text` light `#6F59D6`, dark `#9A85FF`; form border `--input` `#8B8B96` light / `#73737E` dark; chart `series-1 #846AFF`, `series-2` `#8E8E9A` / `#7A7A85`, `grid` `#EEEEF1` / `#2D2D33`.
- Font: CRM Inter 300-900 via Google Fonts CDN (`index.html`), stack `Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`. Base 13px/18px (`text-ui`), micro 11px/14px (`xs2`), title `text-xl sm:text-2xl` semibold `tracking-tight`, KPI `text-2xl` semibold tabular, `-webkit-font-smoothing: antialiased`. EA uses Geist (self-hosted) with 12/13/14/22/30/60px scale.
- Radii: CRM `card 8px`, `shell 10px`, controls `rounded-md` 6px, popover/dialog `rounded-lg` 8px, auth card `rounded-2xl` 16px, pills full. EA `--radius .625rem`: sm 6, md 8, lg 10, xl 14 (panels).
- Shadows: CRM popover `shadow-xl shadow-black/20`, dialog `shadow-2xl shadow-black/40` on a `bg-black/50` scrim, phone sidebar `0 20px 25px -5px rgb(0 0 0/.3)`. EA panel light `0 1px 2px rgb(10 16 24/.04), 0 4px 16px -8px rgb(10 16 24/.08)`, dark `inset 0 1px 0 rgb(255 255 255/.035)`.
- Spacing: Tailwind 4px scale. Content padding `p-4 sm:p-6` (+ safe-area bottom), card `p-5` (KPI `px-4 py-3`), grids `gap-3`/`gap-4`, sections `space-y-6`. EA content max width 1480px.
- Focus: CRM `:focus-visible { outline: 2px solid accent; outline-offset: 1px }`; inputs `focus:border-accent focus:ring-4 ring-accent/15`. EA outline 2px `--ring #846AFF`, offset 2px.
- Motion: ease-out `cubic-bezier(.23,1,.32,1)`; `.pressable:active` scale .97 (140ms); `.enter` fade + translateY(6px) 220ms; reduced-motion disables both. Scrollbar 8px, thumb `muted/25%`.
- Switching: Tailwind `darkMode: 'class'`; class `dark` on `<html>` (`ThemeContext.tsx` effect). Persist in `localStorage['teamlog_theme']` = `dark|light|system`; default from `localStorage['teamlog_branding'].defaultTheme`, else `dark`. `system` uses `prefers-color-scheme` only when chosen. Top-bar button flips dark/light (sun/moon, `aria-label="Toggle theme"`). `<meta theme-color>` is static `#141416` (not updated). CRM CSP is `script-src 'self'` (`vercel.json`), so it could not use an inline script.
- No-flash (EA `index.html` + `src/context/theme-provider.tsx`): `<html class="dark">` default, a blocking inline `<head>` script reads cookie `outreach-theme` (`light|dark`, 1 year), sets the class and `theme-color` (`#1b1b1f` / `#f4f4f6`) before first paint; toggle writes the cookie and crossfades 280ms with the View Transitions API (skipped for reduced motion). EA ships no CSP.

## 2. Layout shell (CRM `src/components/shell/*`, `src/index.css`)
| Part | Spec |
|---|---|
| Root | `h-dvh flex flex-col`, L/R safe-area padding; only `<main class="flex-1 min-w-0 overflow-y-auto">` scrolls; inner `p-4 sm:p-6`; route change = 10px fade-up, no exit |
| Top bar | `h = --hdr` 40px (52px on `pointer:coarse`) + safe-area top, `bg-rail border-b`, `px-2 gap-1`: sidebar toggle, workspace menu, centred search (md+, 420px, Ctrl K), clock, theme toggle, avatar menu |
| Icon rail | 60px wide (56px under 768px, labels hidden), 32px icon boxes, 18px icons stroke 1.8, label 10px; active = accent/15% fill |
| Sidebar | 240px, `bg-sidebar border-r`, width animates 0-240 (collapse in `localStorage['levelup_sidebar_collapsed']`), rows `h-7` 13px, hover `hover/5`, active accent/14%, section label 11px `subtle` |
| Mobile | Under 768px (or coarse pointer + height under 500px) the sidebar overlays the page right of the rail (`absolute z-30`), collapsed by default, closes after navigating. NO bottom bar. Touch: 44px min hit areas, inputs 16px (no iOS zoom) |
| Page header | `flex-col sm:flex-row sm:items-center justify-between gap-4`: h2 `text-xl sm:text-2xl font-semibold tracking-tight`, sub `text-sm text-muted mt-0.5`, actions right |
| Card | `bg-surface border border-line rounded-card(8px) p-5`; title `text-sm font-semibold`, link `text-xs text-muted` with arrow; empty = one muted line + icon, no empty chart frames |
| KPI tile | `bg-surface border rounded-card px-4 py-3`, value `text-2xl font-semibold tabular-nums`, label `text-xs text-muted`; grid `grid-cols-2 lg:grid-cols-4 gap-3`; warn value in blocked colour. Rich variant (`ui/StatCard.tsx`): p-5, 36px icon chip, 11px uppercase label, delta chip, 64x24 sparkline, hover lift 2px |
| Badge | `ui/Badge.tsx`: `rounded-full border px-2.5 py-0.5 text-xs font-medium`, fill = colour at ~10%, border ~25%, 6px dot. EA `Pill`: `h-6 px-2 text-caption`, tone ok/warn/danger/brand/muted, ALWAYS with icon |
| Buttons | primary `h-8 px-3 rounded-md bg-accent text-accent-fg text-ui font-medium`; outline `border border-line hover:bg-hover/6`; danger `bg-st-blocked text-white`; icon `w-7 h-7 rounded-md text-muted`; auth/submit `h-11 rounded-lg font-semibold`. EA: h-9 default, h-8 sm, 14px |
| Inputs | `h-8 px-2.5 rounded-md border border-line bg-surface-2/60 text-ui focus:border-accent`; label `text-xs font-medium text-muted mb-1.5`; auth fields `h-11 rounded-lg` |
| Table | CRM tables are legacy hard-coded hex (do not copy). EA `ui/table.tsx`: th `h-10 px-2 font-medium`, rows `border-b hover:bg-muted/50`, tabular numbers, `overflow-x-auto` wrapper; table on `lg+`, card list below; sticky first column; row click opens a right drawer |
| Overlays | Popover `min-w-200 rounded-lg border bg-surface p-1`, item `h-8`; Dialog `max-w-sm rounded-lg p-4 max-h-[90dvh]`, title 14px; Esc closes; confirm destructive actions |

## 3. Email Automation dashboard (EA `BRIEF.md` §5-6, `src/components/layout/nav.ts`, `src/features/*`)
- Nav (4 groups): Sending (Overview, Accounts, Leads, Queue, Replies), Content (Templates, Reports), Team (Task reports, Employees: admin), System (Alerts, Settings and Admin: admin). Desktop = collapsible 16rem sidebar (3rem icon mode); phone = bottom tab bar (Overview, Accounts, Replies, Alerts, More opens the sidebar sheet). Header 56px: title, Ctrl K search, system status ("Last check 41 s ago"), notifications, theme toggle, kill switch (admin).
- Overview, top to bottom: greeting + date + one-line brief, period `Segmented` (Today / 7 d / 30 d); Today panel (sent vs capacity, sending windows, sends in last 15 min); Next sends; 6 KPI tiles with 14-day sparkline and delta (replies, positive, reply rate, bounce rate, unsubscribes, AI cost); Needs you; emails by lead country (rings); live activity; 20-day sending forecast + lead supply days left; funnel "how leads progress"; reply-rate heatmap by day and hour; reply rate by niche/country. Employees get a scoped "own numbers" home.
- Accounts: table with health ring (0-100: 80+ Healthy, 60+ Watch, else At risk), today vs limit bar, 7 d / 30 d sends, bounce %, reply %, status pill, mode, owner, inline limit edit, bulk bar, right Sheet drawer. Reports: Overview / Deliverability / Monthly x Daily / Weekly / Monthly x All / Automation / Manual x region; export menu (Excel, CSV, Google Sheet) on every table.
- Theme: see §0 (purple/grey; dark default; light toggle). Sample-data badge until Supabase is wired.
| EA idea | Lead dashboard |
|---|---|
| Period Segmented + daily/weekly/monthly | YES: leads per day / week / month |
| KPI tiles with sparkline and delta | YES: leads today / this month, clients vs leads, score >= 7 share |
| Breakdown by niche / country | YES: plus source and status |
| Funnel "how leads progress" | YES: found > emailed > replied > client |
| Needs you | YES: leads waiting for action (no email, stale, unassigned) |
| Employees cards / folder, own-numbers home | YES: team workload (assigned, open, done, last 7 days) |
| Export menu, reports page, drawer for row detail | YES (CSV minimum) |
| Live activity, command menu, heatmap | OPTIONAL; skip without JS framework |
| Health ring, caps, bounces, deliverability, capacity forecast, windows, kill switch, AI cost, 100-user OAuth cap | NO (sending-specific). Possible analogue: "source health" = last successful run per lead source |

## 4. Security / account rules (CRM `SECURITY-AUDIT.md`, `src/lib/claimSession.ts`, `AuthContext.tsx`, `vercel.json`; EA `docs/SCHEMA.md`, `supabase/migrations/0012`, `src/features/auth/*`). Rules only.
- Email + password only; public sign-up OFF; only the admin creates accounts. Min password 8 (CRM, upper/lower/digit) or 10 (EA `MIN_PASSWORD`).
- One active session per account: a server-side row per user holds the current session id; login claims it, so the older session loses data access at once. Fail closed: if the claim fails, sign out. Re-check on tab focus. Disabling a user deletes the row.
- First login and admin reset set `must_change_password`; no data until changed; cleared only when the password really changes (DB trigger, not the UI).
- Reset: EA = 3 steps (email, 6-digit emailed code, new password) with a generic response (no account enumeration). CRM dropped email reset: admin sets a password (revokes sessions); owner uses a local script. Use the code flow for the Flask app.
- Roles `admin` / `employee`. Employee sees only own rows, cannot edit own profile/role, no admin pages (redirect AND server refusal). Admin-only writes for settings and structure. Last active admin cannot be demoted or deactivated; owner is protected; only 1-2 admins.
- Enforce permissions in the data layer, not just the UI. Admin actions and exports go to an audit log. Service keys never reach the browser or `.env` examples.
- CRM headers (`vercel.json`): CSP `default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'self'; form-action 'self'; frame-ancestors 'none'`, `X-Frame-Options: DENY`, `nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`, HSTS 2 years, restrictive `Permissions-Policy`, `COOP: same-origin`. (Flask: add CSRF tokens on forms and `HttpOnly; Secure; SameSite=Lax` cookies: my addition, not in the sources.)

## 5. Apply to Flask (plain CSS, no CDN)
```css
/* Light = :root (CRM token in comment). Hex converted from CRM RGB channels. */
:root{--bg:#FFFFFF;--rail:#F4F4F6;--sidebar:#F8F8FA;--surface:#FFFFFF;--surface-2:#F2F2F5; /* bg rail sidebar surface surface-2 */
--border:#E6E6EA;--text:#1F1F24;--muted:#6B6B76;--subtle:#9696A0;--hover:rgb(15 15 20/.05); /* subtle: decor only, 2.9:1 */
--accent:#6E4CF5;--accent-fg:#FFFFFF;--accent-text:#6F59D6;--accent-soft:rgb(110 76 245/.14);--ring:#6E4CF5;
--todo:#87909E;--info:#3B82F6;--review:#F59E0B;--done:#22C55E;--blocked:#EF4444; /* dots and bars only */
--ok:#0B7A54;--warn:#8F5805;--danger:#C8323F;--info-text:#2563EB; /* text-safe: EA values; info-text is mine, 5.2:1 */
--shadow-pop:0 12px 32px -8px rgb(0 0 0/.2);--shadow-modal:0 24px 48px -16px rgb(10 16 24/.3);
--r-card:8px;--r-ctl:6px;--r-panel:10px;--hdr:40px;--rail-w:60px;--side-w:240px;--ease:cubic-bezier(.23,1,.32,1);
--font:Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;color-scheme:light}
@media (pointer:coarse){:root{--hdr:52px}} @media (max-width:767px){:root{--rail-w:56px}}
[data-theme=dark]{--bg:#141416;--rail:#0E0E10;--sidebar:#18181B;--surface:#1E1E22;--surface-2:#26262B;
--border:#2A2A30;--text:#E6E6E9;--muted:#91919B;--subtle:#696973;--hover:rgb(255 255 255/.06);
--accent:#846AFF;--accent-text:#9A85FF;--accent-soft:rgb(132 106 255/.14);--ring:#846AFF;
--ok:#34D399;--warn:#FBBF24;--danger:#FF6B7A;--info-text:#60A5FA;
--shadow-pop:0 12px 32px -8px rgb(0 0 0/.5);--shadow-modal:0 24px 64px -12px rgb(0 0 0/.7);color-scheme:dark}
```
- Mono (true black-and-white) option: `--accent:#1F1F24;--accent-fg:#FFFFFF;--accent-text:#1F1F24` light and `--accent:#E6E6E9;--accent-fg:#141416;--accent-text:#E6E6E9` dark; keep ok/warn/danger for status only. Owner decision.
- Fonts: system stack above works with zero files. For Inter, self-host a `woff2` under `/static/fonts` (no Google CDN, which a strict CSP would block).
- Toggle, no inline script: the server reads cookie `theme` (`dark` default) and renders `<html lang="en" data-theme="{{ theme }}">` plus `<meta name="color-scheme" content="dark light">` and `theme-color`. First paint is right with zero JS. External `/static/theme.js` (end of body, `script-src 'self'` is enough) handles the click: on `[data-theme-toggle]` set `document.documentElement.dataset.theme`, write `document.cookie='theme='+t+'; path=/; max-age=31536000; SameSite=Lax'`, update `theme-color` (dark `#141416`, light `#F4F4F6`) and the button `aria-label`. Sun/moon as inline SVG, swapped by CSS on `[data-theme]`. To follow the OS when no cookie exists, add a tiny blocking `<script src="/static/theme-init.js">` in `<head>` (still CSP-safe).
- Skeleton of the fixed shell: `.app{display:grid;grid-template:"top top" var(--hdr) "side main" minmax(0,1fr)/auto minmax(0,1fr);height:100vh;height:100dvh;overflow:hidden}` `.main{grid-area:main;min-height:0;overflow-y:auto;overscroll-behavior:contain;scrollbar-gutter:stable;padding:16px}` (24px from 640px).

Ten rules for the fixed shell and mobile
1. DO make `.app` the only full-height box (`100dvh`, `overflow:hidden`) and `.main` the only scroller; DON'T let `body`/`html` scroll. Put `min-height:0` on every grid/flex child that holds a scroller.
2. DON'T use bare `100vh` (iOS toolbars); declare `100vh` first, then `100dvh`. Add `viewport-fit=cover` and pad with `env(safe-area-inset-*)`.
3. DO give header, rail and sidebar fixed sizes from variables; DON'T size them by content, so nothing shifts between pages. `scrollbar-gutter:stable` on `.main`.
4. DO animate only `transform` and `opacity` (drawer = `translateX`); DON'T animate width/height/top/left. Honour `prefers-reduced-motion`.
5. DO use an off-canvas drawer below 768px (fixed, `z-index:30`, scrim `rgb(0 0 0/.5)`, closes on link click and Esc, `aria-expanded` on the menu button); DON'T add a bottom bar unless there are 5 or fewer top-level pages.
6. DO set 44px min hit areas and 16px inputs under `@media (pointer:coarse)`, plus `touch-action:manipulation` and `-webkit-tap-highlight-color:transparent`; DON'T rely on hover for anything.
7. DO wrap tables in `overflow-x:auto` with tabular numbers and a sticky first column, and switch to a stacked card list below 1024px; DON'T allow page-level horizontal scroll (test `scrollWidth === innerWidth` at 320-768px).
8. DO reserve KPI/card heights (`min-height`) so loading and empty states do not jump; DON'T render empty chart frames, show one muted line.
9. DO use only the tokens (no hex in component CSS) and pair every status colour with an icon or text; text on tokens needs 4.5:1, `--subtle` is decoration only.
10. DO keep CSP strict: external CSS/JS only, no inline `style=""` or `<script>`, no CDN fonts/icons; DON'T add a JS framework, vanilla `theme.js` plus a small `shell.js` (drawer) is enough.

Not found: CRM dark-mode shadow tokens (only Tailwind utilities used), a CRM mobile bottom bar, any CRM dashboard widget list beyond `src/components/dashboard/DashboardView.tsx` (admin home: 4 stat tiles, Today panel, attention list), a CRM-side 6-digit reset flow (removed 2026-11-04).
