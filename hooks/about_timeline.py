"""The About us timeline follows the blog by itself.

At every build the <ol class="hi-ab-tl"> list in docs/about-us.md and .fa.md is rebuilt from the blog posts
(tools/about_page.py, timeline_html): a post that is published (draft: false) appears on the About page
in the same build, with its date, title, description and link. The Markdown files are not changed.
"""
import importlib.util
import os
import re

_MOD = None
_OL = re.compile(r'(<ol class="hi-ab-tl">).*?(</ol>)', re.S)


def _about():
    global _MOD
    if _MOD is None:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tools', 'about_page.py')
        spec = importlib.util.spec_from_file_location('about_page', path)
        _MOD = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_MOD)
    return _MOD


def on_page_markdown(markdown, page, config, files, **kwargs):
    src = page.file.src_uri
    if src not in ('about-us.md', 'about-us.fa.md') or '<ol class="hi-ab-tl">' not in markdown:
        return markdown
    lang = 'fa' if src.endswith('.fa.md') else 'en'
    items = _about().timeline_html(lang)
    return _OL.sub(lambda m: m.group(1) + items + m.group(2), markdown, count=1)
