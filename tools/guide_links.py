#!/usr/bin/env python3
"""Add articles that are not on the app or manager guide page yet (docs/app/index*.md, docs/manager/index*.md).

Every article of docs/app and docs/manager/<category>/ that the guide page does not link to is added to it:
- manager: into the section (category box) whose articles are in the same folder, e.g. a new
  docs/manager/domain-worker-cdn-and-tunneling/X.md goes to the "Domain, Worker, CDN" box;
- app: into the box with the app's articles; the main pages of Hiddify Core (docs/core/index and
  docs/core/cli, the app's engine) go there too. The core's feature pages are reached from those pages.
The new link copies the look of the box's other links, with the article's title (the Persian title on
the Persian page when the article has an .fa.md). It goes after the box's visible links.

usage:  python3 tools/guide_links.py          (make guides)
"""
import glob, os, re, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
# Pages outside the guide's folder that belong on its guide page.
EXTRA = {"app": ["core", "core/cli"], "manager": []}
SKIP = re.compile(r"(^|/)(index|old-index|index-old|index2|changelog)(\.[a-z]{2})?\.md$")
ITEM = re.compile(r'([ \t]*)<div class="flex items-center gap-2">\s*<div>\s*<div class="h-2 w-2 rounded-full[^"]*"></div>\s*</div>\s*'
                  r'<a href="([^"]+)"[^>]*>.*?</a>\s*</div>\n', re.S)


def title_of(path, heading_first=False):
    s = open(path, encoding="utf-8").read()
    h = re.search(r"^#\s+(.+)$", s, re.M)
    if heading_first and h:
        return h.group(1).strip()
    m = re.match(r"---\n(.*?)\n---", s, re.S)
    if m:
        t = re.search(r"^title:\s*(.+)$", m.group(1), re.M)
        if t:
            return t.group(1).strip().strip("'\"")
    h = re.search(r"^#\s+(.+)$", s, re.M)
    return h.group(1).strip() if h else os.path.basename(path)[:-3]


def norm(href):
    """/fa/manager/a/b/ -> manager/a/b"""
    return urllib.parse.unquote(re.sub(r"^/(fa/)?", "", href.split("#")[0]).strip("/"))


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


def sections(page):
    """[(start, end, items)] for each box: items are (match) of its article links (not its videos)."""
    starts = [m.start() for m in re.finditer(r'id="section-\d+"', page)] or [0]
    out = []
    for i, st in enumerate(starts):
        end = starts[i + 1] if i + 1 < len(starts) else len(page)
        items = [m for m in ITEM.finditer(page, st, end)]
        out.append((st, end, items))
    return out


def folder(path):
    parts = path.split("/")
    if parts[0] == "core":
        return "app"
    return "/".join(parts[:2]) if parts[0] == "manager" else parts[0]


def update(kind, lang):
    page_path = os.path.join(DOCS, kind, "index.fa.md" if lang == "fa" else "index.md")
    page = open(page_path, encoding="utf-8").read()
    linked = {norm(h) for h in re.findall(r'href="(/(?:fa/)?(?:' + "|".join([kind] + EXTRA[kind]) + r')/[^"]*)"', page)}
    new = [a for a in articles(kind) if a not in linked]
    added = []
    for art in new:
        secs = sections(page)
        best, score = None, 0
        for st, end, items in secs:
            n = sum(1 for m in items if folder(norm(m.group(2))) == folder(art))
            if n > score:
                best, score = (st, end, items), n
        if not best:
            print(f"{kind}/{lang}: no box for {art}, skipped")
            continue
        st, end, items = best
        last = [m for m in items if folder(norm(m.group(2))) == folder(art)][-1]
        hidden = page.find('md:hidden', st, end)
        # after the last visible link of the box (the md:hidden block is the "show more" part)
        anchor = [m for m in items if hidden < 0 or m.start() < hidden]
        at = (anchor[-1] if anchor else last).end()
        base = art + "/index" if os.path.isdir(os.path.join(DOCS, art)) else art
        src = os.path.join(DOCS, base + (".fa.md" if lang == "fa" and os.path.exists(os.path.join(DOCS, base + ".fa.md")) else ".md"))
        href = ("/fa/" if lang == "fa" else "/") + urllib.parse.quote(art, safe="/'") + "/"
        tmpl = (anchor[-1] if anchor else last).group(0)
        tmpl = re.sub(r'<a href="[^"]+"[^>]*>.*?</a>',
                      f'<a href="{href}" target="_blank" class="text-secondaryText text-sm">{title_of(src, art in EXTRA[kind])}</a>', tmpl, flags=re.S)
        page = page[:at] + tmpl + page[at:]
        added.append(art)
    if added:
        open(page_path, "w", encoding="utf-8").write(page)
    print(f"{kind}/{os.path.basename(page_path)}: {len(added)} new article{'s' if len(added) != 1 else ''}"
          + "".join(f"\n  + {a}" for a in added))
    return added


def main():
    for kind in ("app", "manager"):
        for lang in ("en", "fa"):
            update(kind, lang)


if __name__ == "__main__":
    main()
