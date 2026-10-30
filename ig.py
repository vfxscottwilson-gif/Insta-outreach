"""Reads PUBLIC info of business/creator accounts through Meta's official Business Discovery API.
Personal or private accounts cannot be read -> reported as 'unreadable' (you check them manually)."""
import os
import requests

VERSION = os.getenv("GRAPH_VERSION", "v24.0")


def fetch(handle: str) -> dict:
    token, uid = os.getenv("IG_ACCESS_TOKEN", "").strip(), os.getenv("IG_USER_ID", "").strip()
    if not token or not uid:
        return {"status": "disabled"}
    fields = (f"business_discovery.username({handle})"
              "{username,name,biography,followers_count,media_count,media.limit(6){caption}}")
    try:
        r = requests.get(f"https://graph.facebook.com/{VERSION}/{uid}",
                         params={"fields": fields, "access_token": token}, timeout=30)
    except requests.RequestException:
        return {"status": "rate_limited"}
    if r.status_code == 200:
        d = r.json().get("business_discovery", {})
        caps = [(m.get("caption") or "")[:220] for m in d.get("media", {}).get("data", []) if m.get("caption")]
        return {"status": "ok", "name": d.get("name", ""), "bio": d.get("biography", ""),
                "followers": d.get("followers_count"), "captions": caps[:4]}
    try:
        code = r.json().get("error", {}).get("code")
    except ValueError:
        code = None
    if code in (190, 102, 10, 200):
        return {"status": "token_error"}
    if code in (4, 17, 32, 613):
        return {"status": "rate_limited"}
    return {"status": "unreadable"}
