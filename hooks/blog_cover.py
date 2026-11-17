"""Blog posts: show the post's cover (front matter `cover:`, made by tools/blog_covers.py) under its title."""
import re


def on_page_content(html, page, **kwargs):
    cover = page.meta.get("cover") if page.meta else None
    if not cover or not page.file.src_uri.startswith("blog/posts/"):
        return html
    img = (f'<figure class="hi-post-cover"><img src="{cover}" alt="" width="1200" height="630" '
           f'fetchpriority="high"></figure>')
    # right after the first heading (the post title)
    return re.sub(r"(</h1>)", r"\1" + img, html, count=1)
