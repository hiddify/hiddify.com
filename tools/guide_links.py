#!/usr/bin/env python3
"""Add articles that are not on the app or manager guide page yet, then rebuild the pages.

    python3 tools/guide_links.py          (make guides)

The guide pages are built from data/guides/manager.yml and data/guides/app.yml
(tools/guide_page.py). Every article of docs/manager/<category>/ and docs/app that the data file
does not list yet is added to it:
- manager: to the category whose articles are in the same folder, e.g. a new
  docs/manager/domain-worker-cdn-and-tunneling/X.md goes to "Domains, CDN, workers and relays";
- app: to the category with the app's articles; the main pages of Hiddify Core (docs/core/index and
  docs/core/cli) belong to the app page too.
It goes in the category's last group "New" ("تازه‌ها"), created when needed, with the article's own
title; move it to the right group of the data file and give it a shorter title if you like.
"""
import glob, os, re, subprocess, sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
DATA = os.path.join(ROOT, "data", "guides")
# Pages outside the guide's folder that belong on its guide page.
EXTRA = {"app": ["core", "core/cli"], "manager": []}
SKIP = re.compile(r"(^|/)(index|old-index|index-old|index2|changelog)(\.[a-z]{2})?\.md$")
NEW_GROUP = ("تازه‌ها", "New")


def articles(kind):
    out = []
    for f in sorted(glob.glob(os.path.join(DOCS, kind, "**", "*.md"), recursive=True)):
        rel = os.path.relpath(f, DOCS).replace(os.sep, "/")
        if SKIP.search(rel) or re.search(r"\.[a-z]{2}\.md$", rel):
            continue
        if kind == "manager" and rel.count("/") < 2:  # manager articles live in a category folder
            continue
        out.append(rel[:-3])
    return out + EXTRA[kind]


def folder(path):
    parts = path.split("/")
    if parts[0] == "core":
        return "app"
    return "/".join(parts[:2]) if parts[0] == "manager" else parts[0]


def add(text, cat_id, path):
    """The data file's text with path added to the "New" group of category cat_id."""
    m = re.search(rf"(?m)^  - id: {re.escape(cat_id)}\n", text)
    nxt = re.search(r"(?m)^  - id: |^\S", text[m.end():])
    end = m.end() + (nxt.start() if nxt else len(text) - m.end())
    block = text[m.start():end]
    line = f"          - path: {path}\n"
    g = re.search(rf"(?m)^      - fa: {NEW_GROUP[0]}\n        en: {NEW_GROUP[1]}\n        articles:\n((?:          .*\n)*)", block)
    if g:
        block = block[:g.end()] + line + block[g.end():]
    else:
        v = re.search(r"(?m)^    videos:", block)
        at = v.start() if v else len(block)
        block = (block[:at] + f"      - fa: {NEW_GROUP[0]}\n        en: {NEW_GROUP[1]}\n        articles:\n" + line
                 + block[at:])
    return text[:m.start()] + block + text[end:]


def update(kind):
    p = os.path.join(DATA, kind + ".yml")
    text = open(p, encoding="utf-8").read()
    data = yaml.safe_load(text)
    listed = {a["path"] for c in data["categories"] for g in c["groups"] for a in g["articles"]}
    added = []
    for art in articles(kind):
        if art in listed:
            continue
        best, score = None, 0
        for c in data["categories"]:
            n = sum(1 for g in c["groups"] for a in g["articles"] if folder(a["path"]) == folder(art))
            if n > score:
                best, score = c, n
        if not best:
            print(f"{kind}: no category for {art}, skipped")
            continue
        text = add(text, best["id"], art)
        added.append(art)
    if added:
        open(p, "w", encoding="utf-8").write(text)
        yaml.safe_load(text)  # still valid
    print(f"{kind}: {len(added)} new article{'s' if len(added) != 1 else ''}" + "".join(f"\n  + {a}" for a in added), flush=True)
    return added


def main():
    for kind in ("app", "manager"):
        update(kind)
    subprocess.run([sys.executable, os.path.join(ROOT, "tools", "guide_page.py")], check=True)


if __name__ == "__main__":
    main()
