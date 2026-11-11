"""Hardening patch: friendly errors, locked output, Ctrl+C, per-lead failure isolation (one-off, kept for the record)."""


def edit(path, pairs):
    s = open(path, encoding="utf-8").read()
    for o, n in pairs:
        assert o in s, (path, o[:70])
        s = s.replace(o, n, 1)
    open(path, "w", encoding="utf-8").write(s)


edit("app/draft/leads.py", [
    ("    path = str(path)\n    if path.lower().endswith(\".csv\"):\n        df = pd.read_csv(path, dtype=str, keep_default_na=False)\n    else:\n        df = pd.read_excel(path, sheet_name=sheet if sheet is not None else 0, dtype=str, keep_default_na=False)\n",
     "    path = str(path)\n    import os\n    if not os.path.exists(path):\n        raise SystemExit(f\"Input file not found: {path}\")\n"
     "    try:\n        if path.lower().endswith(\".csv\"):\n            try:\n                df = pd.read_csv(path, dtype=str, keep_default_na=False, encoding=\"utf-8-sig\")\n            except UnicodeDecodeError:\n                df = pd.read_csv(path, dtype=str, keep_default_na=False, encoding=\"latin-1\")\n        else:\n            df = pd.read_excel(path, sheet_name=sheet if sheet is not None else 0, dtype=str, keep_default_na=False)\n"
     "    except ValueError as e:\n        raise SystemExit(f\"Could not read the sheet ({e}). Check the --sheet name, or that the file is a real xlsx or csv.\")\n"
     "    except Exception as e:  # noqa: BLE001\n        raise SystemExit(f\"Could not open the file ({type(e).__name__}: {e}). Is it open in Excel, or damaged?\")\n"
     "    if len(df) == 0:\n        raise SystemExit(\"The sheet has a header but no rows below it.\")\n"),
])

edit("app/draft/export.py", [
    ("    tmp = str(path) + \".tmp\"\n    wb.save(tmp)\n    os.replace(tmp, path)\n",
     "    tmp = str(path) + \".tmp\"\n    wb.save(tmp)\n    try:\n        os.replace(tmp, path)\n    except PermissionError:\n"
     "        import time\n        alt = os.path.splitext(str(path))[0] + time.strftime(\"_saved_%H%M%S\") + \".xlsx\"\n"
     "        os.replace(tmp, alt)\n        print(f\"WARNING: {path} is open in Excel, so this save went to {alt}. Close the file and re-run to refresh it.\")\n"
     "        return alt\n    return str(path)\n"),
])

edit("app/draft/store.py", [
    ("        self.db = sqlite3.connect(path)\n        self.db.execute(\"PRAGMA journal_mode=WAL\")\n        self.db.executescript(",
     "        try:\n            self._open(path)\n        except sqlite3.DatabaseError:\n            raise SystemExit(f\"The memory file {path} is damaged. Run again with --fresh to start over.\")\n        old = self.meta(\"fp\")\n        if old and old != fingerprint:\n            raise SystemExit(\"The input sheet or the config changed since this run started.\\n\"\n                             \"Re-run with --fresh to start over, or restore the old files to resume.\")\n        self.set_meta(\"fp\", fingerprint)\n\n    def _open(self, path):\n        self.db = sqlite3.connect(path)\n        self.db.execute(\"PRAGMA journal_mode=WAL\")\n        self.db.executescript("),
    ("            \"CREATE TABLE IF NOT EXISTS cache(k TEXT PRIMARY KEY, v TEXT);\")\n        old = self.meta(\"fp\")\n        if old and old != fingerprint:\n            raise SystemExit(\"The input sheet or the config changed since this run started.\\n\"\n                             \"Re-run with --fresh to start over, or restore the old files to resume.\")\n        self.set_meta(\"fp\", fingerprint)\n",
     "            \"CREATE TABLE IF NOT EXISTS cache(k TEXT PRIMARY KEY, v TEXT);\")\n        self.db.execute(\"SELECT COUNT(*) FROM meta\")\n"),
])

edit("app/run.py", [
    ("    t_run = time.time()\n    for n, (i, raw) in enumerate(pend, 1):\n        gpu.wait_if_hot(settings[\"gpu\"]) if llm_up else None\n        lead, niche = build_lead(raw, templates, settings, store, use_scrape, llm_cfg, llm_up)\n        res = comp.compose(lead, niche, i)\n        review = res[\"violations\"]\n        if llm_up and not review:\n            if llm.might_offend(llm_cfg, res[\"subject\"] + \"\\n\\n\" + res[\"body\"]):\n                review = [\"model flagged possible offence\"]\n        payload = dict(email=lead.email, name=lead.first or \"Team\", niche=niche, subject=res[\"subject\"],\n                       body=res[\"body\"], fus=res[\"fus\"], kind=res[\"kind\"], uses_i=res[\"uses_i\"],\n                       company=lead.company_email, review=review, multi=lead.multi)\n",
     "    t_run = time.time()\n    try:\n        _loop(pend, templates, settings, store, use_scrape, llm_cfg, llm_up, comp, a, stats, t0, t_run)\n    except KeyboardInterrupt:\n        write_out(a.out, store, stats, t0, comp)\n        print(\"\\nStopped. Everything finished so far is saved. Run the same command again to continue.\")\n        sys.exit(130)\n    write_out(a.out, store, stats, t0, comp, final=True)\n\n\ndef _loop(pend, templates, settings, store, use_scrape, llm_cfg, llm_up, comp, a, stats, t0, t_run):\n    for n, (i, raw) in enumerate(pend, 1):\n        if llm_up:\n            gpu.wait_if_hot(settings[\"gpu\"])\n        email = json.loads(raw).get(\"email\", \"\")\n        try:\n            if os.environ.get(\"DRAFT_FAIL_EMAIL\") == email:\n                raise RuntimeError(\"simulated failure (test only)\")\n            lead, niche = build_lead(raw, templates, settings, store, use_scrape, llm_cfg, llm_up)\n            res = comp.compose(lead, niche, i)\n            review = res[\"violations\"]\n            if llm_up and not review:\n                if llm.might_offend(llm_cfg, res[\"subject\"] + \"\\n\\n\" + res[\"body\"]):\n                    review = [\"model flagged possible offence\"]\n            payload = dict(email=lead.email, name=lead.first or \"Team\", niche=niche, subject=res[\"subject\"],\n                           body=res[\"body\"], fus=res[\"fus\"], kind=res[\"kind\"], uses_i=res[\"uses_i\"],\n                           company=lead.company_email, review=review, multi=lead.multi)\n        except Exception as e:  # noqa: BLE001  one bad lead must never stop the run\n            payload = dict(email=email, name=\"Team\", niche=\"unknown\", subject=\"\", body=\"\", fus=[\"\", \"\", \"\", \"\"],\n                           kind=\"error\", uses_i=False, company=False,\n                           review=[f\"draft failed: {type(e).__name__}: {str(e)[:120]}\"], multi=False)\n"),
    ("        if n % settings[\"run\"][\"save_every\"] == 0:\n            write_out(a.out, store, stats, t0, comp)\n    write_out(a.out, store, stats, t0, comp, final=True)\n",
     "        if n % settings[\"run\"][\"save_every\"] == 0:\n            write_out(a.out, store, stats, t0, comp)\n"),
    ("    all_leads, stats = L.read_input(a.input, settings, a.sheet)\n",
     "    all_leads, stats = L.read_input(a.input, settings, a.sheet)\n    if not all_leads:\n        raise SystemExit(f\"No usable emails found in {stats['rows_in']} rows ({stats['no_email']} had no email).\")\n"),
    ("    export.write(out, ready, review, report)\n    if final:", "    saved = export.write(out, ready, review, report)\n    if final:"),
    ("        print(f\"Saved: {out}\")", "        print(f\"Saved: {saved}\")"),
])
print("ok")
