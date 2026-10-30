"""Message safety rules: length, spam words, links, repeated openers, free-sample mention."""
import re

MAX_WORDS = 40  # hard limit (the AI is asked for ~30-35)

# "free" is intentionally NOT here: your first message must mention the free sample.
SPAM_WORDS = [
    "guaranteed", "guarantee", "act now", "limited time", "click here", "buy now",
    "discount", "earn", "make money", "passive income", "cheap", "promo", "sale", "winner",
    "giveaway", "risk-free", "no obligation", "urgent", "100%", "$$$", "investment",
    "crypto", "link in bio", "whatsapp", "telegram", "dm me", "follow back",
    "exclusive deal", "congratulations", "once in a lifetime", "viral", "explode",
]
_URL = re.compile(r"https?://|www\.|\b\w+\.(com|net|org|io|co|pk)\b", re.I)
_FREE = re.compile(r"\bfree\b", re.I)
_NUMBERS = re.compile(r"\d[\d,.]*\s*(%|x\b|k\b|m\b|\+)|\$\s*\d", re.I)


def word_count(text: str) -> int:
    return len(text.split())


def opener(text: str) -> str:
    return " ".join(re.findall(r"[a-z']+", text.lower())[:4])


def problems(text: str, max_words: int = MAX_WORDS, used_openers=(), require_free=False,
             allowed_numbers=()) -> list:
    out = []
    if not text.strip():
        return ["empty message"]
    if word_count(text) > max_words:
        out.append(f"too long ({word_count(text)} words, max {max_words})")
    for w in SPAM_WORDS:
        if re.search(r"(?<!\w)" + re.escape(w) + r"(?!\w)", text, re.I):
            out.append(f"spam word '{w}'")
    if _URL.search(text):
        out.append("contains a link")
    if text.count("!") > 1:
        out.append("too many exclamation marks")
    if "@" in text:
        out.append("contains @")
    if require_free and not _FREE.search(text):
        out.append("must clearly say the sample is free")
    # Invented statistics are the #1 credibility killer: numbers only if they came from CASE_STUDIES.
    for m in _NUMBERS.finditer(text):
        if not any(m.group(0).strip() in a for a in allowed_numbers):
            out.append(f"contains a number/stat ('{m.group(0).strip()}') that is not in your case studies")
            break
    if opener(text) in used_openers:
        out.append("opening words too similar to another message; start differently")
    return out
