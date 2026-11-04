# ROADMAP: what to do, in order

Goal: 400 drafts a day minimum, 700 target. You send by hand for now.

1. **Setup**: `START_HERE.md` steps 1-10 (Outreach sheet, sharing, secrets, dry run, Options, Email Rules).
2. **Keys**: 2-3 Gemini keys, each made in its OWN new Google Cloud project (keys in one project share one quota),
   plus Groq, and Mistral (optional). Run **diagnose-keys** after adding them.
3. **First week**: `DAILY_TARGET` 100-200 while you check the wording. Tighten the **Email Rules** tab.
4. **Inboxes**: pick an option from `INBOX_OPTIONS.md`. For manual sending from several accounts, switch on
   `INBOX_ROTATION` and `FOLLOW_UPS`.
5. **Later**: a cold-email platform (Instantly / Smartlead) or the parked sender (`phase2_parked/`).

## Realistic AI drafts a day (measured: about 1,300 input + up to 1,100 output tokens per 5-email batch)

Formula: AI emails a day = daily requests x 5 (BATCH_SIZE). For Groq the token cap is usually the limit:
tokens a day / about 2,200 tokens per batch x 5. With FOLLOW_UPS On, output is about 60% larger.

| Source | Free daily cap (check your own page) | AI emails a day |
|---|---|---|
| 1 Gemini project, `gemini-2.5-flash-lite` | your RPD in AI Studio > Usage > Rate limits | RPD x 5 |
| + `gemini-2.5-flash` in the same project | its own separate RPD | RPD x 5 |
| Groq account, `llama-3.1-8b-instant` | about 500K tokens a day (last published) | about 1,100 |
| Groq account, `llama-3.3-70b-versatile` | about 100K tokens a day | about 225 |
| Mistral free plan, `mistral-small-latest` | per-second limit + monthly token cap (console > Limits) | a few hundred, while the monthly cap lasts |
| OpenRouter, no credit / $10 credit | 50 / 1,000 requests a day | 250 / up to 5,000 |
| Built-in template (`TEMPLATE_FALLBACK=On`) | none | unlimited |

**Realistic result**: 1 Groq account + 2-3 Gemini projects + Mistral gives about **400-700 AI drafts a day**. The
AI Usage tab shows your real numbers after day one. Leads that are not reached simply wait for the next day,
unless you switch the template on.

**Sheets quota** (measured in the selftest): reading 11 lead sheets and writing 700 drafts takes about
60 reads + 43 writes, about 3.5 minutes of sheet traffic.
- Reads are spaced 3.2 seconds apart, so at most 19 a minute. The lead bot shares the same service account and the
  60-reads-a-minute limit, so this follows CONTRACT.md 4.6.
- Writes run at about 30 a minute or fewer.
- Each lead sheet costs 2 reads: the tab list, plus ONE batched read of all its lead tabs and its Blacklist tab.
