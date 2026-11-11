"""Excel output: Title Case headers, every row exactly 21 high, Arial 11, safe atomic save."""
import os

from openpyxl import Workbook
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE
from openpyxl.styles import Alignment, Font

HEAD = ["Email", "Name", "Subject Line", "Body", "Follow-up 1", "Follow-up 2", "Follow-up 3", "Follow-up 4"]
WIDTHS = [34, 12, 42, 70, 55, 55, 55, 55]


def _safe(v):
    if isinstance(v, str):
        v = ILLEGAL_CHARACTERS_RE.sub("", v)
        if v[:1] in "=+-@":                 # never let a cell be read as a formula
            v = "'" + v
    return v


def _sheet(ws, header, rows, widths):
    ws.append(header)
    for r in rows:
        ws.append([_safe(c) for c in r])
    font = Font(name="Arial", size=11)
    bold = Font(name="Arial", size=11, bold=True)
    for row in ws.iter_rows():
        ws.row_dimensions[row[0].row].height = 21
        for c in row:
            c.font = bold if c.row == 1 else font
            c.alignment = Alignment(wrap_text=False, vertical="center")
    for i, w in enumerate(widths):
        ws.column_dimensions[chr(65 + i)].width = w
    ws.freeze_panes = "A2"


def write(path, ready, review, report):
    wb = Workbook()
    ws = wb.active
    ws.title = "Ready To Send"
    _sheet(ws, HEAD, ready, WIDTHS)
    ws2 = wb.create_sheet("Needs Review")
    _sheet(ws2, HEAD + ["Reason"], review, WIDTHS + [60])
    ws3 = wb.create_sheet("Report")
    _sheet(ws3, ["Item", "Value"], report, [46, 70])
    tmp = str(path) + ".tmp"
    wb.save(tmp)
    try:
        os.replace(tmp, path)
    except PermissionError:
        import time
        alt = os.path.splitext(str(path))[0] + time.strftime("_saved_%H%M%S") + ".xlsx"
        os.replace(tmp, alt)
        print(f"WARNING: {path} is open in Excel, so this save went to {alt}. Close the file and re-run to refresh it.")
        return alt
    return str(path)
