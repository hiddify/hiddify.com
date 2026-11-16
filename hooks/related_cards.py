"""Related-article lists as rich cards, at build time (every page).

The list under "Related articles" / «مقاله‌های مرتبط» / "See also" / «همچنین ببینید» (plain, or already
wrapped in <div class="hi-related">) becomes a grid of cards. Each card has
- an icon: the link's own logo if it has one, else a Material icon picked from the target's topic;
- the link text as the title;
- one line about the target article: its `description:` front matter, else its first paragraph.
Nothing in the Markdown files changes, so the lists stay plain Markdown links.
"""
import html
import os
import re
from functools import lru_cache

HEADING = re.compile(
    r'(<h2[^>]*>\s*(?:Related articles|See also|مقاله‌های مرتبط|همچنین ببینید)\b.*?</h2>)(\s*)'
    r'(?:<div class="hi-related">\s*)?(<ul>.*?</ul>)(\s*</div>)?', re.S)
LI = re.compile(r'<li>\s*<a href="([^"]+)"[^>]*>(.*?)</a>(.*?)</li>', re.S)

# topic -> Material icon (first match on the target path wins)
TOPICS = [
    ("docker", "docker"), ("cloud-init", "cloud-cog-outline"), ("ssh", "console-line"),
    ("prerequisites", "clipboard-check-outline"), ("different-versions", "tag-multiple-outline"),
    ("version-8", "history"), ("installation-and-setup/guide", "rocket-launch-outline"),
    ("cloudflare-ip", "radar"), ("gcore", "earth"), ("amazon", "aws"), ("auto_cdn", "ip-network-outline"), ("cdn", "cloud-outline"), ("cloudflare", "cloud-outline"), ("domain", "web"), ("clean", "radar"),
    ("worker", "cloud-braces"), ("relay", "server-network"), ("tunnel", "transit-connection-variant"),
    ("reality", "shield-lock-outline"), ("fake", "drama-masks"), ("tls", "lock-outline"),
    ("subscription", "link-variant"), ("sub-link", "link-variant"), ("backup", "backup-restore"),
    ("warp", "weather-cloudy"), ("telegram", "send-outline"), ("bot", "robot-outline"),
    ("outbound", "export"), ("proxy-editor", "tune-variant"), ("tools", "toolbox-outline"),
    ("health", "heart-pulse"), ("node", "lan"), ("api", "api"), ("contribut", "hand-heart-outline"),
    ("troubleshoot", "lifebuoy"), ("firewall", "wall"), ("dns", "dns-outline"), ("ipv6", "numeric-6-circle-outline"),
    ("update", "update"), ("configure", "cog-outline"), ("settings", "cog-outline"), ("user", "account-outline"),
    ("client-software", "cellphone-link"), ("app", "cellphone"), ("core", "chip"),
]
ARROW = ('<svg class="hi-rc-go" aria-hidden="true" viewBox="0 0 24 24"><path d="M4 11v2h12l-5.5 5.5 '
         '1.42 1.42L19.84 12l-7.92-7.92L10.5 5.5 16 11H4z"/></svg>')

_ICONS = None
_DOCS = "docs"


def _icon_dir():
    global _ICONS
    if _ICONS is None:
        try:
            import material
            _ICONS = os.path.join(os.path.dirname(material.__file__), ".icons", "material")
        except Exception:
            _ICONS = ""
    return _ICONS


@lru_cache(maxsize=None)
def icon(name):
    p = os.path.join(_icon_dir(), name + ".svg")
    if not os.path.exists(p):
        p = os.path.join(_icon_dir(), "file-document-outline.svg")
    try:
        s = open(p, encoding="utf-8").read().strip()
    except OSError:
        return ""
    return re.sub(r"<svg ", '<svg aria-hidden="true" ', s, count=1)


def topic_icon(path):
    full = path.lower().split("#")[0].rstrip("/")
    last = full.rsplit("/", 1)[-1]
    for p in (last, full):          # the article's own name first, its folder only as a fallback
        for key, name in TOPICS:
            if (full.endswith(key) if "/" in key else key in p):
                return icon(name)
    return icon("file-document-outline")


def clean(md):
    md = re.sub(r"<[^>]+>", "", md)
    md = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", md)
    md = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", md)
    md = re.sub(r"[*_`]+", "", md)
    md = re.sub(r"\{[^}]*\}", "", md)
    return re.sub(r"\s+", " ", md).strip()


@lru_cache(maxsize=None)
def summary(src):
    """One short line about a page: front matter description, else its first real paragraph."""
    try:
        s = open(src, encoding="utf-8").read()
    except OSError:
        return ""
    m = re.match(r"---\n(.*?)\n---\n", s, re.S)
    if m:
        d = re.search(r"^description:\s*(.+)$", m.group(1), re.M)
        if d:
            return short(clean(d.group(1).strip().strip("'\"")))
        s = s[m.end():]
    for block in re.split(r"\n\s*\n", s):
        b = block.strip()
        if not b or b[0] in "#<!|>-*0123456789=`[" or b.startswith(("!!!", "???", "{%", "    ")):
            continue
        t = clean(b)
        if len(t) > 25:
            return short(t)
    return ""


def short(t, n=96):
    m = re.match(r"(.+?[.!؟?。:])(\s|$)", t)
    if m and len(m.group(1)) <= n:
        return m.group(1).rstrip(":")
    return t if len(t) <= n else t[:n].rsplit(" ", 1)[0] + "…"


def source(href, lang):
    """docs/ file of a site link like /fa/manager/x/Y/ or ../Y/ (only absolute site links)."""
    if not href.startswith("/") or href.startswith("//"):
        return None
    from urllib.parse import unquote
    p = unquote(href.split("#")[0]).strip("/")
    fa = p.startswith("fa/") or p == "fa"
    if fa:
        p = p[3:] if p.startswith("fa/") else ""
    base = os.path.join(_DOCS, p) if p else os.path.join(_DOCS, "index")
    for cand in ([base + ".fa.md", base + ".md", os.path.join(base, "index.fa.md"), os.path.join(base, "index.md")]
                 if fa else [base + ".md", os.path.join(base, "index.md")]):
        if os.path.exists(cand):
            return cand
    return None


_BLURBS = None


def blurb(href, lang):
    """The line from data/related_blurbs.yml for a site link, if there is one."""
    global _BLURBS
    if _BLURBS is None:
        try:
            import yaml
            f = os.path.join(os.path.dirname(_DOCS), "data", "related_blurbs.yml")
            _BLURBS = yaml.safe_load(open(f, encoding="utf-8")) or {}
        except Exception:
            _BLURBS = {}
    from urllib.parse import unquote
    key = re.sub(r"^fa/?", "", unquote(href.split("#")[0]).strip("/"))
    return (_BLURBS.get(key) or {}).get(lang, "")


def card(i, href, label, lang):
    logo = re.search(r"<(img|svg)\b.*?(?:/>|</svg>|>)", label, re.S)
    title = clean(re.sub(r"<(img|svg)\b.*?(?:/>|</svg>|>)", "", label, flags=re.S))
    src = source(href, lang)
    sub = blurb(href, lang) or (summary(src) if src else "")
    if logo and "hiddify-app-logo" in logo.group(0):
        ic = '<span class="hi-rc-ic c0"><img alt="" src="/assets/logos/hiddify-mark-white.svg"></span>'
    elif logo:
        ic = f'<span class="hi-rc-ic logo">{logo.group(0)}</span>'
    else:
        ic = f'<span class="hi-rc-ic c{i % 4}">{topic_icon(href)}</span>'
    small = f"<small>{html.escape(sub)}</small>" if sub else ""
    return f'<a class="hi-rc" href="{href}">{ic}<span class="hi-rc-tx"><b>{html.escape(title)}</b>{small}</span>{ARROW}</a>'


def on_config(config, **kwargs):
    global _DOCS
    global _BLURBS
    _DOCS = config["docs_dir"]
    _BLURBS = None
    summary.cache_clear()


def on_page_content(html_text, page, **kwargs):
    uri = page.file.src_uri
    if uri.endswith("index.md") and uri.count("/") <= 1:
        return html_text
    lang = "fa" if uri.endswith(".fa.md") else "en"

    def rep(m):
        items = LI.findall(m.group(3))
        if not items:
            return m.group(0)
        cards = "".join(card(i, h, lab, lang) for i, (h, lab, _) in enumerate(items))
        return f'{m.group(1)}{m.group(2)}<div class="hi-rel2">{cards}</div>'

    html_text = HEADING.sub(rep, html_text, count=1)

    def rep_div(m):
        items = LI.findall(m.group(1))
        if not items:
            return m.group(0)
        return '<div class="hi-rel2">' + "".join(card(i, h, lab, lang) for i, (h, lab, _) in enumerate(items)) + "</div>"

    # any other card list written as <div class="hi-related" markdown="1"> (e.g. the providers on the guide)
    return re.sub(r'<div class="hi-related">\s*(<ul>.*?</ul>)\s*</div>', rep_div, html_text, flags=re.S)
