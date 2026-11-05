After the current UI work, make the Database dashboard (F:\Github Repos\projects\database\app\dashboard) ready for Cloudflare Tunnel + PWA. Do not touch .env or secrets. Keep the smallest diff; run the full test suite; commit locally; never push. Order:

1. dash/authz.py: read DASH_IDLE_HOURS after load_env (lazy), not at import.
2. Session cookie: session.permanent=True with PERMANENT_SESSION_LIFETIME=30 days; keep the 12 h server-side idle check.
3. dash/__init__.py HEADERS: add Strict-Transport-Security max-age=31536000 only when cfg.cookie_secure.
4. dash/serve.py: waitress serve(..., trusted_proxy="127.0.0.1", trusted_proxy_headers={"x-forwarded-proto"}).
5. dash/db.py connect(): PRAGMA busy_timeout=30000; synchronous=NORMAL.
6. Per-IP throttle on /login, /admin/login, /forgot, /reset keyed on CF-Connecting-IP (fallback remote_addr): about 20 attempts per 10 min per IP, in-memory is fine.
7. PWA: dash/static/manifest.json (name "Database", short_name, id, start_url "/", scope "/", display standalone, background_color and theme_color #0E0E10, icons 192, 512, maskable 512); render PNGs from static/logo.svg into dash/static/icons/ plus apple-touch-icon 180; base.html head: link rel=manifest crossorigin="use-credentials", link rel=apple-touch-icon, meta mobile-web-app-capable, apple-mobile-web-app-capable, apple-mobile-web-app-title. No service worker (pages are private, no-store).
8. install/service-run.cmd (no pause, no browser, PYTHONUTF8=1, absolute .venv python) and install/install-service.cmd (Task Scheduler "At startup", run whether logged on or not, restart on failure) plus a daily `manage.py backup --to <other disk>` task.
9. Tests: /login contains rel="manifest"; manifest parses with 192 and 512 icons; HSTS present only when secure; idle hours read from .env.

Report: files changed, test count, commit hash.