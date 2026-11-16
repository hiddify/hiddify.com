"""Links inside article text, at build time (every page).

- A plain link in the text gets a class for its kind, so CSS can draw a small hint after it:
  `hi-ext` (another site, a little ↗) or `hi-int` (another page of this site, a little page icon).
  Links with a class, links around an image, heading anchors and links in code are left alone.
- A paragraph that is only links (for example "More: [A], [B], [C]" or "See [A].") becomes a row of
  small pill buttons (`.hi-pills`), in the same family as the `.hi-back` pill.
Nothing in the Markdown files changes.
"""
import re

A_PLAIN = re.compile(r'<a href="([^"]+)"(?![^>]*\bclass=)([^>]*)>(?!\s*<(?:img|svg)\b)')
PARA = re.compile(r"<p>((?:(?!</?p>).)*?)</p>", re.S)
LINK = re.compile(r'<a href="([^"]+)"[^>]*>(.*?)</a>', re.S)
# words that may stand around the links in a links-only paragraph
FILLER = re.compile(
    r"(?:More|See also|See|Read more|Next|Also|and|or|بیشتر|ببینید|را ببینید|همچنین|و|یا|بعدی|نیز)\b|[:،,.;؛()\s‌]",
    re.I)
ICON = {"ext": "ext", "int": "int"}


def kind(href):
    if href.startswith(("#", "mailto:", "tel:", "javascript:")):
        return None
    if href.startswith(("http://", "https://", "//")):
        return None if re.match(r"https?://(www\.)?hiddify\.com", href) else "ext"
    return "int"


def pills(m):
    inner = m.group(1)
    links = LINK.findall(inner)
    if not links or len(links) > 8:
        return m.group(0)
    rest = FILLER.sub("", LINK.sub("", inner))
    if rest.strip():
        return m.group(0)
    lead = re.match(r"\s*([^<]*?)\s*<a ", inner)
    label = lead.group(1).strip(" :،") if lead and lead.group(1).strip(" :،") else ""
    out = "".join(
        f'<a class="hi-pill hi-pill-{kind(h) or "int"}" href="{h}">{re.sub(r"<[^>]+>", "", t).strip()}</a>'
        for h, t in links)
    lab = f'<span class="hi-pills-lab">{label}</span>' if label and len(label) < 30 else ""
    return f'<p class="hi-pills">{lab}{out}</p>'


def on_page_content(html, page, **kwargs):
    # the guides only (the homepage and the other site pages keep their own design)
    uri = page.file.src_uri
    if not uri.startswith(("manager/", "app/", "core/")) or uri.split("/")[-1].startswith(("index", "old-index", "index-old")):
        return html
    # only inside the article body; leave <pre>/<code> untouched
    parts = re.split(r"(<pre\b.*?</pre>|<code\b.*?</code>)", html, flags=re.S)
    for i in range(0, len(parts), 2):
        seg = PARA.sub(pills, parts[i])

        def mark(m):
            k = kind(m.group(1))
            if not k:
                return m.group(0)
            return f'<a href="{m.group(1)}" class="hi-{k}"{m.group(2)}>'
        parts[i] = A_PLAIN.sub(mark, seg)
    return "".join(parts)
