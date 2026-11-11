"""Email Draft Generator. Usage:  python run.py --input leads.xlsx --out drafts.xlsx
Other flags: --sheet NAME  --limit N  --fresh  --no-llm  --no-scrape  --lint  --check
"""
import sys

if sys.version_info < (3, 11):
    sys.exit("Python 3.11 or newer is needed. Install it from python.org/downloads, then run again.")
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(errors="replace")            # never crash on an accented path or name
    except Exception:  # noqa: BLE001
        pass

import argparse  # noqa: E402
import hashlib  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import re  # noqa: E402
import time  # noqa: E402
from collections import Counter  # noqa: E402
from dataclasses import asdict  # noqa: E402
from pathlib import Path  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from draft import checks, config, export, gpu, leads as L, llm, names, scrape
    from draft.compose import Composer
    from draft.store import Store
except ModuleNotFoundError as e:
    sys.exit(f"A library is missing ({e.name}). Double-click install\\INSTALL.cmd, then run again.")

NICHE_ORDER = ["youtube", "restaurant", "real_estate", "showroom", "ecommerce", "saas"]
# words that prove a niche on their own. Weak words (channel, bar, shop, app, agent) are never used on free text.
STRONG = {"youtube": ["youtube", "youtuber"],
          "restaurant": ["restaurant", "bistro", "eatery", "pizzeria", "steakhouse", "trattoria", "brasserie", "sushi", "diner", "ristorante"],
          "real_estate": ["real estate", "realty", "realtor", "brokerage"],
          "showroom": ["showroom", "dealership"],
          "ecommerce": ["ecommerce", "e-commerce", "shopify"],
          "saas": ["saas"]}


def kw_hit(text, kws):
    return any(re.search(r"\b" + re.escape(k) + r"\b", text) for k in kws)


def resolve_niche(cell, text, templates):
    """The Niche cell decides. Free text decides only when exactly one niche matches on a strong word,
    so a word like 'channel' or 'bar' inside a business name never picks the pack."""
    N = templates["niches"]
    cell = (cell or "").lower()
    if cell.strip():
        for key in NICHE_ORDER:
            if key in N and kw_hit(cell, N[key].get("keywords", [])):
                return key
        for key in N:
            if key not in NICHE_ORDER and key != "generic" and kw_hit(cell, N[key].get("keywords", []) + [key]):
                return key
    text = (text or "").lower()
    hits = [k for k in N if k != "generic" and kw_hit(text, N[k].get("strong_keywords", STRONG.get(k, [])))]
    return hits[0] if len(hits) == 1 else None


def lint(templates, settings):
    bad = 0
    C = templates["common"]
    groups = [("common." + k, C[k]) for k in ("ctas", "asks", "samples", "samples_after_options",
                                               "fu_options_intro", "fu_options_question",
                                               "fu_reminder", "fu_angle", "fu_last")]
    groups += [("common.subjects_" + k, C["subjects_" + k]) for k in ("named", "named_noun", "biz", "plain")]
    for key, n in templates["niches"].items():
        for k in ("openers_person", "openers_company", "insights", "values", "sample_extra"):
            groups.append((f"{key}.{k}", n.get(k, [])))
    for name, lines in groups:
        for ln in lines:
            sample = re.sub(r"\{\w+\}", "Sample Name", ln)
            v = checks.check_line(sample)
            if "subjects" in name:
                v = [x for x in v if not x.startswith("repeated")]
            if v:
                bad += 1
                print(f"LINT {name}: {v} :: {ln[:80]}")
    for key, n in templates["niches"].items():
        for opts in n["options"]:
            v = checks.check_options(opts)
            if v:
                bad += 1
                print(f"LINT {key} options: {v}")
    print("Template lint:", "all clean" if not bad else f"{bad} problem(s)")
    return bad == 0


def file_hash(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:16]


def build_lead(raw, templates, settings, store, use_scrape, guard):
    d = json.loads(raw)
    lead = L.Lead(**{k: v for k, v in d.items() if k in L.Lead.__dataclass_fields__})
    lead.biz = names.clean_biz(lead.biz_raw, settings["names"]["keep_unsplit"])
    lead.company_email = names.is_company_mailbox(lead.email)
    lead.cuisine_phrase = L.cuisine_phrase(lead.cuisine)
    if lead.hint == "youtube" and "youtube" in templates["niches"]:
        niche = "youtube"       # a Channel column means YouTube. Its niche cell is the channel topic, not our pack.
    else:
        niche = resolve_niche(lead.niche_cell, lead.biz_raw, templates)
    if niche is None and lead.hint in templates["niches"]:
        niche = lead.hint                               # the sheet itself says Channel or Cuisine
    if niche is None and use_scrape and lead.website:   # only read the website when the niche is still unknown
        web = scrape.fetch(lead.website, settings["scrape"], store)
        text = f"{lead.biz_raw} {web.get('title', '')} {web.get('description', '')}"
        niche = resolve_niche("", text, templates)
        if niche is None and guard.on and text.strip():
            niche = guard.classify_niche(text, list(templates["niches"].keys()))
    niche = niche or "generic"
    lead.first = names.first_name(lead.name_cell, lead.email, lead.biz, lead.company_email, niche, lead.city)
    return lead, niche


def main():
    ap = argparse.ArgumentParser(description="Email Draft Generator")
    ap.add_argument("--input")
    ap.add_argument("--out")
    ap.add_argument("--sheet")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--fresh", action="store_true")
    ap.add_argument("--no-llm", action="store_true")
    ap.add_argument("--no-scrape", action="store_true")
    ap.add_argument("--lint", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--config")
    a = ap.parse_args()

    settings, templates = config.load(a.config)
    if a.lint:
        sys.exit(0 if lint(templates, settings) else 1)
    llm_cfg = settings["llm"]
    running, has_model, installed = llm.status(llm_cfg)
    if a.check:
        if not running:
            print("Ollama: NOT running (the tool still works without it)")
        elif not has_model:
            print(f"Ollama: running, but model '{llm_cfg['model']}' is not installed. "
                  f"Run: ollama pull {llm_cfg['model']}   Installed: {', '.join(installed) or 'none'}")
        else:
            print(f"Ollama: running, model '{llm_cfg['model']}' ready")
        print("GPU temperature:", gpu.temperature() or "unknown")
        sys.exit(0 if lint(templates, settings) else 1)
    if not a.input or not a.out:
        ap.error("--input and --out are required")
    if not lint(templates, settings):
        sys.exit("Fix the template lines listed above (config\\templates.toml), then run again.")
    out = Path(a.out)
    if out.suffix.lower() != ".xlsx":
        out = out.with_suffix(".xlsx")
    if Path(a.input).resolve() == out.resolve():
        sys.exit("--out must be a different file from --input, or the lead sheet would be overwritten.")
    try:
        out.parent.mkdir(parents=True, exist_ok=True)
        probe = out.parent / (out.name + ".write-test")
        probe.write_text("ok")
        probe.unlink()
    except OSError as e:
        sys.exit(f"Cannot write to the output folder {out.parent} ({e}). Choose another --out location.")

    want_llm = llm_cfg["enabled"] and not a.no_llm
    if want_llm and not running:
        print("Note: Ollama is not running, so the model checks are skipped. Drafts are still built and checked.")
    elif want_llm and not has_model:
        print(f"Note: model '{llm_cfg['model']}' is not installed (run: ollama pull {llm_cfg['model']}). "
              f"Model checks are skipped.")
    guard = llm.Guard(llm_cfg, want_llm and running and has_model)

    t0 = time.time()
    all_leads, stats = L.read_input(a.input, settings, a.sheet)
    if a.limit:
        all_leads = all_leads[:a.limit]
    if not all_leads:
        raise SystemExit(f"No usable emails found in {stats['rows_in']} rows ({stats['no_email']} had no email, "
                         f"{stats['junk']} were junk addresses).")
    for n in stats["notes"]:
        print("Note:", n)
    fp = f"{file_hash(a.input)}:{config.fingerprint(a.config)}:{a.limit}:{a.sheet}"
    store = Store(str(out) + ".state.db", fp, a.fresh)
    store.add_leads([(x.email, json.dumps(asdict(x))) for x in all_leads])
    comp = Composer(settings, templates, store.counts())
    pend = store.pending()
    total = store.total()
    print(f"{stats['rows_in']} rows read, {len(all_leads)} unique emails to draft, "
          f"{total - len(pend)} already done, {len(pend)} to go.")
    use_scrape = settings["scrape"]["enabled"] and not a.no_scrape
    ctx = dict(out=out, store=store, stats=stats, t0=t0, comp=comp, guard=guard)
    try:
        _loop(pend, templates, settings, use_scrape, ctx, total)
    except KeyboardInterrupt:
        write_out(ctx)
        print("\nStopped. Everything finished so far is saved. Run the same command again to continue.")
        sys.exit(130)
    write_out(ctx, final=True)


def _loop(pend, templates, settings, use_scrape, ctx, total):
    store, comp, guard = ctx["store"], ctx["comp"], ctx["guard"]
    save_every = max(settings["run"]["save_every"], total // 20)
    t_run = time.time()
    for n, (i, raw) in enumerate(pend, 1):
        if guard.on:
            gpu.wait_if_hot(settings["gpu"])
        email = json.loads(raw).get("email", "")
        if os.environ.get("DRAFT_INTERRUPT_AFTER") and n == int(os.environ["DRAFT_INTERRUPT_AFTER"]):
            raise KeyboardInterrupt
        try:
            if os.environ.get("DRAFT_FAIL_EMAIL") == email:
                raise RuntimeError("simulated failure (test only)")
            lead, niche = build_lead(raw, templates, settings, store, use_scrape, guard)
            res = comp.compose(lead, niche, i)
            review = res["violations"]
            if not review and guard.might_offend(res["subject"] + "\n\n" + res["body"]):
                review = ["model flagged possible offence, please read before sending"]
            payload = dict(email=lead.email, name=lead.first or "Team", niche=niche, subject=res["subject"],
                           body=res["body"], fus=res["fus"], kind=res["kind"], uses_i=res["uses_i"],
                           company=lead.company_email, review=review, multi=lead.multi)
        except Exception as e:  # noqa: BLE001  one bad lead must never stop the run
            payload = dict(email=email, name="Team", niche="unknown", subject="", body="", fus=["", "", "", ""],
                           kind="error", uses_i=False, company=False,
                           review=[f"draft failed: {type(e).__name__}: {str(e)[:120]}"], multi=False)
        store.save(i, "review" if payload["review"] else "ok", json.dumps(payload), comp.counts)
        if os.environ.get("DRAFT_CRASH_AFTER") and n == int(os.environ["DRAFT_CRASH_AFTER"]):
            raise SystemExit("simulated crash (test only)")
        if n == 10 and len(pend) > 50:
            per = (time.time() - t_run) / n
            print(f"  Estimated time for this run: about {per * len(pend) / 60:.1f} minutes")
        if n % 25 == 0 or n == len(pend):
            per = (time.time() - t_run) / n
            print(f"  {n}/{len(pend)} done, about {per * (len(pend) - n) / 60:.1f} min left")
        if n % save_every == 0 and n != len(pend):
            write_out(ctx)


def write_out(ctx, final=False):
    out, store, stats, t0, comp, guard = (ctx[k] for k in ("out", "store", "stats", "t0", "comp", "guard"))
    ready, review, rows = [], [], []
    for _, status, payload in store.done():
        p = json.loads(payload)
        rows.append(p)
        r = [p["email"], p["name"], p["subject"], p["body"]] + p["fus"]
        (review if p["review"] else ready).append(r + ([" | ".join(p["review"])] if p["review"] else []))
    good = [p for p in rows if p["kind"] != "error"]
    kinds = Counter(p["kind"] for p in good)
    niches = Counter(p["niche"] for p in rows)
    n = max(len(good), 1)
    slot_share = {}
    for k, v in comp.counts.items():
        slot_share.setdefault(k.split("|")[0], []).append(v)
    over = [f"{s} ({max(v) / sum(v):.0%})" for s, v in slot_share.items()
            if len(v) > 1 and sum(v) >= 40 and not s.startswith(("sub", "sign", "optset")) and max(v) / sum(v) > 0.2]
    report = [
        ["Rows in the sheet", stats["rows_in"]],
        ["Columns used", stats["columns"]],
        ["Emails found (including several per cell)", stats["emails_found"]],
        ["Rows without an email", stats["no_email"]],
        ["Cells that held several emails", stats["multi_cells"]],
        ["Duplicate emails removed", stats["duplicates"]],
        ["No-reply addresses skipped", stats["skipped_noreply"]],
        ["Junk addresses skipped (images, placeholders)", stats["junk"]],
        ["Drafts finished", len(rows)],
        ["Ready To Send", len(ready)],
        ["Needs Review", len(review)],
        ["Mix short / options / normal", " / ".join(f"{kinds[k] / n:.0%}" for k in ("short", "options", "normal"))],
        ["Emails using the word I", f"{sum(p['uses_i'] for p in good) / n:.0%}"],
        ["Company mailboxes", f"{sum(p['company'] for p in good) / n:.0%}"],
        ["Name column shows Team", sum(p["name"] == "Team" for p in rows)],
        ["Niches", ", ".join(f"{k} {v}" for k, v in niches.most_common())],
        ["Lines used in over 20% of their slot", ", ".join(over) or "none"],
        ["Model", "on" if guard.on else "off"],
        ["Notes", "; ".join(stats["notes"] + guard.notes) or "none"],
        ["Minutes taken (this session)", round((time.time() - t0) / 60, 1)],
        ["Finished", "yes" if final else "partial save, run still going or stopped"],
    ]
    try:
        saved = export.write(out, ready, review, report)
    except Exception as e:  # noqa: BLE001
        msg = (f"Could not save the Excel file ({type(e).__name__}: {e}). Your drafts are safe in the memory file. "
               f"Free some disk space or close the file, then run the same command again.")
        if final:
            sys.exit(msg)
        print("WARNING:", msg)
        return
    if final:
        print("\n".join(f"{a}: {b}" for a, b in report))
        print(f"Saved: {saved}")


if __name__ == "__main__":
    main()
