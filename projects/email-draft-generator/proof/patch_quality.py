"""One-off quality patch (kept for the record)."""


def edit(path, pairs):
    s = open(path, encoding="utf-8").read()
    for o, n in pairs:
        assert o in s, (path, o[:60])
        s = s.replace(o, n, 1)
    open(path, "w", encoding="utf-8").write(s)


edit("app/draft/compose.py", [
    ('need_cost=ftype != "last", mask=[lead.biz, lead.city])',
     'need_cost=ftype != "last", mask=[lead.biz, lead.city, lead.title])'),
])
edit("app/draft/checks.py", [
    ("def _grammar(text):\n    out = []",
     "def _repeats(text):\n"
     "    ws = re.findall(r\"[a-z0-9']+\", text.lower())\n"
     "    seen, out = set(), []\n"
     "    for i in range(len(ws) - 3):\n"
     "        g = tuple(ws[i:i + 4])\n"
     "        if g in seen:\n"
     "            out.append(\"repeated phrase: \" + \" \".join(g))\n"
     "            break\n"
     "        seen.add(g)\n"
     "    return out\n\n\n"
     "def _grammar(text):\n    out = []\n    out += _repeats(text)"),
])
edit("config/templates.toml", [
    ("It is a small first step that lets you judge the work before anything else is discussed. Does that sound reasonable?",
     "It is a small first step, with nothing else to decide until it has been seen. Does that sound reasonable?"),
])
print("ok")
