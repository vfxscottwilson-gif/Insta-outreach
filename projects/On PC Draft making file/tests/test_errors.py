"""Failure tests. Run:  python tests/test_errors.py   (from the project folder)
Every test tries to break the tool and checks that it fails politely or keeps going."""
import os
import subprocess
import sys
import time
from pathlib import Path

import openpyxl
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TMP = ROOT / "proof"
RUN = [sys.executable, str(ROOT / "app" / "run.py")]
results = []


def test(name):
    def deco(fn):
        try:
            fn()
            results.append((name, True, ""))
        except Exception as e:  # noqa: BLE001
            results.append((name, False, repr(e)[:400]))
        return fn
    return deco


def run(*args, env=None, timeout=300):
    e = dict(os.environ, PYTHONIOENCODING="utf-8", **(env or {}))
    r = subprocess.run(RUN + list(args), capture_output=True, text=True, env=e, encoding="utf-8", timeout=timeout)
    return r, r.stdout + r.stderr


def clean(out):
    for f in (Path(out), Path(str(out) + ".state.db"), Path(str(out) + ".state.db-wal"), Path(str(out) + ".state.db-shm")):
        if f.exists():
            try:
                f.unlink()
            except OSError:
                pass


def sheet(name, rows):
    p = TMP / name
    pd.DataFrame(rows).to_excel(p, index=False)
    return p


def rows_of(path, tab):
    wb = openpyxl.load_workbook(path, read_only=True)
    return [r for r in wb[tab].iter_rows(min_row=2, values_only=True) if r[0]]


GOOD = [dict(Niche="Restaurant", Email=f"info{i}@r{i}.ca", Business=f"Place {i} Kitchen", City="Calgary") for i in range(12)]


@test("missing input file: friendly message, no traceback")
def _():
    r, o = run("--input", str(TMP / "nope.xlsx"), "--out", str(TMP / "e1.xlsx"))
    assert r.returncode != 0 and "not found" in o and "Traceback" not in o, o[-300:]


@test("header-only sheet")
def _():
    p = sheet("e_empty.xlsx", [])
    pd.DataFrame(columns=["Email", "Business"]).to_excel(p, index=False)
    r, o = run("--input", str(p), "--out", str(TMP / "e2.xlsx"))
    assert r.returncode != 0 and "no rows" in o and "Traceback" not in o, o[-300:]


@test("no email column")
def _():
    p = sheet("e_noemail.xlsx", [dict(Business="A", City="B")])
    r, o = run("--input", str(p), "--out", str(TMP / "e3.xlsx"))
    assert r.returncode != 0 and "No email column" in o and "Traceback" not in o, o[-300:]


@test("rows exist but none has an email")
def _():
    p = sheet("e_blank.xlsx", [dict(Email="", Business="A"), dict(Email="n/a", Business="B")])
    r, o = run("--input", str(p), "--out", str(TMP / "e4.xlsx"))
    assert r.returncode != 0 and "No usable emails" in o and "Traceback" not in o, o[-300:]


@test("wrong --sheet name")
def _():
    p = sheet("e_good.xlsx", GOOD)
    r, o = run("--input", str(p), "--out", str(TMP / "e5.xlsx"), "--sheet", "Nope")
    assert r.returncode != 0 and "Could not read" in o and "Traceback" not in o, o[-300:]


@test("garbage file named .xlsx")
def _():
    p = TMP / "e_garbage.xlsx"
    p.write_text("this is not a spreadsheet", encoding="utf-8")
    r, o = run("--input", str(p), "--out", str(TMP / "e6.xlsx"))
    assert r.returncode != 0 and "Could not" in o and "Traceback" not in o, o[-300:]


@test("csv input with accents and BOM")
def _():
    p = TMP / "e_accents.csv"
    p.write_text("﻿Niche,Email,Business,City\nRestaurant,info@cafe.ca,Café Montréal Bistro,Montréal\nRestaurant,care@pho.ca,Phở Saigon,Québec\n", encoding="utf-8")
    out = TMP / "e7.xlsx"
    clean(out)
    r, o = run("--input", str(p), "--out", str(out), "--no-llm", "--no-scrape")
    assert r.returncode == 0, o[-400:]
    assert len(rows_of(out, "Ready To Send")) + len(rows_of(out, "Needs Review")) == 2


@test("output file open in Excel: saves beside it, no crash")
def _():
    p = sheet("e_good.xlsx", GOOD)
    out = TMP / "e8.xlsx"
    clean(out)
    run("--input", str(p), "--out", str(out), "--no-llm", "--no-scrape")
    clean(str(out) + ".state.db") if False else None
    for f in (Path(str(out) + ".state.db"),):
        if f.exists():
            f.unlink()
    held = open(out, "rb")
    try:
        r, o = run("--input", str(p), "--out", str(out), "--no-llm", "--no-scrape")
    finally:
        held.close()
    assert r.returncode == 0 and "WARNING" in o and "_saved_" in o, o[-400:]
    assert list(TMP.glob("e8_saved_*.xlsx")), "alternate file missing"


@test("Ctrl+C mid-run saves progress and resumes")
def _():
    p = sheet("e_good.xlsx", GOOD)
    out = TMP / "e9.xlsx"
    clean(out)
    r1, o1 = run("--input", str(p), "--out", str(out), "--no-llm", "--no-scrape", env={"DRAFT_INTERRUPT_AFTER": "5"})
    assert r1.returncode == 130 and "Run the same command again" in o1, o1[-300:]
    assert out.exists()
    r2, o2 = run("--input", str(p), "--out", str(out), "--no-llm", "--no-scrape")
    assert r2.returncode == 0 and "4 already done" in o2, o2[-300:]
    assert len(rows_of(out, "Ready To Send")) + len(rows_of(out, "Needs Review")) == 12


@test("one lead crashing does not stop the run")
def _():
    p = sheet("e_good.xlsx", GOOD)
    out = TMP / "e10.xlsx"
    clean(out)
    r, o = run("--input", str(p), "--out", str(out), "--no-llm", "--no-scrape", env={"DRAFT_FAIL_EMAIL": "info3@r3.ca"})
    assert r.returncode == 0, o[-300:]
    rev = rows_of(out, "Needs Review")
    assert len(rev) == 1 and rev[0][0] == "info3@r3.ca" and "draft failed" in rev[0][8], rev
    assert len(rows_of(out, "Ready To Send")) == 11


@test("damaged memory file is reported, --fresh recovers")
def _():
    p = sheet("e_good.xlsx", GOOD)
    out = TMP / "e11.xlsx"
    clean(out)
    Path(str(out) + ".state.db").write_bytes(b"not a database at all, just junk bytes" * 50)
    r, o = run("--input", str(p), "--out", str(out), "--no-llm", "--no-scrape")
    assert r.returncode != 0 and "damaged" in o and "Traceback" not in o, o[-300:]
    r2, o2 = run("--input", str(p), "--out", str(out), "--no-llm", "--no-scrape", "--fresh")
    assert r2.returncode == 0, o2[-300:]


@test("hostile data: odd emails, emoji, long names, numbers, 50 emails in a cell")
def _():
    many = "; ".join(f"p{i}@many.com" for i in range(50))
    rows = [
        dict(Niche="YouTube", Email="JOHN@X.COM", Name="John", Business="🔥 The Best Channel 🔥", City=""),
        dict(Niche="Restaurant", Email="john@@x.com", Business="Broken", City="Calgary"),
        dict(Niche="Restaurant", Email=12345, Business="Number Email", City="Calgary"),
        dict(Niche="Restaurant", Email="a@b.co", Business="A" * 200, City="Calgary"),
        dict(Niche="Restaurant", Email="c@d.co", Business="1234567", City="12345"),
        dict(Niche="Restaurant", Email="e@f.co", Business="Zoë's Crêperie & Café (Downtown)", City="Montréal"),
        dict(Niche="Restaurant", Email=many, Business="Many Mails", City="Surrey"),
        dict(Niche="???", Email="g@h.co", Business="Unknown Niche Co", City=None),
        dict(Niche="restaurant", Email="  i@j.co  ", Business="  spaced   out   name ", City="  Calgary "),
        dict(Niche="YouTube", Email="k@l.co", Name="Dr. Jane Smith, PhD", Business="Jane Smith", City=""),
        dict(Niche="Restaurant", Email="m@n.co", Business="DROP TABLE leads;--", City="Calgary"),
        dict(Niche="Restaurant", Email="o@p.co", Business="<b>Bold</b> Bistro", City="Calgary"),
    ]
    p = sheet("e_hostile.xlsx", rows)
    out = TMP / "e12.xlsx"
    clean(out)
    r, o = run("--input", str(p), "--out", str(out), "--no-llm", "--no-scrape")
    assert r.returncode == 0 and "Traceback" not in o, o[-500:]
    ready, review = rows_of(out, "Ready To Send"), rows_of(out, "Needs Review")
    got = {x[0] for x in ready + review}
    assert {f"p{i}@many.com" for i in range(50)} <= got and "john@x.com" in got and "a@b.co" in got
    for x in ready:
        for cell in x[2:8]:
            assert "<" not in str(cell) and ";" not in str(cell) and "(" not in str(cell), x
    assert not [x for x in review if "draft failed" in str(x[8])], review


@test("bad websites and unreachable Ollama do not stop the run")
def _():
    rows = [dict(Niche="Restaurant", Email=f"w{i}@w{i}.ca", Business=f"Web Place {i}", City="Calgary", Website=w)
            for i, w in enumerate(["http://localhost:9/", "not a url", "http://", "https://this-domain-does-not-exist-12345.invalid", "", "https://www.instagram.com/x"])]
    p = sheet("e_web.xlsx", rows)
    out = TMP / "e13.xlsx"
    clean(out)
    t0 = time.time()
    r, o = run("--input", str(p), "--out", str(out), "--fresh", "--no-llm")
    assert r.returncode == 0 and "Traceback" not in o, o[-500:]
    assert time.time() - t0 < 90
    r2, o2 = run("--input", str(p), "--out", str(TMP / "e13b.xlsx"), "--fresh", "--no-scrape")
    assert r2.returncode == 0 and "Ollama is not running" in o2, o2[-400:]
    assert len(rows_of(TMP / "e13b.xlsx", "Ready To Send")) + len(rows_of(TMP / "e13b.xlsx", "Needs Review")) == 6


@test("no output cell is empty or has a stray placeholder")
def _():
    out = TMP / "e12.xlsx"
    for x in rows_of(out, "Ready To Send"):
        for c in x[:8]:
            assert c and "{" not in str(c) and "}" not in str(c) and "None" not in str(c), x


if __name__ == "__main__":
    bad = 0
    for n, ok, err in results:
        print(("PASS " if ok else "FAIL ") + n + ("" if ok else "  ->  " + err))
        bad += not ok
    print(f"\n{len(results) - bad}/{len(results)} passed")
    sys.exit(1 if bad else 0)
