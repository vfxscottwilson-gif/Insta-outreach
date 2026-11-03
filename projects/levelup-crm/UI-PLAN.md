# ClickUp-style UI plan (Phase 1-UI), for approval

Written 2026-11-03. References: the user's 2 ClickUp screenshots, plus their 55-second recording of their own ClickUp workspace in the dark theme.

## Does the preview look like ClickUp? No.
`upgrade/clickup` has only database work so far (Phase 0 SQL). The UI hasn't been touched, so the preview looks the same as the old app. These are the gaps:

| ClickUp (reference) | Our app today |
|---|---|
| Thin far-left **icon rail**: Home, Planner, AI, Teams, Docs, Dashboards, Whiteboards, Forms, Clips, Timesheet, More; Invite/Upgrade at the bottom | One wide sidebar with 11 text links |
| **Second sidebar**: Inbox, Replies, Assigned Comments, My Tasks, More / Channels / Direct Messages / **Spaces tree**; "+ Create" button; Customize Sidebar | None |
| **Top bar**: workspace switcher, centred **Search Ctrl+K**, quick icons, avatar | Breadcrumb, clock, theme toggle |
| **List view** grouped by status (Ready / In Progress / To Do), avatars, flag priorities, dates, inline edit; tabs List / Board / Calendar / + View | Card grid of tasks |
| **Board** (drag between columns), **Gantt/Calendar** | None |
| **Task side panel** (subtasks, comments, activity) | Modal form |
| Dashboard cards: Tasks by Status donut, by Assignee bars, Time Tracked line, by Priority | Custom stat cards and area chart |
| Dense 13 px UI, neutral greys, purple accent, small radius, quiet hover states, fast micro-motion | Big rounded cards and heavy colour |

## What we build
Our own brand (default "LevelUp", our own mark and lucide icons; **no ClickUp name, logo or illustrations**). ClickUp's layout, density and behaviour. Dark theme first, with a light theme too.

1. **Shell**: icon rail, collapsible second sidebar, top bar, router with URLs (`/home`, `/inbox`, `/my-tasks`, `/l/:listId`, `/t/:taskId`, `/timesheet`, …), and a Ctrl+K command palette.
2. **Hierarchy**: Spaces (Department) › Folders (Client) › Lists (Project) in the sidebar tree. Existing projects become Lists.
3. **Tasks**: List view (status groups, inline edit, multi-assignee avatars, priority flags), Board view (drag and drop), Calendar view, and a task **side panel** that slides in from the right (subtasks, comments, activity, timer).
4. **Home / Dashboard**: ClickUp-style cards (status donut, by-assignee bars, time-tracked line, by-priority list) built from the real data.
5. **Every existing feature moves in, none removed**:
   - Clock In/Out goes in the top bar and on the Timesheet page.
   - Hourly and daily reports.
   - My Progress and Performance become Dashboards.
   - Documents & Vault becomes Docs.
   - Team and Settings move into the admin area.
   - Audit Log.
6. **Motion (feels alive)**: every hover, click, open and close is animated, and it respects "reduce motion".
   - Rail and sidebar slide.
   - Panels spring in.
   - List rows animate when they are reordered, added or removed.
   - Drag lifts the card with a shadow.
   - Status chips morph when they change.
   - The checkbox completion ticks.
   - The Ctrl+K palette scales in.
   - Toasts (Sonner) replace `alert()`/`confirm()`.
   - Skeleton loaders.
   - Number counters animate.
   - Page transitions.
   - Buttons press on click.

**Data:** the UI is built on the current `useData()`/`useAuth()` hooks. It works now with today's data, and switches to Supabase later with no UI rewrite (the hook names stay the same).

**Libraries (all free, MIT):** motion, @dnd-kit, cmdk, sonner, recharts. react-router-dom and lucide-react are already installed.
**Skills:** frontend-design, emil-design-eng, animate, ui-ux-pro-max, web-design-guidelines, react-best-practices, animation-performance, webapp-testing.

## Workstreams (pilot first)

| # | Workstream | Owner | Output | Done when |
|---|---|---|---|---|
| U1 | Design tokens + shell + router + Ctrl+K | Opus designs, Sonnet builds | Shell on every page | Side-by-side screenshot with the reference recording; `npm run build` green |
| U2 | **Pilot:** List view + Board + task side panel + motion | Sonnet | Tasks fully ClickUp-like | Playwright: create task → drag across Board → open `/t/:id` → panel animates; **STOP: you review screenshots and preview** |
| U3 | Home dashboard cards + Inbox + My Tasks | Sonnet | | Screenshots |
| U4 | Move the remaining views into the shell (Timesheet, Reports, Docs/Vault, Dashboards, Team, Settings, Audit) | 2 Sonnet sessions in parallel (split by files) | | Every old feature reachable and working |
| U5 | Motion polish + reduced motion + 375 px mobile + Lighthouse | Sonnet, reviewed by Opus | | Lighthouse ≥ 90 |

Proof each step: screenshots in `proof/ui/`, commits on `upgrade/clickup`, then a push to the branch preview link (never production).

## Order change vs ROADMAP
This builds the Phase 1 UI **before** the Phase 0 login and Supabase wiring, because those are blocked on the Supabase project. Production stays on the old `main` until login and Supabase are live.

## Risks
- Pixel-level copying of ClickUp's artwork or illustrations is out of scope (trademark). We match layout and feel, not their assets.
- The `impeccable` skill now appears installed, but it was marked CAUTION earlier, so it is not used without your OK.
