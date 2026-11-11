"""Local model through Ollama. Used only for small checkable jobs.
Every call degrades gracefully, and a circuit breaker switches the model off when it misbehaves,
so a slow or over-strict model can never sink a run."""
import re

import httpx


def status(cfg):
    """(running, model_present, installed_models)"""
    try:
        r = httpx.get(cfg["host"].rstrip("/") + "/api/tags", timeout=3)
        if r.status_code != 200:
            return False, False, []
        have = [m.get("name", "") for m in r.json().get("models", [])]
        want = cfg["model"]
        present = any(h == want or h.split(":")[0] == want or h == want + ":latest" for h in have)
        return True, present, have
    except Exception:  # noqa: BLE001
        return False, False, []


def alive(cfg):
    return status(cfg)[0]


def ask(cfg, prompt):
    base = {"model": cfg["model"], "prompt": prompt, "stream": False,
            "options": {"temperature": 0, "num_predict": 40}}
    for extra in ({"think": False}, {}):            # older Ollama or non-thinking models reject "think"
        try:
            r = httpx.post(cfg["host"].rstrip("/") + "/api/generate", timeout=cfg.get("timeout_seconds", 60),
                           json={**base, **extra})
            if r.status_code != 200:
                continue
            text = r.json().get("response", "")
            text = re.sub(r"<think>.*?</think>", "", text, flags=re.S).strip()
            if text:
                return text
        except httpx.TimeoutException:
            return None
        except Exception:  # noqa: BLE001
            continue
    return None


class Guard:
    """Wraps the model. Disables itself after repeated failures or when it flags too much."""

    def __init__(self, cfg, enabled):
        self.cfg, self.on = cfg, enabled
        self.fails = 0
        self.judged = self.flagged = 0
        self.judge_on = enabled and cfg.get("offence_check", True)
        self.notes = []

    def _call(self, prompt):
        if not self.on:
            return None
        out = ask(self.cfg, prompt)
        if out is None:
            self.fails += 1
            if self.fails >= 3:
                self.on = self.judge_on = False
                self.notes.append("model switched off after 3 failed calls in a row")
            return None
        self.fails = 0
        return out

    def classify_niche(self, text, labels):
        out = self._call(f"Business information: {text[:600]}\nWhich ONE label fits best: {', '.join(labels)}? "
                         f"If unsure answer generic. Answer with only the label.")
        if not out:
            return None
        out = out.lower().strip(" .\n\"'")
        return out if out in labels else None

    def might_offend(self, text):
        if not self.judge_on:
            return False
        out = self._call("Read this cold email. Could a proud business owner take any line as criticism, an insult "
                         "or an assumption about them? Answer only YES or NO.\n\n" + text[:1500])
        if out is None:
            return False
        self.judged += 1
        yes = out.upper().lstrip(" \"'*").startswith("YES")
        self.flagged += yes
        if self.judged >= 20 and self.flagged / self.judged > 0.3:
            self.judge_on = False
            self.notes.append(f"model offence check switched off: it flagged {self.flagged} of the first "
                              f"{self.judged} drafts, which means it is too strict to trust")
            return False
        return yes
