"""Copy the app's data out of one Postgres database and into another (see MOVE-DATABASE.md).

Run with the engine's Python, from app\\engine:

    uv run python ..\\..\\database\\move_data.py export  <folder>                 reads DATABASE_URL from app\\.env
    uv run python ..\\..\\database\\move_data.py import  <folder> --to <new url>  the new database must already have the
                                                                               migrations applied (tools.migrate)
    uv run python ..\\..\\database\\move_data.py list                              table names and row counts only

One CSV file per table (schemas public and engine). The export holds personal data (lead addresses, snippets):
keep the folder private and delete it after the move. Never prints a connection string.
"""
import argparse
import pathlib
import sys

import psycopg

SCHEMAS = ("public", "engine")
SKIP = {("engine", "schema_migrations")}          # the new database records its own migrations


def tables(conn):
    return [(s, t) for s, t in conn.execute(
        "select table_schema, table_name from information_schema.tables where table_schema = any(%s) "
        "and table_type = 'BASE TABLE' order by 1, 2", (list(SCHEMAS),)).fetchall() if (s, t) not in SKIP]


def columns(conn, s, t):
    """Real columns only: generated ones are computed again by the new database."""
    return [r[0] for r in conn.execute(
        "select column_name from information_schema.columns where table_schema = %s and table_name = %s "
        "and is_generated = 'NEVER' order by ordinal_position", (s, t)).fetchall()]


def export(conn, folder: pathlib.Path) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    for s, t in tables(conn):
        cols = ", ".join(f'"{c}"' for c in columns(conn, s, t))
        with (folder / f"{s}.{t}.csv").open("wb") as f, conn.cursor().copy(
                f'copy (select {cols} from "{s}"."{t}") to stdout with (format csv, header true)') as cp:
            for chunk in cp:
                f.write(chunk)
        print(f"exported {s}.{t}")


def load(conn, folder: pathlib.Path) -> None:
    conn.execute("set session_replication_role = replica")      # no triggers or foreign-key checks while loading
    for s, t in tables(conn):
        path = folder / f"{s}.{t}.csv"
        if not path.exists():
            print(f"skipped {s}.{t} (no file)")
            continue
        with path.open("rb") as f:
            header = f.readline().decode().strip()
            conn.execute(f'truncate "{s}"."{t}" cascade')
            with conn.cursor().copy(f'copy "{s}"."{t}" ({header}) from stdin with (format csv)') as cp:
                while chunk := f.read(1 << 16):
                    cp.write(chunk)
        print(f"imported {s}.{t}")
    for s, t, col in conn.execute(                              # identity counters continue after the highest id
            "select table_schema, table_name, column_name from information_schema.columns "
            "where table_schema = any(%s) and is_identity = 'YES'", (list(SCHEMAS),)).fetchall():
        conn.execute(f"select setval(pg_get_serial_sequence('\"{s}\".\"{t}\"', '{col}'), "
                     f"coalesce((select max(\"{col}\") from \"{s}\".\"{t}\"), 0) + 1, false)")
    conn.execute("set session_replication_role = origin")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("cmd", choices=("export", "import", "list"))
    p.add_argument("folder", nargs="?")
    p.add_argument("--to", help="connection string of the NEW database (import only)")
    a = p.parse_args()
    if a.cmd == "import":
        if not a.folder or not a.to:
            p.error("import needs <folder> and --to <new database url>")
        with psycopg.connect(a.to) as conn:
            load(conn, pathlib.Path(a.folder))
        return 0
    from outreach import config, db
    config.load_env()
    with db.connect() as conn:
        if a.cmd == "list":
            for s, t in tables(conn):
                print(f"{s}.{t}: {conn.execute(f'select count(*) from \"{s}\".\"{t}\"').fetchone()[0]} rows")
            return 0
        if not a.folder:
            p.error("export needs <folder>")
        export(conn, pathlib.Path(a.folder))
    return 0


if __name__ == "__main__":
    sys.exit(main())
