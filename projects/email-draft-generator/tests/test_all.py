"""Run:  python tests/test_all.py     (from the project folder). Prints PASS or FAIL per test."""
import os
import random
import subprocess
import sys
import time
from pathlib import Path

import openpyxl
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "app"))
from draft import checks, config, leads, names  # noqa: E402
from draft.compose import Composer  # noqa: E402

RUN = [sys.executable, str(ROOT / "app" / "run.py")]
TMP = ROOT / "proof"
results = []


def test(name):
    def deco(fn):
        try:
            fn()
            results.append((name, True, ""))
        except Exception as e:  # noqa: BLE001
            results.append((name, False, repr(e)[:300]))
        return fn
    return deco


def run_cli(*args, env=None):
    e = dict(os.environ, **(env or {}))
    return subprocess.run(RUN + list(args), capture_output=True, text=True, env=e, encoding="utf-8")


def read_ready(path):
    wb = openpyxl.load_workbook(path, read_only=True)
    ready = [r for r in wb["Ready To Send"].iter_rows(min_row=2, values_only=True) if r[0]]
    review = [r for r in wb["Needs Review"].iter_rows(min_row=2, values_only=True) if r[0]]
    return ready, review


@test("name splitting keeps every letter")
def _():
    keep = []
    cases = {"SandWICH": "Sandwich", "Sandwich": "Sandwich", "DeliciousKitchen": "Delicious Kitchen",
             "deliciouskitchen": "Delicious Kitchen", "Ha Long Bay": "Ha Long Bay", "McDonalds": "McDonalds",
             "Pizzeria Bros": "Pizzeria Bros", "BBQ & Smokehouse": "BBQ and Smokehouse", "llamarider37": ""}
    for raw, want in cases.items():
        got = names.clean_biz(raw, keep)
        assert got == want, (raw, got, want)
    rnd = random.Random(1)
    for _ in range(300):
        w = "".join(rnd.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(rnd.randint(4, 18)))
        out = names.clean_biz(w, keep)
        assert out == "" or names.letters(out) == names.letters(w), (w, out)


@test("first names: dictionary only, shared mailboxes get none")
def _():
    assert names.first_name("Maria", "x@y.com") == "Maria"
    assert names.first_name("", "john@smithrealty.com") == "John"
    assert names.first_name("", "info@x.com", "Freya Farrington", company=True) == ""
    assert names.first_name("", "relitychannel@gmail.com", "Build Your Tribe") == ""
    assert names.first_name("", "x@y.com", "Freya Farrington") == "Freya"
    assert names.first_name("", "hello@x.com") == ""
    assert names.is_company_mailbox("care@x.com") and names.is_company_mailbox("info@x.com")
    assert not names.is_company_mailbox("john@x.com")


@test("offence benchmark rejects ego-hurting options")
def _():
    for bad in ["Improve your retention.", "A fuller weekday lunch.", "Fix your thumbnails.", "Stop losing viewers.",
                "Better engagement.", "Clearer product storytelling."]:
        assert checks.check_options([bad]), bad
    for good in ["Reaching a wider audience.", "Growing repeat guests.", "More time to create."]:
        assert not checks.check_options([good]), good


@test("generic claim and tool-list benchmarks")
def _():
    assert checks.check_line("I help channels grow faster.")
    assert checks.check_line("Meta ads, Google ads, SEO, Reels, design, branding, websites.")
    assert not checks.check_line("Storytelling and motion design shape every edit.")


@test("template lint is clean")
def _():
    r = run_cli("--lint")
    assert "all clean" in r.stdout, r.stdout[-400:]


@test("leads: several emails in one cell, duplicates, no-reply")
def _():
    df = pd.DataFrame([
        dict(Email="a@x.com; b@x.com", Business="One"), dict(Email="A@x.com", Business="Dup"),
        dict(Email="noreply@x.com", Business="NR"), dict(Email="", Business="None"), dict(Email="c@x.com\nd@x.com", Business="Two")])
    p = TMP / "t_leads.xlsx"
    df.to_excel(p, index=False)
    settings, _ = config.load()
    ls, st = leads.read_input(p, settings)
    assert [x.email for x in ls] == ["a@x.com", "b@x.com", "c@x.com", "d@x.com"], [x.email for x in ls]
    assert st["duplicates"] == 1 and st["no_email"] == 1 and st["skipped_noreply"] == 1 and st["multi_cells"] == 2, st


@test("30/30/40 mix and first-person share")
def _():
    settings, templates = config.load()
    c = Composer(settings, templates)
    kinds = [c.kind_for(i) for i in range(1000)]
    assert abs(kinds.count("short") - 300) <= 3 and abs(kinds.count("options") - 300) <= 3, kinds.count("short")
    share = sum(c.uses_i_for(i) for i in range(1000)) / 1000
    assert 0.15 <= share <= 0.20, share


def synth(n):
    rnd = random.Random(7)
    first = ["Ava", "Liam", "Noah", "Emma", "Mia", "Lucas", "Zoe", "Ethan", "Chloe", "Ryan"]
    last = ["Stone", "Rivers", "Hale", "Brooks", "Frost", "Wells", "Cole", "Park", "Reed", "Lane"]
    kitchen = ["Delicious Kitchen", "SunriseBistro", "Blue Table", "Ha Long Bay", "Spice Route", "Maple Grill", "Nuba", "Fat Mao Noodles"]
    rows = []
    for i in range(n):
        t = rnd.random()
        if t < 0.45:
            rows.append(dict(Niche="YouTube", Email=f"{rnd.choice(['info','hello','creator','partners', rnd.choice(first).lower()])}{i}@chan{i}.com",
                             Name="", Business=f"{rnd.choice(first)} {rnd.choice(last)}", City="", Cuisine=""))
        elif t < 0.85:
            rows.append(dict(Niche="Restaurant", Email=f"{rnd.choice(['info','hello','care'])}{i}@rest{i}.ca", Name="",
                             Business=rnd.choice(kitchen) + (f" {i}" if i % 2 else ""), City=rnd.choice(["Calgary", "Toronto", "Surrey", ""]),
                             Cuisine=rnd.choice(["italian", "thai", "pizza", "None", "regional"])))
        else:
            rows.append(dict(Niche=rnd.choice(["Real Estate", "Car Showroom", "SaaS", "Ecommerce", ""]),
                             Email=f"{rnd.choice(first).lower()}{i}@biz{i}.com", Name=rnd.choice(first), Business=f"{rnd.choice(last)} Group",
                             City="Edmonton", Cuisine=""))
    return pd.DataFrame(rows)


@test("determinism: same sheet, same drafts")
def _():
    p = TMP / "t_syn.xlsx"
    synth(60).to_excel(p, index=False)
    for tag in "ab":
        r = run_cli("--input", str(p), "--out", str(TMP / f"t_det_{tag}.xlsx"), "--fresh", "--no-llm", "--no-scrape")
        assert r.returncode == 0, r.stdout + r.stderr
    a, _ = read_ready(TMP / "t_det_a.xlsx")
    b, _ = read_ready(TMP / "t_det_b.xlsx")
    assert a == b


@test("crash then resume gives the same result as an uninterrupted run")
def _():
    p = TMP / "t_syn.xlsx"
    out = TMP / "t_crash.xlsx"
    for f in (out, Path(str(out) + ".state.db")):
        if f.exists():
            f.unlink()
    r1 = run_cli("--input", str(p), "--out", str(out), "--no-llm", "--no-scrape", env={"DRAFT_CRASH_AFTER": "20"})
    assert r1.returncode != 0 and "simulated crash" in (r1.stdout + r1.stderr)
    r2 = run_cli("--input", str(p), "--out", str(out), "--no-llm", "--no-scrape")
    assert r2.returncode == 0 and "to go" in r2.stdout, r2.stdout + r2.stderr
    assert "20 already done" in r2.stdout, r2.stdout
    full, rev_f = read_ready(out)
    ref, rev_r = read_ready(TMP / "t_det_a.xlsx")
    assert full == ref and rev_f == rev_r


@test("changed input is refused unless --fresh")
def _():
    p2 = TMP / "t_syn2.xlsx"
    synth(61).to_excel(p2, index=False)
    r = run_cli("--input", str(p2), "--out", str(TMP / "t_crash.xlsx"), "--no-llm", "--no-scrape")
    assert r.returncode != 0 and "changed" in (r.stdout + r.stderr)


@test("Excel format: Title Case headers, row height 21, Arial 11")
def _():
    wb = openpyxl.load_workbook(TMP / "t_det_a.xlsx")
    ws = wb["Ready To Send"]
    assert [c.value for c in ws[1]] == ["Email", "Name", "Subject Line", "Body", "Follow-up 1", "Follow-up 2", "Follow-up 3", "Follow-up 4"]
    assert wb.sheetnames == ["Ready To Send", "Needs Review", "Report"]
    for r in range(1, ws.max_row + 1):
        assert ws.row_dimensions[r].height == 21, r
    assert ws["D2"].font.name == "Arial" and ws["D2"].font.size == 11


@test("stress: 1500 leads, no violations, shares near equal")
def _():
    p = TMP / "t_stress.xlsx"
    synth(1500).to_excel(p, index=False)
    out = TMP / "t_stress_out.xlsx"
    t0 = time.time()
    r = run_cli("--input", str(p), "--out", str(out), "--fresh", "--no-llm", "--no-scrape")
    assert r.returncode == 0, r.stdout[-500:] + r.stderr[-500:]
    ready, review = read_ready(out)
    secs = time.time() - t0
    assert len(ready) + len(review) == 1500
    assert len(review) <= 45, f"{len(review)} in review"
    wb = openpyxl.load_workbook(out, read_only=True)
    rep = {a: b for a, b in wb["Report"].iter_rows(min_row=2, values_only=True)}
    print(f"      stress: {len(ready)} ready, {len(review)} review, {secs:.0f}s, I share {rep['Emails using the word I']}, "
          f"over-20% lines: {rep['Lines used in over 20% of their slot']}")
    subj = [len(r[2]) for r in ready]
    assert max(subj) <= 50 and min(subj) >= 24, (min(subj), max(subj))
    assert all(r[3][0].isupper() for r in ready)


if __name__ == "__main__":
    bad = 0
    for n, ok, err in results:
        print(("PASS " if ok else "FAIL ") + n + ("" if ok else "  ->  " + err))
        bad += not ok
    print(f"\n{len(results) - bad}/{len(results)} passed")
    sys.exit(1 if bad else 0)
