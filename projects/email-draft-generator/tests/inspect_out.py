import sys, collections, re, openpyxl
sys.stdout.reconfigure(encoding="utf-8")
wb = openpyxl.load_workbook(sys.argv[1], read_only=True)
rev = [r for r in wb["Needs Review"].iter_rows(min_row=2, values_only=True) if r[0]]
c = collections.Counter()
for r in rev:
    for part in str(r[8]).split(" | "):
        c[re.sub(r"\d+", "N", part)[:70]] += 1
print("review rows:", len(rev)); [print(" ", k, v) for k, v in c.most_common(15)]
if len(sys.argv) > 2:
    rows = [r for r in wb["Ready To Send"].iter_rows(min_row=2, values_only=True) if r[0]]
    for r in rows[int(sys.argv[2]):int(sys.argv[2]) + int(sys.argv[3])]:
        print("=" * 70); print(r[0], "|", r[1]); print("Subject:", r[2]); print(); print(r[3])
        for i, f in enumerate(r[4:8], 1): print(f"\n--- FU{i} ({len(f.split())}w) ---\n{f}")
