"""Builds one lead's first email, subject and four follow-ups from approved template pools.

The model never writes free text. Every sentence comes from templates.toml, filled only with
facts present in the sheet. Rotation keeps every line near an equal share of the batch.
"""
import random
import re

from . import checks
from .checks import first_person

PH = re.compile(r"\{(\w+)\}")


def fill(tpl, ctx):
    for k in PH.findall(tpl):
        if not ctx.get(k):
            return None
    return tpl.format(**ctx)


class Composer:
    def __init__(self, settings, templates, counts=None):
        self.s, self.t = settings, templates
        self.seed = settings["run"]["seed"]
        self.counts = dict(counts or {})
        self.C = templates["common"]
        self.signoffs = self.C["signoffs"]
        r = settings["run"]
        self.mix = (r["share_short"], r["share_options"], r["share_normal"])
        self.w = settings["words"]

    # ---------- plan ----------
    def kind_for(self, idx):
        block, pos = divmod(idx, 10)
        seq = ["short"] * 3 + ["options"] * 3 + ["normal"] * 4
        random.Random(f"{self.seed}k{block}").shuffle(seq)
        return seq[pos]

    def uses_i_for(self, idx):
        n = max(1, round(40 * self.s["run"]["share_first_person"]))
        block, pos = divmod(idx, 40)
        flags = [True] * n + [False] * (40 - n)
        random.Random(f"{self.seed}i{block}").shuffle(flags)
        return flags[pos]

    # ---------- picking ----------
    def _count(self, slot, tpl):
        return self.counts.get(f"{slot}|{tpl}", 0)

    def pick(self, slot, lines, ctx, rnd, use_i=True, want_i=False, exclude=(), slack=1):
        c = []
        for t in lines:
            if t in exclude:
                continue
            s = fill(t, ctx)
            if s is not None:
                c.append((t, s, first_person(s.replace(ctx.get("title") or "\0", ""))))
        if not use_i:
            c = [x for x in c if not x[2]] or c
        elif want_i:
            c = [x for x in c if x[2]] or c
        if not c:
            return None
        m = min(self._count(slot, x[0]) for x in c)
        tier = [x for x in c if self._count(slot, x[0]) <= m + slack]
        t, s, _ = rnd.choice(tier)
        return slot, t, s

    def commit(self, picks):
        for slot, t, _ in picks:
            k = f"{slot}|{t}"
            self.counts[k] = self.counts.get(k, 0) + 1

    # ---------- context ----------
    def context(self, lead, niche):
        N = self.t["niches"][niche]
        biz = lead.biz
        ctx = {
            "biz": biz, "city": lead.city, "cuisine": lead.cuisine_phrase, "title": lead.title,
            "noun": N["noun"], "sample_noun": N["sample_noun"], "niche_word": N["niche_word"],
        }
        ctx["biz_or"] = biz or f"your {N['noun']}"
        return ctx, N

    # ---------- first email ----------
    def compose(self, lead, niche, idx):
        kind, use_i = self.kind_for(idx), self.uses_i_for(idx)
        ctx, N = self.context(lead, niche)
        company = lead.company_email
        samples = self.C["samples"] + N.get("sample_extra", [])
        openers = N["openers_company"] if company else N["openers_person"]
        opener_slot = f"{niche}.opener_{'co' if company else 'pe'}"
        lo_hi = tuple(self.w[kind])
        best = None
        for attempt in range(60):
            rnd = random.Random(f"{self.seed}:{idx}:{attempt}")
            picks, paras = [], []

            def P(slot, lines, **kw):
                r = self.pick(slot, lines, ctx, rnd, use_i, slack=1 + attempt // 15, **kw)
                if r:
                    picks.append(r)
                return r

            def add(r):
                if r:
                    paras.append(r[2])

            add(P(opener_slot, openers))
            if kind == "options":
                v = P(f"{niche}.value", N["values"], want_i=use_i)
                add(v)
                add(P("ask", self.C["asks"]))
                sets = N["options"]
                si = min(range(len(sets)), key=lambda i: (self._count("optset", f"{niche}{i}"), rnd.random()))
                picks.append(("optset", f"{niche}{si}", ""))
                paras.append("\n".join(f"{n}. {o}" for n, o in enumerate(sets[si], 1)))
                paras.append(self.C["reply_line"])
                ctx["sample_noun"] = N["sample_noun"]
                add(P("after", self.C["samples_after_options"]))
            else:
                if kind == "normal":
                    if company:
                        a = P(f"{niche}.value", N["values"], want_i=use_i)
                        add(a)
                        b = P(f"{niche}.value2", N["values"], exclude=(a[1],) if a else ())
                        add(b)
                    else:
                        add(P(f"{niche}.insight", N["insights"]))
                        add(P(f"{niche}.value", N["values"], want_i=use_i))
                else:
                    add(P(f"{niche}.value", N["values"], want_i=use_i))
                add(P("sample", samples))
                add(P("cta", self.C["ctas"]))
            sign = rnd.choice([s for s in self.signoffs if self._count("sign", s) <= min(self._count("sign", x) for x in self.signoffs) + 1])
            picks.append(("sign", sign, ""))
            body = "\n\n".join(paras) + "\n\n" + sign
            viol = checks.check_body(body, kind, lo_hi, self.signoffs, mask=[lead.biz, lead.city, lead.title])
            if len(paras) < 4:
                viol.append("too few parts")
            uses_i = first_person("\n\n".join(paras).replace(lead.title, "") if lead.title else "\n\n".join(paras))
            if use_i and not uses_i:
                viol.append("planned first person but none")
            if not use_i and uses_i:
                viol.append("unplanned first person")
            if best is None or len(viol) < len(best[0]):
                best = (viol, body, picks, kind, uses_i)
            if not viol:
                break
        viol, body, picks, kind, uses_i = best
        subj = self.subject(lead, ctx, idx, rnd)
        picks.append(subj[1])
        self.commit([p for p in picks if isinstance(p, tuple)])
        fus, fviol, opt_set = self.followups(lead, ctx, N, niche, kind, idx)
        return dict(subject=subj[0], body=body, fus=fus, kind=kind, uses_i=uses_i,
                    violations=viol + subj[2] + fviol)

    # ---------- subject ----------
    def subject(self, lead, ctx, idx, rnd):
        s, C = self.s["subject"], self.C
        pools = []
        if lead.first and ctx["biz"]:
            pools.append(("sub.named", C["subjects_named"]))
        if ctx["biz"]:
            pools.append(("sub.biz", C["subjects_biz"]))
        pools.append(("sub.plain", C["subjects_plain"]))
        cand = []
        for slot, lines in pools:
            for t in lines:
                x = fill(t, {**ctx, "name": lead.first})
                if x:
                    cand.append((slot, t, x))

        def score(c):
            n = len(c[2])
            base = 0 if s["min_chars"] <= n <= s["target_chars"] else 1 if s["target_chars"] < n <= s["soft_max_chars"] else 2 if n < s["min_chars"] else 3
            named_bonus = 0 if c[0] == "sub.named" else 0.5
            return base + named_bonus
        lo = min(score(c) for c in cand)
        tier = [c for c in cand if score(c) == lo]
        m = min(self._count(c[0], c[1]) for c in tier)
        tier = [c for c in tier if self._count(c[0], c[1]) <= m + 1]
        slot, t, x = rnd.choice(tier)
        viol = []
        if checks.BAD_CHARS.search(x):
            viol.append("subject symbol")
        if len(x) > s["soft_max_chars"]:
            viol.append("subject too long")
        return x, (slot, t, ""), viol

    # ---------- follow-ups ----------
    def followups(self, lead, ctx, N, niche, kind, idx):
        C, w = self.C, tuple(self.w["followup"])
        has_opts = kind == "options"
        plan = ["reminder", "angle", "options", "last"] if has_opts else ["options", "angle", "reminder", "last"]
        outs, allv, picks = [], [], []
        for n, ftype in enumerate(plan):
            best = None
            for attempt in range(40):
                rnd = random.Random(f"{self.seed}:{idx}:fu{n}:{attempt}")
                local = []
                sample_pool = C["samples"] + N.get("sample_extra", [])
                c2 = dict(ctx)
                if ftype in ("reminder", "angle"):
                    s = self.pick("fu.sample", sample_pool, ctx, rnd, True)
                    c2["sample"] = s[2] if s else ""
                    local.append(s)
                    r = self.pick(f"fu.{ftype}", C["fu_reminder" if ftype == "reminder" else "fu_angle"], c2, rnd, True)
                    text = r[2]
                    local.append(r)
                elif ftype == "options":
                    i1 = self.pick("fu.o_intro", C["fu_options_intro"], ctx, rnd, True)
                    q = self.pick("fu.o_q", C["fu_options_question"], ctx, rnd, True)
                    af = self.pick("fu.o_after", C["samples_after_options"], ctx, rnd, True)
                    si = rnd.randrange(len(N["options"]))
                    opts = "\n".join(f"{k}. {o}" for k, o in enumerate(N["options"][si], 1))
                    text = f"{i1[2]}\n\n{q[2]}\n\n{opts}\n\n{C['reply_line']}\n\n{af[2]}"
                    local += [i1, q, af]
                else:
                    r = self.pick("fu.last", C["fu_last"], ctx, rnd, True)
                    text = r[2]
                    local.append(r)
                sign = rnd.choice(self.signoffs)
                full = text + "\n\n" + sign
                v = checks.check_followup(full, self.signoffs, "options" if ftype == "options" else "plain", w,
                                          need_cost=ftype != "last", mask=[lead.biz, lead.city, lead.title])
                if best is None or len(v) < len(best[0]):
                    best = (v, full, [x for x in local if x])
                if not v:
                    break
            v, full, local = best
            self.commit(local)
            outs.append(full)
            allv += [f"follow-up {n + 1}: {x}" for x in v]
        return outs, allv, None
