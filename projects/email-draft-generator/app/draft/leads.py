"""Reads the lead sheet (xlsx or csv), splits cells that hold several emails, removes duplicates."""
import re
from dataclasses import dataclass, field

import pandas as pd

from . import names

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
SKIP_RE = re.compile(r"^(noreply|no-reply|donotreply|do-not-reply|bounce|mailer-daemon|postmaster)@", re.I)

SYNONYMS = {
    "email": ["email", "emails", "e-mail", "email address", "email/contact", "contact email", "contact"],
    "name": ["name", "first name", "contact name", "owner", "owner name", "person"],
    "business": ["business", "business name", "company", "company name", "channel", "channel name",
                 "restaurant", "restaurant name", "brand", "organisation", "organization"],
    "niche": ["niche", "industry", "category", "type"],
    "city": ["city", "town", "search_city", "location"],
    "cuisine": ["cuisine"],
    "video_title": ["video title", "video", "pitch angle", "pitch_angle", "angle", "recent video"],
    "website": ["website", "site", "url", "web", "homepage"],
}
DEMONYM = {"italian", "indian", "japanese", "vietnamese", "mexican", "chinese", "thai", "korean", "french", "greek",
           "asian", "mediterranean", "american", "malaysian", "lebanese", "caribbean", "persian", "peruvian",
           "filipino", "turkish", "brazilian", "polish", "portuguese", "spanish", "ethiopian", "german"}
FOOD = {"pizza": "pizza", "sushi": "sushi", "burger": "burgers", "seafood": "seafood", "sandwich": "sandwiches",
        "barbecue": "barbecue", "chicken": "chicken", "noodle": "noodles", "ramen": "ramen", "tapas": "tapas",
        "brunch": "brunch", "breakfast": "breakfast", "steak_house": "steak", "coffee_shop": "coffee",
        "ice_cream": "ice cream", "donut": "donuts", "bakery": "baked goods", "kebab": "kebabs", "wings": "wings"}


@dataclass
class Lead:
    email: str
    name_cell: str = ""
    biz_raw: str = ""
    niche_cell: str = ""
    city: str = ""
    cuisine: str = ""
    title: str = ""
    website: str = ""
    row: int = 0
    multi: bool = False
    extra: dict = field(default_factory=dict)


def norm(h):
    return re.sub(r"\s+", " ", str(h).strip().lower().replace("_", " "))


def detect_columns(headers, overrides):
    m = {}
    nh = {norm(h): h for h in headers}
    for key, syns in SYNONYMS.items():
        o = (overrides or {}).get(key, "")
        if o and o in headers:
            m[key] = o
            continue
        for s in syns:
            if norm(s) in nh:
                m[key] = nh[norm(s)]
                break
    return m


def clean_title(text):
    m = re.search(r'Saw "([^"]+)"', str(text or ""))
    t = (m.group(1) if m else str(text or "")).strip()
    if not m and len(t) > 70:
        return ""
    if t.endswith("..") or not re.fullmatch(r"[A-Za-z0-9 ,.'\-]+", t) or not 14 <= len(t) <= 55:
        return ""
    lt = [c for c in t if c.isalpha()]
    if not lt or sum(c.isupper() for c in lt) / len(lt) > 0.5:
        return ""
    return t.rstrip(".,")


def cuisine_phrase(c):
    c = str(c or "").strip().lower().split(";")[-1].strip()
    if c in DEMONYM:
        return f"{c.capitalize()} food"
    return FOOD.get(c, "")


def read_input(path, settings, sheet=None):
    path = str(path)
    if path.lower().endswith(".csv"):
        df = pd.read_csv(path, dtype=str, keep_default_na=False)
    else:
        df = pd.read_excel(path, sheet_name=sheet if sheet is not None else 0, dtype=str, keep_default_na=False)
    cols = detect_columns(list(df.columns), settings.get("columns", {}))
    if "email" not in cols:
        raise SystemExit("No email column found. Add a header called Email, or map it in settings.toml [columns].")
    stats = dict(rows_in=len(df), no_email=0, duplicates=0, multi_cells=0, skipped_noreply=0, emails_found=0)
    seen, leads = set(), []
    for i, row in df.iterrows():
        def g(k):
            return str(row[cols[k]]).strip() if k in cols else ""
        found = EMAIL_RE.findall(g("email"))
        if not found:
            stats["no_email"] += 1
            continue
        if len(found) > 1:
            stats["multi_cells"] += 1
        biz_raw = g("business")
        name_cell = g("name")
        if "business" not in cols and name_cell:        # sheets where "name" is the business
            biz_raw, name_cell = name_cell, ""
        for e in found:
            e = e.lower()
            stats["emails_found"] += 1
            if SKIP_RE.match(e):
                stats["skipped_noreply"] += 1
                continue
            if e in seen:
                stats["duplicates"] += 1
                continue
            seen.add(e)
            leads.append(Lead(email=e, name_cell=name_cell, biz_raw=biz_raw, niche_cell=g("niche"),
                              city=names.clean_biz(g("city")), cuisine=g("cuisine"),
                              title=clean_title(g("video_title")), website=g("website"),
                              row=int(i) + 2, multi=len(found) > 1))
    return leads, stats
