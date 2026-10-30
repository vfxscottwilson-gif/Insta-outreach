"""One-click send helper (runs on YOUR computer, not on GitHub).

For each due row in 'Today Queue' it:
  1. waits until the suggested time,
  2. opens that lead's DM chat in the Chrome PROFILE of the right account,
  3. copies the message to your clipboard,
  4. waits for you to paste + press Enter in Instagram, then press Enter here,
  5. stamps Done / Sent At in the sheet and updates Outreach Log (date sent, stage, follow-up dates).

It does NOT type into Instagram or log into anything for you: you stay the sender.
Setup: pip install gspread google-auth tzdata ; create profiles.json (see profiles.example.json) ;
set env vars GOOGLE_SERVICE_ACCOUNT_JSON (path to the JSON file), SHEET_ID, TIMEZONE.
Run:  python send_assist.py            (all accounts)     python send_assist.py acc1 acc2   (only those)
"""
import json
import os
import platform
import shutil
import subprocess
import sys
import time
from datetime import datetime
from zoneinfo import ZoneInfo

import main as M
from main import Q, env, pad, yes, retry
from gspread.utils import rowcol_to_a1


def chrome_path():
    for p in (shutil.which("google-chrome"), shutil.which("chrome"),
              r"C:\Program Files\Google\Chrome\Application\chrome.exe",
              r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
              "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"):
        if p and os.path.exists(p):
            return p
    sys.exit("Chrome not found. Set CHROME_PATH.")


def to_clipboard(text):
    sysname = platform.system()
    cmd = (["clip"] if sysname == "Windows" else ["pbcopy"] if sysname == "Darwin"
           else ["xclip", "-selection", "clipboard"])
    subprocess.run(cmd, input=text.encode("utf-16le" if sysname == "Windows" else "utf-8"), check=True)


def main():
    tz = ZoneInfo(env("TIMEZONE", "America/New_York"))
    profiles = json.load(open(env("PROFILES_FILE", "profiles.json")))
    only = set(a.lstrip("@") for a in sys.argv[1:])
    chrome = env("CHROME_PATH") or chrome_path()
    sh, log_ws, q_ws, acc_ws, run_ws = M.connect()
    gaps = [int(x) for x in env("FOLLOWUP_GAPS", "4,4,4").replace(" ", "").split(",")][:3]
    while len(gaps) < 3:
        gaps.append(gaps[-1])
    qdate = datetime.now(tz).date().isoformat()
    stats = {"sent": 0, "skipped": 0}
    while True:
        qv = M.get_all(q_ws)
        todo = []
        for i, r in enumerate(qv[1:], start=2):
            r = pad(r, len(M.Q_H))
            if r[Q["Queue Date"]] != qdate or yes(r[Q["Done? (type Yes)"]]) or r[Q["Synced"]].strip():
                continue
            if only and r[Q["Agent Account"]] not in only:
                continue
            if r[Q["Agent Account"]] not in profiles:
                continue
            todo.append((r[Q["Suggested Time"]][:5], i, r))
        if not todo:
            print("Queue finished.", stats)
            break
        todo.sort()
        hhmm, row_i, r = todo[0]
        wait = (datetime.strptime(f"{qdate} {hhmm}", "%Y-%m-%d %H:%M").replace(tzinfo=tz) - datetime.now(tz)).total_seconds()
        if wait > 0:
            print(f"Next: {r[Q['Agent Account']]} -> @{r[Q['Instagram Handle']]} at {hhmm}. Waiting {int(wait // 60)} min...")
            time.sleep(wait)
        agent, handle = r[Q["Agent Account"]], r[Q["Instagram Handle"]]
        text = r[Q["Message to Send"]]
        to_clipboard(text)
        subprocess.Popen([chrome, f'--profile-directory={profiles[agent]}', r[Q["Open DM Chat"]]])
        print(f"\n[{agent}] @{handle}  ({r[Q['Type']]})\n{text}\n")
        ans = input("Message copied. Paste + send in Instagram, then press Enter here "
                    "(s = skip this one, q = quit): ").strip().lower()
        if ans == "q":
            break
        if ans == "s":
            retry(lambda: q_ws.update_cell(row_i, Q["Synced"] + 1, "Expired"))
            stats["skipped"] += 1
            continue
        now = datetime.now(tz).strftime("%Y-%m-%d %H:%M")
        retry(lambda: q_ws.batch_update([
            {"range": rowcol_to_a1(row_i, Q["Done? (type Yes)"] + 1), "values": [["Yes"]]},
            {"range": rowcol_to_a1(row_i, Q["Sent At (auto)"] + 1), "values": [[now]]}], value_input_option="RAW"))
        M.sync(log_ws, q_ws, datetime.now(tz).date(), tz, gaps)
        stats["sent"] += 1


if __name__ == "__main__":
    main()
