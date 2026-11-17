#!/usr/bin/env python3
"""Cover images for the blog posts (the card picture on the blog list and the link preview, og:image).

    python3 tools/blog_covers.py [name-filter ...]

For every docs/blog/posts/*.md it writes docs/assets/blog/covers/<file>-<en|fa>.webp (1200x630) and puts
`cover: /assets/blog/covers/...` in the post's front matter. The design is made from the post itself:
its category (colour theme), the version in its slug (big number), its title, its date, and the first
picture in the post (shown in a glass frame). data/blog/covers.yml can override any of these per post.
Needs google-chrome (headless) to draw the HTML.
"""
import datetime, html, json, os, re, subprocess, sys, tempfile
from pathlib import Path

import yaml

SITE = Path(__file__).resolve().parent.parent
POSTS = SITE / "docs" / "blog" / "posts"
OUT = SITE / "docs" / "assets" / "blog" / "covers"
OVR = SITE / "data" / "blog" / "covers.yml"
FA = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
JM = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]

THEMES = {  # category -> (colour 1, colour 2, glow, label en, label fa, icon)
    "Manager": ("#7c6cff", "#455fe9", "#a78bfa", "Hiddify Manager", "هیدیفای‌منیجر", "server"),
    "Panel": ("#7c6cff", "#455fe9", "#a78bfa", "Hiddify Manager", "هیدیفای‌منیجر", "server"),
    "App": ("#22d3ee", "#455fe9", "#38bdf8", "Hiddify app", "اپ هیدیفای", "phone"),
    "Anniversary": ("#fbbf24", "#ec4899", "#f472b6", "Hiddify", "هیدیفای", "cake"),
    "Hello": ("#34d399", "#22d3ee", "#2dd4bf", "Hiddify", "هیدیفای", "spark"),
    "Project": ("#34d399", "#455fe9", "#2dd4bf", "Hiddify", "هیدیفای", "spark"),
}
ICONS = {  # Material Design icon paths (24x24)
    "chip": "M6 4h12v1h3v2h-3v2h3v2h-3v2h3v2h-3v2h3v2h-3v1H6v-1H3v-2h3v-2H3v-2h3v-2H3V9h3V7H3V5h3V4m5 11v3h1v-3h-1m2 0v3h1v-3h-1m2 0v3h1v-3h-1Z",
    "list": "M3 5h6v6H3V5m2 2v2h2V7H5m6 0h10v2H11V7m0 8h10v2H11v-2m-6 5-3.5-3.5 1.41-1.41L5 17.17l4.59-4.58L11 14l-6 6Z",
    "dns": "M19 15v4H5v-4h14m1-2H4a1 1 0 0 0-1 1v6a1 1 0 0 0 1 1h16a1 1 0 0 0 1-1v-6a1 1 0 0 0-1-1M7 18.5A1.5 1.5 0 0 1 5.5 17 1.5 1.5 0 0 1 7 15.5 1.5 1.5 0 0 1 8.5 17 1.5 1.5 0 0 1 7 18.5M19 5v4H5V5h14m1-2H4a1 1 0 0 0-1 1v6a1 1 0 0 0 1 1h16a1 1 0 0 0 1-1V4a1 1 0 0 0-1-1M7 8.5A1.5 1.5 0 0 1 5.5 7 1.5 1.5 0 0 1 7 5.5 1.5 1.5 0 0 1 8.5 7 1.5 1.5 0 0 1 7 8.5Z",
    "puzzle": "M22 13.5c0 1.76-1.3 3.22-3 3.46V20a2 2 0 0 1-2 2h-3.8v-.3a2.7 2.7 0 0 0-2.7-2.7c-1.5 0-2.7 1.21-2.7 2.7v.3H4a2 2 0 0 1-2-2v-3.8h.3C3.79 16.2 5 15 5 13.5c0-1.5-1.21-2.7-2.7-2.7H2V7a2 2 0 0 1 2-2h3.04c.24-1.7 1.7-3 3.46-3s3.22 1.3 3.46 3H17a2 2 0 0 1 2 2v3.04c1.7.24 3 1.7 3 3.46M17 15h1.5a1.5 1.5 0 0 0 1.5-1.5 1.5 1.5 0 0 0-1.5-1.5H17V7h-5V5.5A1.5 1.5 0 0 0 10.5 4 1.5 1.5 0 0 0 9 5.5V7H4v2.12c1.76.68 3 2.38 3 4.38s-1.25 3.7-3 4.38V20h2.12a4.7 4.7 0 0 1 4.38-3c2 0 3.7 1.25 4.38 3H17v-5Z",
    "router": "m20.2 5.9.8-.8C19.6 3.7 17.8 3 16 3c-1.8 0-3.6.7-5 2.1l.8.8C13 4.8 14.5 4.2 16 4.2s3 .6 4.2 1.7m-.9.8c-.9-.9-2.1-1.4-3.3-1.4-1.2 0-2.4.5-3.3 1.4l.8.8c.7-.7 1.6-1 2.5-1 .9 0 1.8.3 2.5 1l.8-.8M19 13h-2V9h-2v4H5a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2M8 18H6v-2h2v2m3.5 0h-2v-2h2v2m3.5 0h-2v-2h2v2Z",
    "console": "M20 19V7H4v12h16m0-16a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h16m-7 14v-2h5v2h-5m-3.42-4L5.57 9H8.4l3.3 3.3c.39.39.39 1.03 0 1.42L8.42 17H5.59l3.99-4Z",
    "web": "M16.36 14c.08-.66.14-1.32.14-2 0-.68-.06-1.34-.14-2h3.38c.16.64.26 1.31.26 2s-.1 1.36-.26 2m-5.15 5.56c.6-1.11 1.06-2.31 1.38-3.56h2.95a8.03 8.03 0 0 1-4.33 3.56M14.34 14H9.66c-.1-.66-.16-1.32-.16-2 0-.68.06-1.35.16-2h4.68c.09.65.16 1.32.16 2 0 .68-.07 1.34-.16 2M12 19.96c-.83-1.2-1.5-2.53-1.91-3.96h3.82c-.41 1.43-1.08 2.76-1.91 3.96M8 8H5.08A7.923 7.923 0 0 1 9.4 4.44C8.8 5.55 8.35 6.75 8 8m-2.92 8H8c.35 1.25.8 2.45 1.4 3.56A8.008 8.008 0 0 1 5.08 16m-.82-2C4.1 13.36 4 12.69 4 12s.1-1.36.26-2h3.38c-.08.66-.14 1.32-.14 2 0 .68.06 1.34.14 2M12 4.03c.83 1.2 1.5 2.54 1.91 3.97h-3.82c.41-1.43 1.08-2.77 1.91-3.97M18.92 8h-2.95a15.65 15.65 0 0 0-1.38-3.56c1.84.63 3.37 1.9 4.33 3.56M12 2C6.47 2 2 6.5 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10A10 10 0 0 0 12 2Z",
    "server": "M4 1h16a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1m0 8h16a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1v-4a1 1 0 0 1 1-1m0 8h16a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1v-4a1 1 0 0 1 1-1M9 5h1V3H9v2m0 8h1v-2H9v2m0 8h1v-2H9v2M5 3v2h2V3H5m0 8v2h2v-2H5m0 8v2h2v-2H5z",
    "phone": "M17 19H7V5h10m0-4H7c-1.11 0-2 .89-2 2v18a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V3c0-1.11-.9-2-2-2z",
    "cake": "M12 6a2 2 0 0 0 2-2c0-.38-.1-.73-.29-1.03L12 0l-1.71 2.97c-.19.3-.29.65-.29 1.03a2 2 0 0 0 2 2m4.6 9.99-1.07-1.07-1.08 1.07c-1.3 1.3-3.58 1.31-4.89 0l-1.07-1.07-1.09 1.07C6.75 16.64 5.88 17 4.96 17c-.73 0-1.4-.23-1.96-.61V21a1 1 0 0 0 1 1h16a1 1 0 0 0 1-1v-4.61c-.56.38-1.23.61-1.96.61-.92 0-1.79-.36-2.44-1.01M18 9h-5V7h-2v2H6a3 3 0 0 0-3 3v1.54c0 1.08.88 1.96 1.96 1.96.52 0 1.02-.2 1.38-.57l2.14-2.13 2.13 2.13c.74.74 2.03.74 2.77 0l2.14-2.13 2.13 2.13c.37.37.86.57 1.38.57 1.08 0 1.96-.88 1.96-1.96V12C21 10.34 19.66 9 18 9z",
    "spark": "M12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21 12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2z",
}


def front(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    return (yaml.safe_load(m.group(1)) or {}, m) if m else ({}, None)


def version(slug, cat):
    m = re.search(r"(?:manager|app|next|panel)-(\d+(?:-\d+)?)$", slug or "")
    if m:
        return m.group(1).replace("-", ".")
    if "four" in (slug or ""):
        return "4"
    if "second" in (slug or ""):
        return "2"
    if "one-year" in (slug or ""):
        return "1"
    return ""


def first_image(text):
    for m in re.finditer(r'<img[^>]*src="([^"]+)"|!\[[^\]]*\]\(([^)\s]+)', text):
        src = m.group(1) or m.group(2)
        if src.startswith("/assets/") and not src.endswith((".svg", ".gif")) and "/logos/" not in src:
            return src
    return None


def jdate(d):
    gy, gm, gd = d.year, d.month, d.day
    g = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    gy2 = gy + 1 if gm > 2 else gy
    days = 355666 + 365 * gy + (gy2 + 3) // 4 - (gy2 + 99) // 100 + (gy2 + 399) // 400 + gd + g[gm - 1]
    jy = -1595 + 33 * (days // 12053); days %= 12053; jy += 4 * (days // 1461); days %= 1461
    if days > 365:
        jy += (days - 1) // 365; days = (days - 1) % 365
    jm = 1 + days // 31 if days < 186 else 7 + (days - 186) // 30
    jd = 1 + (days % 31 if days < 186 else (days - 186) % 30)
    return f"{jd} {JM[jm - 1]} {jy}".translate(FA)


def page(c, lang):
    fa = lang == "fa"
    c1, c2, glow, len_, lfa, icon = THEMES.get(c["cat"], THEMES["Project"])
    icon = c.get("icon", icon)
    label = lfa if fa else len_
    ver = c.get("ver", "")
    vtxt = (c.get("ver_fa") or ver.translate(FA)) if fa else ver
    unit = c.get("unit_fa" if fa else "unit_en", "")
    shot = c.get("shot")
    font = "/assets/webfonts/Vazirmatn-RD[wght].woff2" if fa else "/assets/webfonts/Inter-var.woff2"
    portrait = False
    if shot:
        try:
            from PIL import Image
            w, h = Image.open(SITE / "docs" / shot.lstrip("/")).size
            portrait = h > w * 1.25
        except Exception:
            pass
    pic = (f'<div class="shot{" phone" if portrait else ""}"><img src="{shot}"></div>' if shot else
           f'<div class="glyph"><svg viewBox="0 0 24 24"><path d="{ICONS[icon]}"/></svg></div>')
    return f"""<!doctype html><html dir="{'rtl' if fa else 'ltr'}"><head><meta charset="utf-8"><style>
@font-face{{font-family:F;src:url({font});font-weight:100 900}}
*{{box-sizing:border-box;margin:0}}
html,body{{width:1200px;height:630px;overflow:hidden}}
body{{font-family:F,sans-serif;color:#fff;background:#0b1020;position:relative}}
.bg{{position:absolute;inset:0;background:
 radial-gradient(620px 420px at {'85%' if fa else '15%'} 0%,{c1}55,transparent 70%),
 radial-gradient(700px 500px at {'10%' if fa else '90%'} 110%,{c2}66,transparent 70%),
 radial-gradient(400px 300px at 50% 50%,{glow}22,transparent 70%),
 linear-gradient(135deg,#0b1020,#111836 55%,#0b1020)}}
.grid{{position:absolute;inset:0;background-image:linear-gradient(#ffffff0a 1px,transparent 1px),linear-gradient(90deg,#ffffff0a 1px,transparent 1px);background-size:44px 44px;-webkit-mask-image:radial-gradient(800px 500px at 50% 40%,#000,transparent 80%)}}
.wrap{{position:absolute;inset:0;display:flex;align-items:center;gap:40px;padding:56px 64px}}
.txt{{flex:1.15;display:flex;flex-direction:column;gap:18px;min-width:0}}
.pill{{align-self:flex-start;display:inline-flex;align-items:center;gap:10px;padding:8px 18px;border-radius:999px;background:#ffffff14;border:1px solid #ffffff26;font-size:22px;font-weight:600;letter-spacing:{'0' if fa else '.02em'}}}
.pill i{{width:10px;height:10px;border-radius:50%;background:linear-gradient(135deg,{c1},{c2});box-shadow:0 0 14px {glow}}}
.ver{{font-size:{'150' if len(vtxt) <= 3 else '120'}px;line-height:.95;font-weight:800;letter-spacing:-.02em;background:linear-gradient(120deg,#fff 10%,{c1} 55%,{glow});-webkit-background-clip:text;color:transparent}}
.ver small{{font-size:44px;font-weight:700;margin-inline-start:10px;-webkit-text-fill-color:#ffffffcc}}
h1{{font-size:{'40' if fa else '38'}px;line-height:1.35;font-weight:{'800' if fa else '700'};display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden;text-wrap:balance}}
.date{{font-size:22px;color:#ffffffa8;font-weight:500}}
.side{{flex:.95;height:100%;display:flex;align-items:center;justify-content:center;position:relative}}
.shot{{width:100%;max-height:440px;border-radius:22px;padding:10px;background:#ffffff14;border:1px solid #ffffff30;box-shadow:0 40px 80px -20px #000c,0 0 80px -10px {glow}66;transform:perspective(1200px) rotateY({'8deg' if fa else '-8deg'}) rotateX(3deg);overflow:hidden}}
.shot img{{display:block;width:100%;max-height:420px;object-fit:cover;object-position:top;border-radius:14px}}
.shot.phone{{width:300px;height:540px;max-height:none;border-radius:46px;padding:12px;background:#0d1224;border:2px solid #ffffff3a;transform:perspective(1200px) rotateY({'10deg' if fa else '-10deg'}) rotateZ({'2deg' if fa else '-2deg'})}}
.shot.phone img{{height:100%;max-height:none;border-radius:34px}}
.glyph{{width:300px;height:300px;border-radius:60px;display:flex;align-items:center;justify-content:center;background:linear-gradient(145deg,#ffffff1f,#ffffff08);border:1px solid #ffffff30;box-shadow:0 40px 80px -20px #000c,0 0 120px -10px {glow}88}}
.glyph svg{{width:150px;height:150px;fill:url(#g)}}
.logo{{position:absolute;{'left' if fa else 'right'}:44px;bottom:30px;height:34px;opacity:.9}}
</style></head><body><div class="bg"></div><div class="grid"></div>
<svg width="0" height="0" style="position:absolute"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="{c1}"/></linearGradient></defs></svg>
<div class="wrap"><div class="txt"><span class="pill"><i></i>{html.escape(label)}</span>
{f'<div class="ver">{vtxt}<small>{html.escape(unit)}</small></div>' if vtxt else ''}
<h1>{html.escape(c['title'])}</h1><div class="date">{html.escape(c['date_fa'] if fa else c['date_en'])}</div></div>
<div class="side">{pic}</div></div>
<img class="logo" src="/assets/hiddify-logo-white.svg"></body></html>"""


def set_fm(text, key, value):
    """set `key: value` in the front matter (replace or add before the closing ---)"""
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    body = m.group(1)
    if re.search(rf"^{key}:", body, re.M):
        body = re.sub(rf"^{key}:.*$", f"{key}: {value}", body, count=1, flags=re.M)
    else:
        body += f"\n{key}: {value}"
    return "---\n" + body + "\n---\n" + text[m.end():]


def main(filters):
    OUT.mkdir(parents=True, exist_ok=True)
    ovr = yaml.safe_load(OVR.read_text(encoding="utf-8")) if OVR.exists() else {}
    tmp = SITE / ".cache" / "blog" / "cover-html"
    tmp.mkdir(parents=True, exist_ok=True)
    jobs = []
    for f in sorted(POSTS.glob("*.md")):
        lang = "fa" if f.name.endswith(".fa.md") else "en"
        name = f.name[:-6] if lang == "fa" else f.name[:-3]
        if filters and not any(x in name for x in filters):
            continue
        text = f.read_text(encoding="utf-8")
        meta, m = front(text)
        if not m:
            continue
        d = meta.get("date")
        d = d if isinstance(d, datetime.date) else datetime.date.fromisoformat(str(d).strip())
        cat = (meta.get("categories") or ["Project"])[0]
        title = re.search(r"^# (.+)$", text, re.M).group(1).strip()
        title = re.sub(r"[🎉🎆]\s*", "", title).strip()
        c = dict(cat=cat, title=title, ver=version(meta.get("slug", ""), cat), shot=first_image(text),
                 date_en=f"{d.day} {d:%B %Y}", date_fa=jdate(d))
        if cat in ("Project", "Hello") and not c["ver"]:
            c["ver"] = str(d.year)          # projects show their year as the big number (solar year in Persian)
            c["ver_fa"] = jdate(d).split()[-1]
        if cat == "Anniversary" and c["ver"]:
            c.update(unit_en=" years" if c["ver"] != "1" else " year", unit_fa=" سال")
        o = dict(ovr.get(name, {}))
        o.update(o.pop(lang, {}) or {})
        o.pop("en", None); o.pop("fa", None)
        c.update(o)
        h = tmp / f"{name}-{lang}.html"
        h.write_text(page(c, lang), encoding="utf-8")
        png = tmp / f"{name}-{lang}.png"
        jobs.append((f, lang, name, h, png))
    for f, lang, name, h, png in jobs:
        url = f"file://{h}"
        # file:// cannot load /assets; serve the html as a sibling of the assets through the docs dir instead
        html_doc = h.read_text(encoding="utf-8").replace('src="/assets/', f'src="{(SITE / "docs" / "assets").as_uri()}/').replace("url(/assets/", f"url({(SITE / 'docs' / 'assets').as_uri()}/")
        h.write_text(html_doc, encoding="utf-8")
        subprocess.run(["google-chrome", "--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files",
                        "--window-size=1200,630", "--virtual-time-budget=4000", f"--screenshot={png}", url],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
        out = OUT / f"{name}-{lang}.webp"
        from PIL import Image
        Image.open(png).convert("RGB").save(out, "WEBP", quality=88, method=6)
        rel = "/assets/blog/covers/" + out.name
        text = set_fm(f.read_text(encoding="utf-8"), "cover", rel)
        if lang == "fa":  # the Persian (solar) date shown on the blog list card
            meta, _ = front(text)
            d = meta["date"] if isinstance(meta["date"], datetime.date) else datetime.date.fromisoformat(str(meta["date"]).strip())
            text = set_fm(text, "date_fa", jdate(d))
        f.write_text(text, encoding="utf-8")
        print(out.relative_to(SITE))


if __name__ == "__main__":
    main(sys.argv[1:])
