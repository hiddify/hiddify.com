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


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--check", nargs=2, metavar=("PRODUCT", "TAG"))
    a.add_argument("--product", choices=sorted(PRODUCTS))
    a.add_argument("--release", help="GitHub release JSON (gh api repos/<repo>/releases/latest)")
    a.add_argument("--commits", nargs="*", default=[], help="text files with one commit subject per line (gh api .../compare/<prev>...<tag>)")
    a.add_argument("--all", help="list of releases JSON (gh api repos/<repo>/releases): notes of the betas of the same major are added")
    o = a.parse_args()
    if o.check:
        check(*o.check)
    elif o.product and o.release:
        others = json.loads(Path(o.all).read_text(encoding="utf-8")) if o.all else []
        commits = [l for f in o.commits if Path(f).exists() for l in Path(f).read_text(encoding="utf-8").splitlines()]
        write(o.product, json.loads(Path(o.release).read_text(encoding="utf-8")), others, commits)
    else:
        a.error("use --check PRODUCT TAG, or --product and --release")


if __name__ == "__main__":
    sys.exit(main())
