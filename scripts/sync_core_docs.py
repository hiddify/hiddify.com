#!/usr/bin/env python3
"""Copy hiddify-sing-box's docs/hiddify into docs/core/sing-box, in this site's layout.

    python3 scripts/sync_core_docs.py <path to hiddify-sing-box>

hiddify-sing-box writes each page as name.en.md and name.fa.md; this site takes name.md for
English and name.fa.md for Persian, and links to name.md from both languages. The script renames
the pages, fixes their links, drops the language links (the site has its own language switch) and
the RTL wrapper of the Persian pages, and writes the section titles. docs/core/sing-box is
replaced as a whole, so edit the pages in hiddify-sing-box, not here.
"""

import re
import shutil
import sys
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
TARGET = SITE / "docs" / "core" / "sing-box"
SOURCE_URL = "https://github.com/hiddify/hiddify-sing-box/blob/v5/"

# Section folder: (weight, English title, Persian title)
SECTIONS = {
    "": (-50, "sing-box features", "قابلیت‌های sing-box هیدیفای"),
    "features": (-100, "Features", "قابلیت‌ها"),
    "features/protocols": (-100, "Protocols", "پروتکل‌ها"),
    "features/transports": (-90, "Transports", "ترنسپورت‌ها"),
    "features/dns": (-80, "DNS", "DNS"),
    "features/groups": (-70, "Groups and monitoring", "گروه‌ها و پایش"),
    "bugfix": (10, "Bug fixes", "رفع باگ‌ها"),
}
# Pages outside a section that need a place in the menu.
PAGE_WEIGHTS = {"app_considerations.md": 20}

LANGUAGE_LINK = re.compile(r"^\[(?:فارسی|English)\]\([^)]*\)(?: · )?")
PAGE_LINK = re.compile(r"\.(?:en|fa)\.md(?=[)#])")
SOURCE_LINK = re.compile(r"\]\((?:\.\./)+((?:test|replace|protocol|option|docs)/[^)]*)\)")


def convert(text: str, persian: bool) -> str:
    lines = text.split("\n")
    if persian:
        if lines and lines[0].strip() == '<div dir="rtl">':
            lines = lines[1:]
        while lines and not lines[-1].strip():
            lines.pop()
        if lines and lines[-1].strip() == "</div>":
            lines.pop()
    lines = [LANGUAGE_LINK.sub("", line) for line in lines]
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip("\n") + "\n"
    text = PAGE_LINK.sub(".md", text)
    # links to files of the repository outside docs/hiddify go to GitHub
    return SOURCE_LINK.sub(lambda m: "](" + SOURCE_URL + m.group(1) + ")", text)


def front_matter(**fields) -> str:
    body = "".join(f"{key}: {value}\n" for key, value in fields.items())
    return f"---\n{body}---\n\n"


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    source = Path(sys.argv[1]) / "docs" / "hiddify"
    if not (source / "index.md").is_file():
        sys.exit(f"{source} has no index.md: give the path of a hiddify-sing-box checkout")

    if TARGET.exists():
        shutil.rmtree(TARGET)
    for page in sorted(source.rglob("*.md")):
        relative = page.relative_to(source)
        persian = page.name.endswith(".fa.md")
        name = page.name.removesuffix(".en.md").removesuffix(".fa.md").removesuffix(".md")
        target = TARGET / relative.parent / (name + (".fa.md" if persian else ".md"))
        target.parent.mkdir(parents=True, exist_ok=True)
        text = convert(page.read_text(encoding="utf-8"), persian)
        section = relative.parent.as_posix()
        if name == "index" and relative.parent == Path("."):
            weight, english, farsi = SECTIONS[""]
            text = front_matter(title=farsi if persian else english, weight=weight) + text
        elif relative.as_posix() in PAGE_WEIGHTS:
            text = front_matter(weight=PAGE_WEIGHTS[relative.as_posix()]) + text
        target.write_text(text, encoding="utf-8")

    for section, (weight, english, farsi) in SECTIONS.items():
        if not section:
            continue
        folder = TARGET / section
        if not folder.is_dir():
            continue
        depth = "../" * (section.count("/") + 1)
        for title, suffix, intro in (
            (english, ".md", "Choose a page from the menu, or see the [list of every feature]({}index.md)."),
            (farsi, ".fa.md", "یک صفحه را از منو انتخاب کنید، یا [فهرست همهٔ قابلیت‌ها]({}index.md) را ببینید."),
        ):
            (folder / ("index" + suffix)).write_text(
                front_matter(title=title, weight=weight, comments="false")
                + f"# {title}\n\n{intro.format(depth)}\n",
                encoding="utf-8",
            )

    print(f"copied {source} to {TARGET.relative_to(SITE)}")


if __name__ == "__main__":
    main()
