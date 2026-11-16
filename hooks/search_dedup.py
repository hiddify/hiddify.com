"""Clean the search index after each build: drop duplicate entries, and list each guide-page video
as a search result of its own.

`mkdocs serve` with --dirtyreload adds every page to the search index again on each rebuild, so
after a few edits every entry is there several times. The duplicates break the highlighting in the
search results (nested <mark> tags shown as text). A normal `mkdocs build` has no duplicates, so
this hook changes nothing there."""
import json, os

from mkdocs.plugins import event_priority


@event_priority(-1000)  # after the i18n plugin, which writes the index again for each language
def on_post_build(config, **kwargs):
    path = os.path.join(config["site_dir"], "search", "search_index.json")
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    seen, docs = set(), []
    for d in data.get("docs", []):
        # a video card on a guide page (<h4 id="video-ID">): make it a result of its own, not one of
        # "N more on this page" under the guide page. guide.js opens ?v=ID at that video.
        loc = d.get("location") or ""
        if "#video-" in loc:
            base, vid = loc.split("#video-", 1)
            d = dict(d, location=f"{base}?v={vid}")
        key = (d.get("location"), d.get("title"), d.get("text"))
        if key not in seen:
            seen.add(key)
            docs.append(d)
    if len(docs) != len(data.get("docs", [])):
        data["docs"] = docs
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
