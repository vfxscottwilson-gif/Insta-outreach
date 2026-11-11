# 01 Roadmap

Status on 2026-11-05 (from `app\CLAUDE.md` and `PROGRESS.md`; nothing re-tested for this page).

## Done and live
- Login (email + password only, one device per account, lockout after 5 wrong tries via `login-guard`)
- Tasks (list/board/calendar), projects, teams, clock in/out rules, hourly and daily reports, Editor Tracker, admin portal (add/remove people, set passwords, settings, branding)
- Google Sheet mirror every 5 minutes; daily keep-alive so the Free Supabase project does not pause
- Security audit with live tests (`docs\SECURITY-AUDIT.md`)

## Open / next
| Item | Why | Where tracked |
|---|---|---|
| CAPTCHA (Cloudflare Turnstile, free) | Blocks guessing passwords directly against the login API | `docs\SECURITY-AUDIT.md` |
| Documents vault still stored in the browser | Do not keep real passwords there until moved to the database | `app\CLAUDE.md` |
| Low-data / offline PWA mode | Queued, waiting for the owner's yes | `app\CLAUDE.md` |
| First real schema export (`DATABASE_URL`) | Cloud backup is data-only until then | `database\RESTORE.md` |

Full phased plan: `docs\ROADMAP.md`. Features: `docs\FEATURES.md`. Prices: `docs\PRICES.md`.
