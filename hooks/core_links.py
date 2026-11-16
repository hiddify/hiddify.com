"""Core guide (docs/core): link lists as cards, at build time.

The feature pages are copied from hiddify-sing-box (scripts/sync_core_docs.py replaces them), so the
cards are made here instead of in the files:
- the list under "See also" / «همچنین ببینید» / "Related articles" / «مقاله‌های مرتبط» -> .hi-related cards
- the list under "Sources and credits" / «منبع‌ها و قدردانی» -> .hi-sources cards (project logo, name, note)
"""
import re

RELATED = r"(?:See also|Related articles|همچنین ببینید|مقاله‌های مرتبط)"
SOURCES = r"(?:Sources and credits|منبع‌ها و قدردانی)"
GH = '<img class="hi-src-logo" src="/assets/logos/github.svg" alt="">'


def _list_after(html, title, fn):
    pat = re.compile(r'(<h2[^>]*>\s*' + title + r'\b.*?</h2>)(.*?)(<ul>.*?</ul>)', re.S)

    def rep(m):
        if "hi-related" in m.group(2) or "hi-sources" in m.group(2):
            return m.group(0)
        return m.group(1) + m.group(2) + fn(m.group(3))
    return pat.sub(rep, html, count=1)


def _source_item(m):
    href, name, note = m.group(1), m.group(2), m.group(3).strip().lstrip(":").strip()
    if "<a " in note:          # a note with its own links: keep it as a plain item
        return m.group(0)
    logo = GH if "github.com" in href else '<span class="hi-src-logo hi-src-web"></span>'
    note_html = f"<small>{note}</small>" if note else ""
    return f'<li><a href="{href}">{logo}<span><b>{name}</b>{note_html}</span></a></li>'


def _sources(ul):
    ul = re.sub(r'<li><a href="([^"]+)">(.*?)</a>(.*?)</li>', _source_item, ul, flags=re.S)
    return f'<div class="hi-sources">{ul}</div>'


def on_page_content(html, page, **kwargs):
    if not page.file.src_uri.startswith("core/"):
        return html
    html = _list_after(html, RELATED, lambda ul: f'<div class="hi-related">{ul}</div>')
    html = _list_after(html, SOURCES, _sources)
    return html
