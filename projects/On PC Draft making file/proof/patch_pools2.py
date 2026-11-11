"""Add name-free openers so a lead with no usable business name still gets a full email (one-off patch)."""
import re


def append(text, section, key, lines):
    start = text.index(section)
    m = re.compile(rf"^{key} = \[\n", re.M).search(text, start)
    assert m, (section, key)
    end = text.index("\n]", m.end())
    add = "".join(f' "{ln}",\n' for ln in lines)
    return text[:end + 1] + add + text[end + 1:]


p = "config/templates.toml"
t = open(p, encoding="utf-8").read()
ADD = {
    "youtube": (["Viewers decide within seconds whether a video deserves their time, and the edit decides what they see in those seconds."],
                ["Channels that publish on a schedule need a production process that scales with the audience.",
                 "Behind every consistent channel, someone is deciding what stays in the video and what goes."]),
    "restaurant": (["Diners pick a restaurant from a handful of photos, a few reviews and one good search result.",
                    "A great meal starts long before the first course, usually on a phone.",
                    "Restaurants earn repeat guests by being easy to find and easy to remember."],
                   ["Running a restaurant means the kitchen, the floor and the online presence all need attention at once.",
                    "Restaurants are chosen in a few seconds on a phone, long before anyone sits down."]),
    "real_estate": (["Buyers and sellers form an opinion of an agent in the first minute online."],
                    ["Brokerages balance listings, clients and marketing all at once."]),
    "showroom": (["Customers often decide which showroom to visit before they leave the house."],
                 ["Showrooms balance sales, stock and marketing all at once."]),
    "ecommerce": (["Shoppers decide in seconds whether a store feels trustworthy.",
                   "Every product page has a few seconds to earn a second look."],
                  ["Stores balance products, ads and customer service all at once."]),
    "saas": (["Buyers decide in the first minute whether a product is worth a demo.",
              "Software wins when a buyer understands the value in the first few seconds."],
             ["Product teams balance roadmap, growth and messaging all at once."]),
    "generic": (["Customers decide in the first few seconds online whether a business feels trustworthy."],
                ["Teams running a business balance service, operations and marketing all at once."]),
}
for niche, (person, company) in ADD.items():
    sec = f"[niches.{niche}]"
    t = append(t, sec, "openers_person", person)
    t = append(t, sec, "openers_company", company)
open(p, "w", encoding="utf-8").write(t)

n = open("app/draft/names.py", encoding="utf-8").read()
o = '    if re.search(r"\\d{3,}", out) or len(out) > 40 or len(out) < 2:'
assert o in n
n = n.replace(o, '    if " " not in out and re.search(r"[A-Za-z]", out) and re.search(r"\\d", out):\n        return ""                                               # handle such as llamarider37\n' + o, 1)
open("app/draft/names.py", "w", encoding="utf-8").write(n)
print("ok")
