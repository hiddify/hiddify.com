#!/usr/bin/env python3
"""One spelling for words the Persian pages wrote in several ways.

    python3 tools/fa_spelling.py            fix every docs/**/*.fa.md   (make spelling)
    python3 tools/fa_spelling.py --check    only list what would change

The search box applies the same rules to what readers type (docs/assets/js/search-spelling.js).
Only prose is changed: code blocks, inline code, link targets, HTML tags and URLs are left alone.
docs/instagram is skipped: its titles are the YouTube videos' own titles. scripts/sync_core_docs.py
applies the same rules to the Core pages it copies from hiddify-sing-box.
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FA = "؀-ۿ‌"          # Persian letters and the zero-width non-joiner
B = rf"(?<![{FA}])"                 # a word start: no Persian letter before

# (wrong spellings, the one spelling)
RULES = [
    (r"کلودفلر|کلود فلر|کلاودفلر|کلود‌فلر", "کلادفلر"),       # Cloudflare
    (r"ریالیتی|ریلیتی|رئالیتی", "ریالتی"),                      # Reality
    (r"پراکسی", "پروکسی"),                                      # proxy
    (r"هایدیفای", "هیدیفای"),
    (r"هیدیفای منیجر", "هیدیفای‌منیجر"),
    (r"بروزرسانی|به روز رسانی|به‌روز رسانی|به روزرسانی", "به‌روزرسانی"),
    (r"نرم افزار", "نرم‌افزار"),
    (r"آیپی|آی پی|ایپی", "آی‌پی"),                              # IP
    (r"تانل", "تونل"),                                          # tunnel (تانلینگ -> تونلینگ too)
    (r"ورکرز", "ورکر"),                                         # Cloudflare Workers
]
RULES = [(re.compile(B + "(?:" + a + ")"), b) for a, b in RULES]

# parts of a page that are not prose
PROTECT = re.compile(
    r"```.*?```|~~~.*?~~~"            # fenced code
    r"|`[^`\n]*`"                     # inline code
    r"|\]\([^)]*\)"                   # link targets
    r"|<[^<>]+>"                      # HTML tags with their attributes
    r"|https?://\S+",                 # bare URLs
    re.S)


COUNT = [0]


def fix(text):
    out, pos = [], 0
    for m in PROTECT.finditer(text):
        out.append(fix_prose(text[pos:m.start()]))
        out.append(m.group(0))
        pos = m.end()
    out.append(fix_prose(text[pos:]))
    return "".join(out)


def fix_prose(s):
    for pat, good in RULES:
        s, n = pat.subn(good, s)
        COUNT[0] += n
    return s


def main():
    check = "--check" in sys.argv
    changed = 0
    for f in sorted(glob.glob(os.path.join(ROOT, "docs", "**", "*.fa.md"), recursive=True)):
        rel = os.path.relpath(f, ROOT)
        if rel.startswith("docs/instagram/"):
            continue
        s = open(f, encoding="utf-8").read()
        COUNT[0] = 0
        new = fix(s)
        if new != s:
            changed += 1
            n = COUNT[0]
            print(f"{rel}: {n} word{'s' if n != 1 else ''}")
            if not check:
                open(f, "w", encoding="utf-8").write(new)
    print(f"{changed} page{'s' if changed != 1 else ''} {'to fix' if check else 'fixed'}")
    return 1 if check and changed else 0


if __name__ == "__main__":
    sys.exit(main())
