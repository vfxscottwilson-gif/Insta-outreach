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
    r"mail|general|feedback|help|events?|catering|manager|owner|management|business|studio|agency|"
    r"collab\w*|sponsor\w*|talent|noreply|no-reply|donotreply|accounts?|billing|hello\d*|welcome|newsletter)$",
    re.I,
)
TITLES = {"dr", "mr", "mrs", "ms", "prof", "coach", "pastor", "sir", "chef"}
BUSINESS_WORDS = {
    "media", "agency", "studio", "studios", "labs", "group", "team", "official", "channel", "tv", "show",
    "podcast", "news", "kitchen", "restaurant", "cafe", "bistro", "grill", "pizza", "realty", "homes",
    "properties", "capital", "academy", "school", "shop", "store", "motors", "auto", "bar", "pub",
}


def fold(text):
    return unicodedata.normalize("NFKD", str(text or "")).encode("ascii", "ignore").decode()


def letters(s):
    return re.sub(r"[^a-z]", "", s.lower())


def _fix_token(tok, keep):
    if tok in keep or not tok.isalpha():
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
    if (tok.islower() and len(tok) >= 10) or (tok.istitle() and len(tok) >= 12):
        parts = wordninja.split(tok.lower())
        if len(parts) >= 2 and all(len(p) >= 3 for p in parts):
            return " ".join(p.title() for p in parts)
    return tok


def clean_biz(raw, keep=()):
    """Display name for a business or channel. Safe: returns '' when unsure."""
    t = fold(raw).strip()
    if not t:
        return ""
    t = re.sub(r"\(.*?\)", " ", t)
    for sep in (" - ", " | ", ": ", " : ", ", "):
        if sep in t:
            t = t.split(sep)[0]
    t = t.replace("&", " and ").replace("+", " and ")
    t = re.sub(r"[^A-Za-z0-9 '.\-]", " ", t)
    t = re.sub(r"\s+", " ", t).strip(" .-")
    keep = set(keep)
    out = " ".join(_fix_token(tok, keep) for tok in t.split())
    out = re.sub(r"\bAi\b", "AI", out)
    if letters(out) != letters(t):                              # invariant
        out = t
    if out.islower():
        out = out.title()
    if " " not in out and re.search(r"[A-Za-z]", out) and re.search(r"\d", out):
        return ""                                               # handle such as llamarider37
    if re.search(r"\d{3,}", out) or len(out) > 40 or len(out) < 2:
        return ""                                               # handles like llamarider37
    return out


def _known_first_name(word):
    w = word.strip(".,'")
    return w.isalpha() and 2 <= len(w) <= 20 and _DET.get_gender(w) != "unknown"


def _person_shaped(biz):
    """'Freya Farrington' yes, 'Build Your Tribe' no. Needs a dictionary first name plus plain surname words."""
    w = biz.split()
    if not 2 <= len(w) <= 3 or not all(x.isalpha() and x[0].isupper() for x in w):
        return ""
    if not _known_first_name(w[0]) or any(x.lower() in BUSINESS_WORDS | {"the", "and", "of", "my", "your"} for x in w[1:]):
        return ""
    if len(w[1]) < 3:
        return ""
    return w[0].capitalize()


def first_name(sheet_name, email, biz="", company=False):
    """Sheet name wins. Else a dictionary first name from a personal email handle or a person-shaped
    channel name. Else ''. Never guesses."""
    if company:
        return ""                      # shared mailbox: never addressed by a person's name
    if not sheet_name and not company and biz and _person_shaped(biz):
        return _person_shaped(biz)
    toks = [t for t in re.sub(r"[^A-Za-z' .]", " ", fold(sheet_name)).split() if t.lower().strip(".") not in TITLES]
    if toks:
        w = toks[0].strip(".,'")
        if w.isalpha() and 2 <= len(w) <= 20 and w.lower() not in BUSINESS_WORDS and len(toks) <= 4:
            return w.capitalize()
    local = (email or "").split("@")[0]
    local = re.split(r"[._\-+]", local)[0]
    if local.isalpha() and len(local) >= 3 and not GENERIC_PREFIX.match(local) and _known_first_name(local):
        return local.capitalize()
    return ""


def is_company_mailbox(email):
    local = (email or "").split("@")[0].lower()
    base = re.split(r"[._\-+]", local)[0]
    return bool(GENERIC_PREFIX.match(local) or GENERIC_PREFIX.match(base))
