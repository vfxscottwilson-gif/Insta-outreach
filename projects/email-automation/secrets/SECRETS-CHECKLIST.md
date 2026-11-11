# Secrets checklist (names only, DRAFT)

Names taken from `app\.env.example`. NEVER write values here. Real values live in `app\.env` and your password manager.

| Secret name | Used by | Where to get it |
|---|---|---|
| SUPABASE_URL | engine, web | Supabase dashboard > Project Settings > API |
| SUPABASE_SERVICE_ROLE_KEY | engine | Same page, service_role key (server only) |
| SUPABASE_ACCESS_TOKEN | CLI/migrations | Supabase dashboard > Account > Access Tokens |
| DATABASE_URL | engine, migrate | Supabase > Connect > Session pooler URI |
| GOOGLE_OAUTH_CLIENT_ID / GOOGLE_OAUTH_CLIENT_SECRET | Gmail sending | Google Cloud > APIs & Services > Credentials (see START_HERE part B) |
| GOOGLE_SA_JSON | Reading lead sheets | Google Cloud service account key (START_HERE part D) |
| GEMINI_API_KEY / GROQ_API_KEY | AI writing | Provider dashboards |
| CLOUDFLARE_ACCOUNT_ID / CLOUDFLARE_API_TOKEN | Deploy web app | Cloudflare dashboard |
| ADMIN_EMAIL / ADMIN_INITIAL_PASSWORD | First admin login | You choose; change after first login |
