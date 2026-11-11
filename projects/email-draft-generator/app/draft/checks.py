"""Benchmarks. Every subject, body and follow-up passes through here before it is allowed out."""
import re

BAD_CHARS = re.compile(r"[+;:=|*#@&_~^<>\[\]{}\\/()!\"—–•“”]")
# words that could read as criticism or trigger a proud owner
OFFENCE = re.compile(
    r"\b(fix|fixes|fixing|improve|improving|improvement|low|weak|weakness|struggl\w*|los(e|ing|t)|missing|miss|"
    r"lack\w*|poor|slow|empty|bad|fail\w*|problem\w*|broken|worse|worst|cheap|desperate|suffer\w*|"
    r"stronger|better|fuller|clearer|bigger|larger|not enough|underperform\w*|stagnant|struggle)\b",
    re.I,
)
GENERIC_CLAIM = re.compile(r"\bhelps?\s+(\w+\s+){0,3}grow\b|\bhelp(ed)?\s+(\w+\s+){0,2}grow\b", re.I)
TOOLS = re.compile(r"\b(ads|seo|reels|branding|websites?|graphics|thumbnails?|logos?|flyers?)\b", re.I)
COST = re.compile(r"\b(zero cost|no cost|free of cost|no charge)\b", re.I)
BARE_FREE = re.compile(r"\bfree\b(?! of cost)", re.I)
FIRST_PERSON = re.compile(r"\b(I|me|my|mine)\b")
VOWEL_EXC = re.compile(r"^(uni|use|usu|one|eu|ubi)", re.I)
SIGNOFFS_RE = re.compile(r"^[A-Z][A-Za-z ]+,$")


def words(text):
    return len(text.split())


def first_person(text):
    return bool(FIRST_PERSON.search(text))


def split_signoff(text):
    lines = text.rstrip().split("\n")
    if lines and SIGNOFFS_RE.match(lines[-1]):
        return "\n".join(lines[:-1]).rstrip(), lines[-1]
    return text, ""


def _repeats(text):
    ws = re.findall(r"[a-z0-9']+", text.lower())
    seen, out = set(), []
    for i in range(len(ws) - 3):
        g = tuple(ws[i:i + 4])
        if g in seen:
            out.append("repeated phrase: " + " ".join(g))
            break
        seen.add(g)
    return out


def _grammar(text):
    out = []
    out += _repeats(text)
    if "  " in text:
        out.append("double space")
    if re.search(r"\b(\w+) \1\b", text, re.I):
        out.append("repeated word")
    for m in re.finditer(r"\b(a|an) (\w+)", text):
        art, nxt = m.group(1), m.group(2)
        vowel = nxt[0].lower() in "aeiou" and not VOWEL_EXC.match(nxt)
        if art == "a" and vowel and not nxt.lower().startswith("hour"):
            out.append(f"a/an: {art} {nxt}")
        if art == "an" and not vowel and nxt.lower() not in ("hour", "honest"):
            out.append(f"a/an: {art} {nxt}")
    if re.search(r"[a-z]\s+[,.?]", text):
        out.append("space before punctuation")
    if re.search(r",,|\.\.", text):
        out.append("double punctuation")
    return out


def check_line(text):
    """Checks that apply to any single template line."""
    v = []
    if BAD_CHARS.search(text.replace("\n", " ")):
        v.append("symbol " + BAD_CHARS.search(text.replace("\n", " ")).group(0))
    if OFFENCE.search(text):
        v.append("offence word " + OFFENCE.search(text).group(0))
    if GENERIC_CLAIM.search(text):
        v.append("generic claim (help ... grow)")
    for ln in text.split("\n"):
        if len(TOOLS.findall(ln)) >= 3:
            v.append("tool list")
    v += _grammar(text)
    return v


def check_options(opts):
    v = []
    for o in opts:
        n = words(o)
        if not 2 <= n <= 6:
            v.append(f"option length: {o}")
        if OFFENCE.search(o):
            v.append(f"option offence word: {o}")
        if BAD_CHARS.search(o):
            v.append(f"option symbol: {o}")
    return v


def _mask(text, mask):
    for m in sorted(mask or [], key=len, reverse=True):
        if m:
            text = text.replace(m, "Sample Name")
    return text


def check_body(body, kind, word_range, signoffs, need_cost=True, mask=None):
    """kind: short | normal | options. Returns a list of violations (empty = pass)."""
    v = []
    main, sign = split_signoff(body)
    if not body or not body[0].isupper():
        v.append("first letter not capital")
    if sign not in signoffs:
        v.append("missing sign-off")
    for para in main.split("\n\n"):
        if para and not (para[0].isupper() or para[0].isdigit()):
            v.append("paragraph starts lowercase")
    lines = main.split("\n")
    num_lines = [ln for ln in lines if re.match(r"^\d\. ", ln)]
    body_for_line_checks = "\n".join(ln for ln in lines if not re.match(r"^\d\. ", ln))
    v += check_line(body_for_line_checks)
    lo, hi = word_range
    if not lo <= words(main) <= hi:
        v.append(f"word count {words(main)} outside {lo}-{hi}")
    if need_cost:
        if "30-60 second" not in main:
            v.append("sample line missing 30-60 second")
        if not COST.search(main):
            v.append("sample line missing cost wording")
        if BARE_FREE.search(main):
            v.append("bare word free")
    if kind == "options":
        if len(num_lines) != 3:
            v.append("options not exactly 3")
        else:
            idx = [i for i, ln in enumerate(lines) if re.match(r"^\d\. ", ln)]
            if idx != list(range(idx[0], idx[0] + 3)):
                v.append("options not contiguous")
            elif lines[idx[0] - 1] != "" or (idx[2] + 1 < len(lines) and lines[idx[2] + 1] != ""):
                v.append("options spacing")
            v += check_options([ln[3:] for ln in num_lines])
        if "Just reply with 1, 2, or 3." not in lines:
            v.append("reply line missing or not on its own line")
    elif num_lines:
        v.append("options in a non-options email")
    return v


def check_followup(text, signoffs, kind, word_range, need_cost=True, mask=None):
    v = []
    main, sign = split_signoff(text)
    if sign not in signoffs:
        v.append("missing sign-off")
    if not text or not text[0].isupper():
        v.append("first letter not capital")
    lines = main.split("\n")
    v += check_line("\n".join(ln for ln in lines if not re.match(r"^\d\. ", ln)))
    lo, hi = word_range
    if not lo <= words(main) <= hi:
        v.append(f"word count {words(main)} outside {lo}-{hi}")
    has_cost = bool(COST.search(main))
    if need_cost and (not has_cost or "30-60 second" not in main):
        v.append("sample line missing")
    if not need_cost and (re.search(r"\b(sample|free|zero cost|no cost)\b", main, re.I)):
        v.append("last follow-up must not pitch")
    if kind == "options":
        nl = [ln for ln in lines if re.match(r"^\d\. ", ln)]
        if len(nl) != 3 or "Just reply with 1, 2, or 3." not in lines:
            v.append("follow-up options malformed")
        else:
            v += check_options([ln[3:] for ln in nl])
    return v
