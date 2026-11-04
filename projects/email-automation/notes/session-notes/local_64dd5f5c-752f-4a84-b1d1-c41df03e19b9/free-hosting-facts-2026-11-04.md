# Free hosting facts (checked 2026-11-04)

Method note: official pages fetched directly; third-party sources via web search (2025-2026). Where I could not get 3 independent sources I say so. Quotes are short and exact as returned by the fetch tool.

## 1. Vercel Hobby: commercial use
**Not allowed.**
- Fair use guidelines (https://vercel.com/docs/limits/fair-use-guidelines, last_updated 2026-09-14): "Hobby teams are restricted to non-commercial personal use only."
- Same page: "All commercial usage of the platform requires either a Pro or Enterprise plan."
- Definition: "any Deployment that is used for the purpose of financial gain of anyone involved in any part of the production of the project". Examples include "Advertising the sale of a product or service" and "Receiving payment to create, update, or host the site". Donations are not commercial.
- Terms of Service s.4 (https://vercel.com/legal/terms): "You shall only use the Services under a Hobby plan for your personal or non-commercial use."
- Plan page (https://vercel.com/docs/plans/hobby): "the Hobby plan restricts users to non-commercial, personal use only."
- Third party (2026): https://zplatform.ai/guides/is-vercel-free/ , https://convika.com/compare/vercel-hobby-commercial-use/ - both say Hobby cannot be used for commercial/business sites.
- Verdict: a small business app that serves a business = commercial. Hobby is not ToS-compliant. Pro is $20/month per seat (third party; not re-verified on pricing page).

## 2. Vercel Cron and Functions on Hobby
Cron (https://vercel.com/docs/cron-jobs/usage-and-pricing, updated 2026-07-15):
- Minimum interval: Hobby "Once per day". "Hobby accounts are limited to cron jobs that run once per day."
- Precision: "Per-hour (±59 min)"; "a cron job configured as 0 1 * * * ... will trigger anywhere between 1:00 am and 1:59 am."
- Count: table says 100 cron jobs per project on Hobby (changelog "Cron jobs now support 100 per project on every plan"). Some third-party pages still say 2; they look outdated. Sources disagree; official says 100.
- Expressions running more often "will fail during deployment".
- Independent confirmation: https://steadycron.com/guides/vercel-cron-limits/ and https://crontap.com/blog/vercel-cron-hourly-limit-and-how-to-beat-it (both: Hobby = once per day).

Functions (https://vercel.com/docs/functions/limitations, updated 2026-08-24):
- Max duration with Fluid compute: Hobby "300s (5 minutes)" default and maximum. Pro max 800s (1800s beta).
- Without Fluid compute: not verified (this page only documents the Fluid table; Fluid is default for new projects).
- Memory: Hobby "2 GB / 1 vCPU".
- Python: supported, versions "3.12 (default)", 3.13, 3.14 (https://vercel.com/docs/functions/runtimes/python). Runs as ASGI/WSGI web apps (HTTP-triggered), bundle 500 MB.
- Hobby monthly included (https://vercel.com/docs/plans/hobby and fair-use page): Function invocations "First 1,000,000"; Active CPU "4 CPU-hrs"; Provisioned memory "360 GB-hrs". Fast Data Transfer 100 GB.
- Over the limit: "you will have to wait until 30 days have passed before you can use the feature again."

## 3. Python worker on Vercel Hobby every 1-2 min?
**No.**
- Limiting rule 1 (ToS): Hobby is non-commercial only (section 1).
- Limiting rule 2 (technical): Hobby cron runs "once per day" with ±59 min precision. Every 1-2 min is impossible via Vercel Cron.
- Rule 3 (quota): even with an external pinger, 1-min runs of ~1-2 min = 720-1,440 min/day = 12-24 h/day. Active CPU cap is 4 h/month on Hobby; email/Gmail work is mostly I/O wait (which does not count as Active CPU per limits page: "Waiting for I/O ... does not count towards active CPU time") but provisioned memory 360 GB-hrs at 2 GB = 180 h/month, vs ~720 h needed. Not viable. (My arithmetic.)
- Per-run 300 s cap is fine for 1-2 min runs; it is not the blocker.

## 4. Cloudflare Pages Free and Netlify Free
Cloudflare Pages
- Limits (https://developers.cloudflare.com/pages/platform/limits/): Free "Builds per month" 500; "Cloudflare Pages sites can contain up to 20,000 files on the Free plan"; "limit of 100 projects"; 100 custom domains per project.
- Bandwidth: "On both free and paid plans, requests to static assets are free and unlimited." (https://developers.cloudflare.com/pages/functions/pricing/). Functions share the Workers Free daily quota (100,000 requests/day).
- Commercial use: Cloudflare ToS (https://www.cloudflare.com/terms/) has no non-commercial restriction on Free Services (s.2.6 only: may end Free Services "in our sole discretion"; s.2.2.1(h) bars processing credit card info on a property receiving Free Services). Third party: https://convika.com/compare/cloudflare-pages-commercial-use/ says allowed. Not stated as an explicit permission anywhere; "no restriction found" is the accurate wording.
- Third party limit confirmation: https://convika.com/compare/cloudflare-pages-limits/ (500 builds, 20,000 files, 25 MiB).

Netlify Free
- Credit plan (https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/credit-based-pricing-plans/): "300 credits/month with credit hard limit"; "You'll never be charged for the Free plan." Costs: 20 credits/GB bandwidth, 15 credits per production deploy, 2 credits per 10,000 requests.
- What happens at the limit: official page silent; third parties say sites pause until next month (https://www.stork.ai/blog/netlify-pricing-2026). Not verified officially.
- Commercial use: no non-commercial restriction found on the pricing/docs/terms-of-use pages; the governing Self-Serve Subscription Agreement PDF could not be read by my tool. Third parties (flexprice, costbench-type sites) say allowed. Status: not verified from the agreement itself.

## 5. Google Cloud Free Tier e2-micro
Source: https://docs.cloud.google.com/free/docs/free-cloud-features
- Regions: "1 non-preemptible e2-micro VM instance per month" in Oregon us-west1, Iowa us-central1, or South Carolina us-east1.
- Limit is by time: "Your Free Tier e2-micro instance limit is by time, not by instance."
- Disk: "30 GB-months standard persistent disk" (standard, not SSD).
- Egress: "1 GB of outbound data transfer from North America to all region destinations (excluding China and Australia) per month."
- Card: "A Google Cloud billing account is required to access the Google Cloud Free Tier." A new billing account comes via Free Trial which needs "a credit card or other payment method". So a card is required. Third party: https://www.lilachbullock.com/is-google-cloud-free/ , https://yangworks.dev/guides/google-cloud-free-tier-e2-micro (same).
- Time limit: none stated for the Free Tier; the $300 trial credit lasts 90 days (third party). Google "may change or eliminate the limits with 30 days' advance notice".
- Above limits: "Any usage that exceeds the Free Tier usage limits is billed at standard rates."
- Hidden cost: external IPv4 is billed (about $0.005/h, about $3.65/month per third party https://yangworks.dev/guides/google-cloud-free-tier-e2-micro). Official pricing page could not be read by my tool: not verified officially. Also egress beyond 1 GB/month is billed; Gmail API traffic is small but non-zero.
- Reliability for always-on Python (1 GB RAM): e2-micro has 2 shared vCPUs (burstable, ~0.25 vCPU baseline) and 1 GB RAM. Fine for a light I/O-bound job each 1-2 min. No SLA for free tier shown; "not verified". Real risk is memory pressure with big Python deps; add swap.

## 6. Oracle Cloud Always Free
- Idle rule (https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm): instance idle if during a 7-day period "CPU utilization for the 95th percentile is less than 20%", "Network utilization is less than 20%", and "Memory utilization is less than 20%" (memory test applies to A1 shapes only). Consequence on that page not captured by my fetch (third parties: instance stopped/reclaimed after notice).
- A1 allowance: "no more than 2 OCPUs and 12 GB of memory in total" (https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier.htm). Older 4 OCPU/24 GB is gone per this page; third parties disagree on the date (Aug 18 vs June 2026).
- Card: "most users need a mobile phone number and a credit card to create an account." "Your credit card will not be charged unless you upgrade your account." Third parties: prepaid/virtual cards rejected.
- A light worker will probably trip the idle rule (less than 20% CPU and network over 7 days). Real risk of reclamation. Also card required.

## 7. Supabase Free
- Pause: pricing page (https://supabase.com/pricing): "Free projects are paused after 1 week of inactivity." Edge Functions "500,000 included"; DB "500 MB"; egress "5 GB".
- Activity definition (https://supabase.com/kb/faqs/platform/free-project-pausing): "If a Free project gets too little database activity over a week, Supabase pauses it." and "Opening the project in the dashboard or sending real requests from your app both count as activity." and "A few requests a day is usually enough ... though that isn't a guarantee."
- A worker querying the database every minute: yes, real queries count as activity, so it would keep the project awake. Official text does not define the threshold ("not verified" exactly); community answer says queries/transactions count, a bare connection may not (https://github.com/orgs/supabase/discussions/51126). Use a real SELECT/UPDATE.
- Edge Functions (https://supabase.com/docs/guides/functions/limits): "Free plan: 150s" wall clock; "Maximum CPU Time: 2s"; "Maximum Memory: 256MB". Runtime is Deno/TypeScript, not Python.
- Edge invocation price above quota: "$2 per 1 million invocations" (paid plans only; Free shows "-") (https://supabase.com/docs/guides/functions/pricing).
- Free projects: "You are granted two free projects." (https://supabase.com/docs/guides/platform/billing-on-supabase)
- pg_cron on Free: Supabase Cron docs (https://supabase.com/docs/guides/cron) list no plan restriction; sub-minute allowed: "You can use [1-59] seconds ... as the cron syntax" on Postgres 15.1.1.61+. Recommended "no more than 8 Jobs run concurrently", "each Job should run no more than 10 minutes". Third parties say it works on Free; one (1bench.dev) claims Pro-only and conflicts. Status: likely yes, not verified on a live Free project. Easy test: enable it in Dashboard on the Free project.
- pg_cron can POST to an Edge Function or HTTP URL (pg_net), so it can act as a free every-minute trigger for an external HTTPS endpoint.

## 8. Other free ways to run a Python job every 1-2 min
GitHub Actions correction (one line): the schedule is unreliable (docs: "The schedule event can be delayed during periods of high loads"; "some queued jobs may be dropped"; "shortest interval ... once every 5 minutes", https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows). So 1-2 min is impossible. On email: the Acceptable Use Policy bars "relay any form of unsolicited advertising or solicitation through our servers" and "sending unsolicited emails to users" (https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies). It bars unsolicited, not all, email; the "terms bar sending email" claim is only partly right. Also a 2-min schedule at about 1-2 min per run uses over 40,000 min/month on a private repo (my arithmetic; free private allowance not verified, the page did not state it).
Options:
1. Free-tier VM: GCP e2-micro (card needed, US region, watch IPv4 charge). Most realistic truly-free always-on option.
2. Oracle Always Free (card; idle reclaim risk).
3. The owner's own PC/server as the worker (free, but not always on).
4. Cloudflare Workers Free Cron Triggers: 5 per account, but "10 ms" CPU per cron invocation on Free (https://developers.cloudflare.com/workers/platform/limits/). That is a JS trigger only, not a 1-2 min Python run. Useful only as a pinger to wake another host.
5. Supabase pg_cron + pg_net to call an HTTPS endpoint (the worker), but the worker still needs a host.
6. Paid fallbacks (not free): Vercel Pro $20/mo (third party) enabling per-minute cron; a small VPS.
Not verified: any free PaaS (Render, Fly, Railway etc.) was not checked; do not assume free.

## Disagreements / not verified list
- Vercel Hobby cron count: official 100; some third parties say 2 (outdated).
- Vercel function max duration without Fluid compute: not verified.
- Netlify commercial use from the Subscription Agreement: not verified (PDF unreadable).
- Netlify behaviour at 300 credits: third party only.
- GCP external IPv4 charge: third party only.
- Oracle reclamation consequence and A1 cut date: official page partial; third parties conflict on date.
- Supabase pg_cron on Free and exact "activity" threshold: not verified officially.
