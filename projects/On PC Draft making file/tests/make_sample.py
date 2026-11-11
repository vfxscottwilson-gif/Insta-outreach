"""Builds tests/sample_leads.xlsx from your real lead files plus edge cases."""
import sys, openpyxl, pandas as pd
sys.stdout.reconfigure(encoding="utf-8")
rows = []
wb = openpyxl.load_workbook(r"C:\Users\Khizar Malik\Downloads\YT leads.xlsx", read_only=True, data_only=True)
n = 0
for r in wb["ALL (view only)"].iter_rows(min_row=2, values_only=True):
    r = tuple(r) + (None,) * (29 - len(r))
    if r[4] and r[12] and "@" in str(r[12]):
        rows.append(dict(Niche="YouTube", Email=r[12], Name="", Business=r[4], City="", Cuisine="", **{"Video Title": r[16]}, Website=r[14]))
        n += 1
    if n >= 40: break
wb.close()
wb = openpyxl.load_workbook(r"C:\Users\Khizar Malik\Downloads\Canada resturants leads.xlsx", read_only=True, data_only=True)
n = 0
for r in wb["canada_ranked"].iter_rows(min_row=2, values_only=True):
    r = tuple(r) + (None,) * (54 - len(r))
    if r[4] and r[13] and (r[6] or 0) >= 60:
        rows.append(dict(Niche="Restaurant", Email=r[13], Name="", Business=r[4], City=r[33], Cuisine=r[30], **{"Video Title": ""}, Website=r[14]))
        n += 1
    if n >= 40: break
wb.close()
rows += [
    dict(Niche="Restaurant", Email="owner.maria@gmail.com; info@deliciouskitchen.ca", Name="Maria", Business="DeliciousKitchen", City="Calgary", Cuisine="italian", **{"Video Title": ""}, Website=""),
    dict(Niche="Restaurant", Email="info@sandwichshop.ca", Name="", Business="SandWICH", City="Toronto", Cuisine="sandwich", **{"Video Title": ""}, Website=""),
    dict(Niche="Real Estate", Email="john@smithrealty.com", Name="John", Business="Smith Realty Group", City="Edmonton", Cuisine="", **{"Video Title": ""}, Website=""),
    dict(Niche="", Email="care@carshowroom.ca", Name="", Business="Prime Motors Showroom", City="Surrey", Cuisine="", **{"Video Title": ""}, Website=""),
    dict(Niche="Restaurant", Email="info@deliciouskitchen.ca", Name="", Business="Delicious Kitchen", City="Calgary", Cuisine="", **{"Video Title": ""}, Website=""),
    dict(Niche="", Email="hello@somethingweird.ca", Name="", Business="", City="", Cuisine="", **{"Video Title": ""}, Website=""),
    dict(Niche="Restaurant", Email="", Name="", Business="No Email Cafe", City="Toronto", Cuisine="", **{"Video Title": ""}, Website=""),
]
pd.DataFrame(rows).to_excel("tests/sample_leads.xlsx", index=False)
print(len(rows), "rows written")
