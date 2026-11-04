# MOTION: what moves on the Lead Dashboard, and how

Rules ported from the Outreach app (`..\web\src\styles\index.css`, read-only reference). Plain CSS + two small
external scripts (`dash/static/charts.js`, `dash/static/auth.js`); strict CSP, no inline styles.

## Principles
- Animate **transform, opacity and SVG `stroke-dashoffset` only** (plus one custom property for the beam). No width, height, top, left, colour-only loops.
- **Every keyframe is `from`-only.** The resting style is the final state, so `prefers-reduced-motion: reduce` (which sets `animation: none` on everything in `app.css`) shows the finished page: full bars, drawn lines, static border, final numbers.
- **No layout shift**: cards and KPI tiles have `min-height`; the count-up pins the number's final width before rolling; the tooltip is one fixed element moved with `transform`.
- Stagger comes from `--i`, set by the classes `.i0` to `.i39` (server-rendered, never an inline style). Marks past 40 share the last slot.

## Easings
| Token | Curve | Used for |
|---|---|---|
| `--ease` | `cubic-bezier(.23,1,.32,1)` (ease-out, Apple-like settle) | rise, fade, grow, pop, count-up, segmented highlight |
| drawer | `cubic-bezier(.32,.72,0,1)` | line draw-in, card hover lift |
| linear | `linear` | the orbiting beam only |

## Timings
| Element | Animation | Duration | Delay |
|---|---|---|---|
| Page cards / KPI tiles / login rows (`.rise`) | fade + 8px rise | 520 ms | `--i` x 45 ms + 40 ms |
| Bars (`.grow-y` / `.grow-x`) | scale from baseline / from the left (`transform-box: fill-box`) | 700 / 800 ms | `--i` x 14 / 50 ms + 160 ms |
| Lines and sparklines (`.draw`, `pathLength=1`) | `stroke-dashoffset` 1 -> 0 | 1100 ms | 120 ms |
| Dots (`.pop`) | scale 0 -> 1 after the line | 400 ms | `--i` x 14 ms + 700 ms |
| Donut slices, legend rows, value labels (`.fade`) | opacity | 500 ms | `--i` x 14 ms + 180 ms |
| KPI / hero numbers (`[data-count]`) | count-up 0 -> value, ease-out quartic, then a 3.5% "settle" bump | 900 ms (1200 ms after a pulse) | tile index x 40 ms |
| Hero border beam (`.card.hero::before`) | conic highlight rotating behind a 1px ring | 7 s loop | none |
| Live dot (`.live i::after`) | ring expands 1 -> 2.6x and fades | 2 s loop | none |
| Sync pulse (`.pulse`) | glow ring on the hero, numbers roll to the new counts | 1.6 s, once per poll hit | poll every 60 s |
| Period / range switch (`.panel.swap`) | shown panel rises in | 400 ms | none |
| Segmented tab, buttons | background/colour 200 ms, press scale .97 140 ms | | |
| Country card hover | lift 2px + brand shadow (hover-capable pointers only) | 340 ms | |
| Login primary button | glow deepens, arrow nudges 2px | 300 / 200 ms | |

Login page order: brand row (i0) -> card (i1) -> fields (i2, i3) -> button (i4) -> hint (i5) -> note (i7); whole entrance about 550 ms.

## Reduced motion
- CSS: `@media (prefers-reduced-motion: reduce) { * { animation: none; transition: none } }` already in `app.css` covers rise, grow, draw, pop, beam, ping, pulse and the panel swap.
- JS: `charts.js` reads the same media query and writes the final number at once (no roll, no settle).
- The hero keeps its gradient border (static) and the live badge keeps its dot (static).

## Performance notes
- The beam is a single composited pseudo-element (`will-change: transform`); the inner cover is a plain background, so repaint stays inside the 1px ring.
- SVG bar growth uses `transform-box: fill-box` so no per-bar inline `transform-origin` is needed.
- Tooltips attach one delegated listener per event type on `document`; the native `<title>` becomes `aria-label` on first hover so screen readers keep the text and the browser tooltip does not double ours.
- Count-up uses `requestAnimationFrame`; at most 13 numbers start within 480 ms on the dashboard.
