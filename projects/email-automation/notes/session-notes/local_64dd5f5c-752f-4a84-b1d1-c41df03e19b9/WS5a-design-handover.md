# WS5a design system: hand-over (2026-11-03)

Commits on `app` main: `228fe1f` (tokens, shell, Overview), `cc62d8e` (Accounts, a11y, docs). Not pushed.

## Where things are (`app/web/`)
- Tokens: `src/styles/theme.css` (dark default `.dark`, light `:root`), utilities + motion keyframes: `src/styles/index.css` (`panel`, `pressable`, `rise`, `grow-x/y`, `fade-in`, `shimmer`, `live-dot`).
- Shell: `src/components/layout/` (shadcn sidebar collapsible=icon, header with status / bell / theme / Pause all, phone tab bar + "More" sheet). Nav config: `nav.ts`.
- Screens: `src/features/overview/`, `src/features/accounts/`. Other 8 routes render `ComingNext`.
- Charts (no chart lib): `src/components/charts/column-chart.tsx` (stacked, capacity marker, annotation, sr-only table), `chart-tip.tsx`.
- Caps clamp: `src/lib/caps.ts` (70 / 650, safe bands 50-60 / 500-600); check `node scripts/caps.check.ts`.
- Mock data: `src/mocks/` (fixed NOW 2026-11-03 15:42Z, seeded). Types mapped to `docs/SCHEMA.md` views in the header comment of `types.ts`.

## Decisions
- Palette: bg #07090D, surface #0E131B, accent #4DB8FF (ink text #04121F on it, 8.65:1). Light: accent stays as fill; text/lines use #0A6FB8. Chart: new leads = accent, follow-ups = neutral slate (highlight pattern; blue+violet failed CVD validation).
- Type: Geist Variable (self-hosted via fontsource), tabular numbers everywhere. Custom sizes registered in `cn()` tailwind-merge config (required, or colours get dropped).
- Motion: CSS keyframes for entrances (transform/opacity only), Motion springs for nav pill / segmented / ticker, View Transitions for theme switch. Reduced motion collapses all.
- Filters are `Segmented` (aria-pressed buttons), not Radix Tabs.

## Open items
- Engine asked (message sent) for `v_reply_rate` dim `weekday_hour`, `ai_cost_mtd_usd`, and 7-days-ago KPIs for deltas.
- Main JS chunk 598 kB (193 kB gzip): split vendor chunks when real screens land.
- Sidebar collapse animates width (shadcn default, layout not composite); rare action, left as is.
- Magic UI not used yet (NumberFlow + Motion covered every need).
- Push notifications and Tauri come later (WS6 / packaging).
