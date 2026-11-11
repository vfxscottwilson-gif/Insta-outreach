"""Updates the guide for version 2 and rebuilds the zip. Run from the project folder."""
import zipfile
from pathlib import Path

root = Path(".").resolve()


def edit(path, pairs):
    s = open(path, encoding="utf-8").read()
    for o, n in pairs:
        if n in s:
            continue
        assert o in s, (path, o[:60])
        s = s.replace(o, n, 1)
    open(path, "w", encoding="utf-8").write(s)


edit("START-HERE.md", [
    ("If your sheet has no Business column, the **Name** column is treated as the business name.",
     "If your sheet has no Business column, the **Name** column is treated as the business name.\n\n"
     "Good to know:\n"
     "- **No name known = `Team`** in the Name column (capital T only), so your script writes \"Hi Team,\".\n"
     "- A column called **Channel** means every row is a YouTube channel, whatever the Niche cell says (in your YouTube sheet that cell is the channel's topic).\n"
     "- The header row may sit below a title row, and a sheet with no Email header still works if one column clearly holds emails. The Report tab shows which columns were used.\n"
     "- Junk addresses from scraping (`logo@2x.png`, `x@sentry.io`, `name@domain.com`) and no-reply addresses are skipped and counted.\n"
     "- Branch mailboxes such as `london@` or `brooklyn@` are never treated as a person's name."),
    ("- Close Excel before re-running with the same output name.",
     "- Close Excel before re-running with the same output name. If you forget, the save goes to a file beside it and you are told.\n"
     "- Only one run per output file at a time. A second one is refused.\n"
     "- The website is read only when the niche is still unknown, so large sheets stay fast.\n"
     "- The model protects itself: after 3 failed calls in a row, or if it flags over 30% of drafts as offensive, it switches off for the rest of the run and the Report tab says so."),
    ("Any line with a banned word or symbol is reported.",
     "Any line with a banned word or symbol is reported, typing mistakes are explained in plain words, and a run refuses to start until the file is clean."),
    ("| \"input or config changed\" | add `--fresh` |",
     "| \"input or config changed\" | add `--fresh` |\n"
     "| \"Another run is already writing\" | wait for the first window to finish, or use another `--out` name |\n"
     "| \"has a typing mistake\" | open `config\\templates.toml` at the line shown: a quote or comma is missing |"),
])

s = open("README.md", encoding="utf-8").read()
if "test_v2.py" not in s:
    lines = [ln for ln in s.split("\n") if "test_all.py" not in ln]
    s = "\n".join(lines).rstrip() + ("\n\n40 tests: `python tests\\test_all.py` (12 behaviour), `python tests\\test_errors.py` (14 failure), "
                                     "`python tests\\test_v2.py` (14 safeguards).\n")
    open("README.md", "w", encoding="utf-8").write(s)

s = open("CLAUDE.md", encoding="utf-8").read()
i = s.index("**Status / next step")
s = s[:i] + ("**Status / next step (2026-11-11):** v2 hardened after a full audit. 40/40 tests pass (tests/test_all.py 12, "
             "test_errors.py 14, test_v2.py 14). Verified on the real YT and restaurant sheets (300 rows each). Ollama is "
             "still not installed, so the model path is untested end to end. Next: user installs Ollama, runs `--check`, "
             "pilots 20 rows, reviews templates. Small niche packs (saas, ecommerce, real estate, showroom, generic) still "
             "exceed the 15% line-share cap.\n")
open("CLAUDE.md", "w", encoding="utf-8").write(s)

keep = ["START-HERE.md", "README.md", ".gitignore"]
for folder, pats in [("app", ["*.py", "requirements.txt"]), ("app/draft", ["*.py"]), ("config", ["*.toml"]),
                     ("install", ["*.cmd"]),
                     ("tests", ["test_all.py", "test_errors.py", "test_v2.py", "make_sample.py", "inspect_out.py"])]:
    for pat in pats:
        keep += [str(p.relative_to(root)) for p in sorted((root / folder).glob(pat))]
for out in (Path.home() / "Downloads" / "Email Draft Generator.zip", root / "Email Draft Generator.zip"):
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in keep:
            z.write(root / f, "Email Draft Generator/" + f.replace("\\", "/"))
        z.writestr("Email Draft Generator/proof/README.txt", "Test outputs are written here.\n")
    print(len(keep), "files ->", out, round(out.stat().st_size / 1024), "KB")
