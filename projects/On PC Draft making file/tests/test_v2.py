"""Tests for the version 2 safeguards. Run:  python tests/test_v2.py   (from the project folder)"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

import openpyxl
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TMP = ROOT / "proof"
sys.path.insert(0, str(ROOT / "app"))
from draft import checks, config, leads, llm, names  # noqa: E402
from draft.compose import Composer  # noqa: E402
import run as runmod  # noqa: E402

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


def run(*args, env=None):
    e = dict(os.environ, PYTHONIOENCODING="utf-8", **(env or {}))
    r = subprocess.run(RUN + list(args), capture_output=True, text=True, env=e, encoding="utf-8", timeout=600)
    return r, r.stdout + r.stderr


def tabs(path):
    wb = openpyxl.load_workbook(path, read_only=True)
    return {n: [r for r in wb[n].iter_rows(min_row=2, values_only=True) if r[0]] for n in wb.sheetnames}


def fresh(out):
    for s in ("", ".state.db", ".state.db-wal", ".state.db-shm"):
        p = Path(str(out) + s)
        if p.exists():
            try:
                p.unlink()
            except OSError:
                pass


@test("no name: the Name column shows Team (capital T only)")
def _():
    p = TMP / "v_team.xlsx"
    pd.DataFrame([dict(Niche="Restaurant", Email="info@a.ca", Business="Blue Table"),
                  dict(Niche="Restaurant", Email="zzqx@b.ca", Business="Maple Grill"),
                  dict(Niche="Restaurant", Email="maria@c.ca", Business="Nuba", Name="")]).to_excel(p, index=False)
    out = TMP / "v_team_out.xlsx"
    fresh(out)
    r, o = run("--input", str(p), "--out", str(out), "--no-llm", "--no-scrape")
    assert r.returncode == 0, o[-300:]
    got = {x[0]: x[1] for t in ("Ready To Send", "Needs Review") for x in tabs(out)[t]}
    assert got["info@a.ca"] == "Team" and got["zzqx@b.ca"] == "Team" and got["maria@c.ca"] == "Maria", got


@test("first names never guessed")
def _():
    f = names.first_name
    assert f("Maria", "x@y.com") == "Maria" and f("maria lopez", "x@y.com") == "Maria"
    assert f("Jean-Luc Picard", "x@y.com") == "Jean-Luc"
    assert f("Info Desk", "x@y.com") == "" and f("nan", "x@y.com") == "" and f("Sales Team", "x@y.com") == ""
    assert f("", "john@smithrealty.com") == "John"
    assert f("", "dev@x.com") == "" and f("", "shop@x.com") == "" and f("", "hello@x.com") == ""
    assert f("", "x@y.com", "Freya Farrington", niche="youtube") == "Freya"
    assert f("", "x@y.com", "Madison Avenue", niche="restaurant") == ""
    assert f("", "x@y.com", "Chelsea Market", niche="youtube") == ""
    assert f("", "info@x.com", "Freya Farrington", company=True, niche="youtube") == ""
    assert f("Maria", "info@x.com", company=True) == "Maria"      # a name you typed is always used
    assert f("", "london@turtlejacks.com") == "" and f("", "brooklyn@rakunyc.com") == ""
    assert f("", "orlando@x.com", city="Orlando") == "" and f("", "orlando@x.com", city="Calgary") == "Orlando"
    assert f("", "x@y.com", "The Edge Show", niche="youtube") == ""


@test("names keep accents, lose emoji and tags, never change letters")
def _():
    c = names.clean_biz
    assert c("Montréal") == "Montréal" and c("Café Zoë") == "Café Zoë"
    assert c("🔥 The Best Channel 🔥") == "The Best Channel"
    assert c("<b>Bold</b> Bistro") == "Bold Bistro"
    assert c("SHARRA") == "Sharra" and c("BBQ King") == "BBQ King"
    assert c("None") == "" and c("nan") == "" and c("12345") == "" and c("A" * 200) == ""
    assert c("SandWICH") == "Sandwich" and c("DeliciousKitchen") == "Delicious Kitchen"


@test("junk scraped emails are dropped")
def _():
    p = TMP / "v_junk.xlsx"
    pd.DataFrame([dict(Email="logo@2x.png; real@place.ca; abc@sentry.io; you@example.com; name@domain.com; "
                             "real@place.ca; REAL@place.ca; john..doe@x.com; 5f2a9c1b3d4e5f6a7b8c9d0e@wixpress.com")]).to_excel(p, index=False)
    settings, _ = config.load()
    ls, st = leads.read_input(p, settings)
    assert [x.email for x in ls] == ["real@place.ca"], [x.email for x in ls]
    assert st["junk"] >= 5, st


@test("header below a title row, and a sheet with no Email header")
def _():
    settings, _ = config.load()
    p = TMP / "v_hdr.xlsx"
    pd.DataFrame([["My lead list", "", ""], ["", "", ""], ["Business", "Email", "City"],
                  ["Blue Table", "a@b.ca", "Calgary"]]).to_excel(p, index=False, header=False)
    ls, st = leads.read_input(p, settings)
    assert [x.email for x in ls] == ["a@b.ca"] and ls[0].biz_raw == "Blue Table", (ls, st)
    p2 = TMP / "v_nohdr.xlsx"
    pd.DataFrame([dict(Stuff="Blue Table", Reach="a@b.ca"), dict(Stuff="Nuba", Reach="c@d.ca")]).to_excel(p2, index=False)
    ls, st = leads.read_input(p2, settings)
    assert len(ls) == 2 and "Reach" in " ".join(st["notes"]), st


@test("niche: the cell decides, weak words in a name never do, headers give a hint")
def _():
    _, t = config.load()
    r = runmod.resolve_niche
    assert r("YouTube", "", t) == "youtube" and r("Car Showroom", "", t) == "showroom"
    assert r("Real estate agent", "", t) == "real_estate" and r("Coffee shop", "", t) in ("restaurant", "ecommerce")
    assert r("", "Channel Islands Bar Association", t) is None
    assert r("", "Tech Edit", t) is None
    assert r("", "Luigi Italian Restaurant", t) == "restaurant"
    assert r("AI & Automation Business", "", t) is None
    settings, _ = config.load()
    p = TMP / "v_hint.xlsx"
    pd.DataFrame([dict(Channel="Some Creator", Email="a@b.com", niche="AI & Automation Business")]).to_excel(p, index=False)
    ls, _ = leads.read_input(p, settings)
    assert ls[0].hint == "youtube"


@test("the mix in settings.toml is really used")
def _():
    settings, templates = config.load()
    settings["run"].update(share_short=0.5, share_options=0.1, share_normal=0.4)
    c = Composer(settings, templates)
    k = [c.kind_for(i) for i in range(1000)]
    assert k.count("short") == 500 and k.count("options") == 100 and k.count("normal") == 400, (k.count("short"), k.count("options"))


@test("config mistakes are explained, not crashed on")
def _():
    d = TMP / "v_cfg"
    if d.exists():
        shutil.rmtree(d)
    shutil.copytree(ROOT / "config", d)
    t = (d / "templates.toml").read_text(encoding="utf-8")
    (d / "templates.toml").write_text(t.replace('ctas = [\n "Would you like to give it a try?",', 'ctas = [\n "Would you like to give it a try?"', 1), encoding="utf-8")
    r, o = run("--lint", "--config", str(d))
    assert r.returncode != 0 and "typing mistake" in o and "Traceback" not in o, o[-300:]
    (d / "templates.toml").write_text(t.replace("A 30-60 second {sample_noun} is available", "A 30-60 second {sampel_noun} is available", 1), encoding="utf-8")
    r, o = run("--lint", "--config", str(d))
    assert r.returncode != 0 and "unknown placeholder" in o and "Traceback" not in o, o[-300:]
    (d / "templates.toml").write_text(t, encoding="utf-8")
    s = (d / "settings.toml").read_text(encoding="utf-8")
    (d / "settings.toml").write_text(s.replace("share_short = 0.30", "share_short = 0.60"), encoding="utf-8")
    r, o = run("--lint", "--config", str(d))
    assert r.returncode != 0 and "must add to 1.0" in o, o[-300:]


@test("a bad template line stops the run before any draft is written")
def _():
    d = TMP / "v_cfg2"
    if d.exists():
        shutil.rmtree(d)
    shutil.copytree(ROOT / "config", d)
    t = (d / "templates.toml").read_text(encoding="utf-8")
    (d / "templates.toml").write_text(t.replace('"Would you like to give it a try?",', '"Fix your weak content now!",', 1), encoding="utf-8")
    p = TMP / "v_team.xlsx"
    r, o = run("--input", str(p), "--out", str(TMP / "v_bad.xlsx"), "--config", str(d), "--no-llm", "--no-scrape", "--fresh")
    assert r.returncode != 0 and "LINT" in o and "Fix the template lines" in o, o[-300:]


@test("two runs on the same output file are refused")
def _():
    from draft.store import Store
    path = str(TMP / "v_lock.xlsx.state.db")
    fresh(TMP / "v_lock.xlsx")
    a = Store(path, "fp")
    try:
        r, o = run("--input", str(TMP / "v_team.xlsx"), "--out", str(TMP / "v_lock.xlsx"), "--no-llm", "--no-scrape")
        assert r.returncode != 0 and "Another run" in o and "Traceback" not in o, o[-300:]
    finally:
        a.db.close()
        a._lockf.close()


@test("output safety: same file as input refused, missing folder created, extension fixed")
def _():
    p = TMP / "v_team.xlsx"
    r, o = run("--input", str(p), "--out", str(p), "--no-llm", "--no-scrape")
    assert r.returncode != 0 and "different file" in o, o[-300:]
    sub = TMP / "v_newdir"
    if sub.exists():
        shutil.rmtree(sub)
    r, o = run("--input", str(p), "--out", str(sub / "deep" / "out"), "--no-llm", "--no-scrape")
    assert r.returncode == 0 and (sub / "deep" / "out.xlsx").exists(), o[-300:]


@test("model circuit breaker: failures and an over-strict judge switch it off")
def _():
    g = llm.Guard({"host": "http://127.0.0.1:9", "model": "x", "timeout_seconds": 1}, True)
    for _ in range(3):
        assert g.classify_niche("text", ["a"]) is None
    assert not g.on and g.notes
    g2 = llm.Guard({"host": "", "model": "x"}, True)
    g2._call = lambda prompt: "YES"
    flags = [g2.might_offend("x") for _ in range(25)]
    assert not g2.judge_on and flags[-1] is False and "too strict" in g2.notes[0]


@test("benchmarks catch leaks: placeholder, None, missing period, bare free in a follow-up")
def _():
    so = ["Best regards,"]
    base = "Good food earns the first visit only when guests find it first.\n\n"
    ok = base + "Brand, content and search are planned together, because guests experience them together.\n\n" \
        "A 30-60 second sample Reel is available at zero cost, with no commitment attached.\n\nWould that be worth a try?\n\nBest regards,"
    assert not [x for x in checks.check_body(ok, "short", (30, 60), so) if "word count" not in x]
    assert any("placeholder" in x for x in checks.check_body(ok.replace("guests find", "{biz} guests find"), "short", (30, 60), so))
    assert any("empty value" in x for x in checks.check_body(ok.replace("Good food", "None food"), "short", (30, 60), so))
    assert any("period" in x for x in checks.check_body(ok.replace("worth a try?", "worth a try"), "short", (30, 60), so))
    fu = "Following up on my earlier email in case it got buried.\n\nA free 30-60 second sample Reel is available at zero cost.\n\nBest regards,"
    assert any("bare word free" in x for x in checks.check_followup(fu, so, "plain", (5, 70)))


@test("cells can never be read as formulas")
def _():
    from draft import export
    out = TMP / "v_formula.xlsx"
    export.write(out, [["=cmd@x.com", "Team", "+Subject", "Body\x0b text", "a", "b", "c", "d"]], [], [["k", "v"]])
    r = tabs(out)["Ready To Send"][0]
    assert r[0].startswith("'=") and r[2].startswith("'+") and "\x0b" not in r[3], r


if __name__ == "__main__":
    bad = 0
    for n, ok, err in results:
        print(("PASS " if ok else "FAIL ") + n + ("" if ok else "  ->  " + err))
        bad += not ok
    print(f"\n{len(results) - bad}/{len(results)} passed")
    sys.exit(1 if bad else 0)
