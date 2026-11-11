"""Name cleaning, run-together word splitting, first names, mailbox type.

Hard invariant: cleaning may add spaces and fix capitals, but never adds, drops or
changes a letter ("Sandwich" must never become "WTICH").
"""
import re
import unicodedata

import gender_guesser.detector as _gg
import wordninja

_DET = _gg.Detector(case_sensitive=False)

GENERIC_PREFIX = re.compile(
    r"^(info|hello|hi|hey|contact|support|care|cares|careers?|jobs?|hr|partnerships?|partners?|sales|admin|"
    r"team|office|enquir\w*|inquir\w*|press|media|booking\w*|reservations?|orders?|marketing|service\w*|"
    r"mail|email|inbox|general|feedback|help|events?|catering|manager|owner|management|business|biz|studio|"
    r"agency|collab\w*|sponsor\w*|talent|noreply|no-reply|donotreply|accounts?|billing|hello\d*|welcome|"
    r"newsletter|dev|web|webmaster|shop|store|news|tech|ads|pr|it|design|video|digital|social|creative|legal|"
    r"finance|ops|crew|staff|club|fans|work|mgmt|connect|reach|ask|main|public|official|the|my|your|me|"
    r"customer\w*|client\w*|privacy|security|abuse|postmaster|root|test|demo|sample|example|user|guest)\d*$",
    re.I,
)
TITLES = {"dr", "mr", "mrs", "ms", "miss", "prof", "coach", "pastor", "sir", "chef", "rev"}
BUSINESS_WORDS = {
    "media", "agency", "studio", "studios", "labs", "group", "team", "official", "channel", "tv", "show",
    "podcast", "news", "kitchen", "restaurant", "cafe", "bistro", "grill", "pizza", "realty", "homes",
    "properties", "capital", "academy", "school", "shop", "store", "motors", "auto", "bar", "pub", "market",
    "avenue", "street", "house", "company", "inc", "ltd", "llc", "co", "info", "admin", "support", "sales",
    "office", "manager", "owner", "reception", "desk", "customer", "service", "none", "nan", "null", "unknown",
}
NOT_NAMES = {"the", "an", "and", "my", "our", "your", "this", "that", "big", "new", "old", "best", "real", "just",
             "hey", "team", "merch", "ask", "mr", "sir", "king", "queen", "prince", "baby", "miss", "lady", "guy",
             "man", "boy", "girl", "coach", "chef", "doc", "major", "captain", "true", "pure", "pro", "top", "art",
             "star", "sunny", "lucky", "happy", "angel", "love", "hope", "joy", "sky", "rain", "storm", "blue"}
# place names that double as first names: a handle like london@ is a branch mailbox, not a person
PLACES = {"london", "brooklyn", "paris", "kingston", "hamilton", "windsor", "surrey", "vancouver", "toronto",
          "calgary", "ottawa", "montreal", "dallas", "houston", "phoenix", "denver", "boston", "chicago", "vegas",
          "berlin", "milan", "melbourne", "perth", "dublin", "york", "richmond", "burlington", "cambridge",
          "oxford", "bristol", "preston", "lincoln", "jackson", "madison", "camden", "chelsea", "kensington",
          "devon", "trinity", "regina", "victoria", "sydney", "florence", "savannah", "austin", "india", "china"}
NULLS = {"", "none", "nan", "null", "n/a", "na", "-", "unknown"}


def fold(text):
    return unicodedata.normalize("NFKD", str(text or "")).encode("ascii", "ignore").decode()


def letters(s):
    return "".join(ch for ch in str(s).casefold() if ch.isalnum())


def _fix_token(tok, keep):
    if tok in keep or not (tok.isascii() and tok.isalpha()):
        return tok
    m = re.fullmatch(r"([A-Z][a-z]+)([A-Z]{2,})", tok)          # SandWICH
    if m:
        if len(wordninja.split(tok.lower())) == 1:
            return tok.title()
        return f"{m.group(1)} {m.group(2).title()}"
    if re.search(r"[a-z][A-Z]", tok):                           # DeliciousKitchen
        parts = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", tok).split()
        if len(parts[0]) >= 3 and parts[0] not in ("Mac", "Mc"):
            return " ".join(parts)
        return tok
    if tok.isupper() and len(tok) >= 5:                         # SHARRA -> Sharra, BBQ stays
        tok = tok.title()
    if (tok.islower() and len(tok) >= 10) or (tok.istitle() and len(tok) >= 12):
        parts = wordninja.split(tok.lower())
        if len(parts) >= 2 and all(len(p) >= 3 for p in parts):
            return " ".join(p.title() for p in parts)
    return tok


def clean_biz(raw, keep=()):
    """Display name for a business, channel or city. Safe: returns '' when unsure."""
    t = unicodedata.normalize("NFC", str(raw if raw is not None else "")).strip()
    if t.lower() in NULLS:
        return ""
    t = re.sub(r"<[^>]*>", " ", t)
    t = re.sub(r"\(.*?\)", " ", t).replace("’", "'").replace("‘", "'")
    for sep in (" - ", " – ", " — ", " | ", ": ", " : ", ", "):
        if sep in t:
            t = t.split(sep)[0]
    t = t.replace("&", " and ").replace("+", " and ").replace("_", " ")
    t = "".join(ch if (ch.isalnum() or ch in " '.-") else " " for ch in t)
    t = re.sub(r"\s+", " ", t).strip(" .-'")
    if not t:
        return ""
    keep = set(keep)
    out = " ".join(_fix_token(tok, keep) for tok in t.split())
    out = re.sub(r"\bAi\b", "AI", out)
    if letters(out) != letters(t):                              # invariant: never change a letter
        out = t
    if out.islower():
        out = out.title()
    if " " not in out and re.search(r"[^\W\d]", out) and re.search(r"\d", out):
        return ""                                               # handle such as llamarider37
    if re.fullmatch(r"[\d .\-]+", out) or re.search(r"\d{4,}", out) or len(out) > 40 or len(out) < 2:
        return ""
    return out


def _known_first_name(word):
    w = fold(word).strip(".,'")
    return (w.isalpha() and 2 <= len(w) <= 20 and w.lower() not in NOT_NAMES
            and _DET.get_gender(w) != "unknown")


def _person_shaped(biz):
    """'Freya Farrington' yes, 'Build Your Tribe' no."""
    w = biz.split()
    if not 2 <= len(w) <= 3 or not all(x.isalpha() and x[0].isupper() for x in w):
        return ""
    if not _known_first_name(w[0]) or any(x.lower() in BUSINESS_WORDS | {"the", "and", "of", "my", "your"} for x in w[1:]):
        return ""
    if len(w[1]) < 3 or _known_first_name(w[1]) and len(w) == 2 and w[1].lower() in ("may", "june", "april"):
        return ""
    return w[0].capitalize()


def first_name(sheet_name, email, biz="", company=False, niche="", city=""):
    """Order: the Name you typed, then a dictionary first name from a personal email handle,
    then (YouTube only) a person-shaped channel name. Otherwise '' and the sheet shows Team. Never guesses."""
    toks = [t for t in re.findall(r"[^\W\d_]+(?:[-'][^\W\d_]+)*", str(sheet_name or ""))
            if t.lower() not in TITLES]
    if toks and str(sheet_name).strip().lower() not in NULLS:
        w = toks[0]
        if 2 <= len(w) <= 20 and w.lower() not in BUSINESS_WORDS and len(toks) <= 4 and not GENERIC_PREFIX.match(w):
            return "-".join(p.capitalize() for p in w.split("-"))
    if company:
        return ""                                               # shared mailbox: no inferred name
    local = (email or "").split("@")[0]
    local = re.split(r"[._\-+]", local)[0]
    place = local.lower() in PLACES or (city and local.lower() == fold(city).lower().replace(" ", ""))
    if (local.isalpha() and len(local) >= 3 and not place and not GENERIC_PREFIX.match(local)
            and _known_first_name(local)):
        return local.capitalize()
    if niche == "youtube" and biz:
        return _person_shaped(biz)
    return ""


def is_company_mailbox(email):
    local = (email or "").split("@")[0].lower()
    base = re.split(r"[._\-+]", local)[0]
    return bool(GENERIC_PREFIX.match(local) or GENERIC_PREFIX.match(base))
