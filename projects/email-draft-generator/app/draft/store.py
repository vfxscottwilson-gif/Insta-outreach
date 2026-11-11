"""SQLite memory. Every finished lead is saved at once, so a crash resumes where it stopped."""
import json
import sqlite3


class Store:
    def __init__(self, path, fingerprint, fresh=False):
        import os
        if fresh and os.path.exists(path):
            os.remove(path)
        try:
            self._open(path)
        except sqlite3.DatabaseError:
            raise SystemExit(f"The memory file {path} is damaged. Run again with --fresh to start over.")
        old = self.meta("fp")
        if old and old != fingerprint:
            raise SystemExit("The input sheet or the config changed since this run started.\n"
                             "Re-run with --fresh to start over, or restore the old files to resume.")
        self.set_meta("fp", fingerprint)

    def _open(self, path):
        self.db = sqlite3.connect(path)
        self.db.execute("PRAGMA journal_mode=WAL")
        self.db.executescript(
            "CREATE TABLE IF NOT EXISTS meta(k TEXT PRIMARY KEY, v TEXT);"
            "CREATE TABLE IF NOT EXISTS leads(i INTEGER PRIMARY KEY, email TEXT UNIQUE, status TEXT, payload TEXT);"
            "CREATE TABLE IF NOT EXISTS cache(k TEXT PRIMARY KEY, v TEXT);")
        self.db.execute("SELECT COUNT(*) FROM meta")

    def meta(self, k, default=None):
        r = self.db.execute("SELECT v FROM meta WHERE k=?", (k,)).fetchone()
        return r[0] if r else default

    def set_meta(self, k, v):
        self.db.execute("INSERT OR REPLACE INTO meta VALUES(?,?)", (k, v))
        self.db.commit()

    def add_leads(self, leads_json):
        for i, (email, payload) in enumerate(leads_json):
            self.db.execute("INSERT OR IGNORE INTO leads VALUES(?,?,?,?)", (i, email, "pending", payload))
        self.db.commit()

    def pending(self):
        return self.db.execute("SELECT i, payload FROM leads WHERE status='pending' ORDER BY i").fetchall()

    def save(self, i, status, payload, counts):
        self.db.execute("UPDATE leads SET status=?, payload=? WHERE i=?", (status, payload, i))
        self.db.execute("INSERT OR REPLACE INTO meta VALUES('counts',?)", (json.dumps(counts),))
        self.db.commit()

    def counts(self):
        return json.loads(self.meta("counts", "{}"))

    def done(self):
        return self.db.execute("SELECT i, status, payload FROM leads WHERE status!='pending' ORDER BY i").fetchall()

    def total(self):
        return self.db.execute("SELECT COUNT(*) FROM leads").fetchone()[0]

    def cache_get(self, k):
        r = self.db.execute("SELECT v FROM cache WHERE k=?", (k,)).fetchone()
        return json.loads(r[0]) if r else None

    def cache_set(self, k, v):
        self.db.execute("INSERT OR REPLACE INTO cache VALUES(?,?)", (k, json.dumps(v)))
        self.db.commit()
