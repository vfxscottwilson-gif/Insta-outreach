"""Version 2 hardening for the smaller modules (one-off patch, kept for the record). Run from the project folder."""


def edit(path, pairs):
    s = open(path, encoding="utf-8").read()
    for o, n in pairs:
        assert o in s, (path, o[:70])
        s = s.replace(o, n, 1)
    open(path, "w", encoding="utf-8").write(s)


edit("app/draft/checks.py", [
    ('FIRST_PERSON = re.compile(r"\\b(I|me|my|mine)\\b")', 'FIRST_PERSON = re.compile(r"\\b(I|[Mm]e|[Mm]y|[Mm]ine)\\b")'),
    ("    if not body or not body[0].isupper():\n        v.append(\"first letter not capital\")\n    if sign not in signoffs:",
     "    if not body or not body[0].isupper():\n        v.append(\"first letter not capital\")\n    v += _shape(main)\n    if sign not in signoffs:"),
    ("def check_body(body, kind, word_range, signoffs, need_cost=True, mask=None):",
     "def _shape(main):\n    \"\"\"Structure every email and follow-up must have.\"\"\"\n    v = []\n"
     "    if \"{\" in main or \"}\" in main:\n        v.append(\"unfilled placeholder\")\n"
     "    if re.search(r\"\\b(None|nan|null)\\b\", main):\n        v.append(\"empty value leaked into the text\")\n"
     "    for para in main.split(\"\\n\\n\"):\n        last = para.strip().split(\"\\n\")[-1]\n"
     "        if last and last[-1] not in \".?\":\n            v.append(\"paragraph does not end with a period or question mark\")\n            break\n"
     "    if \"\\n\\n\\n\" in main:\n        v.append(\"extra blank line\")\n"
     "    return v\n\n\ndef check_body(body, kind, word_range, signoffs, need_cost=True, mask=None):"),
])

edit("app/draft/export.py", [
    ("from openpyxl.styles import Alignment, Font\n",
     "from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE\nfrom openpyxl.styles import Alignment, Font\n"),
    ("def _sheet(ws, header, rows, widths):\n    ws.append(header)\n    for r in rows:\n        ws.append(r)\n",
     "def _safe(v):\n    if isinstance(v, str):\n        v = ILLEGAL_CHARACTERS_RE.sub(\"\", v)\n"
     "        if v[:1] in \"=+-@\":                 # never let a cell be read as a formula\n            v = \"'\" + v\n    return v\n\n\n"
     "def _sheet(ws, header, rows, widths):\n    ws.append(header)\n    for r in rows:\n        ws.append([_safe(c) for c in r])\n"),
])

edit("app/draft/store.py", [
    ("        if fresh and os.path.exists(path):\n            os.remove(path)\n",
     "        self._lock(path)\n        if fresh:\n            for suffix in (\"\", \"-wal\", \"-shm\"):\n                if os.path.exists(path + suffix):\n                    os.remove(path + suffix)\n"),
    ("    def _open(self, path):",
     "    def _lock(self, path):\n        \"\"\"One run per output file. The lock frees itself if the program dies.\"\"\"\n"
     "        self._lockf = open(path + \".lock\", \"a+\")\n        try:\n            try:\n                import msvcrt\n"
     "                self._lockf.seek(0)\n                msvcrt.locking(self._lockf.fileno(), msvcrt.LK_NBLCK, 1)\n"
     "            except ImportError:\n                import fcntl\n                fcntl.flock(self._lockf.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)\n"
     "        except OSError:\n            raise SystemExit(\"Another run is already writing to this output file. Wait for it to finish, \"\n"
     "                             \"or use a different --out name.\")\n\n    def _open(self, path):"),
    ("        self.db = sqlite3.connect(path)\n", "        self.db = sqlite3.connect(path, timeout=30)\n"),
])

edit("app/draft/scrape.py", [
    ("    url = (url or \"\").strip().split(\";\")[0].strip()\n    if not url.startswith(\"http\"):\n        return {}\n",
     "    url = (url or \"\").strip().split(\";\")[0].split()[0].strip() if (url or \"\").strip() else \"\"\n"
     "    if url and not url.startswith(\"http\") and re.fullmatch(r\"[\\w.-]+\\.[A-Za-z]{2,}(/\\S*)?\", url):\n        url = \"https://\" + url\n"
     "    if not url.startswith(\"http\"):\n        return {}\n"),
])

edit("config/settings.toml", [
    ("timeout_seconds = 60\n", "timeout_seconds = 60\noffence_check = true       # second opinion on tone. Switches itself off if it flags over 30% of drafts.\n"),
    ("save_every = 50            # partial Excel save every N leads",
     "save_every = 50            # partial Excel save every N leads (large runs save about 20 times in total)"),
])
print("ok")
