# Secrets Checklist

None are required. The scraper runs free with no keys.
Optional keys go in `secrets\.env` (one `NAME=value` per line). Never paste a key into chat or a Settings file.

| Name | What It Unlocks | Cost |
|---|---|---|
| `IG_ACCESS_TOKEN` + `IG_USER_ID` | Measured Instagram posts in 30 days and followers (official Meta API). Needed to prove the "2 posts a month" benchmark | Free; needs your own Instagram Business account linked to a Facebook Page |
| `APIFY_API_TOKEN` | Instagram activity without any Instagram login; Google Maps data | Free plan has a small monthly credit (not re-verified today) |
| `SERPER_API_KEY` | Google review counts and ratings, which make the revenue estimate possible | Paid after a free trial (not re-verified today) |
| `GOOGLE_PLACES_API_KEY` | Google Maps as the business source instead of the free map | Free tier, then paid |
| `HUNTER_API_KEY` | Extra emails and decision-maker names | Free tier |

The local AI model needs no key. Its name goes in `Settings\Benchmarks And Rules.csv` (`LOCAL_LLM_MODEL`).
Full key list and where to get each: `F:\Github Repos\projects\lead-bot-worldwide\app\Secrets Guide.md`.
