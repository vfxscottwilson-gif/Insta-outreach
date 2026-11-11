"""Widen small pools so no line exceeds about 15% of its slot (one-off patch, kept for the record)."""
import re


def append(text, section, key, lines):
    start = text.index(section) if section else 0
    m = re.compile(rf"^{key} = \[\n", re.M).search(text, start)
    assert m, (section, key)
    end = text.index("\n]", m.end())
    add = "".join(f' "{ln}",\n' for ln in lines)
    return text[:end + 1] + add + text[end + 1:]


p = "config/templates.toml"
t = open(p, encoding="utf-8").read()

t = append(t, "[common]", "fu_reminder", [
    "Circling back on my earlier email about {biz_or}.\\n\\n{sample}\\n\\nIt costs nothing to find out whether it fits, and a quick yes is all that is needed to begin.",
    "Just checking that my earlier note reached you.\\n\\n{sample}\\n\\nThere is no obligation attached, and you stay in control of what happens next. Would you like to go ahead?",
])
t = append(t, "[common]", "fu_angle", [
    "Perhaps a different starting point helps.\\n\\nSome people prefer to begin with a question rather than a proposal, so here is one for {biz_or}. What result would make the next quarter feel like a win? {sample}\\n\\nWhat would that be?",
    "Thinking about {biz_or} from another side.\\n\\nThe best results usually start from a single clear priority. Share yours, and the sample can be shaped around it. {sample}\\n\\nWhat is the priority right now?",
])
t = append(t, "[common]", "fu_last", [
    "Wrapping up my notes here.\\n\\nIf now is not the moment, I understand completely, and I will not follow up again. Whenever {biz_or} is ready to take the next step, a single line is enough to restart the conversation.\\n\\nAll the best.",
    "This will be my final message on the subject.\\n\\nI know how full a calendar gets for a busy {noun}, so I am happy to leave the door open. If the right moment arrives, just reply and we will pick it up from there.\\n\\nThank you for your time.",
])
t = append(t, "[common]", "fu_options_intro", ["Replying is simple on this one.", "Here is a quick way to answer."])
t = append(t, "[common]", "fu_options_question", [
    "What is {biz_or} aiming for this year?", "Which goal would {biz_or} put first?", "Which of these fits best right now?"])
t = append(t, "[niches.youtube]", "openers_company", [
    "Behind a channel like {biz}, planning, filming and editing all compete for the same hours.",
    "A channel like {biz} lives in a feed where every video competes with thousands of others for the same click.",
    "Keeping the quality of every upload on {biz} consistent is a job in itself.",
])
t = append(t, "[niches.restaurant]", "openers_company", [
    "Running {biz} means the kitchen, the floor and the online presence all need attention at once.",
    "Restaurants like {biz} are chosen in a few seconds on a phone, long before anyone sits down.",
    "Behind a restaurant like {biz}, the online presence is often the last item on a very long list.",
])
open(p, "w", encoding="utf-8").write(t)

n = open("app/draft/names.py", encoding="utf-8").read()
o = '    if not sheet_name and not company and biz and _person_shaped(biz):'
assert o in n
n = n.replace(o, '    if company:\n        return ""                      # shared mailbox: never addressed by a person\'s name\n' + o, 1)
open("app/draft/names.py", "w", encoding="utf-8").write(n)
print("ok")
