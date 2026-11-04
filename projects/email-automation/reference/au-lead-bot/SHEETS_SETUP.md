# SHEETS_SETUP: up to 10 Google Sheets (worldwide) + 1 (Australia-only edition)

The worldwide bot (v5) writes each country to its own Google Sheet, plus one worldwide YouTube sheet:

| Sheet | GitHub secret | Filled by job | Tab 1 |
|---|---|---|---|
| Leads – United States | `SHEET_ID_US` | `collect (us)` | **Master Dashboard** (all sheets), tab 2 = **US Stats** |
| Leads – Canada | `SHEET_ID_CA` | `collect (ca)` | Stats |
| Leads – United Kingdom | `SHEET_ID_GB` (`SHEET_ID_UK` also works) | `collect (uk)` | Stats |
| Leads – Australia | `SHEET_ID_AU` | `collect (au)` | Stats |
| Leads – New Zealand | `SHEET_ID_NZ` | `collect (nz)` | Stats |
| Leads – Ireland | `SHEET_ID_IE` | `collect (ie)` | Stats |
| Leads – UAE *(optional)* | `SHEET_ID_AE` | `collect (uae)` | Stats |
| Leads – Saudi Arabia *(optional)* | `SHEET_ID_SA` | `collect (saudi)` | Stats |
| Leads – Qatar *(optional)* | `SHEET_ID_QA` | `collect (qatar)` | Stats |
| Leads – YouTube (worldwide) | `SHEET_ID_YOUTUBE` | `collect (youtube)` | Stats |
| *Australia-only edition (separate repo)* | `SHEET_ID_AU_ONLY` | its own workflow | Stats |

A missing secret is fine. That job prints `SKIP <country>: no SHEET_ID_<country> secret set` and ends green, and the
Master Dashboard lists it under "Sheets skipped". Start with one or two countries if you like. No US sheet? The
Master Dashboard then goes to the first sheet that exists.

## Step 1. Find the robot's email (2 minutes)

The bot logs in as a Google **service account**. Its email ends in `.iam.gserviceaccount.com`. Find it in **Google
Cloud Console** → your bot's project → **IAM & Admin → Service Accounts**: copy the email from the "Email" column.

You can also open the key file you downloaded for `GOOGLE_SA` and copy the value of `"client_email"`. Do that
yourself, and never share or upload the file: it is the robot's password.

## Step 2. Create the sheets and share each one (2 minutes per sheet)

For each sheet you want:
1. **Create it:** go to sheets.new and name it, e.g. `Leads – United States`.
2. **Share it:** click **Share** → paste the robot email → choose **Editor** → untick "Notify people" → **Share**.
   Without Editor access, that job fails with "no access. Share it with the service-account email as Editor".
3. **Copy its id:** the part of the address between `/d/` and `/edit`, e.g.
   `https://docs.google.com/spreadsheets/d/`**`1AbC...xyz`**`/edit`. You may also paste the whole URL as the secret.

Leave the sheets empty. The first run creates every tab.

## Step 3. Add the secrets in GitHub (5 minutes)

Repo → **Settings → Secrets and variables → Actions → New repository secret**, once per sheet: `SHEET_ID_US`,
`SHEET_ID_CA`, `SHEET_ID_GB`, `SHEET_ID_AU`, `SHEET_ID_NZ`, `SHEET_ID_IE`, `SHEET_ID_AE`, `SHEET_ID_SA`,
`SHEET_ID_QA`, `SHEET_ID_YOUTUBE`. The value is the id from Step 2. Keep `GOOGLE_SA` as it is.

- All other keys are optional, with **one secret per key**: see **[SECRETS_GUIDE.md](SECRETS_GUIDE.md)**.
- The old single `SHEET_ID` is used only when **no** `SHEET_ID_*` secret exists.

## Step 4. Run it

**Actions → Run Lead Bot → Run workflow.** You will see `setup`, then the `collect (...)` jobs (5 at a time), then
`finish`.
- The first log lines of every job are the **registration report** (which keys were accepted).
- Each sheet gets a **Run Log** row and an updated **Stats** tab.

## Step 5 (only if you are coming from the old single sheet): avoid re-adding old leads

Duplicates are tracked per sheet: the **Seen** tab plus every `Place Id` already in the lead tabs. After the first
run, copy the old sheet's **Seen** rows (without the header) under the header of each new sheet's **Seen** tab.

## What you get in every sheet

- **Tab 1, Stats** (Master Dashboard + US Stats in the US sheet):
  - Totals, leads today, PRIME count, last run time and run health, and the keys registered.
  - One row per niche with total / today / PRIME / segment counts / progress bar.
  - **Values are overwritten in place every run.** No new row is added per day.
- **Hidden `Meta` tab:** the bot's own counters, run health and a write lock. Don't edit it. Unhide it via
  View → Hidden sheets if you're curious.
- **One tab per niche.** **New leads are always added BELOW the last row. Rows are never sorted, moved or rewritten.**
  - Your `Status`, `My Notes` and any columns you add yourself are safe.
  - You may reorder columns or add your own: the bot finds columns by their header name.
  - Use a Google Sheets filter view (Data → Filter views) to sort for yourself without changing the real order.
- **Lead columns:**
  - Front: `Niche, Group, Segment, ICP Score /10, Tier, Revenue Band, Company Name, Decision Maker Name, First Name, …
    Personal Email, Generic Email, Other Emails, Phone, socials, Website, address…`
  - Then **`Lead Insight`**: 3-4 lines on who they are and their likely pains. The lead bot **never writes email
    drafts**; the outreach bot does (see `CONTRACT.md`).
  - The evidence columns come after `Place Id`.
- **Old v4 tabs:** `Dashboard` and `All Leads` are no longer updated. Delete them whenever you like. Old `Case Study`
  / `Email Subject` / `Email Draft` columns stay in old tabs and are left blank on new rows.

## The YouTube sheet

One tab per YouTube niche.
- **Gates** (Rules tab, editable):
  - Subscribers **20,000–500,000**.
  - Last upload within **14 days**.
  - Median views of the last ~5 videos **≥ 20,000**.
- **Country:** channels with an unknown country are allowed; their `Country` cell is blank.

## Limits the bot respects

- **Google Sheets reads (60/min per service account, shared by all jobs).** Each job reads all its control tabs in 1-2
  batched requests and its lead tabs in 2-4. Jobs start 20 s apart, 5 at a time, and back off on 429.
- **Sheets writes (300/min per project).** About 4 writes per search.
- **10,000,000 cells per sheet.** The bot stops adding rows at 9.5M (Rules › `CELL_LIMIT_STOP`) and shows an ERROR in
  Run health. A busy country sheet grows by roughly 20,000-30,000 cells/day, mostly the `Seen` tab (6 columns per
  business checked). That is about a year before the limit. When the Stats tab shows trouble, delete `Seen` rows that
  start with `Rejected:` and are older than 120 days; they are re-checked anyway.
