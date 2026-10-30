"""Instagram outreach assistant (v3).

Run order: sync what was sent -> expire stale queue rows -> schedule follow-ups ->
re-queue anything that fell through -> write new personalised DMs -> fill 'Today Queue'
with a staggered, multi-account schedule.  `python main.py --sync-only` only does the sync.
"""
import json
import os
import random
import re
import sys
import time
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import gspread
from gspread.utils import rowcol_to_a1

import ig
import styles
from ai import AI
from rules import problems, opener

LOG_TAB, QUEUE_TAB, ACC_TAB, RUN_TAB = "Outreach Log", "Today Queue", "Accounts", "Run Log"
LOG_H = ["Date Added", "Agent Account", "Niche", "Name", "Instagram Handle", "Profile Link", "Open DM Chat",
         "Account About", "Followers", "Email", "Phone", "LinkedIn / Website", "Location",
         "Message Sent", "Message Sent On", "Replied? (Yes/No)", "Replied At (auto)", "Reply Message",
         "Follow-up 1", "Follow-up 1 Text", "Follow-up 2", "Follow-up 2 Text", "Follow-up 3", "Follow-up 3 Text",
         "Lead Status", "Stage", "Next Due (auto)", "Notes", "Style"]
Q_H = ["Queue Date", "Suggested Time", "Agent Account", "Type", "Name", "Instagram Handle", "Open DM Chat",
       "Profile Link", "Before You Send", "Message to Send", "Done? (type Yes)", "Sent At (auto)", "Synced", "Style"]
ACC_H = ["Account", "Start Date (YYYY-MM-DD)", "Status (Active/Paused)", "Pause Until (YYYY-MM-DD)",
         "Max Per Day Override", "Phase (auto)", "Notes"]
RUN_H = ["Run time", "Summary", "Problems"]
C, Q = {}, {}     # header -> column index, filled by connect() from the REAL sheet headers
STAGES = ["Message sent", "Follow-up 1 sent", "Follow-up 2 sent", "Follow-up 3 sent (done)"]
STOP_STATUS = {"interested", "call booked", "client", "not interested", "do not contact", "unsubscribed"}
HARD_CAP = 20


# ---------------------------------------------------------------- helpers
def env(k, d=""):
    return (os.getenv(k) or d).strip()


def yes(v):
    return str(v).strip().lower() in ("yes", "y", "true", "done", "1", "✔", "✓")


def pad(r, n):
    return list(r) + [""] * (n - len(r))


def clean_handle(v):
    v = str(v).strip()
    m = re.search(r"instagram\.com/(?:_u/)?([A-Za-z0-9._]+)", v, re.I)
    h = m.group(1) if m else v.lstrip("@").split("?")[0].strip("/ ")
    if h.lower() in ("p", "reel", "reels", "explore", "stories", "accounts", "direct"):
        return ""
    return h.lower() if re.fullmatch(r"[A-Za-z0-9._]{1,30}", h) else ""


def fmt(d):
    return d.strftime(env("DATE_FORMAT", "%d-%b-%Y"))


def parse_date(s):
    s = str(s).strip()[:11].strip()
    for f in ("%Y-%m-%d", env("DATE_FORMAT", "%d-%b-%Y"), "%d/%m/%Y", "%d-%m-%Y"):
        try:
            return datetime.strptime(s[:len(datetime.now().strftime(f))], f).date()
        except ValueError:
            pass
    return None


def parse_dt(s, tz):
    try:
        return datetime.strptime(str(s).strip()[:16], "%Y-%m-%d %H:%M").replace(tzinfo=tz)
    except ValueError:
        return None


def retry(fn, tries=5):
    """Google Sheets sometimes answers 429/5xx. Wait and retry instead of crashing the whole run."""
    for i in range(tries):
        try:
            return fn()
        except gspread.exceptions.APIError as e:
            code = getattr(getattr(e, "response", None), "status_code", 0)
            if code in (429, 500, 502, 503) and i < tries - 1:
                time.sleep(15 * (i + 1))
                continue
            raise
        except Exception as e:  # network blips
            if i < tries - 1 and "Connection" in type(e).__name__ + str(e):
                time.sleep(10 * (i + 1))
                continue
            raise


def get_all(ws):
    return retry(lambda: ws.get_all_values())


def batch(ws, data):
    for i in range(0, len(data), 400):
        retry(lambda: ws.batch_update(data[i:i + 400], value_input_option="RAW"))


def append(ws, rows):
    for i in range(0, len(rows), 200):
        retry(lambda: ws.append_rows(rows[i:i + 200], value_input_option="RAW"))


def get_tab(sh, title, headers):
    """Open (or create) a tab. NEVER overwrite existing headers: missing ones are appended at the end."""
    try:
        ws = retry(lambda: sh.worksheet(title))
    except gspread.WorksheetNotFound:
        ws = retry(lambda: sh.add_worksheet(title, rows=2000, cols=len(headers) + 2))
        retry(lambda: ws.update(range_name="A1", values=[headers]))
        retry(lambda: ws.freeze(rows=1))
        return ws, list(headers)
    cur = [h.strip() for h in retry(lambda: ws.row_values(1))]
    if not any(cur):
        retry(lambda: ws.update(range_name="A1", values=[headers]))
        return ws, list(headers)
    missing = [h for h in headers if h not in cur]
    if missing:
        if ws.col_count < len(cur) + len(missing):
            retry(lambda: ws.resize(cols=len(cur) + len(missing)))
        retry(lambda: ws.update(range_name=rowcol_to_a1(1, len(cur) + 1), values=[missing]))
        cur += missing
    return ws, cur


def connect():
    """Open the sheet and bind column maps to the real headers. Returns the 4 worksheets."""
    global LOG_H, Q_H
    raw = env("GOOGLE_SERVICE_ACCOUNT_JSON")
    info = json.loads(raw) if raw.lstrip().startswith("{") else json.load(open(raw))
    gc = gspread.service_account_from_dict(info)
    sh = retry(lambda: gc.open_by_key(env("SHEET_ID")))
    log_ws, LOG_H = get_tab(sh, LOG_TAB, LOG_H)
    q_ws, Q_H = get_tab(sh, QUEUE_TAB, Q_H)
    acc_ws, _ = get_tab(sh, ACC_TAB, ACC_H)
    run_ws, _ = get_tab(sh, RUN_TAB, RUN_H)
    C.clear(); C.update({h: i for i, h in enumerate(LOG_H)})
    Q.clear(); Q.update({h: i for i, h in enumerate(Q_H)})
    return sh, log_ws, q_ws, acc_ws, run_ws


# ---------------------------------------------------------------- leads
def read_leads(sh):
    name = env("LEADS_TAB")
    ws = retry(lambda: sh.worksheet(name)) if name else sh.get_worksheet(0)
    rows = get_all(ws)
    if len(rows) < 2:
        return [], 0
    hdr = [h.strip().lower() for h in rows[0]]

    def col(inc, exc=()):
        for i, h in enumerate(hdr):
            if any(k in h for k in inc) and not any(k in h for k in exc):
                return i
        return None

    hc = col(("instagram", "insta", "handle", "social"), ("linkedin", "facebook", "tiktok", "youtube"))
    if hc is None and "ig" in hdr:
        hc = hdr.index("ig")
    if hc is None:
        raise RuntimeError("Leads tab: no column header containing 'Instagram' / 'Handle' found.")
    cols = {
        "name": col(("name",), ("user", "company", "business", "handle", "insta")),
        "niche": col(("niche", "category", "industry", "profession")),
        "bio": col(("bio", "about", "description")),
        "email": col(("email", "e-mail")),
        "phone": col(("phone", "mobile", "contact number")),
        "web": col(("linkedin", "website", "web")),
        "location": col(("address", "location", "city", "country")),
    }
    out, seen, skipped = [], set(), 0
    for r in rows[1:]:
        if not any(str(x).strip() for x in r):
            continue
        g = lambda i: r[i].strip() if i is not None and i < len(r) else ""
        h = clean_handle(g(hc))
        if not h:
            skipped += 1
            continue
        if h in seen:
            continue
        seen.add(h)
        out.append({"handle": h, **{k: g(v) for k, v in cols.items()}})
    return out, skipped


# ---------------------------------------------------------------- accounts
def account_cap(r, today, limit):
    r = pad(r, 7)
    if r[2].strip().lower() == "paused":
        return 0, "Paused"
    pu = parse_date(r[3])
    if pu and pu >= today:
        return 0, f"Paused until {pu}"
    if r[4].strip().isdigit():
        return min(int(r[4]), HARD_CAP), "Manual limit"
    sd = parse_date(r[1])
    if not sd:
        return min(limit, 5), "Set a start date (capped at 5/day)"
    age = (today - sd).days
    if age < 14:
        return 0, f"Warm-up day {age} (no outreach before day 14)"
    if age < 28:
        return min(limit, 5), "Ramp-up (max 5/day)"
    return min(limit, HARD_CAP), "Full"


def load_accounts(acc_ws, seed, today, limit):
    rows = get_all(acc_ws)
    have = {r[0].strip().lstrip("@") for r in rows[1:] if r and r[0].strip()}
    new = [[a, "", "Active", "", "", "", ""] for a in seed if a not in have]
    if new:
        append(acc_ws, new)
        rows = get_all(acc_ws)
    caps, upd = {}, []
    for i, r in enumerate(rows[1:], start=2):
        r = pad(r, 7)
        if not r[0].strip():
            continue
        name = r[0].strip().lstrip("@")
        caps[name], phase = account_cap(r, today, limit)
        upd.append({"range": rowcol_to_a1(i, 6), "values": [[phase]]})
    if upd:
        batch(acc_ws, upd)
    return caps


# ---------------------------------------------------------------- sync
def sync(log_ws, q_ws, today, tz, gaps):
    """Copy what you marked as sent into the Outreach Log; expire queue rows from earlier days."""
    log, qv = get_all(log_ws), get_all(q_ws)
    hcol, n_log = C["Instagram Handle"], len(LOG_H)
    pos = {}
    for i, r in enumerate(log[1:], start=2):
        pos.setdefault(pad(r, n_log)[hcol], i)
    log_b, q_b, count, qdate = [], [], 0, today.isoformat()
    for qi, r in enumerate(qv[1:], start=2):
        r = pad(r, len(Q_H))
        synced = r[Q["Synced"]].strip().lower()
        if synced in ("yes", "expired"):
            continue
        done = yes(r[Q["Done? (type Yes)"]])
        if not done:
            qd = r[Q["Queue Date"]].strip()
            if qd and qd < qdate:       # you skipped it yesterday: free the slot, it is re-queued below
                q_b.append({"range": rowcol_to_a1(qi, Q["Synced"] + 1), "values": [["Expired"]]})
            continue
        row = pos.get(r[Q["Instagram Handle"]])
        if row:
            sent = (parse_dt(r[Q["Sent At (auto)"]], tz) or datetime.now(tz)).date()
            put = lambda h, v: log_b.append({"range": rowcol_to_a1(row, C[h] + 1), "values": [[v]]})
            t = r[Q["Type"]]
            if t == "Message":
                put("Message Sent On", fmt(sent)); put("Stage", STAGES[0]); put("Lead Status", "Contacted")
                put("Next Due (auto)", (sent + timedelta(days=gaps[0])).isoformat())
            else:
                n = int(t[-1])
                put(f"Follow-up {n}", fmt(sent)); put("Stage", STAGES[n])
                put("Next Due (auto)", (sent + timedelta(days=gaps[n])).isoformat() if n < 3 else "")
            count += 1
        q_b.append({"range": rowcol_to_a1(qi, Q["Synced"] + 1), "values": [["Yes"]]})
    batch(log_ws, log_b)
    batch(q_ws, q_b)
    if log_b or q_b:
        log, qv = get_all(log_ws), get_all(q_ws)
    return count, log, qv


def used_today(qv, tz, now, qdate):
    """Sends per account that count against the limit: everything queued today + anything sent in the last 24h.
    (Fixes the old bug where re-running the workflow could exceed the daily limit.)"""
    used = {}
    for r in qv[1:]:
        r = pad(r, len(Q_H))
        if r[Q["Synced"]].strip().lower() == "expired":
            continue
        sent = parse_dt(r[Q["Sent At (auto)"]], tz) if yes(r[Q["Done? (type Yes)"]]) else None
        if r[Q["Queue Date"]].strip() == qdate or (sent and now - sent < timedelta(hours=24)):
            a = r[Q["Agent Account"]]
            used[a] = used.get(a, 0) + 1
    return used


# ---------------------------------------------------------------- writing
COMMON = """You write short Instagram DMs for a human sender at a video and growth agency. Rules:
- UNDER 40 words in total (aim for 28-36). Plain text only: no emojis, no hashtags, no links, no phone numbers, no @.
- Format: 2 or 3 very short lines separated by a blank line (easy to scan).
- Sound like a real person: casual, warm, specific. Never mention being an AI.
- Only use the recipient's first name if it is given, and at most once. Skip it if unsure.
- Mention ONE specific, true detail from their profile info. Never invent facts, results, clients or numbers.
- Pick only ONE service that fits their likely pain point. Never list services.
- {free}
- End with one easy, low-pressure question.
- Output ONLY the message text."""

FU_GOALS = {
    1: "This is follow-up 1. Gently follow up and add one small NEW personal touch. Briefly remind them the sample is free. Do not repeat earlier wording.",
    2: "This is follow-up 2. Take a different angle: share one quick, useful idea relevant to their niche. No pitch.",
    3: "This is follow-up 3 (last). Friendly, no-pressure check-in; say you will not keep messaging after this.",
}


def case_studies():
    return [x.strip() for x in re.split(r"\n|\|\|", env("CASE_STUDIES")) if x.strip()]


def build_prompt(c, fu=0, prev="", fixes="", style=""):
    first = c["name"].split(" ")[0] if c.get("name") else ""
    sample = env("FREE_SAMPLE", "a free 30-60 second sample video made for them")
    free = ("The FIRST message must clearly say the sample is free (use the word 'free'): " + sample
            if not fu else "No need to repeat the free sample unless the goal says so.")
    ctx = (f"Sender: {env('SENDER_NAME', 'the sender')} from {env('AGENCY_NAME', 'our agency')}\n"
           f"Agency services: {env('OFFER')}\nRecipient first name: {first or 'unknown'}\n"
           f"Niche: {c.get('niche') or 'unknown'}\nBio: {c.get('bio') or 'n/a'}\n"
           f"Recent posts: {' | '.join(c.get('captions', [])) or 'n/a'}\n")
    if fu:
        goal = FU_GOALS[fu] + f"\nEarlier message sent:\n{prev}\n"
    else:
        instr = styles.STYLES[style][0]
        cs = "\n".join(f"- {x}" for x in case_studies())
        goal = f"This is the FIRST message.\nANGLE ({style}): {instr}\n"
        if styles.STYLES[style][1]:
            goal += f"CASE_STUDIES (the only facts you may use):\n{cs}\n"
    fix = f"\nYour last attempt was rejected: {fixes}. Fix this.\n" if fixes else ""
    return f"{COMMON.format(free=free)}\n\n{ctx}\n{goal}{fix}"


def write_message(ai, c, fu=0, prev="", used=(), style=""):
    fixes, t = "", ""
    allowed = case_studies()
    for _ in range(3):
        t = ai.generate(build_prompt(c, fu, prev, fixes, style))
        t = re.sub(r"^(message|dm)\s*:\s*", "", t.strip().strip('"“”'), flags=re.I)
        t = re.sub(r"\n{3,}", "\n\n", t)
        p = problems(t, used_openers=used if not fu else (), require_free=(not fu), allowed_numbers=allowed)
        if not p:
            return t, ""
        fixes = "; ".join(p)
    return t, fixes


# ---------------------------------------------------------------- scheduling
def send_window(tz, day):
    m = re.match(r"(\d{1,2}):(\d{2})\s*-\s*(\d{1,2}):(\d{2})", env("SEND_WINDOW", "09:00-21:00"))
    a, b = ((int(m[1]), int(m[2])), (int(m[3]), int(m[4]))) if m else ((9, 0), (21, 0))
    return (datetime(day.year, day.month, day.day, *a, tzinfo=tz),
            datetime(day.year, day.month, day.day, *b, tzinfo=tz))


def assign_times(rows, tz, now):
    """Round-robin across accounts. Each account waits 15-20 min between its own messages;
    accounts start at staggered, random offsets so the sends interleave (no bursts)."""
    lo, hi = (int(x) for x in (re.findall(r"\d+", env("MSG_GAP_MINUTES", "15-20")) + ["15", "20"])[:2])
    start, end = send_window(tz, now.date())
    base = max(start, now + timedelta(minutes=3))
    by = {}
    for r in rows:
        by.setdefault(r[Q["Agent Account"]], []).append(r)
    agents = list(by)
    random.shuffle(agents)
    for k, a in enumerate(agents):
        t = base + timedelta(minutes=k * random.randint(2, 4) + random.randint(0, 2))
        random.shuffle(by[a])
        for r in by[a]:
            late = t.date() != now.date() or t > end
            r[Q["Suggested Time"]] = t.strftime("%H:%M") + (" (late, tomorrow is better)" if late else "")
            t += timedelta(minutes=random.randint(min(lo, hi), max(lo, hi)), seconds=random.randint(0, 59))
    return sorted(rows, key=lambda r: (r[Q["Suggested Time"]][:5], r[Q["Agent Account"]]))


# ---------------------------------------------------------------- main
def main(sync_only=False):
    errors = []
    S = {"synced": 0, "followups": 0, "new": 0, "requeued": 0, "private": 0, "review": 0, "no_handle": 0}
    need = ["GOOGLE_SERVICE_ACCOUNT_JSON", "SHEET_ID"] + ([] if sync_only else ["AI_API_KEYS", "OFFER"])
    for k in need:
        if not env(k):
            sys.exit(f"MISSING SETTING: {k}. See SETUP_GUIDE.md.")
    tz = ZoneInfo(env("TIMEZONE", "America/New_York"))
    now = datetime.now(tz)
    today, qdate = now.date(), now.date().isoformat()
    sh, log_ws, q_ws, acc_ws, run_ws = connect()
    gaps = [int(x) for x in re.findall(r"\d+", env("FOLLOWUP_GAPS", "4,4,4"))][:3] or [4, 4, 4]
    while len(gaps) < 3:
        gaps.append(gaps[-1])
    try:
        S["synced"], log, qv = sync(log_ws, q_ws, today, tz, gaps)
        if sync_only:
            print("Synced:", S["synced"])
            return
        limit = int(env("DAILY_LIMIT_PER_ACCOUNT", "10") or 10)
        seed = [a.strip().lstrip("@") for a in env("AGENT_ACCOUNTS").split(",") if a.strip()]
        cap = load_accounts(acc_ws, seed, today, limit)
        if not cap:
            sys.exit("No accounts. Fill AGENT_ACCOUNTS or the Accounts tab.")
        for a, n in used_today(qv, tz, now, qdate).items():
            if a in cap:
                cap[a] = max(0, cap[a] - n)
        pending = {(pad(r, len(Q_H))[Q["Instagram Handle"]], pad(r, len(Q_H))[Q["Type"]])
                   for r in qv[1:] if pad(r, len(Q_H))[Q["Synced"]].strip().lower() not in ("yes", "expired")}

        ai = AI(env("AI_API_KEYS"))
        used = {opener(pad(r, len(LOG_H))[C["Message Sent"]]) for r in log[1:]} - {""}
        recent_styles = [pad(r, len(LOG_H))[C["Style"]] for r in log[-60:]]
        have_cases = bool(case_studies())
        new_q, new_log, upd = [], [], []

        def qrow(agent, typ, name, handle, link, dm, text, style=""):
            warm = ("Follow them and like 2 recent posts, wait a few minutes, then send"
                    if typ == "Message" else "Send inside the same chat as before")
            r = [""] * len(Q_H)
            for k, v in {"Queue Date": qdate, "Agent Account": agent, "Type": typ, "Name": name,
                         "Instagram Handle": handle, "Open DM Chat": dm, "Profile Link": link,
                         "Before You Send": warm, "Message to Send": text, "Done? (type Yes)": "No",
                         "Style": style}.items():
                r[Q[k]] = v
            return r

        # 1) Due follow-ups
        for i, r in enumerate(log[1:], start=2):
            r = pad(r, len(LOG_H))
            g = lambda h: r[C[h]]
            stage, due = g("Stage"), g("Next Due (auto)")
            if stage not in STAGES[:3] or yes(g("Replied? (Yes/No)")) or not due or due > qdate:
                continue
            if g("Lead Status").strip().lower() in STOP_STATUS:
                continue
            n = STAGES.index(stage) + 1
            agent, handle = g("Agent Account"), g("Instagram Handle")
            if (handle, f"Follow-up {n}") in pending or cap.get(agent, 0) <= 0:
                continue
            try:
                text, bad = write_message(ai, {"name": g("Name"), "niche": g("Niche"), "bio": g("Account About")},
                                          n, g("Message Sent"))
            except Exception as e:
                errors.append(str(e)[:150]); break
            if bad:
                upd.append({"range": rowcol_to_a1(i, C["Notes"] + 1), "values": [[f"Follow-up {n}: write manually ({bad})"]]})
                continue
            upd.append({"range": rowcol_to_a1(i, C[f"Follow-up {n} Text"] + 1), "values": [[text]]})
            new_q.append(qrow(agent, f"Follow-up {n}", g("Name"), handle, g("Profile Link"), g("Open DM Chat"), text))
            pending.add((handle, f"Follow-up {n}")); cap[agent] -= 1; S["followups"] += 1
            time.sleep(2)

        # 2) Re-queue messages that were written but never made it to a queue (skipped yesterday / crash)
        for r in log[1:]:
            r = pad(r, len(LOG_H))
            g = lambda h: r[C[h]]
            handle, agent = g("Instagram Handle"), g("Agent Account")
            if g("Stage") != "Queued" or (handle, "Message") in pending or cap.get(agent, 0) <= 0:
                continue
            if yes(g("Replied? (Yes/No)")) or g("Lead Status").strip().lower() in STOP_STATUS:
                continue
            if not g("Message Sent").strip():
                continue
            new_q.append(qrow(agent, "Message", g("Name"), handle, g("Profile Link"), g("Open DM Chat"),
                              g("Message Sent"), g("Style")))
            pending.add((handle, "Message")); cap[agent] -= 1; S["requeued"] += 1

        # 3) New leads
        known = {pad(r, len(LOG_H))[C["Instagram Handle"]] for r in log[1:]}
        ig_ok = True
        try:
            leads, S["no_handle"] = read_leads(sh)
        except Exception as e:
            errors.append(str(e)[:150]); leads = []
        for lead in leads:
            if lead["handle"] in known:
                continue
            if not cap or max(cap.values()) <= 0:
                break
            agent = max(cap, key=cap.get)
            info = ig.fetch(lead["handle"]) if ig_ok else {"status": "disabled"}
            if info["status"] == "token_error":
                errors.append("Instagram token invalid/expired: make a new IG_ACCESS_TOKEN. Continuing without profile reading.")
                ig_ok, info = False, {"status": "disabled"}
            if info["status"] == "rate_limited":
                errors.append("Instagram lookups rate-limited; continuing without profile reading for this run.")
                ig_ok, info = False, {"status": "disabled"}
            h = lead["handle"]
            row = {k: "" for k in LOG_H}
            row.update({"Date Added": fmt(today), "Agent Account": agent, "Niche": lead["niche"],
                        "Name": lead["name"] or info.get("name", ""), "Instagram Handle": h,
                        "Profile Link": f"https://www.instagram.com/{h}/", "Open DM Chat": f"https://ig.me/m/{h}",
                        "Followers": info.get("followers") or "", "Email": lead["email"], "Phone": lead["phone"],
                        "LinkedIn / Website": lead["web"], "Location": lead["location"], "Lead Status": "New"})
            known.add(h)
            if info["status"] == "unreadable" and not (lead["niche"] or lead["bio"]):
                row.update({"Account About": "Private or personal account (cannot be read)", "Message Sent": "Private",
                            "Stage": "Private - follow manually", "Notes": "Add niche/bio in Leads tab or write manually"})
                new_log.append(row); S["private"] += 1; continue
            ctx = {"name": row["Name"], "niche": lead["niche"], "bio": info.get("bio") or lead["bio"],
                   "captions": info.get("captions", [])}
            row["Account About"] = (ctx["bio"] or "").replace("\n", " ")[:160]
            if not ctx["niche"] and not ctx["bio"]:
                row.update({"Stage": "Needs review", "Notes": "No niche/bio. Add niche or bio to the Leads tab."})
                new_log.append(row); S["review"] += 1; continue
            style = styles.pick(recent_styles, have_cases)
            try:
                text, bad = write_message(ai, ctx, used=used, style=style)
            except Exception as e:
                errors.append(str(e)[:150]); known.discard(h); break
            row.update({"Message Sent": text, "Style": style})
            if bad:
                row.update({"Stage": "Needs review", "Notes": f"AI draft rejected: {bad}"})
                S["review"] += 1
            else:
                used.add(opener(text)); recent_styles.append(style)
                row.update({"Stage": "Queued", "Replied? (Yes/No)": "No"})
                new_q.append(qrow(agent, "Message", row["Name"], h, row["Profile Link"], row["Open DM Chat"], text, style))
                cap[agent] -= 1; S["new"] += 1
            new_log.append(row)
            time.sleep(2)

        # 4) Write everything (log first, so a crash never loses a lead: unqueued 'Queued' rows are re-queued next run)
        batch(log_ws, upd)
        if new_log:
            append(log_ws, [[r.get(k, "") for k in LOG_H] for r in new_log])
        if new_q:
            append(q_ws, assign_times(new_q, tz, now))
        S["ai_notes"] = len(ai.notes)
        errors += ai.notes
    except SystemExit:
        raise
    except Exception as e:
        errors.append(f"CRASH: {type(e).__name__}: {str(e)[:200]}")
        raise
    finally:
        msg = ", ".join(f"{k}={v}" for k, v in S.items())
        try:
            retry(lambda: run_ws.append_row([datetime.now(tz).strftime("%Y-%m-%d %H:%M"), msg, " | ".join(errors)]))
        except Exception:
            pass
        print("Done:", msg)
        if errors:
            print("Problems:", " | ".join(errors))


if __name__ == "__main__":
    main(sync_only="--sync-only" in sys.argv)
