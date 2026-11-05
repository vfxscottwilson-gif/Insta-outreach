# Progress: Database / Lead Dashboard (updated 2026-11-05)

**Decision (user, 2026-11-04):** the Flask **Lead Dashboard** is the working app (data, sync, login, access). The **Database UI preview** chat is the design it will be re-skinned to. The Supabase backend plan is frozen (docs kept). The second-Gmail Supabase account is not needed now.

## Subjects (one titled chat per topic)
| Chat | Owns | State |
|---|---|---|
| Database app: Control room (brief, preview, approval) | Plan, handoffs, tracker, verification of the other chats | Running (this chat), in sidebar group "Database app (lead tracking)" |
| Build: Lead-gen dashboard & database (folder `app/dashboard`, moved from `D:\All Automations Records\Lead Dashboard` on 2026-11-05; old folder = backup) | The working Flask app and its gap list (`HANDOFF-GAPS.md`, 46 items) | Building P1 gaps; applied default decisions (below) |
| Database UI: clickable preview (folder `projects/database/app/web`) | The look: screens, tokens, motion; will write `DESIGN-HANDOFF.md` | Building (checkpoint `cf6dc27`, tsc clean) |

## Tracker
| Workstream | Session | Status | % | Last update | Blocker | Next step |
|---|---|---|---|---|---|---|
| Lead Dashboard core: sync, login, admin users, assign, tabs/inventory, password vault, theme + phone shell | Build: Lead-gen dashboard & database | Built; 327 tests pass in `app/dashboard` (re-run after move); demo serves (login 200, CSP + X-Frame-Options DENY) | 100 | 2026-11-05 | - | - |
| Lead Dashboard gaps (HANDOFF-GAPS, 48 items) | same | B1 done: owner + admin cap 2, deactivate/re-add/delete accounts, Approvals, Trash/purge, tombstones, 2-sweep missing rule + breaker, reach events, DNC, append-only audit, bell. Also: tzmap, write-back pilot test (bot append row unchanged) | 40 | 2026-11-05 | - | B2 per-sheet access + employee dashboards, B3 2-min scanner, B4 metrics/time zones/country folders/editable lists, B5 more charts + motion |
| Design: Database UI preview | Database UI: clickable preview | Screens being built on mock data | 40 | 2026-11-04 | - | `DESIGN-HANDOFF.md` (CSS variables, shell, components, motion), screenshots |
| Apply design to the Flask app | Build: Lead-gen dashboard & database | Base theme applied (CRM tokens, dark default, purple, fixed shell, phone drawer, logo, 38 screenshots in `app/dashboard/proof/`); login page restyle to match CRM/Outreach in B5 | 50 | 2026-11-05 | `DESIGN-HANDOFF.md` (optional token update) | Login page like Outreach (brand row, card, rise-in motion), more graphs + motion |
| Brief, red-team, handoffs, ICP reference | Control room | Done: BRIEF (frozen), REDTEAM, UI-SPEC, HANDOFF-TO-LEAD-DASHBOARD, OVERLAP, `reference/ICP-PROMPT-youtube-creators.md` | 100 | 2026-11-04 | - | - |
| Pilot on real sheets (AU Leads + AU Only suggested) | Lead Dashboard chat | Not started | 0 | 2026-11-04 | **You:** sheet links, Google service account, Gmail app password | After P1 |
| Supabase backend (schema, scanner, hosted web app) | - | FROZEN, nothing deleted | - | 2026-11-04 | - | Revisit only if you want it hosted later |

## Defaults applied by the Lead Dashboard chat (you may override any)
Purple dark-default theme with light toggle; app name "Database", brand "Level Up VFX"; local PC first, Cloudflare Tunnel later; you are the owner, 2 admins incl. owner (owner changes the cap), both approve removals; employees may "Mark contacted"; write-back OFF until a one-sheet pilot passes; employees can request removal, either admin approves, Trash 30 days, typed purge; day basis = each sheet's own date, Pakistan time only for live arrival views; no task module; per-sheet access Hidden/View/Contribute (existing employees migrated to View + assigned-only); employee-added leads allowed, approval before any export; business hours 9-17 local.

## Needs you (one batch)
1. Sheet links or IDs for the pilot (AU Leads + AU Only suggested) and whether the lead bots are still running.
2. A Google service account in its own Google Cloud project (sign-in link given when you are ready); share the sheets with its email as **Viewer**.
3. A Gmail app password for reset-code emails (goes to `.env` through the clipboard script, never into chat).
4. Say if you want to override any default above.
