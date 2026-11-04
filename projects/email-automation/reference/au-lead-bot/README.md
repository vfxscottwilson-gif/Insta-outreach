# Lead Bot v5 ($0, worldwide edition)

Daily lead generation for a video/social agency. It finds local businesses that can pay $500 to $1,000+ per month,
plus YouTube creators ($1k-2k):
- **Countries:** US, Canada, UK, Australia, New Zealand, Ireland; optional UAE, Saudi Arabia, Qatar.
- **Niches:** surgeons, dentists, clinics, real estate, boutique gyms, upscale restaurant groups, showrooms, builders
  and more.
- **Sources:** free maps, the business websites, free YouTube pages, and optional APIs.

**What it writes for each lead:**
- Facts-only contact data (company, decision maker, personal/generic emails, phone, socials, address, website).
- A Segment (PRIME … HAS-AGENCY), an ICP score, and a short **Lead Insight**.
- Each country goes to its own Google Sheet. Rows are **append-only**: never sorted or rewritten.
- **The lead bot never writes emails.** The outreach bot reads the sheets via [`../CONTRACT.md`](../CONTRACT.md)
  (a copy is in this repo as `CONTRACT.md`).

**Start here: [`00_START_HERE_SETUP_GUIDE.md`](00_START_HERE_SETUP_GUIDE.md)**, then:
- [`SHEETS_SETUP.md`](SHEETS_SETUP.md): up to 10 sheets plus the AU-only one; share each with the service account.
- [`SECRETS_GUIDE.md`](SECRETS_GUIDE.md): one GitHub secret per key, with format, free limit and what it unlocks.
- [`UPGRADE_V5.md`](UPGRADE_V5.md): what changed in v5, the tests, remaining risks.
- Older notes: [`UPGRADE_V4.md`](UPGRADE_V4.md) (segments, measured leads/day), [`UPGRADE_V3.md`](UPGRADE_V3.md),
  [`UPGRADE_V2.md`](UPGRADE_V2.md).

**Running it:**
- **On GitHub Actions:** `.github/workflows/run-lead-bot.yml`. The main program is `src/leadbot.py`.
- **Try it without Google:** `python src/leadbot.py --local --country US` writes `local_sheet/US/*.csv`.
- **Tests:** `python src/selftest.py` and `python -m unittest discover -s tests`.

**Australia-only edition:** `D:/All Automations Records/Lead generation/au-only-lead-bot`. Same code, with
`src/market.py` = AU, ABN columns, and its own single sheet `SHEET_ID_AU_ONLY`.
