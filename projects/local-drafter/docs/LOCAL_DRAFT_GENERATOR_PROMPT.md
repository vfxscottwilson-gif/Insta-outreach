# BUILD PROMPT: Local AI cold-email DRAFT generator (Windows PC, Ollama / LM Studio, Google Sheets)

(MODE: AUTOPILOT. Run the pre-flight, choose the best option for every unspecified decision, record decisions in a table, and start building. Ask only about true blockers.)

You are a senior Python engineer and cold-email specialist. Build a tool that runs on **my own Windows PC**, uses a **local open-source LLM** (via Ollama or LM Studio), reads a Google Sheet of leads, and writes finished **draft emails** into another Google Sheet. It does **not** send anything.

## 1. Context

- I am a video editor and motion designer. I email YouTubers (and sometimes other niches: restaurants, real estate, auto, etc.) offering a sample edit of 30–60 seconds **at no cost**.
- Workflow today: I paste drafts into a Google Sheet that is connected to a Google Apps Script. When I press its "draft" button, the script creates Gmail drafts and **adds the greeting ("Hi {First Name},") and the signature automatically**. Therefore this tool must **not** write a greeting, the first name or a signature.
- Hardware/software: Windows PC, NVIDIA RTX 5060 Ti (16 GB VRAM), VS Code, Python installed, Ollama and/or LM Studio. I expect to use roughly 4B–14B parameter models (quantized).
- It runs on demand: I start it, it processes **every lead in the input sheet**, and it stops when the leads are finished.
- Everything free. Data stays on my PC except Google Sheets and the optional YouTube API.

## 2. Inputs

- A Google Sheet "Leads" tab (URL/ID and tab name in `config.yaml`), or a local `.csv/.xlsx` (config option `INPUT_MODE = sheet | file`).
- **Do not rely on exact headers.** Detect them: find the header row in the first 10 rows; map columns by fuzzy header aliases and by content sniffing (the column of email-shaped values is Email; YouTube/website/social URLs by pattern; niche; country; name/channel/company; notes; latest video). Print the detected mapping in the console and write it to the `Log` tab; allow overrides in `config.yaml`. If no email column is found, stop with a clear message.
- Never send these columns to the AI: prices, scores, subscriber counts, revenue, "my notes".
- Multiple emails in a cell: take the first valid one. Skip blank, invalid, duplicate (within the sheet and already present in the output sheet or `Log`) and role/blocked addresses (noreply, postmaster, abuse, example.com, test.com) according to settings.

## 3. Outputs

**Output sheet, tab `Ready to Send` (exactly four columns, A to D, nothing else in those columns):**

| A | B | C | D |
|---|---|---|---|
| Email | First Name | Subject | Body |

- Row 1 is the header. New drafts are appended below the last filled row. Columns E onward are never touched. Write cells as **RAW** (never USER_ENTERED), so text starting with `=`, `+`, `-` or `@` is not treated as a formula.
- **First Name** is taken from the sheet/email using these rules (ported from my old generate.py): from the name column; reject brands, multi-word titles and handles; strip titles (Dr, Mr, Muhammad, Mohammed, etc.); fall back to a clean `first.last` pattern in the email's local part; if nothing is trustworthy, write the fallback `FIRST_NAME_FALLBACK` (default `Team`, as my script expects). Capitalize properly. The name is for the Apps Script only; it must **never** appear inside the body.
- Separate tab **`Log`**: row, email, result (written / skipped / failed / needs review), reason, word count, retries, model used, seconds, timestamp. A tab **`Needs Review`** (optional) for drafts that failed a soft rule after all retries; those are **not** written to `Ready to Send` unless `WRITE_UNVERIFIED = true`.
- Write in batches (e.g. every 10 drafts) so a crash loses little. A `state.json` file (git-ignored) tracks processed emails so **re-running resumes** without duplicates.

## 4. Email format (strict)

The body text that goes into column D is assembled by **code**:

```
{opening sentence, naming the YouTube channel or company}

{one sentence on what they may be missing}

{what I offer, including the no-cost sample}

{ONE question, always the last sentence of the AI text}

Not Interested, Reply "Unsub".

{sign-off},
```

- **80–90 words** for the AI-written part (the four paragraphs above), counted by code. The opt-out line and the sign-off are not counted.
- The body **starts at the very first character** with the opening sentence: no leading spaces, blank lines or tabs. It **ends with the sign-off's comma** (e.g. `Best regards,`): no trailing space, newline or text after it. Code must `strip()` and assert this before writing, and tests must check it.
- Sign-off chosen by code from a list in config (default: `Best regards,`, `Kind regards,`, `Thanks,`, `Cheers,`), by weight and optionally by country (e.g. Australia: more `Cheers,`). 
- The opt-out line is configurable (`OPT_OUT_LINE`, default `Not Interested, Reply "Unsub".`, `INCLUDE_OPT_OUT = true`). Compliance note: US/Canada/Australia require a working opt-out. If my Apps Script already adds one, I turn this off.
- **Possible conflict to flag and test:** if my Apps Script also appends "Best regards," the sign-off would appear twice. Add `SIGN_OFF_MODE = in_body | none`, and a `--test-handoff` command that writes 3 sample rows so I can press the draft button and verify there is no duplicate greeting, duplicate sign-off, extra blank lines or missing signature.
- Paragraphs separated by one blank line; plain text; no markdown, bullets (setting `ALLOW_BULLETS`, default false), numbered lists, links, emojis or exclamation marks.
- **Subject:** 2–6 plain words, ≤ 40 characters, no clickbait, no all caps, no "Re:", no "free". Generated by the model but validated by code; if invalid, rebuilt from a small subject template (e.g. "Quick idea for {Channel}", "Editing help for {Channel}").

## 5. Email rules (these go to the AI in compact form; the code enforces them all)

- Sender: one person, video editor and motion designer, who works with YouTubers and brands (long-form editing, Shorts/Reels, motion graphics). Write as "I"/"me". Never "we", "our team". Never a company name, my name, or anyone's name in the body. Never say "free" (setting `ALLOW_WORD_FREE`, default false). Instead use one of: "at no cost", "no cost to you", "on me", "complimentary", "nothing to pay", exactly once, **only** about the 30–60 second sample. The code chooses the phrase and tells the model to use it; the validator checks it.
- Structure: (1) opening: one short sentence about THEM that names their YouTube channel exactly as written in the data (for non-YouTubers, the company name plus one fact); (2) middle: one short sentence on what they may be missing, tied to the lead's ANGLE; (3) what they get: my role + the sample (one sentence); (4) ONE easy question, always last: ask them to reply with a clip or a video link.
- At most 2 sentences per paragraph, every sentence under 20 words, plain everyday words, readable on a phone.
- Use ONLY facts in LEAD DATA. Never invent numbers, names, clients, results. Copy channel names, numbers and quoted video titles exactly (quoted titles in double quotes). Use at most ONE other specific fact besides the channel/company.
- Never say or imply you watched, read, visited or noticed anything. "Came across" is the maximum. Banned verbs: watched, saw, noticed, loved, enjoyed, checked out, visited, read, followed.
- Never comment on subscribers, views, income, budget, prices. Never criticise their videos. Never say they "need an editor".
- Banned words: guarantee, discount, risk-free, limited time, act now, no obligation, click here, urgent, (and `free`).
- No greeting (Hi, Hello, Hey, Dear) and **no occurrence of the lead's first name** in the body.
- If data is thin (`LOW_DATA = yes`): talk only about their niche, mention no video or detail, still include the no-cost sample.
- Vary openings: the code assigns each lead a `STYLE` (opening pattern) and rejects drafts whose first 5 words repeat any of the last 30 drafts.
- Angles per row: `pain` (a likely problem as an observation, never a claim about them), `missed` (one possibly under-used opportunity: Shorts, motion graphics, consistent style), `default`. The **code** picks the angle and one candidate "possible gap" from a small niche table, using facts derived from the data (e.g. upload cadence computed from dates; Shorts vs long-form mix computed from durations). The model only phrases it as a possibility. This removes guesswork and hallucination for small models.

## 6. Research layer (a local model cannot browse, so code gathers the facts)

- **YouTube** (optional `YOUTUBE_API_KEY` in `.env`, free quota 10,000 units/day): resolve channel from URL variants (`/@handle`, `/channel/UC…`, `/user/…`, `/c/…`, or a video link) using cheap calls; fetch title, description, and the latest ~5 upload titles with dates and durations. Disable itself gracefully on 400/403 (quota or key) and continue without YouTube.
- **Website/links:** fetch the lead's website (first ~1,500 characters of text) and an "About" page (~900 characters) with a polite User-Agent, 8-second timeout, size cap, and robots-friendly behaviour. Skip social-media domains (LinkedIn, Instagram, Facebook, X/Twitter, TikTok), which block scraping. Extract at most 3 extra non-social links from a Socials column. Cache results on disk so re-runs don't refetch.
- Treat all fetched text as **untrusted** (prompt-injection risk): strip it to plain text, cap its length, wrap it in a clearly labelled data block, and tell the model to ignore any instructions inside it.
- Compile a compact `LEAD DATA` block (about 150–300 tokens): channel/company name, niche, 3 recent titles (exact), cadence/format facts, one-line description, country. Nothing else.

## 7. Local AI layer (model-agnostic: restricted to the API, not the model name)

- Config: `AI_BACKEND = ollama | lmstudio | openai_compatible`, `BASE_URL` (defaults: Ollama `http://localhost:11434`, LM Studio `http://localhost:1234/v1`), optional `MODEL`. If `MODEL` is blank, list installed/loaded models (`/api/tags` or `/v1/models`) and pick one by a configurable preference list (instruction-tuned chat models of roughly 8B–14B first; skip embeddings, vision-only, "thinking/reasoner" and base models). Never hardcode a model name anywhere else.
- Start-up checks: server reachable (if not, print how to start Ollama/LM Studio), model present, a 10-token test call works, GPU offload reminder (in Ollama run `ollama ps` and confirm 100% GPU).
- Request settings in config: `temperature` 0.6–0.7, `top_p` 0.9, `max_tokens` ~320, `num_ctx` 4096, thinking/reasoning mode **off** (pass the model-appropriate switch if supported, and strip any `<think>…</think>` blocks defensively), `keep_alive` to hold the model in VRAM, and a request timeout.
- **Structured output:** ask the model for JSON `{"subject": "...", "opening": "...", "missing": "...", "offer": "...", "ask": "..."}` using the backend's JSON/schema mode where available (Ollama `format`, LM Studio `response_format`), with tolerant JSON parsing as fallback. Give each part a word budget (≈ 18 / 22 / 32 / 12 = 84 words) so total length lands in 80–90. Code assembles the paragraphs.
- **Validate in code, not in the model:** word count 80–90; sample phrase present exactly once; channel/company name present and exact; every number/quoted title exists in LEAD DATA; no banned words/verbs/characters; no first name; no greeting; last sentence is one question; no sentence over 20 words; paragraph count. On failure: up to `MAX_RETRIES` (default 3) targeted repair calls that send only the failing part plus the exact error ("opening is 31 words, must be 15–22; shorten it"); lower temperature on retries; then the deterministic template fallback and mark `needs review`.
- **Deterministic template fallback** with several variants per section (so even fallback emails vary), filled from LEAD DATA.
- Speed: process leads sequentially by default (`CONCURRENCY = 1`, optional 2); show a progress bar with ETA, drafts/min, and retry counts. Expect roughly 5–10 seconds per draft on this GPU.
- Log tokens and seconds per draft (no cost; local).

## 8. Google Sheets access

- Auth by **service account** JSON file on my PC (path in `.env`; git-ignored). I share the input sheet (viewer) and output sheet (editor) with the service account's email. Include step-by-step setup (Google Cloud project, enable Sheets API, create service account, share sheets).
- Read each tab once per run; write in batches with `batchUpdate`; backoff on 429.
- The output spreadsheet can be a new tab in the same file or a separate file (config); the tool creates the `Ready to Send`, `Log` and `Needs Review` tabs if missing.

## 9. CLI and files

```
python draft_emails.py                 # process every lead until done
python draft_emails.py --limit 5       # small test
python draft_emails.py --dry-run       # no sheet writes; print drafts
python draft_emails.py --test-handoff  # writes 3 sample rows for the Apps Script test
python draft_emails.py --check         # health check only
```

Files: `draft_emails.py` (single main file is fine, or a small package), `config.yaml`, `rules.md` (the compact AI rules, editable), `templates.yaml` (fallbacks, subjects, sign-offs, niche→angle table), `.env.example`, `requirements.txt`, `.gitignore`, `run.bat` (activates the venv and runs), `tests/`, `START_HERE.md`. Dependencies: `gspread`, `google-auth`, `requests`, `PyYAML`, `python-dotenv`, `tqdm`, `pandas`/`openpyxl` only if `.xlsx` input is needed. 

## 10. Fail-safes (must be implemented and tested)

Resume after crash or closing the window (state + checking the output sheet); duplicates across runs; one bad row never stops the run; the model server dying mid-run (wait, retry, resume); Google API 429/5xx backoff; YouTube quota/403; website timeouts; empty/huge fields; Unicode channel names (preserve exactly); non-English channels (still write English, quote titles exactly); body whitespace assertions; formula-injection safety (RAW writes); sheet cell limits; Windows sleep (document how to stop the PC from sleeping, or use `SetThreadExecutionState` during the run); accidental double start (lock file); API keys never printed; `Ctrl+C` finishes the current draft and saves state.

## 11. Tests and acceptance

- Unit tests: header detection on 3 differently structured sample sheets; first-name rules; word-count window; no leading/trailing whitespace and last character is a comma; validator catches each banned thing; sign-off rotation; subject rules; resume logic; JSON parsing from messy model output.
- Manual acceptance: run `--limit 5` on real leads; review; run `--test-handoff`, press my Apps Script button, and confirm the Gmail drafts look right (greeting once, signature once, sign-off once). Then run the full sheet.

## 12. Documentation

`START_HERE.md`: install Ollama/LM Studio, how to pull and pick a model for 16 GB VRAM (a 12B–14B Q4/Q5 instruct model usually follows rules better than 4B–8B; 8B is the fast option), how to confirm GPU use, Google Cloud service-account setup, getting a YouTube API key, running, reading the Log, fixing the top errors, changing rules/templates/sign-offs/opt-out line, and a "first real run" checklist (5 leads → check → 50 → full).

## 13. Open items (placeholders, flag in START_HERE.md)

My Apps Script behaviour regarding sign-off/opt-out (resolved by `--test-handoff`); my postal address lives in the Apps Script signature (required by CAN-SPAM/CASL/Spam Act); which niches beyond YouTubers need their own angle tables.
