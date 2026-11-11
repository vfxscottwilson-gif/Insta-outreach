"""Email Draft Generator. Usage:  python run.py --input leads.xlsx --out drafts.xlsx
Other flags: --sheet NAME  --limit N  --fresh  --no-llm  --no-scrape  --lint  --check
"""
import argparse
import json
import sys
import time
from collections import Counter
from dataclasses import asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from draft import checks, config, export, gpu, leads as L, llm, names, scrape  # noqa: E402
from draft.compose import Composer  # noqa: E402
from draft.store import Store  # noqa: E402

import hashlib  # noqa: E402
import os  # noqa: E402
import re  # noqa: E402

NICHE_ORDER = ["youtube", "restaurant", "real_estate", "showroom", "ecommerce", "saas"]


def kw_hit(text, kws):
    return any(re.search(r"\b" + re.escape(k) + r"\b", text) for k in kws)


def resolve_niche(cell, text, templates):
    N = templates["niches"]
    for source in (cell.lower(), text.lower()):
        if not source.strip():
            continue
        for key in NICHE_ORDER:
            if kw_hit(source, N[key]["keywords"]):
                return key
    return None


def lint(templates, settings):
    bad = 0
    C = templates["common"]
    groups = [("common." + k, C[k]) for k in ("ctas", "asks", "samples", "samples_after_options", "fu_options_intro", "fu_options_question")]
    groups += [("common." + k, C[k]) for k in ("fu_reminder", "fu_angle", "fu_last")]
    groups += [("common.subjects_" + k, C["subjects_" + k]) for k in ("named", "biz", "plain")]
    for key, n in templates["niches"].items():
        for k in ("openers_person", "openers_company", "insights", "values", "sample_extra"):
            groups.append((f"{key}.{k}", n.get(k, [])))
    for name, lines in groups:
        for ln in lines:
            sample = re.sub(r"\{\w+\}", "Sample Name", ln).replace("\\n", "\n")
            v = checks.check_line(sample)
            if "subject" in name:
                v = [x for x in v if "symbol" not in x or ln.count(",") == 0]
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


def build_lead(raw, templates, settings, store, use_scrape, llm_cfg, llm_up):
    lead = L.Lead(**json.loads(raw))
    web = scrape.fetch(lead.website, settings["scrape"], store) if use_scrape else {}
    keep = settings["names"]["keep_unsplit"]
    lead.biz = names.clean_biz(lead.biz_raw, keep)
    lead.company_email = names.is_company_mailbox(lead.email)
    lead.first = names.first_name(lead.name_cell, lead.email, lead.biz, lead.company_email)
    lead.cuisine_phrase = L.cuisine_phrase(lead.cuisine)
    text = f"{lead.biz_raw} {web.get('title', '')} {web.get('description', '')}"
    niche = resolve_niche(lead.niche_cell, text, templates)
    if niche is None and llm_up:
        labels = list(templates["niches"].keys())
        niche = llm.classify_niche(llm_cfg, text, labels)
    return lead, niche or "generic"


def main():
    ap = argparse.ArgumentParser()
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
    llm_up = llm_cfg["enabled"] and not a.no_llm and llm.alive(llm_cfg)
    if a.check:
        print("Ollama:", "running" if llm.alive(llm_cfg) else "NOT running (the tool still works without it)")
        print("GPU temperature:", gpu.temperature() or "unknown")
        sys.exit(0 if lint(templates, settings) else 1)
    if not a.input or not a.out:
        ap.error("--input and --out are required")
    if llm_cfg["enabled"] and not a.no_llm and not llm_up:
        print("Note: Ollama is not running, so the model checks are skipped. Drafts are still built and checked.")

    t0 = time.time()
    all_leads, stats = L.read_input(a.input, settings, a.sheet)
    if a.limit:
        all_leads = all_leads[:a.limit]
    fp = f"{file_hash(a.input)}:{config.fingerprint(a.config)}:{a.limit}"
    store = Store(str(a.out) + ".state.db", fp, a.fresh)
    store.add_leads([(x.email, json.dumps(asdict(x))) for x in all_leads])
    comp = Composer(settings, templates, store.counts())
    pend = store.pending()
    total = store.total()
    print(f"{stats['rows_in']} rows read, {len(all_leads)} unique emails to draft, "
          f"{total - len(pend)} already done, {len(pend)} to go.")
    use_scrape = settings["scrape"]["enabled"] and not a.no_scrape
    t_run = time.time()
    for n, (i, raw) in enumerate(pend, 1):
        gpu.wait_if_hot(settings["gpu"]) if llm_up else None
        lead, niche = build_lead(raw, templates, settings, store, use_scrape, llm_cfg, llm_up)
        res = comp.compose(lead, niche, i)
        review = res["violations"]
        if llm_up and not review:
            if llm.might_offend(llm_cfg, res["subject"] + "\n\n" + res["body"]):
                review = ["model flagged possible offence"]
        payload = dict(email=lead.email, name=lead.first or "Team", niche=niche, subject=res["subject"],
                       body=res["body"], fus=res["fus"], kind=res["kind"], uses_i=res["uses_i"],
                       company=lead.company_email, review=review, multi=lead.multi)
        store.save(i, "review" if review else "ok", json.dumps(payload), comp.counts)
        if os.environ.get("DRAFT_CRASH_AFTER") and n == int(os.environ["DRAFT_CRASH_AFTER"]):
            raise SystemExit("simulated crash (test only)")
        if n % 25 == 0 or n == len(pend):
            per = (time.time() - t_run) / n
            print(f"  {n}/{len(pend)} done, about {per * (len(pend) - n) / 60:.1f} min left")
        if n % settings["run"]["save_every"] == 0:
            write_out(a.out, store, stats, t0, comp)
    write_out(a.out, store, stats, t0, comp, final=True)


def write_out(out, store, stats, t0, comp, final=False):
    ready, review, rows = [], [], []
    for _, status, payload in store.done():
        p = json.loads(payload)
        rows.append(p)
        r = [p["email"], p["name"], p["subject"], p["body"]] + p["fus"]
        (review if p["review"] else ready).append(r + ([" | ".join(p["review"])] if p["review"] else []))
    kinds = Counter(p["kind"] for p in rows)
    niches = Counter(p["niche"] for p in rows)
    n = max(len(rows), 1)
    slot_share = {}
    for k, v in comp.counts.items():
        slot = k.split("|")[0]
        slot_share.setdefault(slot, []).append(v)
    over = [f"{s} ({max(v) / sum(v):.0%})" for s, v in slot_share.items()
            if len(v) > 1 and not s.startswith("sub") and max(v) / sum(v) > 0.2]
    report = [
        ["Rows in the sheet", stats["rows_in"]],
        ["Emails found (including several per cell)", stats["emails_found"]],
        ["Rows without an email", stats["no_email"]],
        ["Cells that held several emails", stats["multi_cells"]],
        ["Duplicate emails removed", stats["duplicates"]],
        ["No-reply addresses skipped", stats["skipped_noreply"]],
        ["Drafts finished", len(rows)],
        ["Ready To Send", len(ready)],
        ["Needs Review", len(review)],
        ["Mix short / options / normal", " / ".join(f"{kinds[k] / n:.0%}" for k in ("short", "options", "normal"))],
        ["Emails using the word I", f"{sum(p['uses_i'] for p in rows) / n:.0%}"],
        ["Company mailboxes", f"{sum(p['company'] for p in rows) / n:.0%}"],
        ["Niches", ", ".join(f"{k} {v}" for k, v in niches.most_common())],
        ["Lines used in over 20% of their slot", ", ".join(over) or "none"],
        ["Minutes taken (this session)", round((time.time() - t0) / 60, 1)],
        ["Finished", "yes" if final else "partial save"],
    ]
    export.write(out, ready, review, report)
    if final:
        print("\n".join(f"{a}: {b}" for a, b in report))
        print(f"Saved: {out}")


if __name__ == "__main__":
    main()
