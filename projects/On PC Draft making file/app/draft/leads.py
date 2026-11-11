"""Reads the lead sheet (xlsx or csv), finds the columns, splits cells that hold several emails,
drops junk and duplicate addresses."""
import os
import re
from dataclasses import dataclass, field

import pandas as pd

from . import names

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
SKIP_RE = re.compile(r"^(noreply|no-reply|no_reply|donotreply|do-not-reply|bounce|mailer-daemon|postmaster)@", re.I)
JUNK_TLD = re.compile(r"\.(png|jpe?g|gif|webp|svg|bmp|ico|css|js|json|pdf|mp4|webm|woff2?)$", re.I)
JUNK_DOMAIN = re.compile(r"@(.*\.)?(sentry\.io|wixpress\.com|sentry-next\.wixpress\.com|example\.(com|org|net)|domain\.com|"
                         r"email\.com|yourdomain\.com|mysite\.com|website\.com|test\.com|godaddy\.com|placeholder\.com)$", re.I)
JUNK_LOCAL = re.compile(r"^(example|your|youremail|yourname|name|firstname|lastname|username|user|email|test|"
                        r"john\.?doe|jane\.?doe|[0-9a-f]{24,})@", re.I)

SYNONYMS = {
    "email": ["email", "emails", "e-mail", "e mail", "email address", "email/contact", "contact email",
              "mail", "email id", "contact"],
    "name": ["name", "first name", "firstname", "contact name", "owner", "owner name", "person", "full name"],
    "business": ["business", "business name", "company", "company name", "channel", "channel name",
                 "restaurant", "restaurant name", "brand", "organisation", "organization", "store", "shop name"],
    "niche": ["niche", "industry", "category", "type", "segment"],
    "city": ["city", "town", "search city", "location"],
    "cuisine": ["cuisine"],
    "video_title": ["video title", "video", "pitch angle", "angle", "recent video", "latest video"],
    "website": ["website", "site", "url", "web", "homepage", "link"],
}
HEADER_NICHE = {"channel": "youtube", "channel name": "youtube", "restaurant": "restaurant",
                "restaurant name": "restaurant", "cuisine": "restaurant"}
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
    hint: str = ""                      # niche implied by a column header such as Channel or Cuisine
    extra: dict = field(default_factory=dict)


def norm(h):
    return re.sub(r"\s+", " ", str(h).strip().lower().replace("_", " "))


def detect_columns(headers, overrides):
    m = {}
    nh = {}
    for h in headers:
        nh.setdefault(norm(h), h)
    for key, syns in SYNONYMS.items():
        o = (overrides or {}).get(key, "")
        if o:
            if o in headers:
                m[key] = o
                continue
            raise SystemExit(f"settings.toml [columns] {key} = \"{o}\" but the sheet has no such header. "
                             f"Headers found: {', '.join(map(str, headers))}")
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


def _load(path, sheet, header):
    if path.lower().endswith(".csv"):
        try:
            return pd.read_csv(path, dtype=str, keep_default_na=False, encoding="utf-8-sig", header=header)
        except UnicodeDecodeError:
            return pd.read_csv(path, dtype=str, keep_default_na=False, encoding="latin-1", header=header)
    return pd.read_excel(path, sheet_name=sheet if sheet is not None else 0, dtype=str,
                         keep_default_na=False, header=header)


def read_input(path, settings, sheet=None):
    path = str(path)
    if not os.path.exists(path):
        raise SystemExit(f"Input file not found: {path}")
    if not path.lower().endswith((".xlsx", ".xlsm", ".csv")):
        raise SystemExit("The input must be an .xlsx or .csv file. Old .xls files: open in Excel and Save As .xlsx.")
    overrides = settings.get("columns", {})
    notes = []
    try:
        df = _load(path, sheet, 0)
        cols = detect_columns(list(df.columns), overrides)
        if "email" not in cols:                                  # header may sit below a title row
            raw = _load(path, sheet, None)
            for r in range(min(10, len(raw))):
                if any(norm(v) in SYNONYMS["email"] for v in raw.iloc[r]):
                    df = _load(path, sheet, r)
                    cols = detect_columns(list(df.columns), overrides)
                    notes.append(f"header found on row {r + 1}")
                    break
        if "email" not in cols and len(df):                      # last resort: the column that holds emails
            head = df.head(200)
            best, share = None, 0.0
            for c in df.columns:
                s = sum(bool(EMAIL_RE.search(str(v))) for v in head[c]) / max(len(head), 1)
                if s > share:
                    best, share = c, s
            if best is not None and share >= 0.3:
                cols["email"] = best
                notes.append(f"no Email header, used column '{best}' because it holds email addresses")
    except SystemExit:
        raise
    except ValueError as e:
        raise SystemExit(f"Could not read the sheet ({e}). Check the --sheet name, or that the file is a real xlsx or csv.")
    except PermissionError:
        raise SystemExit("Could not open the input file. Close it in Excel and run again.")
    except Exception as e:  # noqa: BLE001
        raise SystemExit(f"Could not open the file ({type(e).__name__}: {e}). Is it open in Excel, or damaged?")
    if len(df) == 0:
        raise SystemExit("The sheet has a header but no rows below it.")
    if "email" not in cols:
        raise SystemExit("No email column found. Add a header called Email, or map it in settings.toml [columns]. "
                         f"Headers found: {', '.join(map(str, df.columns))}")
    hint = ""
    for key in ("business", "cuisine"):
        if key in cols and norm(cols[key]) in HEADER_NICHE:
            hint = HEADER_NICHE[norm(cols[key])]
            break
    stats = dict(rows_in=len(df), no_email=0, duplicates=0, multi_cells=0, skipped_noreply=0, emails_found=0,
                 junk=0, notes=notes, columns=", ".join(f"{k}={v}" for k, v in cols.items()))
    seen, leads = set(), []
    for i, row in df.iterrows():
        def g(k):
            return str(row[cols[k]]).strip() if k in cols else ""
        found = list(dict.fromkeys(e.lower().strip(".") for e in EMAIL_RE.findall(g("email"))))
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
            stats["emails_found"] += 1
            if SKIP_RE.match(e):
                stats["skipped_noreply"] += 1
                continue
            if JUNK_TLD.search(e) or JUNK_DOMAIN.search(e) or JUNK_LOCAL.match(e) or ".." in e:
                stats["junk"] += 1
                continue
            if e in seen:
                stats["duplicates"] += 1
                continue
            seen.add(e)
            leads.append(Lead(email=e, name_cell=name_cell, biz_raw=biz_raw, niche_cell=g("niche"),
                              city=names.clean_biz(g("city")), cuisine=g("cuisine"),
                              title=clean_title(g("video_title")), website=g("website"),
                              row=int(i) + 2, multi=len(found) > 1, hint=hint))
    return leads, stats
