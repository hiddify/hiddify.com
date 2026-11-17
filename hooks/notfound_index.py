"""A small list of every page (address + title) for the "Did you mean" box of the 404 page.

The full search index is about 6 MB, too heavy for a page that only has to suggest a few addresses,
so this writes assets/404-index.json: [[url, title], ...] for both languages (Persian urls start
with "fa/"). overrides/404.html matches the missing address against it in the browser.
"""
import json
import os

_PAGES = {}  # not cleared between builds: mkdocs-static-i18n runs one build per language in the same process


def on_page_context(context, page, config, nav, **kwargs):
    url = page.url or ""
    if url.endswith("404.html") or page.meta.get("draft"):
        return context
    title = page.meta.get("title") or page.title or ""
    if title:
        _PAGES[url] = str(title)
    return context


def on_post_build(config, **kwargs):
    out = os.path.join(config["site_dir"], "assets", "404-index.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(sorted(_PAGES.items()), f, ensure_ascii=False, separators=(",", ":"))
