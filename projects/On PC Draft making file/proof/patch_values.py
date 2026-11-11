import re


def append(text, section, key, lines):
    start = text.index(section)
    m = re.compile(rf"^{key} = \[\n", re.M).search(text, start)
    end = text.index("\n]", m.end())
    return text[:end + 1] + "".join(f' "{ln}",\n' for ln in lines) + text[end + 1:]


p = "config/templates.toml"
t = open(p, encoding="utf-8").read()
t = append(t, "[niches.youtube]", "values", [
    "Strong channels share one habit, every cut serves the story, and the rest follows.",
    "Edits built for retention keep the viewer curious from the first second to the last.",
    "I treat every video as a small film, with a hook, a middle that earns attention and an ending worth finishing.",
])
t = append(t, "[niches.restaurant]", "values", [
    "Strong restaurant brands share one habit, every post and page looks and sounds like the dining room.",
    "Guests return to restaurants that feel consistent, online and at the table, and that consistency is designed on purpose.",
    "I treat every restaurant as a story with a place, a plate and a person behind it.",
])
open(p, "w", encoding="utf-8").write(t)
print("ok")
