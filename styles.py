"""Message angles. The bot rotates them (least-used first) so no two messages read the same."""
import random
from collections import Counter

# name: (instruction for the writer, needs real case studies?)
STYLES = {
    "pain_mirror": ("Mirror one frustration people in THEIR niche commonly have (for example: posting steadily but "
                    "reach or enquiries stay flat). Show you understand it, then say the free sample shows the fix.", False),
    "content_advice": ("Act like a helpful peer: give ONE concrete micro-tip about the kind of content on their "
                       "profile (hook, pacing, caption, format). Then mention the free sample as a demo of it.", False),
    "money_on_table": ("Point out, in general terms, that profiles like theirs lose enquiries or sales when "
                       "content/ads/follow-up is weak. No numbers, no invented claims. Then the free sample.", False),
    "fear_of_loss": ("Gently note that others in their niche are already using stronger video/ads/SEO, and "
                     "attention goes to them. Keep it honest and general, never threatening. Then the free sample.", False),
    "curiosity_gap": ("Make one specific observation about their profile that you could improve, but do not say how. "
                      "Ask a question that makes them curious. Mention the free sample.", False),
    "compliment_gap": ("Give one genuine, specific compliment, name one small gap you noticed, and offer the "
                       "free sample to show the improvement.", False),
    "direct_value": ("Lead with the free sample: you would like to make a free 30-60 second sample for them, "
                     "no strings. One line on why it suits their niche.", False),
    "case_study": ("Use exactly ONE real result from CASE_STUDIES (type of client + result), then link it to "
                   "their situation and offer the free sample. Use only facts and numbers from CASE_STUDIES.", True),
    "success_story": ("Tell a one-line success story using ONLY a real case from CASE_STUDIES, in a human tone, "
                      "then offer the free sample.", True),
}


def pick(recent_styles, have_cases: bool) -> str:
    pool = [k for k, (_, needs) in STYLES.items() if have_cases or not needs]
    counts = Counter(s for s in recent_styles if s in pool)
    low = min(counts.get(k, 0) for k in pool)
    return random.choice([k for k in pool if counts.get(k, 0) == low])
