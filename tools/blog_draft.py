#!/usr/bin/env python3
"""Draft a blog post when Hiddify app or Hiddify Manager gets a new major version
(used by .github/workflows/blog-release.yml).

    python3 tools/blog_draft.py --check <product> <tag>
        prints "new=true|false": the tag is a stable release whose major version has no post yet
        (data/blog/releases.yml keeps the last major version that has a post, per product)
    python3 tools/blog_draft.py --product <product> --release <release.json>
        writes docs/blog/posts/<Name>.md and <Name>.fa.md as drafts (draft: true, not shown on the
        site) from the GitHub release, and records the major version in data/blog/releases.yml

<product> is "manager" (hiddify/Hiddify-Manager) or "app" (hiddify/hiddify-app).

The draft follows the blog's release-post layout: a short summary box, "What changes for you",
"Should I update?", the download button, and the full release notes folded at the end. A person
then rewrites the summary in plain words, translates the Persian file and sets `draft: false`.
"""
import argparse
import datetime
import json
import os
import re
import sys
from pathlib import Path

import yaml
from packaging.version import Version

SITE = Path(os.environ.get("BLOG_SITE") or Path(__file__).resolve().parent.parent)  # BLOG_SITE: try it in another folder
STATE = SITE / "data" / "blog" / "releases.yml"
POSTS = SITE / "docs" / "blog" / "posts"
FA_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")

PRODUCTS = {
    "manager": {
        "repo": "hiddify/Hiddify-Manager",
        "name": "Hiddify Manager", "fa": "هیدیفای‌منیجر",
        "category": "Manager",
        "file": "Hiddify-Manager-v{major}-is-released",
        "slug": "hiddify-manager-{major}",
        "get": "/manager/installation-and-setup/guide/",
        "get_fa": "/fa/manager/installation-and-setup/guide/",
        "get_label": "Install or update Hiddify Manager", "get_label_fa": "نصب یا به‌روزرسانی هیدیفای‌منیجر",
        "update": "Take a [backup](/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/) first. Then in the panel open **Actions** › **Update**, or run `hiddify upgrade release` on the server.",
        "update_fa": "اول یک [پشتیبان](/fa/manager/configuration-and-advanced-settings/How-to-backup-and-restore-panel-on-Hiddify/) بگیرید. بعد در پنل صفحهٔ **اقدامات** › **به‌روزرسانی** را بزنید، یا روی سرور دستور `hiddify upgrade release` را اجرا کنید.",
    },
    "app": {
        "repo": "hiddify/hiddify-app",
        "name": "Hiddify app", "fa": "اپ هیدیفای",
        "category": "App",
        "file": "Hiddify-app-v{major}-is-released",
        "slug": "hiddify-app-{major}",
        "get": "/app/How-to-install-Hiddify-app/",
        "get_fa": "/fa/app/How-to-install-Hiddify-app/",
        "get_label": "Download the Hiddify app", "get_label_fa": "دانلود اپ هیدیفای",
        "update": "Update from the store you installed it from (Google Play, App Store), or download the new version.",
        "update_fa": "از همان فروشگاهی که نصب کرده‌اید (گوگل‌پلی، اپ‌استور) به‌روزرسانی کنید، یا نسخهٔ تازه را دانلود کنید.",
    },
}


def state():
    return yaml.safe_load(STATE.read_text(encoding="utf-8")) if STATE.exists() else {}


def major(tag):
    v = Version(str(tag).lstrip("v"))
    return None if v.is_prerelease or v.is_devrelease else v.major


def check(product, tag):
    m = major(tag)
    last = (state().get(product) or {}).get("major", 0)
    print(f"new={'true' if m and m > last else 'false'}")
    print(f"major={m or ''}")


def bullets(body, limit=10):
    """The first list items of the release notes, cleaned of links to commits and PR numbers."""
    out = []
    for line in body.splitlines():
        m = re.match(r"\s*[-*•]\s+(.*)", line)
        if not m:
            continue
        t = m.group(1)
        t = re.sub(r"\(?\[?#\d+\]?(\([^)]*\))?\)?", "", t)          # (#123) / [#123](...)
        t = re.sub(r"\bby @\S+( in \S+)?", "", t)
        t = re.sub(r"https?://\S+", "", t)
        t = re.sub(r"\s+", " ", t).strip(" .:")
        if len(t) > 8 and t.lower() not in {x.lower() for x in out}:
            out.append(t)
        if len(out) >= limit:
            break
    return out


def from_commits(lines, limit=12):
    """Commit subjects -> change list (feat/new/add first, then fixes); release and merge commits dropped."""
    feats, fixes, seen = [], [], set()
    for l in lines:
        l = l.strip()
        m = re.match(r"(feat|new|add|fix|perf)(\([^)]*\))?!?:\s*(.+)", l, re.I)
        if not m:
            continue
        t = m.group(3).strip(" .")
        t = t[0].upper() + t[1:]
        if t.lower() in seen:
            continue
        seen.add(t.lower())
        (fixes if m.group(1).lower() == "fix" else feats).append(t)
    return (feats + fixes)[:limit]


def write(product, rel, others=(), commits=()):
    p = PRODUCTS[product]
    tag = rel["tag_name"]
    m = major(tag)
    if not (rel.get("body") or "").strip() or len(others):
        # the stable release often has no notes of its own: use every release (betas too) of this major
        same = [r for r in others if str(r.get("tag_name", "")).lstrip("v").split(".")[0] == str(m)]
        parts = [(rel.get("body") or "").strip()] + [f"### {r['tag_name']}\n\n{(r.get('body') or '').strip()}"
                                                     for r in same if r["tag_name"] != tag and (r.get("body") or "").strip()]
        rel = dict(rel, body="\n\n".join(x for x in parts if x))
    date = datetime.date.fromisoformat(rel["published_at"][:10])
    name = p["file"].format(major=m)
    slug = p["slug"].format(major=m)
    url = rel.get("html_url") or f"https://github.com/{p['repo']}/releases/tag/{tag}"
    body = (rel.get("body") or "").strip()
    items = bullets(body) or from_commits(commits) or ["(no list in the release notes: write the main changes here)"]
    if not body and commits:
        body = "Changes since the previous major version (commit messages):\n\n" + "\n".join(
            "- " + c.strip() for c in commits if c.strip() and not re.match(r"(release|merge)\b", c.strip(), re.I))
    notes = "\n".join("    " + l for l in body.splitlines()) or "    (no release notes)"
    head = lambda desc, extra="", tags="  - Hiddify\n  - Release\n": (
        f"---\ndraft: true\ndate: {date}\nslug: {slug}\nauthors:\n  - hiddify\n"
        f"categories:\n  - {p['category']}\ntags:\n{tags}"
        f"description: {json.dumps(desc, ensure_ascii=False)}\n{extra}---\n\n")
    en = head(f"{p['name']} {m} is out: what changes for you") + f"""# {p['name']} {m} is out

<!-- DRAFT made by tools/blog_draft.py from {url}. Rewrite the summary in plain words, check every
     point against the release, then set draft: false. -->

!!! abstract "In 30 seconds"
    {p['name']} **{tag.lstrip('v')}** was released on {date:%d %B %Y}. (One or two plain sentences: the
    biggest change and who it helps.)

<!-- more -->

## What changes for you

{chr(10).join('- ' + t for t in items)}

## Should I update?

(Yes / who should wait, and anything to do before or after the update.)

{p['update']}

<div class="hi-cta-wrap"><a class="hi-cta" href="{p['get']}">{p['get_label']}</a></div>

??? note "Full release notes (for experts)"
{notes}

    Source: [{p['repo']} {tag}]({url})

## Related articles

- [{p['get_label']}]({p['get']})
"""
    fa_date = f"{date:%Y/%m/%d}".translate(FA_DIGITS)
    fa = head(f"{p['fa']} {m} منتشر شد: چه چیزی برای شما عوض می‌شود".translate(FA_DIGITS), tags="  - هیدیفای\n  - نسخهٔ تازه\n") + f"""# {p['fa']} {str(m).translate(FA_DIGITS)} منتشر شد

<!-- پیش‌نویس، ساخته‌شده با tools/blog_draft.py از {url}. خلاصه را به زبان ساده بنویسید، فهرست را
     ترجمه و با نسخهٔ منتشرشده مقایسه کنید، بعد draft: false بگذارید. -->

!!! abstract "در ۳۰ ثانیه"
    {p['fa']} **{tag.lstrip('v').translate(FA_DIGITS)}** در {fa_date} منتشر شد. (یکی دو جملهٔ ساده: مهم‌ترین تغییر و
    اینکه به چه کسی کمک می‌کند.)

<!-- more -->

## چه چیزی برای شما عوض می‌شود

{chr(10).join('- ' + t + ' <!-- ترجمه شود -->' for t in items)}

## باید به‌روزرسانی کنم؟

(بله / چه کسی صبر کند، و کارهایی که پیش یا پس از به‌روزرسانی لازم است.)

{p['update_fa']}

<div class="hi-cta-wrap"><a class="hi-cta" href="{p['get_fa']}">{p['get_label_fa']}</a></div>

??? note "متن کامل تغییرات (برای کاربران حرفه‌ای)"
{notes}

    منبع: [{p['repo']} {tag}]({url})

## مقاله‌های مرتبط

- [{p['get_label_fa']}]({p['get_fa']})
"""
    for suffix, text in ((".md", en), (".fa.md", fa)):
        f = POSTS / (name + suffix)
        if f.exists():
            print(f"{f.relative_to(SITE)} already exists, left as it is")
        else:
            f.write_text(text, encoding="utf-8")
            print(f"wrote {f.relative_to(SITE)}")
    st = state()
    st[product] = {"major": m, "tag": tag, "post": name, "date": str(date)}
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text("# Last major version with a blog post, per product; written by tools/blog_draft.py.\n"
                     + yaml.safe_dump(st, sort_keys=True, allow_unicode=True), encoding="utf-8")
    for t in items:
        print(f"- {t}")


# ---- anniversaries --------------------------------------------------------------------------------
# Hiddify was born on 1 Mehr 1401 (23 September 2022). Every year after 23 September, --check-anniversary
# says whether that year's post is missing, and --anniversary writes it as a draft from the GitHub releases
# of the year (Hiddify Manager, the app, the core) and the blog posts published in it.
BIRTH = datetime.date(2022, 9, 23)
WORD_EN = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}
WORD_FA = {1: "یک", 2: "دو", 3: "سه", 4: "چهار", 5: "پنج", 6: "شش", 7: "هفت", 8: "هشت", 9: "نه", 10: "ده"}
ORD_FA = {1: "اول", 2: "دوم", 3: "سوم", 4: "چهارم", 5: "پنجم", 6: "ششم", 7: "هفتم", 8: "هشتم", 9: "نهم", 10: "دهم"}
JM = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]


def ordinal(n):
    return {1: "1st", 2: "2nd", 3: "3rd"}.get(n if n < 20 else n % 10, f"{n}th") if not 10 < n % 100 < 14 else f"{n}th"


def jalali(d):
    gy, gm, gd = d.year, d.month, d.day
    g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    gy2 = gy + 1 if gm > 2 else gy
    days = 355666 + 365 * gy + (gy2 + 3) // 4 - (gy2 + 99) // 100 + (gy2 + 399) // 400 + gd + g_d_m[gm - 1]
    jy = -1595 + 33 * (days // 12053); days %= 12053
    jy += 4 * (days // 1461); days %= 1461
    if days > 365:
        jy += (days - 1) // 365; days = (days - 1) % 365
    jm, jd = (1 + days // 31, 1 + days % 31) if days < 186 else (7 + (days - 186) // 30, 1 + (days - 186) % 30)
    return jy, jm, jd


def fa_date(d):
    jy, jm, jd = jalali(d)
    return f"{jd} {JM[jm - 1]} {jy}".translate(FA_DIGITS)


def last_anniversary(today=None):
    today = today or datetime.date.today()
    y = today.year if today >= datetime.date(today.year, 9, 23) else today.year - 1
    return y - BIRTH.year, datetime.date(y, 9, 23)


def check_anniversary(today=None):
    n, day = last_anniversary(today)
    name = f"{ordinal(n)}-anniversary"
    print(f"new={'true' if n >= 1 and not (POSTS / (name + '.md')).exists() else 'false'}")
    print(f"years={n}")
    print(f"name={name}")


def stable(path, start, end):
    """Stable releases of a GitHub releases JSON list, published in [start, end), oldest first."""
    if not path or not Path(path).exists():
        return []
    out = []
    for r in json.loads(Path(path).read_text(encoding="utf-8")):
        if r.get("draft") or r.get("prerelease") or not r.get("published_at"):
            continue
        d = datetime.date.fromisoformat(r["published_at"][:10])
        if start <= d < end and major(r["tag_name"]) is not None:
            out.append((d, r["tag_name"].lstrip("v")))
    return sorted(out)


def year_posts(start, end, lang):
    out = []
    for f in sorted(POSTS.glob("*.fa.md" if lang == "fa" else "*.md")):
        if lang == "en" and f.name.endswith(".fa.md"):
            continue
        s = f.read_text(encoding="utf-8")
        if re.search(r"^draft:\s*true", s, re.M):
            continue
        m = re.search(r"^date:\s*(\S+)", s, re.M)
        t = re.search(r"^#\s+(.+)$", s, re.M)
        if not m or not t:
            continue
        d = datetime.date.fromisoformat(m.group(1)[:10])
        if start < d < end and "anniversary" not in f.name:
            out.append((d, t.group(1).strip(), f.name.replace(".fa.md", ".md")))   # links name the .md file in both languages
    return sorted(out)


def write_anniversary(manager_json, app_json, core_json, today=None):
    n, day = last_anniversary(today)
    if n < 1:
        return
    name = f"{ordinal(n)}-anniversary"
    prev = f"{ordinal(n - 1)}-anniversary" if n > 1 else ""
    start = datetime.date(day.year - 1, 9, 23)
    rel = {k: stable(p, start, day) for k, p in (("manager", manager_json), ("app", app_json), ("core", core_json))}

    def span(k, fa):
        r = rel[k]
        if not r:
            return "(بدون نسخهٔ پایدار)" if fa else "(no stable release)"
        a, b = r[0][1], r[-1][1]
        a = a.translate(FA_DIGITS) if fa else a
        b = b.translate(FA_DIGITS) if fa else b
        cnt = str(len(r)).translate(FA_DIGITS) if fa else str(len(r))
        return (f"{cnt} نسخهٔ پایدار، از {a} تا **{b}**" if fa else f"{cnt} stable releases, from {a} to **{b}**")

    def posts(lang):
        p = year_posts(start, day, lang)
        if not p:
            return "- (TODO)"
        return "\n".join(f"- [{t}]({f}) ({fa_date(d) if lang == 'fa' else f'{d:%B %Y}'})" for d, t, f in p)

    head = lambda desc, tags: (f"---\ndraft: true\ndate: {day}\nslug: hiddify-turns-{WORD_EN.get(n, n)}\nauthors:\n  - hiddify\n"
                               f"categories:\n  - Anniversary\ntags:\n{tags}description: {json.dumps(desc, ensure_ascii=False)}\n---\n\n")
    en = head(f"Hiddify turned {WORD_EN.get(n, n)} on {day:%d %B %Y}: a look back at year {WORD_EN.get(n, n)}.",
              "  - Hiddify\n  - Internet Freedom Solution\n") + f"""# Hiddify turns {WORD_EN.get(n, n)}

<!-- DRAFT made by tools/blog_draft.py --anniversary. Write the "In 30 seconds" box and one short section per
     product in plain words from the lists below, check every number, then set draft: false. -->

!!! abstract "In 30 seconds"
    Hiddify turned {WORD_EN.get(n, n)} on {day:%d %B %Y}. (Two plain sentences: the biggest things of this year.)
    This post looks back at the year{f", from the [last anniversary]({prev}.md) to today" if prev else ""}.

<!-- more -->

## Year {WORD_EN.get(n, n)} in a few numbers

- **Hiddify Manager**: {span("manager", False)}. ([GitHub](https://github.com/hiddify/Hiddify-Manager/releases))
- **Hiddify app**: {span("app", False)}. ([GitHub](https://github.com/hiddify/hiddify-app/releases))
- **Hiddify core**: {span("core", False)}. ([GitHub](https://github.com/hiddify/hiddify-core/releases))

*({start:%d %B %Y} to {day:%d %B %Y}, from the GitHub releases.)*

## This year on the blog

{posts("en")}

## Thank you

Hiddify is made by a small team and many volunteers: people who translate the app, try the test versions, report
problems and answer questions in the groups. Thank you all. The open internet is a right for everyone.

- Star the projects on [GitHub](https://github.com/hiddify) and rate the app in the stores.
- Tell a friend and share our guides.
- If you can, [support us](/donation-and-support/).

<div class="hi-cta-wrap"><a class="hi-cta" href="/app/How-to-install-Hiddify-app/">Download the Hiddify app</a></div>
"""
    fa_n = WORD_FA.get(n, str(n).translate(FA_DIGITS))
    fa = head(f"هیدیفای در {fa_date(day)} {fa_n} ساله شد: مروری بر سال {ORD_FA.get(n, '')}.",
              "  - هیدیفای\n  - راهکار آزادی اینترنت\n") + f"""# هیدیفای {fa_n} ساله شد

<!-- پیش‌نویس، ساخته‌شده با tools/blog_draft.py --anniversary. کادر «در ۳۰ ثانیه» و برای هر محصول یک بخش کوتاه را
     از روی فهرست‌های زیر به زبان ساده بنویسید، عددها را چک کنید، بعد draft: false بگذارید. -->

!!! abstract "در ۳۰ ثانیه"
    هیدیفای در {fa_date(day)} {fa_n} ساله شد. (دو جملهٔ ساده: مهم‌ترین‌های امسال.)
    این پست سال {ORD_FA.get(n, '')} را{f"، از [سالگرد قبل]({prev}.md) تا امروز،" if prev else ""} مرور می‌کند.

<!-- more -->

## سال {ORD_FA.get(n, '')} در چند عدد

- **هیدیفای‌منیجر**: {span("manager", True)}. ([گیت‌هاب](https://github.com/hiddify/Hiddify-Manager/releases))
- **اپ هیدیفای**: {span("app", True)}. ([گیت‌هاب](https://github.com/hiddify/hiddify-app/releases))
- **هستهٔ هیدیفای**: {span("core", True)}. ([گیت‌هاب](https://github.com/hiddify/hiddify-core/releases))

*(از {fa_date(start)} تا {fa_date(day)}، طبق نسخه‌های گیت‌هاب.)*

## امسال در بلاگ

{posts("fa")}

## سپاس

هیدیفای را یک تیم کوچک و داوطلبان زیادی می‌سازند: کسانی که اپ را ترجمه می‌کنند، نسخه‌های آزمایشی را امتحان
می‌کنند، مشکل‌ها را گزارش می‌دهند و در گروه‌ها به پرسش‌ها جواب می‌دهند. از همه‌تان ممنونیم. اینترنت آزاد حق همهٔ مردم است.

- به پروژه‌ها در [گیت‌هاب](https://github.com/hiddify) ستاره بدهید و در فروشگاه‌ها به اپ امتیاز بدهید.
- به یک دوست بگویید و راهنماهای ما را به اشتراک بگذارید.
- اگر می‌توانید، [از ما حمایت کنید](/fa/donation-and-support/).

<div class="hi-cta-wrap"><a class="hi-cta" href="/fa/app/How-to-install-Hiddify-app/">دانلود اپ هیدیفای</a></div>
"""
    for suffix, text in ((".md", en), (".fa.md", fa)):
        f = POSTS / (name + suffix)
        if f.exists():
            print(f"{f.relative_to(SITE)} already exists, left as it is")
        else:
            f.write_text(text, encoding="utf-8")
            print(f"wrote {f.relative_to(SITE)}")
    # the cover: a cake and the big number of years
    ovr = SITE / "data" / "blog" / "covers.yml"
    txt = ovr.read_text(encoding="utf-8") if ovr.exists() else ""
    if not re.search(rf"^{name}:", txt, re.M):
        unit = " year" if n == 1 else " years"
        ovr.write_text(txt.rstrip("\n") + f'\n{name}: {{ver: "{n}", unit_en: "{unit}", unit_fa: " سال", icon: cake}}\n', encoding="utf-8")
    for k in ("manager", "app", "core"):
        print(f"- {k}: {len(rel[k])} stable releases")


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--check", nargs=2, metavar=("PRODUCT", "TAG"))
    a.add_argument("--check-anniversary", action="store_true", help="new=true when this year's anniversary post is missing")
    a.add_argument("--anniversary", nargs=3, metavar=("MANAGER_JSON", "APP_JSON", "CORE_JSON"),
                   help="write this year's anniversary post as a draft from the releases lists (gh api repos/<repo>/releases)")
    a.add_argument("--today", help="pretend today is this date (YYYY-MM-DD), for testing")
    a.add_argument("--product", choices=sorted(PRODUCTS))
    a.add_argument("--release", help="GitHub release JSON (gh api repos/<repo>/releases/latest)")
    a.add_argument("--commits", nargs="*", default=[], help="text files with one commit subject per line (gh api .../compare/<prev>...<tag>)")
    a.add_argument("--all", help="list of releases JSON (gh api repos/<repo>/releases): notes of the betas of the same major are added")
    o = a.parse_args()
    today = datetime.date.fromisoformat(o.today) if o.today else None
    if o.check_anniversary:
        check_anniversary(today)
    elif o.anniversary:
        write_anniversary(*o.anniversary, today=today)
    elif o.check:
        check(*o.check)
    elif o.product and o.release:
        others = json.loads(Path(o.all).read_text(encoding="utf-8")) if o.all else []
        commits = [l for f in o.commits if Path(f).exists() for l in Path(f).read_text(encoding="utf-8").splitlines()]
        write(o.product, json.loads(Path(o.release).read_text(encoding="utf-8")), others, commits)
    else:
        a.error("use --check PRODUCT TAG, or --product and --release")


if __name__ == "__main__":
    sys.exit(main())
