#!/usr/bin/env python3
"""Copy hiddify-sing-box's docs/hiddify into the Core section of this site (docs/core).

    python3 scripts/sync_core_docs.py <path to hiddify-sing-box>

The pages are merged into docs/core, not kept in a folder of their own:

    docs/hiddify/index.md           -> docs/core/features/index.md   (the list of every feature)
    docs/hiddify/features/...       -> docs/core/features/...
    docs/hiddify/bugfix/...         -> docs/core/bugfix/...
    docs/hiddify/app_considerations -> docs/core/app_considerations.md

hiddify-sing-box writes each page as name.en.md and name.fa.md; this site takes name.md for
English and name.fa.md for Persian, and links to name.md from both languages. The script renames
the pages, recomputes every link between them for the new places, drops the language links (the
site has its own language switch) and the RTL wrapper of the Persian pages, and writes the section
titles. docs/core/features, docs/core/bugfix and docs/core/app_considerations*.md are replaced as a
whole, so edit those pages in hiddify-sing-box, not here. docs/core/index*.md and docs/core/cli*.md
belong to this site and are not touched.
"""

import posixpath
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
from fa_spelling import fix as fa_spelling  # noqa: E402  one spelling for Persian words

SITE = Path(__file__).resolve().parent.parent
CORE = SITE / "docs" / "core"
OLD_TARGET = CORE / "sing-box"  # where the pages lived before they were merged into docs/core
SOURCE_URL = "https://github.com/hiddify/hiddify-sing-box/blob/v5/"

# Section folder (in docs/core): (weight, English title, Persian title)
SECTIONS = {
    "features": (10, "Features", "قابلیت‌ها"),
    "features/protocols": (-100, "Protocols", "پروتکل‌ها"),
    "features/transports": (-90, "Transports", "ترنسپورت‌ها"),
    "features/dns": (-80, "DNS", "DNS"),
    "features/groups": (-70, "Groups and monitoring", "گروه‌ها و پایش"),
    "bugfix": (50, "Bug fixes", "رفع باگ‌ها"),
}
# Pages outside a section that need a place in the menu.
PAGE_WEIGHTS = {"app_considerations": 60}
# The heading of the feature list, which was the front page of the sing-box docs.
FEATURES_HEADING = ("Core features", "قابلیت‌های هسته")

LANGUAGE_LINK = re.compile(r"^\[(?:فارسی|English)\]\([^)]*\)(?: · )?")
LINK = re.compile(r"\]\(([^)\s]+)\)")


def place(source_path: str) -> str:
    """docs/hiddify-relative path of a page (without language suffix) -> docs/core-relative path."""
    if source_path == "index.md":
        return "features/index.md"
    return source_path


def fix_link(target: str, page_source: str) -> str:
    """A link in page_source (docs/hiddify-relative) rewritten for the page's new place."""
    if re.match(r"^[a-z]+:|^#|^/", target):
        return target
    path, _, anchor = target.partition("#")
    if not path:
        return target
    resolved = posixpath.normpath(posixpath.join(posixpath.dirname(page_source), path))
    if resolved.startswith("../"):
        # outside docs/hiddify: a file of the repository, on GitHub
        repo_path = posixpath.normpath(posixpath.join("docs/hiddify", resolved))
        return SOURCE_URL + repo_path + ("#" + anchor if anchor else "")
    if not resolved.endswith(".md"):
        return target
    resolved = re.sub(r"\.(?:en|fa)\.md$", ".md", resolved)
    here = re.sub(r"\.(?:en|fa)\.md$", ".md", page_source)
    new = posixpath.relpath(place(resolved), posixpath.dirname(place(here)))
    return new + ("#" + anchor if anchor else "")


def convert(text: str, persian: bool, page_source: str) -> str:
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
    if persian:
        text = fa_spelling(text)
    return LINK.sub(lambda m: "](" + fix_link(m.group(1), page_source) + ")", text)


def front_matter(**fields) -> str:
    body = "".join(f"{key}: {value}\n" for key, value in fields.items())
    return f"---\n{body}---\n\n"


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    source = Path(sys.argv[1]) / "docs" / "hiddify"
    if not (source / "index.md").is_file():
        sys.exit(f"{source} has no index.md: give the path of a hiddify-sing-box checkout")

    for old in (OLD_TARGET, CORE / "features", CORE / "bugfix"):
        if old.exists():
            shutil.rmtree(old)
    for old in CORE.glob("app_considerations*.md"):
        old.unlink()

    for page in sorted(source.rglob("*.md")):
        relative = page.relative_to(source)
        persian = page.name.endswith(".fa.md")
        name = page.name.removesuffix(".en.md").removesuffix(".fa.md").removesuffix(".md")
        page_source = (relative.parent / page.name).as_posix()
        target_rel = place((relative.parent / (name + ".md")).as_posix())
        target = CORE / (target_rel[:-3] + (".fa.md" if persian else ".md"))
        target.parent.mkdir(parents=True, exist_ok=True)
        text = convert(page.read_text(encoding="utf-8"), persian, page_source)
        if target_rel == "features/index.md":
            weight, english, farsi = SECTIONS["features"]
            heading = FEATURES_HEADING[1 if persian else 0]
            text = re.sub(r"^# .*$", "# " + heading, text, count=1, flags=re.M)
            text = front_matter(title=farsi if persian else english, weight=weight) + text
        elif name in PAGE_WEIGHTS and relative.parent == Path("."):
            text = front_matter(weight=PAGE_WEIGHTS[name]) + text
        target.write_text(text, encoding="utf-8")

    for section, (weight, english, farsi) in SECTIONS.items():
        folder = CORE / section
        if section == "features" or not folder.is_dir():
            continue
        to_list = posixpath.relpath("features/index.md", section)
        for title, suffix, intro in (
            (english, ".md", "Choose a page from the menu, or see the [list of every feature]({})."),
            (farsi, ".fa.md", "یک صفحه را از منو انتخاب کنید، یا [فهرست همهٔ قابلیت‌ها]({}) را ببینید."),
        ):
            (folder / ("index" + suffix)).write_text(
                front_matter(title=title, weight=weight, comments="false")
                + f"# {title}\n\n{intro.format(to_list)}\n",
                encoding="utf-8",
            )

    print(f"copied {source} into {CORE.relative_to(SITE)}")


if __name__ == "__main__":
    main()
