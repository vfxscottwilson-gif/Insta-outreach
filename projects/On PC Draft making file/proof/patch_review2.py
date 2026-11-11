"""Fixes from the independent review (one-off patch, kept for the record). Run from the project folder."""
import re


def edit(path, pairs):
    s = open(path, encoding="utf-8").read()
    for o, n in pairs:
        assert o in s, (path, o[:70])
        s = s.replace(o, n, 1)
    open(path, "w", encoding="utf-8").write(s)


def append(text, section, key, lines):
    start = text.index(section)
    m = re.compile(rf"^{key} = \[\n", re.M).search(text, start)
    end = text.index("\n]", m.end())
    return text[:end + 1] + "".join(f' "{ln}",\n' for ln in lines) + text[end + 1:]


T = "config/templates.toml"
edit(T, [
    # wording: soft, never passive-aggressive or assuming
    ("A quiet inbox tells me the moment is not right, and I respect that completely, so no response is expected. Whenever growth for {biz_or} comes into focus, my help is still available.",
     "Timing is everything, and it may simply not be the right moment. Whenever growth for {biz_or} comes into focus, a short note is welcome at any time."),
    ("I will take the quiet as a not now rather than a no, and that makes sense for a busy {noun}, so nothing further is needed from you. If reaching more people ever moves up the list, my inbox is open.",
     "Timing is often the only thing standing between an idea and a yes, and that is easy to respect. If the goal of reaching more people comes into focus later, my inbox is open."),
    ("I know how full a calendar gets for a busy {noun}, so I am happy to leave the door open.",
     "I know how full a calendar can get, so I am happy to leave the conversation open."),
    ("The door stays open for {biz_or} whenever the moment is right.", "A short note from {biz_or} is welcome whenever the moment is right."),
    ("Would you like to go ahead?", "Would a quick start suit you?"),
    ("Shall I go ahead?", "Would a quick start suit you?"),
    ("What result would make the next quarter feel like a win? {sample}\\n\\nWhat would that be?",
     "What result would make the next quarter feel like a win? {sample}\\n\\nI would be glad to hear your thoughts."),
    ("A direct answer helps shape a sample that is relevant from the first second. {sample}\\n\\nWhat would it be?",
     "A direct answer helps shape a sample that is relevant from the first second. {sample}\\n\\nDoes one thing stand out?"),
    ("which online efforts bring guests in and which only look busy.", "which online efforts bring guests in and which only collect likes."),
    ("which online efforts bring customers in and which only look busy.", "which online efforts bring customers in and which only collect likes."),
    ("Keeping a channel like {biz} publishing on schedule while the audience keeps growing takes a coordinated team.",
     "Keeping a channel like {biz} publishing on a schedule is a craft of its own."),
    ("Production is rarely the only task on a channel's plate, and that holds for {biz} as well.",
     "Behind every upload on {biz} sit planning, filming and editing, and each one takes real time."),
    ("On YouTube, the first minute of a video does more for reach than almost anything else.",
     "On YouTube, the first minute of a video carries a great deal of weight."),
    ("Channels I have edited for have grown on one principle, build every video to be finished.",
     "Channels I have edited for have grown on one principle, which is to build every video to be finished."),
    ("Strong channels share one habit, every cut serves the story, and the rest follows.",
     "Strong channels share one habit, which is that every cut serves the story."),
    ("Strong restaurant brands share one habit, every post and page looks and sounds like the dining room.",
     "Strong restaurant brands share one habit, which is that every post and page looks and sounds like the dining room."),
    ("always with the same goal, a video worth finishing.", "always with the same goal of a video worth finishing."),
    ("Keeping listings visible while clients keep calling takes a coordinated team.", "Keeping listings visible while clients keep calling is a job of its own."),
    ("Keeping new arrivals visible online while the floor stays busy takes real coordination.", "Keeping new arrivals visible online while the floor stays busy is a job of its own."),
    ("Keeping {biz} visible online while the kitchen and floor stay busy takes real coordination.", "Keeping {biz} visible online while the kitchen and floor stay busy is a job of its own."),
    ("Keeping a business visible online while the day-to-day stays busy takes real coordination.", "Keeping a business visible online while the day-to-day stays busy is a job of its own."),
    # option sets that were not true for every business
    (' ["Reaching visitors and tourists.", "Growing delivery and takeout.", "Growing the loyalty base."],',
     ' ["Growing word of mouth.", "Growing guest loyalty.", "Building local awareness."],'),
    (' ["More enquiries before the visit.", "Growing the local brand.", "Highlighting new arrivals."],',
     ' ["More enquiries before the visit.", "Growing the local brand.", "Growing customer referrals."],'),
])
t = open(T, encoding="utf-8").read()
t = append(t, "[niches.youtube]", "options", [])  if False else t
# extra option sets (arrays of arrays: insert before the closing of each options block)


def add_sets(text, section, sets):
    start = text.index(section)
    m = re.compile(r"^options = \[\n", re.M).search(text, start)
    end = text.index("\n]", m.end())
    add = "".join(" [" + ", ".join(f'"{o}"' for o in s) + "],\n" for s in sets)
    return text[:end + 1] + add + text[end + 1:]


t = add_sets(t, "[niches.youtube]", [["Growing the subscriber base.", "Reaching viewers beyond the current audience.", "Building the creator brand."],
                                      ["Growing community engagement.", "Winning more recommendations.", "Planning the next season of content."]])
t = add_sets(t, "[niches.restaurant]", [["Growing reservations.", "Growing group bookings.", "Reaching new neighbourhoods."],
                                        ["Growing brand recognition.", "Growing the social following.", "Growing the dinner crowd."]])
# more subject patterns
t = append(t, "subjects_named = [", "subjects_named", []) if False else t
for key, extra in {
    "subjects_named": ["{name}, thinking about {biz}", "{name}, a quick idea for {biz}", "{name}, how {biz} could reach further", "{name}, growth ideas for {biz}"],
    "subjects_biz": ["Ideas for {biz}", "Reaching further with {biz}", "Growth ideas for {biz}", "Thinking about {biz}"],
    "subjects_plain": ["Ideas for your {noun}", "Reaching further with your {noun}", "Growth ideas for your {noun}", "Thinking about your {noun}"],
}.items():
    t = append(t, "[common]", key, extra)
t = append(t, "[common]", "subjects_named_noun", []) if False else t
t = t.replace("subjects_plain = [", 'subjects_named_noun = [\n "{name}, a thought on your {noun}",\n "{name}, an idea for your {noun}",\n "{name}, where your {noun} could grow next",\n "{name}, thinking about your {noun}",\n "{name}, a quick idea for your {noun}",\n "{name}, growth ideas for your {noun}",\n]\nsubjects_plain = [', 1)
open(T, "w", encoding="utf-8").write(t)

C = "app/draft/compose.py"
edit(C, [
    # subject: question patterns only on options emails; never repeat the name twice
    ("    def subject(self, lead, ctx, idx, rnd):\n        s, C = self.s[\"subject\"], self.C\n        pools = []\n        if lead.first and ctx[\"biz\"]:\n            pools.append((\"sub.named\", C[\"subjects_named\"]))",
     "    def subject(self, lead, ctx, idx, rnd, kind=\"normal\"):\n        s, C = self.s[\"subject\"], self.C\n        pools = []\n        dup = bool(lead.first and ctx[\"biz\"] and ctx[\"biz\"].lower().split()[0] == lead.first.lower())\n        if lead.first and ctx[\"biz\"] and not dup:\n            pools.append((\"sub.named\", C[\"subjects_named\"]))\n        elif lead.first:\n            pools.append((\"sub.named\", C[\"subjects_named_noun\"]))"),
    ("        cand = []\n        for slot, lines in pools:\n            for t in lines:\n                x = fill(t, {**ctx, \"name\": lead.first})",
     "        cand = []\n        for slot, lines in pools:\n            for t in lines:\n                if \"question\" in t and kind != \"options\":\n                    continue\n                x = fill(t, {**ctx, \"name\": lead.first})"),
    ("        subj = self.subject(lead, ctx, idx, rnd)", "        subj = self.subject(lead, ctx, idx, rnd, kind)"),
    # follow-ups: no sentence may repeat the first email or an earlier follow-up
    ("        outs, allv, picks = [], [], []\n", "        outs, allv, picks = [], [], []\n        used = set(self.sentences(body))\n"),
    ("    def followups(self, lead, ctx, N, niche, kind, idx):", "    @staticmethod\n    def sentences(text):\n        out = []\n        for s in re.split(r\"(?<=[.?])\\s+|\\n+\", text):\n            s = s.strip()\n            if len(s.split()) >= 5 and not s.startswith((\"1.\", \"2.\", \"3.\")) and s != \"Just reply with 1, 2, or 3.\":\n                out.append(s)\n        return out\n\n    def followups(self, lead, ctx, N, niche, kind, idx, body=\"\"):"),
    ("                if best is None or len(v) < len(best[0]):\n                    best = (v, full, [x for x in local if x])",
     "                if any(s in used for s in self.sentences(full)):\n                    v = v + [\"repeats an earlier sentence\"]\n                if best is None or len(v) < len(best[0]):\n                    best = (v, full, [x for x in local if x])"),
    ("            outs.append(full)\n", "            outs.append(full)\n            used.update(self.sentences(full))\n"),
    ("        fus, fviol, opt_set = self.followups(lead, ctx, N, niche, kind, idx)", "        fus, fviol, opt_set = self.followups(lead, ctx, N, niche, kind, idx, body)"),
])
print("ok")
