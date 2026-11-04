# 02 Architecture

- Front end: none. The Google Sheet is the interface.
- Back end: one Python script, `app\organizer.py` (read Inbox, AI classify, validate in code, file, rebuild summary tabs).
- Hosting: GitHub Actions (`app\.github\workflows\organize.yml`, daily, with a run lock). Database: the Google Sheet.
- Data flow: Inbox rows (+ optional Figma stickies) -> AI picks type/status/priority/dates -> code validates -> filing tabs, `Review Needed` for unclear notes, `_Ledger` remembers what was filed -> `Attention Needed` and `Monthly Summary` rebuilt.

| Want to change | File |
|---|---|
| Everything about filing, AI prompt, tabs | `app\organizer.py` |
| Schedule, env wiring | `app\.github\workflows\organize.yml` |
| Python packages | `app\requirements.txt` |
