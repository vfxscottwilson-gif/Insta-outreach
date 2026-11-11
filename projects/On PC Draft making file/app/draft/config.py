"""Loads and validates settings.toml and templates.toml from the project config folder."""
import hashlib
import re
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = ROOT / "config"

COMMON_LISTS = ["signoffs", "ctas", "asks", "samples", "samples_after_options", "fu_reminder", "fu_angle",
                "fu_options_intro", "fu_options_question", "fu_last", "subjects_named", "subjects_named_noun",
                "subjects_biz", "subjects_plain"]
NICHE_LISTS = ["openers_person", "openers_company", "insights", "values", "options"]
NICHE_STR = ["noun", "sample_noun", "niche_word"]
SETTINGS = {"run": ["seed", "share_short", "share_options", "share_normal", "share_first_person", "save_every"],
            "words": ["short", "normal", "options", "followup"],
            "subject": ["min_chars", "target_chars", "soft_max_chars"],
            "llm": ["enabled", "host", "model"], "gpu": ["guard", "pause_above_c", "resume_below_c"],
            "scrape": ["enabled"], "names": ["keep_unsplit"]}
KNOWN_SLOTS = {"biz", "city", "cuisine", "title", "noun", "sample_noun", "niche_word", "biz_or", "sample", "name"}


def _read(path):
    try:
        with open(path, "rb") as f:
            return tomllib.load(f)
    except FileNotFoundError:
        raise SystemExit(f"Missing config file: {path}")
    except tomllib.TOMLDecodeError as e:
        raise SystemExit(f"{path.name} has a typing mistake: {e}\n"
                         f"Usual causes: a missing quote, a missing comma between lines, or a quote inside the text.")


def validate(settings, templates):
    """Returns a list of problems in plain words. Empty list = fine."""
    p = []
    for sec, keys in SETTINGS.items():
        if sec not in settings:
            p.append(f"settings.toml: section [{sec}] is missing")
            continue
        for k in keys:
            if k not in settings[sec]:
                p.append(f"settings.toml: [{sec}] {k} is missing")
    if p:
        return p
    r = settings["run"]
    total = r["share_short"] + r["share_options"] + r["share_normal"]
    if abs(total - 1.0) > 0.011:
        p.append(f"settings.toml: share_short + share_options + share_normal must add to 1.0 (now {total:.2f})")
    for k, v in settings["words"].items():
        if not (isinstance(v, list) and len(v) == 2 and v[0] < v[1]):
            p.append(f"settings.toml: [words] {k} must look like [50, 60]")
    C = templates.get("common")
    if not C:
        return p + ["templates.toml: section [common] is missing"]
    for k in COMMON_LISTS:
        if not isinstance(C.get(k), list) or len(C[k]) < 2:
            p.append(f"templates.toml: [common] {k} needs at least 2 lines")
    if C.get("reply_line") != "Just reply with 1, 2, or 3.":
        p.append('templates.toml: reply_line must stay exactly "Just reply with 1, 2, or 3."')
    N = templates.get("niches", {})
    if "generic" not in N:
        p.append("templates.toml: [niches.generic] is required as the safe fallback")
    for key, n in N.items():
        for k in NICHE_STR:
            if not isinstance(n.get(k), str) or not n.get(k):
                p.append(f"templates.toml: [niches.{key}] {k} is missing")
        for k in NICHE_LISTS:
            if not isinstance(n.get(k), list) or len(n[k]) < 2:
                p.append(f"templates.toml: [niches.{key}] {k} needs at least 2 lines")
        for k in ("openers_person", "openers_company"):
            if isinstance(n.get(k), list) and not any("{" not in ln for ln in n[k]):
                p.append(f"templates.toml: [niches.{key}] {k} needs at least one line without a placeholder, "
                         f"for leads with no business name")
        for s in n.get("options", []):
            if not (isinstance(s, list) and len(s) == 3):
                p.append(f"templates.toml: [niches.{key}] every option set needs exactly 3 options")

    def walk(prefix, obj):
        if isinstance(obj, str):
            for slot in re.findall(r"\{(\w*)\}", obj):
                if slot not in KNOWN_SLOTS:
                    p.append(f"templates.toml: {prefix} uses unknown placeholder {{{slot}}}")
            if obj.count("{") != obj.count("}"):
                p.append(f"templates.toml: {prefix} has an unclosed brace: {obj[:50]}")
        elif isinstance(obj, list):
            for x in obj:
                walk(prefix, x)
        elif isinstance(obj, dict):
            for k, v in obj.items():
                walk(f"{prefix}.{k}" if prefix else k, v)
    walk("", templates)
    return p


def load(config_dir=None):
    d = Path(config_dir) if config_dir else CONFIG_DIR
    settings = _read(d / "settings.toml")
    templates = _read(d / "templates.toml")
    problems = validate(settings, templates)
    if problems:
        raise SystemExit("The config files need fixing before a run:\n  - " + "\n  - ".join(problems[:15]))
    return settings, templates


def fingerprint(config_dir=None):
    d = Path(config_dir) if config_dir else CONFIG_DIR
    h = hashlib.sha256()
    for name in ("settings.toml", "templates.toml"):
        h.update((d / name).read_bytes())
    return h.hexdigest()[:16]
