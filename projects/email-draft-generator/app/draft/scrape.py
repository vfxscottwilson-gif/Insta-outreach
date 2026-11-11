"""Reads a lead's own public homepage (title and description only), politely. Failure is fine."""
import re
import time
import urllib.robotparser
from urllib.parse import urlparse

import httpx

SOCIAL = ("instagram.com", "facebook.com", "tiktok.com", "twitter.com", "x.com", "linkedin.com", "youtube.com",
          "pin.it", "pinterest.com")
_last = {}


def fetch(url, cfg, store=None):
    url = (url or "").strip().split(";")[0].strip()
    if not url.startswith("http"):
        return {}
    host = urlparse(url).netloc.lower()
    if not host or any(host.endswith(s) for s in SOCIAL):
        return {}
    if store is not None:
        hit = store.cache_get("web:" + host)
        if hit is not None:
            return hit
    out = {}
    try:
        rp = urllib.robotparser.RobotFileParser()
        rp.set_url(f"{urlparse(url).scheme}://{host}/robots.txt")
        rp.parse(httpx.get(rp.url, timeout=4, follow_redirects=True).text.splitlines())
        if rp.can_fetch("*", url):
            wait = cfg.get("delay_seconds", 1.0) - (time.time() - _last.get(host, 0))
            if wait > 0:
                time.sleep(wait)
            _last[host] = time.time()
            r = httpx.get(url, timeout=cfg.get("timeout_seconds", 8), follow_redirects=True,
                          headers={"User-Agent": "Mozilla/5.0 (compatible; DraftBot/1.0)"})
            html = r.text[:200000]
            t = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
            d = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']', html, re.S | re.I)
            out = {"title": re.sub(r"\s+", " ", t.group(1)).strip()[:150] if t else "",
                   "description": re.sub(r"\s+", " ", d.group(1)).strip()[:300] if d else ""}
    except Exception:
        out = {}
    if store is not None:
        store.cache_set("web:" + host, out)
    return out
