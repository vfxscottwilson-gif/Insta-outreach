"""Smooth chart proposal for app/dashboard/dash/charts.py. NOT imported by the app (the hyphen in the file name is deliberate).

Run (original venv):  .venv\\Scripts\\python.exe docs\\ui-audit\\chart-smoothing.py
  -> runs the self-test, then writes chart-preview.html next to this file (open it in a browser; add #light for the light theme).

What it replaces in charts.py (same call shapes, same markup contract: .mark groups with <title>, .i0-.i39 stagger classes):
  line_chart  L83-97   -> smooth_line_chart      polyline + dots on every point  -> monotone cubic path, no dots, end dot only
  area_chart  L122-139 -> smooth_area_chart      polyline + flat 12% polygon     -> monotone path + gradient area + 7-day average
  compare_chart L142-164 -> smooth_compare_chart 31 halo dots cut the line       -> two smooth lines, one hover per day, both values
  bar_chart   L64-80   -> smooth_bar_chart       square rects, scaleY squash     -> round-top path (r=6), rises under a clip
  hbar_list   L100-112 -> smooth_hbar_list       rx=2 bars, 9px text             -> pill bars, real-size text, optional row links
  donut       L167-188 -> smooth_donut           butt segments, stroke grows     -> round segment ends, gaps, sweep-in
  sparkline   L213-221 -> smooth_sparkline       polyline                        -> monotone path + end dot
Not replaced: mini_bar (change rx 2 -> 4), stacked_bars (drop the Team workload card instead, see the audit).

Widths: pass w = the card's real inner width so text is not rescaled (1280 px screen: span-4 278, span-6 448, span-8 614, span-12 950).
Colours and motion live in charts-smooth.css; hover crosshair, tooltip and number tween in charts-smooth.js.
"""
import re
import sys
import xml.etree.ElementTree as ET
from datetime import date
from itertools import count
from math import ceil, pi, sqrt
from pathlib import Path

from markupsafe import Markup, escape

ML, MR, MT, MB = 34, 18, 12, 24   # plot margins: y labels left, half of the last x label right
STAGGER = 40                      # app.css defines .i0 .. .i39
_ids = count(1)


def _uid(prefix):
    return f"{prefix}{next(_ids)}"


def _i(n):
    return f"i{min(n, STAGGER - 1)}"


# ---------------------------------------------------------------- monotone cubic (Fritsch-Carlson)

def monotone_tangents(xs, ys):
    """Fritsch-Carlson slopes for strictly increasing xs. Between two points the curve never leaves [y_k, y_k+1]."""
    n = len(xs)
    dx = [xs[i + 1] - xs[i] for i in range(n - 1)]
    if any(v <= 0 for v in dx):
        raise ValueError("x values must be strictly increasing")
    d = [(ys[i + 1] - ys[i]) / dx[i] for i in range(n - 1)]                      # secant slopes
    m = [d[0]] + [0.0 if d[i - 1] * d[i] <= 0 else (d[i - 1] + d[i]) / 2 for i in range(1, n - 1)] + [d[-1]]
    for i in range(n - 1):
        if d[i] == 0:
            m[i] = m[i + 1] = 0.0                                                # flat run stays flat
            continue
        a, b = m[i] / d[i], m[i + 1] / d[i]
        s = a * a + b * b
        if s > 9:                                                                # outside the monotone disc: pull back
            t = 3 / sqrt(s)
            m[i], m[i + 1] = t * a * d[i], t * b * d[i]
    return m


def monotone_path(pts):
    """SVG path 'M..C..C..' through pts [(x, y)] with strictly increasing x; '' for none, 'M' only for one point."""
    if not pts:
        return ""
    if len(pts) == 1:
        return f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    m = monotone_tangents(xs, ys)
    out = [f"M{xs[0]:.1f},{ys[0]:.1f}"]
    for i in range(len(pts) - 1):
        h = (xs[i + 1] - xs[i]) / 3                                             # control points sit at x thirds: x(t) is linear
        out.append(f"C{xs[i] + h:.1f},{ys[i] + m[i] * h:.1f} {xs[i + 1] - h:.1f},{ys[i + 1] - m[i + 1] * h:.1f} "
                   f"{xs[i + 1]:.1f},{ys[i + 1]:.1f}")
    return "".join(out)


# ---------------------------------------------------------------- shared pieces

def _axis(peak, intervals=3):
    """Nice y step (1/2/5 x 10^k) with at most `intervals` gaps, and the rounded-up top."""
    for step in (s * 10 ** k for k in range(12) for s in (1, 2, 5)):
        if step * intervals >= peak:
            break
    return step, step * ceil(max(peak, 1) / step)


def _svg(w, h, title, summary, inner):
    cls = "chart sm wide" if w > 450 else "chart sm"   # wide charts scroll inside the card on a phone instead of shrinking their text
    return Markup(f'<svg class="{cls}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title)}. {escape(summary)}">'
                  f'<title>{escape(title)}</title><desc>{escape(summary)}</desc>{inner}</svg>')


def _empty(w, h, title):
    return _svg(w, h, title, "No data.", f'<text x="{w / 2:.0f}" y="{h / 2:.0f}" text-anchor="middle">No data yet</text>')


def _summary(rows, unit):
    if not rows:
        return "No data."
    label, peak = max(rows, key=lambda r: r[1])
    return f"{sum(v for _, v in rows):,} {unit} in total." + (f" Highest: {peak:,} on {label}." if peak else "")


def _yaxis(w, ph, step, top):
    out = ""
    for v in range(0, top + 1, step):
        y = MT + ph - ph * v / top
        out += (f'<line x1="{ML}" x2="{w - MR}" y1="{y:.1f}" y2="{y:.1f}" class="grid{" base" if v == 0 else ""}"/>'
                f'<text x="{ML - 8}" y="{y + 4:.1f}" text-anchor="end">{v:,}</text>')
    return out


def _xlabels(texts, xs, y, max_labels=6):
    """At most `max_labels` labels, counted back from the last so the newest point is always named."""
    n = len(texts)
    step = max(1, ceil(n / max_labels))
    return "".join(f'<text x="{xs[i]:.1f}" y="{y}" text-anchor="middle">{escape(texts[i])}</text>'
                   for i in range(n) if (n - 1 - i) % step == 0)


def _day(iso):
    d = date.fromisoformat(iso)
    return f"{d.day} {d:%b}", f"{d:%a} {d.day} {d:%b}"       # axis tick, tooltip label (weekday shows the weekend dips)


def _mark(title, body, x=None, y=None, y2=None, href=None):
    """Hoverable, keyboard-focusable mark. data-x/y/y2 (viewBox units) tell charts-smooth.js where the crosshair goes."""
    data = "".join(f' data-{k}="{v:.1f}"' for k, v in (("x", x), ("y", y), ("y2", y2)) if v is not None)
    if href:
        return f'<a class="mark" href="{escape(href)}"{data}><title>{escape(title)}</title>{body}</a>'
    return f'<g class="mark" tabindex="0"{data}><title>{escape(title)}</title>{body}</g>'


def _hit(x0, x1, y0, y1):
    return f'<rect class="hit" x="{x0:.1f}" y="{y0:.1f}" width="{max(x1 - x0, 1):.1f}" height="{y1 - y0:.1f}" rx="6"/>'


def _gradient(gid, y0, y1):
    return (f'<defs><linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="0" y1="{y0}" x2="0" y2="{y1}">'
            '<stop offset="0" class="gs0"/><stop offset="1" class="gs1"/></linearGradient></defs>')


def _endpoint(x, y):
    return (f'<g class="endpt"><circle class="halo" cx="{x:.1f}" cy="{y:.1f}" r="9"/>'
            f'<circle class="dot" cx="{x:.1f}" cy="{y:.1f}" r="4.5"/></g>')


_HOVER = '<line class="xh" y1="{y0}" y2="{y1}"/><circle class="fp" r="5"/>'


# ---------------------------------------------------------------- line / area

def smooth_area_chart(rows, title, w=614, h=250, unit="leads", avg=7):
    """Daily series [(YYYY-MM-DD, n)] on evenly spaced days: monotone line, gradient area, optional trailing average."""
    if not rows:
        return _empty(w, h, title)
    vals = [v for _, v in rows]
    step, top = _axis(max(vals))
    pw, ph, n = w - ML - MR, h - MT - MB, len(rows)
    base = MT + ph
    xs = [ML + pw * i / max(n - 1, 1) for i in range(n)]

    def y(v):
        return MT + ph - ph * v / top
    ys = [y(v) for v in vals]
    gid, line_d = _uid("ag"), monotone_path(list(zip(xs, ys)))
    area = line = avg_line = ""
    if n > 1:
        area = f'<path class="agrad" fill="url(#{gid})" d="{line_d}L{xs[-1]:.1f},{base:.1f}L{xs[0]:.1f},{base:.1f}Z"/>'
        line = f'<path class="line draw" pathLength="1" d="{line_d}"/>'
    if avg and n > avg:   # a trailing mean needs a full window: start at the first complete one
        pts = [(xs[i], y(sum(vals[i - avg + 1:i + 1]) / avg)) for i in range(avg - 1, n)]
        avg_line = f'<path class="line avg" d="{monotone_path(pts)}"/>'
    slot = pw / max(n - 1, 1)
    marks = ""
    for i, (label, v) in enumerate(rows):
        tick, tip = _day(label)
        marks += _mark(f"{tip}: {v:,} {unit}", _hit(max(ML, xs[i] - slot / 2), min(ML + pw, xs[i] + slot / 2), MT, base),
                       x=xs[i], y=ys[i])
    inner = (_gradient(gid, MT, base) + _yaxis(w, ph, step, top) + area + avg_line + line + _endpoint(xs[-1], ys[-1])
             + _xlabels([_day(r[0])[0] for r in rows], xs, h - 6) + _HOVER.format(y0=MT, y1=base) + marks)
    return _svg(w, h, title, _summary([(_day(a)[1], b) for a, b in rows], unit), inner)


def smooth_line_chart(rows, title, w=950, h=200, unit="clients"):
    """Series [(YYYY-MM-DD, n)] placed by real date so gaps stay visible; line only (no area)."""
    if not rows:
        return _empty(w, h, title)
    step, top = _axis(max(v for _, v in rows))
    pw, ph = w - ML - MR, h - MT - MB
    days = [date.fromisoformat(r[0]).toordinal() for r in rows]
    lo, hi = days[0], days[-1]
    xs = [ML + pw * (d - lo) / max(hi - lo, 1) for d in days]
    ys = [MT + ph - ph * v / top for _, v in rows]
    base = MT + ph
    line = f'<path class="line draw" pathLength="1" d="{monotone_path(list(zip(xs, ys)))}"/>' if len(rows) > 1 else ""
    marks = "".join(_mark(f"{_day(r[0])[1]}: {r[1]:,} {unit}",
                          _hit(xs[i] - 8, xs[i] + 8, MT, base), x=xs[i], y=ys[i]) for i, r in enumerate(rows))
    inner = (_yaxis(w, ph, step, top) + line + _endpoint(xs[-1], ys[-1]) + _xlabels([_day(r[0])[0] for r in rows], xs, h - 6)
             + _HOVER.format(y0=MT, y1=base) + marks)
    return _svg(w, h, title, _summary([(_day(a)[1], b) for a, b in rows], unit), inner)


def smooth_compare_chart(this, last, title, w=278, h=220, unit="leads"):
    """Cumulative leads per day-of-month: this month (accent, filled) against last month (grey ghost)."""
    days = max(len(this), len(last))
    if not days:
        return _empty(w, h, title)
    step, top = _axis(max(this + last, default=0))
    pw, ph = w - ML - MR, h - MT - MB
    base = MT + ph
    xs = [ML + pw * i / max(days - 1, 1) for i in range(days)]

    def y(v):
        return MT + ph - ph * v / top
    gid = _uid("cg")
    ghost = f'<path class="line ghost" d="{monotone_path([(xs[i], y(v)) for i, v in enumerate(last)])}"/>' if len(last) > 1 else ""
    pts = [(xs[i], y(v)) for i, v in enumerate(this)]
    now = area = ""
    if len(this) > 1:
        d = monotone_path(pts)
        area = f'<path class="agrad" fill="url(#{gid})" d="{d}L{pts[-1][0]:.1f},{base:.1f}L{pts[0][0]:.1f},{base:.1f}Z"/>'
        now = f'<path class="line draw" pathLength="1" d="{d}"/>'
    slot = pw / max(days - 1, 1)
    marks = ""
    for i in range(days):
        parts = ([f"{this[i]:,} this month"] if i < len(this) else []) + ([f"{last[i]:,} last month"] if i < len(last) else [])
        ya, yb = (y(this[i]) if i < len(this) else None), (y(last[i]) if i < len(last) else None)
        marks += _mark(f"Day {i + 1}: " + ", ".join(parts), _hit(max(ML, xs[i] - slot / 2), min(ML + pw, xs[i] + slot / 2), MT, base),
                       x=xs[i], y=ya if ya is not None else yb, y2=yb if ya is not None else None)
    summary = f"This month {this[-1] if this else 0:,} so far, last month {last[-1] if last else 0:,} in total."
    inner = (_gradient(gid, MT, base) + _yaxis(w, ph, step, top) + ghost + area + now
             + (f'<circle class="ghostdot" cx="{xs[len(this) - 1]:.1f}" cy="{y(last[len(this) - 1]):.1f}" r="3.5"/>' if this and len(last) >= len(this) else "")   # last month on the same day
             + (_endpoint(*pts[-1]) if pts else "") + _xlabels([str(i + 1) for i in range(days)], xs, h - 6, 5)
             + _HOVER.format(y0=MT, y1=base) + '<circle class="fp fp2" r="4"/>' + marks)
    return _svg(w, h, title, summary, inner)


def smooth_sparkline(points, w=88, h=28):
    """KPI tile trend: monotone path scaled min..max (shape, not volume) and an end dot. Decorative, aria-hidden."""
    if not points:
        return Markup("")
    lo, hi = min(points), max(points)
    n = max(len(points) - 1, 1)
    pad = 3
    pts = [(w * i / n if len(points) > 1 else w / 2,
            h / 2 if hi == lo else h - pad - (h - 2 * pad) * (v - lo) / (hi - lo)) for i, v in enumerate(points)]
    path = f'<path class="line draw" pathLength="1" d="{monotone_path(pts)}"/>' if len(pts) > 1 else ""
    return Markup(f'<svg class="spark sm" viewBox="0 0 {w} {h}" aria-hidden="true" focusable="false">{path}'
                  f'<circle class="spk-dot" cx="{pts[-1][0]:.1f}" cy="{pts[-1][1]:.1f}" r="2.5"/></svg>')


# ---------------------------------------------------------------- bars

def _bar_d(x, y, w, h, r):
    """Bar with a round top (radius r, clamped to half the width and the height) and a square foot."""
    r = max(0.0, min(r, w / 2, h))
    if r < 0.5:
        return f"M{x:.1f},{y + h:.1f}V{y:.1f}H{x + w:.1f}V{y + h:.1f}Z"
    return (f"M{x:.1f},{y + h:.1f}V{y + r:.1f}A{r:.1f},{r:.1f} 0 0 1 {x + r:.1f},{y:.1f}H{x + w - r:.1f}"
            f"A{r:.1f},{r:.1f} 0 0 1 {x + w:.1f},{y + r:.1f}V{y + h:.1f}Z")


def smooth_bar_chart(rows, title, tick=str, w=614, h=220, unit="leads", highlight_last=False, radius=6):
    """Vertical bars [(label, n)] with round tops. Bars rise from under the baseline (clip), so the corners never squash."""
    if not rows:
        return _empty(w, h, title)
    step, top = _axis(max(v for _, v in rows))
    pw, ph, n = w - ML - MR, h - MT - MB, len(rows)
    base, slot = MT + ph, pw / n
    bw = max(min(slot * 0.62, 40.0), 3.0)
    cid, marks, xs = _uid("bc"), "", []
    for i, (label, v) in enumerate(rows):
        cx = ML + slot * (i + 0.5)
        xs.append(cx)
        bh = ph * v / top
        bar = (f'<path class="bar{" cur" if highlight_last and i == n - 1 else ""} {_i(i)}" '
               f'd="{_bar_d(cx - bw / 2, base - bh, bw, bh, radius)}"/>') if v else ""
        marks += _mark(f"{label}: {v:,} {unit}", _hit(cx - slot / 2 + 1, cx + slot / 2 - 1, MT, base) + bar, x=cx, y=base - bh)
    inner = (f'<defs><clipPath id="{cid}"><rect x="0" y="0" width="{w}" height="{base}"/></clipPath></defs>'
             + _yaxis(w, ph, step, top) + f'<g clip-path="url(#{cid})">{marks}</g>'
             + _xlabels([tick(r[0]) for r in rows], xs, h - 6))
    return _svg(w, h, title, _summary(rows, unit), inner)


def smooth_hbar_list(rows, title, w=278, unit="leads", href=None, bar_h=10):
    """Ranked pill bars: label left, value at the bar end. href(label) -> url makes each row a link (country -> its folder)."""
    rh, lw = 30, min(128, int(w * 0.46))
    track = w - lw - 48
    peak, total = max((v for _, v in rows), default=0), sum(v for _, v in rows)
    cid, out = _uid("hc"), ""
    cap = max(int((lw - 8) / 6.0), 4)   # 12px text is about 6px per character
    for i, (label, v) in enumerate(rows):
        y0 = i * rh
        bw = max(track * v / peak, bar_h) if peak and v else 0
        text = label if len(label) <= cap else label[:cap - 1] + "…"
        body = (_hit(0, w, y0 + 1, y0 + rh - 1)
                + f'<text x="{lw - 8}" y="{y0 + rh / 2 + 4:.1f}" text-anchor="end">{escape(text)}</text>'
                + (f'<g clip-path="url(#{cid})"><rect class="bar {_i(i)}" x="{lw}" y="{y0 + (rh - bar_h) / 2:.1f}" width="{bw:.1f}" '
                   f'height="{bar_h}" rx="{bar_h / 2}"/></g>' if v else "")
                + f'<text class="val" x="{lw + bw + 8:.1f}" y="{y0 + rh / 2 + 4:.1f}">{v:,}</text>')
        pct = f" ({v * 100 / total:.0f}%)" if total else ""
        out += _mark(f"{label}: {v:,} {unit}{pct}", body, href=href(label) if href else None)
    H = max(len(rows), 1) * rh
    inner = f'<defs><clipPath id="{cid}"><rect x="{lw}" y="0" width="{w - lw}" height="{H}"/></clipPath></defs>{out}'
    return _svg(w, H + 2, title, _summary(rows, unit), inner)


# ---------------------------------------------------------------- donut

def smooth_donut(rows, title, size=168, unit="leads", top_n=6, center=None, classes=None, stroke=14, gap=5, min_share=0.04):
    """Ring with round segment ends and `gap` px between segments. Slices under `min_share` fold into "Other".
    center=(value, small_text) replaces the default total; classes=['t-a', ...] replaces the .s0-.s8 palette."""
    rows = [(str(k), int(v)) for k, v in rows if v]
    total = sum(v for _, v in rows)
    keep = [r for r in rows[:top_n] if r[1] >= min_share * total]
    rest = total - sum(v for _, v in keep)
    if rest:
        keep.append(("Other", rest))
    rows = keep
    c = size / 2
    r = c - stroke / 2 - 2
    circ = 2 * pi * r
    segs, pos = "", 0.0
    for i, (label, v) in enumerate(rows):
        a = circ * v / total
        cls = classes[i] if classes and i < len(classes) else f"s{i}"
        if len(rows) > 1 and a < gap + stroke + 1:   # shortcut: a sliver shorter than one capsule is not drawn; legend still lists it
            pos += a
            continue
        if len(rows) == 1:
            dash, start, cap = circ, 0.0, "butt"
        else:
            dash = max(a - gap - stroke, 0.01)       # round caps add stroke/2 at both ends, so subtract one stroke width
            start, cap = pos + (a - dash) / 2, "round"
        segs += _mark(f"{label}: {v:,} {unit} ({v * 100 / total:.1f}%)",
                      f'<circle class="seg {cls} {_i(i)}" cx="{c:.1f}" cy="{c:.1f}" r="{r:.1f}" stroke-width="{stroke}" '
                      f'stroke-linecap="{cap}" stroke-dasharray="{dash:.2f} {circ:.2f}" stroke-dashoffset="{-start:.2f}"/>')
        pos += a
    big, small = center if center else (total, unit)
    if isinstance(big, (int, float)):
        dec = 0 if isinstance(big, int) else 1
        attr, big = f' data-count="{big}" data-decimals="{dec}"', f"{big:,.{dec}f}"
    else:
        attr = ""
    inner = (f'<g class="ringg" transform="rotate(-90 {c:.1f} {c:.1f})"><circle class="ring" cx="{c:.1f}" cy="{c:.1f}" r="{r:.1f}" '
             f'stroke-width="{stroke}"/>{segs}</g>'
             f'<text x="{c:.1f}" y="{c - 1:.1f}" text-anchor="middle" class="big"{attr}>{escape(big)}</text>'
             f'<text x="{c:.1f}" y="{c + 17:.1f}" text-anchor="middle">{escape(small)}</text>')
    svg = (f'<svg class="chart sm ringchart" viewBox="0 0 {size} {size}" role="img" '
           f'aria-label="{escape(title)}. {escape(_summary(rows, unit))}"><title>{escape(title)}</title>{inner}</svg>')
    legend = "".join(f'<li class="fade {_i(i)}"><i class="{classes[i] if classes and i < len(classes) else f"s{i}"}"></i>'
                     f'<span>{escape(label)}</span><b>{v:,}</b><small>{v * 100 / total:.0f}%</small></li>'
                     for i, (label, v) in enumerate(rows))
    return Markup(f'<div class="donut-wrap">{svg}<ul class="legend">{legend}</ul></div>')


# ---------------------------------------------------------------- self-test + preview

def _parse(path):
    nums = [float(t) for t in re.findall(r"-?\d+\.?\d*", path)]
    return nums[:2], [nums[2 + 6 * i: 8 + 6 * i] for i in range((len(nums) - 2) // 6)]


def _bez(p0, p1, p2, p3, t):
    u = 1 - t
    return u ** 3 * p0 + 3 * u * u * t * p1 + 3 * u * t * t * p2 + t ** 3 * p3


def _assert_monotone(pts, tol=0.06):
    (x0, y0), segs = _parse(monotone_path(pts))
    for k, (c1x, c1y, c2x, c2y, x1, y1) in enumerate(segs):
        lo, hi = min(pts[k][1], pts[k + 1][1]) - tol, max(pts[k][1], pts[k + 1][1]) + tol
        prev_x = -1e9
        for s in range(21):
            t = s / 20
            x, y = _bez(pts[k][0], c1x, c2x, x1, t), _bez(pts[k][1], c1y, c2y, y1, t)
            assert lo <= y <= hi, f"overshoot in segment {k}: y={y:.3f} outside [{lo:.2f},{hi:.2f}]"
            assert x >= prev_x - 1e-9, "x went backwards"
            prev_x = x
    return len(segs)


def _xml(markup):
    ET.fromstring(str(markup))   # well-formed (escaped titles, closed tags)


def self_test():
    # 1. monotone path: never overshoots, on the shapes that make naive splines ring
    cases = {"spike": [0, 0, 10, 0, 0], "step": [0, 0, 0, 9, 9, 9], "zigzag": [14, 2, 15, 2, 13, 3, 17, 4], "down": [9, 7, 7, 3, 0],
             "flat": [4, 4, 4, 4], "tail": [1, 1, 1, 1, 1, 30], "daily": [14, 15, 13, 2, 5, 15, 11, 16, 9, 8, 5, 2, 8, 15, 11, 8, 8, 2, 2, 9]}
    for name, vals in cases.items():
        pts = [(10 + 20 * i, 100 - 4.0 * v) for i, v in enumerate(vals)]
        _assert_monotone(pts)
        nonuni = [(x ** 1.15, y) for x, y in pts]            # uneven x spacing (real dates with gaps)
        _assert_monotone(nonuni)
    spike = monotone_path([(0, 100), (20, 100), (40, 60), (60, 100), (80, 100)])
    assert "60.0" in spike, "the peak must be a data point, not smoothed away"
    # 2. edge cases
    assert monotone_path([]) == "" and monotone_path([(1, 2)]) == "M1.0,2.0"
    two = monotone_path([(0, 0), (30, 30)])
    assert two == "M0.0,0.0C10.0,10.0 20.0,20.0 30.0,30.0", two      # two points = straight line
    try:
        monotone_path([(0, 1), (0, 2)])
        raise SystemExit("duplicate x must raise")
    except ValueError:
        pass
    # 3. every chart renders well-formed SVG for normal, empty, one-point and all-zero data
    series = [(f"2026-10-{d:02d}", v) for d, v in zip(range(8, 31), cases["daily"] * 2)]
    for rows in (series, [], series[:1], [(d, 0) for d, _ in series]):
        for fn in (lambda r: smooth_area_chart(r, "Per day"), lambda r: smooth_line_chart(r, "Clients"),
                   lambda r: smooth_bar_chart([(a[5:], b) for a, b in r], "Bars", highlight_last=True),
                   lambda r: smooth_hbar_list([(a, b) for a, b in r][:8], "Rank", href=lambda l: "/c/" + l),
                   lambda r: smooth_donut([(a, b) for a, b in r], "Ring"), lambda r: smooth_sparkline([b for _, b in r])):
            out = fn(rows)
            if out:   # the sparkline of nothing is an empty string on purpose
                _xml(out)
    _xml(smooth_compare_chart([8, 16, 27, 33, 46], [10, 20, 31, 40, 52, 60, 71, 80], "Pace"))
    _xml(smooth_compare_chart([], [], "Pace"))
    _xml(smooth_compare_chart([5], [3, 9], "Pace"))
    # 4. marks: one per point, value in the tooltip, crosshair data present
    svg = str(smooth_area_chart(series, "Per day"))
    assert svg.count('class="mark"') == len(series) and "Thu 8 Oct: 14 leads" in svg and 'data-x="' in svg
    assert svg.count("<path class=\"line draw\"") == 1 and "<polyline" not in svg and "pathLength=\"1\"" in svg
    assert 'class="line avg"' in smooth_area_chart(series, "x") and 'class="line avg"' not in smooth_area_chart(series, "x", avg=0)
    # 5. y axis is minimal: at most 4 labels
    assert len(re.findall(r'class="grid', svg)) <= 4
    # 6. bars: round-top path stays valid for tiny, wide and zero heights
    for h in (0.2, 3, 6, 40, 180):
        d = _bar_d(10, 200 - h, 14, h, 6)
        assert "nan" not in d and d.endswith("Z")
    assert _bar_d(10, 100, 14, 0, 6).startswith("M10.0,100.0V100.0H24.0"), "zero height = flat, no arc"
    bars = str(smooth_bar_chart([("a", 5), ("b", 0), ("c", 9)], "B"))
    assert bars.count('class="mark"') == 3 and bars.count('class="bar') == 2 and "clip-path=" in bars
    # 7. donut: capsules never overlap and every gap is at least `gap`; full circle for one slice
    rows = [("A", 232), ("B", 167), ("C", 343)]
    root = ET.fromstring(str(smooth_donut(rows, "Q")).replace("&nbsp;", " "))
    circles = [e for e in root.iter("circle") if "seg" in (e.get("class") or "").split()]
    r = float(circles[0].get("r"))
    circ, stroke, caps = 2 * pi * r, float(circles[0].get("stroke-width")), []
    for e in circles:
        dash = float(e.get("stroke-dasharray").split()[0])
        start = -float(e.get("stroke-dashoffset"))
        caps.append((start - stroke / 2, start + dash + stroke / 2))
    caps.sort()
    for (a0, a1), (b0, b1) in zip(caps, caps[1:] + [(caps[0][0] + circ, 0)]):
        assert b0 - a1 >= 5 - 0.05, f"gap too small: {b0 - a1:.2f}"
    assert abs(sum(b - a for a, b in caps) + 5 * len(caps) - circ) < 0.2, "capsules + gaps must fill the ring"
    assert all(e.get("stroke-linecap") == "round" for e in circles)
    one = str(smooth_donut([("Only", 10)], "x"))
    assert 'stroke-linecap="butt"' in one and one.count('class="seg') == 1
    folded = str(smooth_donut([("big", 500), ("tiny", 3), ("tiny2", 2)], "x"))
    assert "Other" in folded and "tiny" not in folded.replace("tiny2", "").replace("Other", ""), "slivers fold into Other"
    # 8. hbar rows link when href is given, escape labels, and truncate long ones
    hb = str(smooth_hbar_list([("A <b>&", 5), ("x" * 40, 3)], "R", href=lambda l: "/countries/" + l[:1]))
    assert hb.count('<a class="mark"') == 2 and "&lt;b&gt;" in hb and "…" in hb
    assert not re.search(r'clip-path="url\(#hc\d+\)"><(text|rect class="hit")', hb), "clip must wrap only the bar, never the label"
    assert folded.count('class="seg') == 1, "a sliver (Other = 5 of 505) is listed in the legend but not drawn as a dot in the ring"
    print("self-test OK: %d cases, monotone no-overshoot verified by sampling every segment" % (len(cases) * 2))


def preview(path):
    rnd_state = 7
    last, run = [], 0
    for i in range(31):
        rnd_state = (rnd_state * 1103515245 + 12345) % 2 ** 31
        run += 5 + rnd_state % 11
        last.append(run)
    daily = [14, 15, 13, 2, 5, 15, 11, 16, 9, 8, 5, 2, 8, 15, 11, 8, 8, 2, 2, 9, 10, 17, 15, 18, 3, 4, 9, 10, 10, 13]
    end = date(2026, 11, 5).toordinal()
    rows = [(date.fromordinal(end - len(daily) + 1 + i).isoformat(), v) for i, v in enumerate(daily)]
    months = [("Dec", 120), ("Jan", 180), ("Feb", 150), ("Mar", 210), ("Apr", 260), ("May", 240), ("Jun", 290), ("Jul", 310), ("Aug", 280),
              ("Sep", 330), ("Oct", 297), ("Nov", 46)]
    country = [("United States", 273), ("Australia", 258), ("United Kingdom", 74), ("Unknown", 74), ("Canada", 63)]
    niche = [("Furniture Showrooms", 96), ("Restaurants & Cafes", 96), ("Thumbnail Design", 86), ("Real Estate Agents", 85), ("Video Editing", 84)]
    cards = f"""
<div class="g12">
 <section class="kpis span-12" style="margin:0;grid-template-columns:repeat(4,1fr)">
  <div class="kpi rise i0"><span>Today</span><b data-count="13">13</b><div class="trend">{smooth_sparkline(daily[-14:])}<span class="delta" data-dir="up">+4</span></div></div>
  <div class="kpi rise i1"><span>This week</span><b data-count="42">42</b><small>39 same days last week</small><div class="trend"><span class="delta" data-dir="up">+7.7%</span></div></div>
  <div class="kpi rise i2"><span>This month</span><b data-count="46">46</b><small>43 same days last month</small><div class="trend"><span class="delta" data-dir="up">+7.0%</span></div></div>
  <div class="kpi rise i3"><span>Quality</span><b data-count="6.6" data-decimals="1" data-suffix="/10">6.6/10</b><small>54% score A or B</small></div>
 </section>
 <section class="card span-8 rise i4"><div class="card-head"><div><h2>Leads per day</h2><p class="sub">Line = each day, grey = 7-day average</p></div>
  <div class="seg" role="tablist" data-seg="days"><a role="tab" href="#" data-val="30" aria-selected="true">30 d</a><a role="tab" href="#" data-val="60" aria-selected="false" tabindex="-1">60 d</a></div></div>
  <div class="panel" data-seg-panel="days" data-val="30">{smooth_area_chart(rows, "Leads added per day, last 30 days")}</div>
  <div class="panel" data-seg-panel="days" data-val="60" hidden>{smooth_area_chart(rows, "Leads added per day, last 60 days", avg=7)}</div></section>
 <section class="card span-4 rise i5"><h2>Month pace</h2><p class="sub">This month vs last month, running total</p>
  {smooth_compare_chart([8, 16, 27, 33, 46], last, "This month vs last month, cumulative")}</section>
 <section class="card span-8 rise i6"><h2>Leads per month</h2>{smooth_bar_chart(months, "Leads per month", highlight_last=True)}</section>
 <section class="card span-4 rise i7"><h2>By country</h2>{smooth_hbar_list(country, "Leads by country", href=lambda l: "#" + l)}</section>
 <section class="card span-4 rise i8"><h2>By niche</h2>{smooth_hbar_list(niche, "Leads by niche")}</section>
 <section class="card span-4 rise i9"><h2>Lead quality</h2>{smooth_donut([("A", 232), ("B", 167), ("C", 343)], "Quality tiers", center=(6.6, "of 10"), classes=["t-a", "t-b", "t-c"])}</section>
 <section class="card span-4 rise i10"><h2>Where leads sit</h2>{smooth_donut([("Furniture", 96), ("Restaurants", 96), ("Thumbnails", 86), ("Real estate", 85), ("Video", 84), ("Dentists", 65), ("Tiny", 2)], "By niche")}</section>
 <section class="card span-12 rise i11"><h2>Clients over time</h2>{smooth_line_chart([(f"2026-10-{d:02d}", v) for d, v in zip(range(6, 31), [19, 19, 20, 20, 20, 20, 22, 22, 22, 22, 22, 23, 23, 23, 24, 24, 24, 24, 24, 24, 24, 24, 25, 25, 25])], "Clients over time")}</section>
</div>"""
    html = f"""<!doctype html><html lang="en" data-theme="dark"><head><meta charset="utf-8"><title>Smooth charts preview</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="../../app/dashboard/dash/static/app.css"><link rel="stylesheet" href="charts-smooth.css">
<style>html,body{{height:auto;overflow:auto}}body{{padding:24px 0}}.wrap{{width:992px;max-width:100%;margin:0 auto}}</style>
<script>if(location.hash==="#light")document.documentElement.dataset.theme="light";</script></head>
<body><div class="wrap"><h1>Smooth charts preview</h1><p class="muted">Generated by chart-smoothing.py. Add #light to the address for the light theme.</p>{cards}</div>
<script src="charts-smooth.js"></script></body></html>"""
    Path(path).write_text(html, encoding="utf-8")


if __name__ == "__main__":
    self_test()
    out = Path(__file__).with_name("chart-preview.html")
    preview(out)
    print("wrote", out, file=sys.stdout)
