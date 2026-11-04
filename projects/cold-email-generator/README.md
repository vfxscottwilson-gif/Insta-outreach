# Cold Email Generator

Turns a lead sheet into a ready-to-send file: first email plus 4 follow-ups per lead, ICP score, Arial 11.

## Run (needs Python 3, `pip install openpyxl gender-guesser`)
```
python app/gen_emails.py            # YT pilot: 12 rows
python app/gen_emails.py --full     # YT full batch
python app/gen_restaurant_emails.py --full
python app/check_rules.py "<output.xlsx>" yt     # or: rest
```
Input/output paths are set at the top of each script (Downloads folder).

## Rules
All rules are in `docs/MASTER-PROMPT.md` (paste it into a new chat with each new lead sheet).

## Status / next step
- 2026-11-05: both generators rebuilt, rule checker 0 violations (YT 539 rows, restaurants 1,909 rows). Independent review pending.
- Scripts need a copy of this file path in `INPUT_FILE`/`OUTPUT_FILE` when moved to another PC.
- No secrets used.
