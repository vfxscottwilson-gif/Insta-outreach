"""Local model through Ollama. Used only for small checkable jobs. Every call degrades gracefully."""
import re

import httpx


def alive(cfg):
    try:
        return httpx.get(cfg["host"].rstrip("/") + "/api/tags", timeout=3).status_code == 200
    except Exception:
        return False


def ask(cfg, prompt):
    try:
        r = httpx.post(cfg["host"].rstrip("/") + "/api/generate", timeout=cfg.get("timeout_seconds", 60),
                       json={"model": cfg["model"], "prompt": prompt, "stream": False, "think": False,
                             "options": {"temperature": 0, "num_predict": 40}})
        text = r.json().get("response", "")
        return re.sub(r"<think>.*?</think>", "", text, flags=re.S).strip()
    except Exception:
        return None


def classify_niche(cfg, text, labels):
    out = ask(cfg, f"Business information: {text[:600]}\nWhich ONE label fits best: {', '.join(labels)}? "
                   f"Answer with only the label.")
    if not out:
        return None
    out = out.lower().strip(" .\n")
    return out if out in labels else None


def might_offend(cfg, text):
    """True when the model thinks a proud owner could read the text as criticism. None if unavailable."""
    out = ask(cfg, "Read this cold email. Could a proud business owner take any line as criticism, an insult or "
                   "an assumption about them? Answer only YES or NO.\n\n" + text[:1500])
    if not out:
        return None
    return out.upper().startswith("YES")
