# START HERE: Email Draft Generator

Turns a lead sheet into one row per email: Email, Name, Subject Line, Body, Follow-up 1 to 4. Runs on your PC. No paid service, no API key.

## What you get
- **Ready To Send** tab: the finished drafts (row height 21, Title Case headers, Arial 11).
- **Needs Review** tab: drafts that failed a benchmark, with the reason. Never send these without reading them.
- **Report** tab: emails in, duplicates removed, emails out, mix of email types, minutes taken.
- Bodies start without "Hi" and end with a sign-off, so your Google Apps Script keeps adding "Hi Name,".

## One-time setup (about 20 minutes)
1. **Python 3.11 or newer.** Download from python.org/downloads. In the installer, tick **Add python.exe to PATH**. Check: open Command Prompt, type `python --version`.
2. **Project libraries.** Double-click `install\INSTALL.cmd`. It installs: openpyxl, pandas, httpx, wordninja, gender-guesser. (Needs internet once.)
3. **Ollama (the local model, optional but recommended).** Download from ollama.com/download and install. Then in Command Prompt:
   ```
   ollama pull qwen3:4b
   ```
   If that name is not found, open ollama.com/library, pick a **4B instruct** model, and put its exact name in `config\settings.toml` under `[llm] model`.
4. **Check everything:**
   ```
   python app\run.py --check
   ```
   You should see the Ollama line, your GPU temperature and "Template lint: all clean".

## Your sheet (xlsx or csv)
One header row. Column names are found automatically. Only **Email** is required.

| Column | Example | Used for |
|---|---|---|
| Email | `info@x.com; owner@x.com` | several emails in one cell become several rows |
| Niche | YouTube, Restaurant, Real Estate, Showroom, Ecommerce, SaaS | picks the template pack; blank = detected, then safe generic pack |
| Name | Maria | first name for the Name column |
| Business (or Channel / Company) | DeliciousKitchen | business name, split and cleaned automatically |
| City, Cuisine | Calgary, italian | restaurant lines |
| Website | https://... | read politely (title and description only) |
| Video Title (or Pitch Angle) | Saw "My video title" | quoted only when complete and clean |

If your sheet has no Business column, the **Name** column is treated as the business name.

## Run it
```
python app\run.py --input "C:\path\leads.xlsx" --out "C:\path\drafts.xlsx"
```
Useful flags: `--sheet "Sheet name"`, `--limit 50` (test on 50 first), `--no-llm`, `--no-scrape`, `--fresh` (start over).

**Always pilot first:** run with `--limit 20`, open the file, read it, then run the full sheet.

## If it stops (power cut, crash, closed window)
Run the **same command again**. It remembers every finished lead (file `drafts.xlsx.state.db` beside the output) and continues. If you changed the sheet or the settings, it refuses and asks for `--fresh`, so two different runs never mix.

## Change things yourself (no coding)
- `config\settings.toml`: word ranges, the 30/30/40 mix, how often "I" appears (15-20%), subject length, model name, GPU temperature limits.
- `config\templates.toml`: every sentence, per niche: openers, expert lines, value lines, option sets, CTAs, sample lines, follow-ups, sign-offs. After editing, run `python app\run.py --lint`. Any line with a banned word or symbol is reported.

## What the benchmarks enforce (every email, every follow-up)
- Only commas, periods, question marks. No + ; : = | & ( ) ! dashes except inside words and 30-60.
- Offence list: no fix, improve, low, weak, losing, missing, better, fuller, stronger, problem and similar. Options must be growth goals.
- No "help ... grow" line, no tool lists, no repeated 4-word phrase inside one email.
- Sample line always has 30-60 second and zero cost, no cost or free of cost. Bare "free" is not allowed.
- Word ranges: short 50-60, normal 70-80, options 80-90, follow-ups 40-70. Last follow-up never pitches.
- Options: exactly 3, each 2-6 words, then `Just reply with 1, 2, or 3.` on its own line.
- Business names may gain spaces but never change a letter.

## How the follow-ups work
- First email has the 1, 2, 3 options: Follow-up 1 is a normal reminder, Follow-up 3 is the options email.
- First email has no options: Follow-up 1 is the options email, Follow-up 3 is a normal reminder.
- Follow-up 2 is always a different angle. Follow-up 4 is the last touch, no pitch.
- Send them as replies in the same thread.

## Facts only: how it avoids guessing
- It uses only what is in your sheet and the title and description of the lead's own homepage.
- It never states follower, view, upload or revenue numbers, and never says anything is weak.
- Openers are expert observations about the niche tied to the lead's name, city, cuisine or a complete video title.
- A first name is used only if you wrote it or a personal email handle is a dictionary name. Shared mailboxes (info, hello, care, careers, partnerships, sales...) get Name = Team.

## Time and safety
- Without the model: about 1,500 drafts in under a minute (measured). With the model checks on, allow a few seconds per lead. The tool prints minutes left every 25 leads.
- **Your GPU fans do not work.** The tool pauses when the card passes the limit (default 78 C) and resumes below 70 C. Fix the fans before any 5,000-lead overnight run.
- Close Excel before re-running with the same output name.

## Not in version 1 (on purpose)
- The model does not write whole emails. Wrong facts are the biggest risk of a 4B model, so templates plus checks write the text. The model classifies the niche when unclear and gives a second opinion on offence.
- instructor, litellm and dspy are installed later only if needed: instructor when the model must return structured data, litellm to swap models, dspy to tune prompts once you have reply data. langchain and vllm are not used.
- Instagram and other social pages are not scraped.

## Troubleshooting
| Symptom | Fix |
|---|---|
| `python` not found | reinstall Python with Add to PATH ticked |
| `No email column found` | rename the header to Email or set it in settings.toml `[columns]` |
| "Ollama is not running" | start Ollama, or ignore: the tool works without it |
| Many rows in Needs Review | read the Reason column, fix the template line it names, run `--lint`, `--fresh` |
| "input or config changed" | add `--fresh` |
| Excel file will not save | close it in Excel, run the same command again |
