#!/usr/bin/env python3
"""Build the manager and app guide pages from data/guides/*.yml.

    python3 tools/guide_page.py            (make guide-pages)

docs/<page>/index.md and index.fa.md keep their front matter and intro text; everything from the
"guide:start" marker to the "guide:end" marker is written by this script (the "Start here" cards,
the category menu, and for each category its picture, its articles in groups and its videos).
Edit data/guides/<page>.yml, not the generated HTML. An article with no title in the data file
gets the title of the article itself. Articles added in the last NEW_DAYS days (by git history)
get a "new" badge.
"""
import datetime, html, os, re, subprocess, urllib.parse
import yaml
from fa_spelling import fix as fa_spelling

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
DATA = os.path.join(ROOT, "data", "guides")
UPDATE_SHARE, UPDATE_LINES = 0.25, 15
START, END = "<!-- guide:start -->", "<!-- guide:end -->"
OLD_START = '<section class="flex flex-col gap-5 items-center justify-center py-10">'

TEXT = {
    "fa": {"start": "از اینجا شروع کنید", "articles": "مقاله", "videos": "ویدیو", "video_list": "ویدیوها",
           "new": "جدید", "updated": "به‌روز شد", "old": "نسخهٔ پیشین", "upto": "تا نسخهٔ {}", "prev": "قبلی", "next": "بعدی", "jump": "دسته‌ها"},
    "en": {"start": "Start here", "articles": "articles", "videos": "videos", "video_list": "Videos",
           "new": "New", "updated": "Updated", "old": "Earlier version", "upto": "up to v{}", "prev": "Previous", "next": "Next", "jump": "Categories"},
}
FA_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")


def esc(s):
    return html.escape(str(s), quote=True)


def num(n, lang):
    return str(n).translate(FA_DIGITS) if lang == "fa" else str(n)


def icon(name):
    svg = open(os.path.join(DATA, "icons", name + ".svg"), encoding="utf-8").read().strip()
    return svg.replace("<svg ", '<svg aria-hidden="true" ', 1)


def source(path, lang):
    base = os.path.join(DOCS, path)
    if os.path.isdir(base):
        base = os.path.join(base, "index")
    fa = base + ".fa.md"
    return fa if lang == "fa" and os.path.exists(fa) else base + ".md"


def title_of(path, lang):
    s = open(source(path, lang), encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---", s, re.S)
    if m:
        t = re.search(r"^title:\s*(.+)$", m.group(1), re.M)
        if t:
            return t.group(1).strip().strip("'\"")
    h = re.search(r"^#\s+(.+)$", s, re.M)
    return h.group(1).strip() if h else os.path.basename(path)


_dates = {}


def history(f):
    """[(date, lines changed)] of a file, newest first, following renames."""
    out = subprocess.run(["git", "log", "--follow", "--numstat", "--format=@%as", "--", f],
                         cwd=ROOT, capture_output=True, text=True).stdout
    commits = []
    for line in out.splitlines():
        if line.startswith("@"):
            commits.append([line[1:], 0])
        elif line.strip() and commits:
            a, d = line.split("\t")[:2]
            if a != "-":
                commits[-1][1] += int(a) + int(d)
    return commits


def dates(path):
    """(added, updated) dates of an article, 'YYYY-MM-DD' or None.

    added: the first commit of its English or Persian page. updated: the last commit that changed
    at least UPDATE_SHARE of one of its pages (and UPDATE_LINES lines), so renames, link fixes and
    spelling passes over the whole site do not count; or the page's "updated:" front matter.
    """
    if path in _dates:
        return _dates[path]
    added = updated = None
    for lang in ("en", "fa"):
        f = source(path, lang)
        if lang == "fa" and not f.endswith(".fa.md"):
            continue
        rel = os.path.relpath(f, ROOT)
        text = open(f, encoding="utf-8").read()
        h = history(rel)
        if h:
            added = min(added or h[-1][0], h[-1][0])
            size = text.count("\n") + 1
            for d, changed in h[:-1]:
                if changed >= max(UPDATE_LINES, UPDATE_SHARE * size):
                    updated = max(updated or d, d)
                    break
        m = re.search(r"^updated:\s*['\"]?(\d{4}-\d{2}-\d{2})", text.split("\n---", 1)[0], re.M)
        if m:
            updated = max(updated or m.group(1), m.group(1))
    if updated and added and updated <= added:
        updated = None
    _dates[path] = (added, updated)
    return _dates[path]


def href(path, lang):
    return ("/fa/" if lang == "fa" else "/") + urllib.parse.quote(path, safe="/'") + "/"


def article(a, lang):
    """One article link. "upto: 12" marks an article that is only right for versions up to v12 (muted,
    with an "up to v12" tag); "old: true" mutes it without a version. "ver: 14" (the version the article
    was written or checked for) does the same by itself once the product's major version goes past it."""
    title = a.get(lang) or title_of(a["path"], lang)
    attrs, tag = "", ""
    if a.get("ver") and not a.get("upto") and outdated(PRODUCT, a["ver"]):
        a = dict(a, upto=major(a["ver"]))
    if a.get("upto"):
        v = str(a["upto"])
        tag = f'<span class="hg-ver">{TEXT[lang]["upto"].format(num(v, lang))}</span>'
    elif a.get("old"):
        tag = f'<span class="hg-ver">{TEXT[lang]["old"]}</span>'
    if a.get("old") or a.get("upto"):
        cls = "hg-a hg-old"
    else:
        cls = "hg-a"
        added, updated = dates(a["path"])
        if added:
            attrs = f' data-k="{esc(a["path"])}" data-n="{added}"' + (f' data-u="{updated}"' if updated else "")
    return f'<li><a class="{cls}" href="{esc(href(a["path"], lang))}"{attrs}>{esc(title)}</a>{tag}</li>'


VTEXT = {
    "fa": {"kind_word": "ویدیوی یوتیوب. ", "old": "نسخهٔ پیشین", "new": "جدید", "year": "سال {}", "year_in": "در سال {}",
           "manager": "برای نسخهٔ {} منیجر", "app": "برای اپ نسخهٔ {}", "app0": "برای نسخه‌های اولیهٔ اپ (Hiddify Next)", "legacy-app": "اپ قدیمی، دیگر به‌روز نمی‌شود",
           "client": "نسخهٔ قدیمی برنامه", "general": "ضبط‌شده",
           "tip": "این ویدیو برای نسخهٔ قبلی است ({}). ممکن است بخشی یا همهٔ آن با نسخهٔ فعلی فرق داشته باشد.",
           "tip_new": "ویدیوی جدید، برای نسخهٔ فعلی"},
    "en": {"kind_word": "YouTube video. ", "old": "Earlier version", "new": "New", "year": "{}",
           "manager": "For HiddifyManager v{}", "app": "For Hiddify app v{}", "app0": "For early app versions (Hiddify Next)", "legacy-app": "Retired app, no longer updated",
           "client": "Older version of the app", "general": "Recorded",
           "tip": "This video is for an earlier version ({}). Parts of it, or all of it, may differ from the current version.",
           "tip_new": "New video, for the current version"},
}
NEW_VIDEO_DAYS = 120


def jyear(d):
    """Solar Hijri (Persian) year of a Gregorian date."""
    return d.year - 621 if (d.month, d.day) >= (3, 21) else d.year - 622


def vinfo(vid, meta, lang):
    """(css class, badge, line under the title, tooltip) of a video from data/guides/video_meta.yml."""
    m = meta.get(vid)
    if not m:
        return "", "", "", ""
    V, d, kind = VTEXT[lang], m["date"], m["kind"]
    if kind == "current" and m.get("product") and m.get("ver") and outdated(m["product"], m["ver"]):
        kind = m["product"]   # made for an earlier major version: becomes an "Earlier version" video
    year = num(jyear(d), lang) if lang == "fa" else str(d.year)
    if kind == "current":
        if (datetime.date.today() - d).days > NEW_VIDEO_DAYS:
            return "", "", "", ""
        return "hg-v-new", V["new"], "", V["tip_new"]
    if kind == "app" and str(m.get("ver")) == "0":
        what = V["app0"]
    else:
        what = V[kind].format(num(m["ver"], lang)) if kind in ("manager", "app") else V[kind]
    line = f"{what} {V.get('year_in', 'in {}').format(year)}" if kind == "general" else f"{what} · {V['year'].format(year)}"
    return "hg-v-old", V["old"], line, V["tip"].format(line)


def video(vid, titles, lang, meta=None):
    t = titles.get(vid, "")
    cls, badge, line, tip = vinfo(vid, meta or {}, lang)
    # the badge text is drawn by CSS (data-label), so it stays out of the search text
    b = f'<span class="hg-vbadge" data-label="{esc(badge)}"></span>' if badge else ""
    # "YouTube video" for screen readers and for the search, so searching "video" finds the videos
    sub = f'<span class="hg-sr">{VTEXT[lang]["kind_word"]}</span>' + (f'<span class="hg-vmeta">{esc(line)}</span>' if line else "")
    return (f'<a class="hg-v {cls}" href="https://www.youtube.com/watch?v={vid}" target="_blank" rel="noopener" title="{esc(tip or t)}">'
            f'<span class="hg-thumb"><img src="/assets/youtube/{vid}.jpg" alt="" loading="lazy" decoding="async">'
            f'<span class="hg-play"></span>{b}</span><h4 class="hg-vt" id="video-{esc(vid)}">{esc(t)}</h4>{sub}</a>')


def videos(ids, titles, lang, meta=None):
    if not ids:
        return ""
    meta = meta or {}
    # current videos first, then the older ones (newest first); videos without data keep their place
    ids = sorted(ids, key=lambda v: (meta.get(v, {}).get("kind") not in (None, "current"),
                                     -(meta[v]["date"].toordinal()) if v in meta and meta[v].get("kind") != "current" else 0))
    T = TEXT[lang]
    return (f'<div class="hg-videos"><div class="hg-vhead"><h3>{T["video_list"]} '
            f'<span class="hg-count">{num(len(ids), lang)}</span></h3>'
            f'<span class="hg-arrows"><button type="button" class="hg-prev" aria-label="{T["prev"]}">{icon("chevron-left")}</button>'
            f'<button type="button" class="hg-next" aria-label="{T["next"]}">{icon("chevron-right")}</button></span></div>'
            f'<div class="hg-vrow">' + "".join(video(v, titles, lang, meta) for v in ids) + "</div></div>")


def build(data, titles, lang, vmeta=None):
    T = TEXT[lang]
    out = [START, f'<div class="hg" data-l-new="{T["new"]}" data-l-upd="{T["updated"]}">']
    # start here
    out.append(f'<h2 class="hg-h">{T["start"]}</h2><div class="hg-start">')
    for s in data["start"]:
        x = s[lang]
        out.append(f'<a class="hg-card" href="{esc(href(s["path"], lang))}"><span class="hg-ic">{icon(s["icon"])}</span>'
                   f'<span><b>{esc(x["title"])}</b><small>{esc(x["text"])}</small></span></a>')
    out.append("</div>")
    # category menu
    out.append(f'<nav class="hg-nav" aria-label="{T["jump"]}">')
    for c in data["categories"]:
        n = sum(len(g["articles"]) for g in c["groups"])
        out.append(f'<a href="#{c["id"]}" style="--c:{c["color"]}"><img src="{c["image"]}" alt="">'
                   f'<span>{esc(c[lang]["title"])}</span><small>{num(n, lang)}</small></a>')
    out.append("</nav>")
    # categories
    for c in data["categories"]:
        n = sum(len(g["articles"]) for g in c["groups"])
        vids = c.get("videos", {}).get(lang, [])
        meta = f'{num(n, lang)} {T["articles"]}' + (f' · {num(len(vids), lang)} {T["videos"]}' if vids else "")
        out.append(f'<section class="hg-cat" id="{c["id"]}" style="--c:{c["color"]}">'
                   f'<header><img src="{c["image"]}" alt="" loading="lazy"><div>'
                   f'<h2>{esc(c[lang]["title"])}</h2><p>{esc(c[lang]["text"])}</p><span class="hg-meta">{meta}</span></div></header>')
        if c.get("note"):
            nt = c["note"]
            out.append(f'<p class="hg-note">{nt[lang]} <a href="{esc(href(nt["path"], lang))}">{esc(nt["link_" + lang])} ←</a></p>'
                       if lang == "fa" else
                       f'<p class="hg-note">{nt[lang]} <a href="{esc(href(nt["path"], lang))}">{esc(nt["link_" + lang])} →</a></p>')
        out.append('<div class="hg-groups">')
        for g in c["groups"]:
            out.append(f'<div class="hg-g"><h3>{esc(g[lang])}</h3><ul>'
                       + "".join(article(a, lang) for a in g["articles"]) + "</ul></div>")
        out.append("</div>")
        out.append(videos(vids, titles, lang, vmeta))
        out.append("</section>")
    if data.get("legacy"):
        L = data["legacy"]
        out.append(f'<details class="hg-legacy"><summary><b>{esc(L[lang]["title"])}</b>'
                   f'<small>{esc(L[lang]["text"])}</small></summary>{videos(L["videos"], titles, lang, vmeta)}</details>')
    out.append("</div>")
    out.append('<script src="/assets/js/guide.js" defer></script>')
    out.append(END)
    return "\n".join(x for x in out if x)


def check(data):
    """Every article exists, and no article of the section is missing from the page."""
    paths = [a["path"] for c in data["categories"] for g in c["groups"] for a in g["articles"]]
    for p in paths:
        if not os.path.exists(source(p, "en")):
            raise SystemExit(f"{data['page']}: no such article: {p}")
    return paths


VERSIONS = {}   # latest stable releases, from data/guides/versions.yml (tools/versions.py)
PRODUCT = "manager"


def major(v):
    m = re.match(r"\d+", str(v))
    return int(m.group()) if m else 0


def outdated(product, ver):
    """True when ver is an older major version than the product's latest stable release."""
    cur = VERSIONS.get(product)
    return bool(cur) and major(ver) < major(cur)


def instagram(meta):
    """Same "Earlier version" badge on the video tiles of docs/instagram (index.md, index.fa.md)."""
    for lang, name in (("fa", "index.fa.md"), ("en", "index.md")):
        p = os.path.join(DOCS, "instagram", name)
        if not os.path.exists(p):
            continue
        s = open(p, encoding="utf-8").read()

        def tile(m):
            cls, badge = vinfo(m.group(2), meta, lang)[:2]
            extra = f' is-earlier" data-old="{esc(badge)}' if cls == "hg-v-old" else ""
            return f'{m.group(1)}class="post{extra}"'
        new = re.sub(r'(<a href="https://www\.youtube\.com/(?:watch\?v=|shorts/)([A-Za-z0-9_-]{11})" target="_blank" )'
                     r'class="post(?: is-earlier" data-old="[^"]*)?"', tile, s)
        if new != s:
            open(p, "w", encoding="utf-8").write(new)
            print(f"instagram/{name}: badges")


def main():
    global VERSIONS, PRODUCT
    vf = os.path.join(DATA, "versions.yml")
    VERSIONS = (yaml.safe_load(open(vf, encoding="utf-8")) or {}) if os.path.exists(vf) else {}
    titles = yaml.safe_load(open(os.path.join(DATA, "videos.yml"), encoding="utf-8")) or {}
    vm = os.path.join(DATA, "video_meta.yml")
    meta = (yaml.safe_load(open(vm, encoding="utf-8")) or {}) if os.path.exists(vm) else {}
    for page in ("manager", "app"):
        PRODUCT = page
        data = yaml.safe_load(open(os.path.join(DATA, page + ".yml"), encoding="utf-8"))
        check(data)
        for lang in ("en", "fa"):
            p = os.path.join(DOCS, page, "index.fa.md" if lang == "fa" else "index.md")
            s = open(p, encoding="utf-8").read()
            if START in s:
                head, tail = s.split(START, 1)[0], s.split(END, 1)[1]
            else:  # first run on the old hand-written page: drop its cards and their script
                head, tail = s.split(OLD_START, 1)[0], "\n"
            new = head.rstrip("\n") + "\n\n" + fa_spelling(build(data, titles, lang, meta)) + tail
            if new != s:
                open(p, "w", encoding="utf-8").write(new)
            print(f"{page}/{os.path.basename(p)}: built")
    instagram(meta)


if __name__ == "__main__":
    main()
