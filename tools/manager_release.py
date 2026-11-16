#!/usr/bin/env python3
"""Keep the site in step with Hiddify Manager releases (used by .github/workflows/manager-release.yml).

    python3 tools/manager_release.py --check <tag>
        prints "new=true|false" (the release is newer than the one the site shows) and
        "settings=true|false" (it is newer than the version the settings reference was made from)
    python3 tools/manager_release.py --tag <tag> --date <YYYY-MM-DD> [--src <Hiddify-Manager checkout>]
        writes the release into the "latest version" line of docs/manager/index.md and index.fa.md and
        into data/manager/release.yml; with --src (and a newer version) it also rebuilds the settings
        reference (scripts/sync_manager_settings.py) and prints which settings were added or removed.

The settings reference can be ahead of the latest release (made from a beta, for the articles written
for it): it is only rebuilt from a release that is at least as new.
"""
import argparse
import datetime
import re
import subprocess
import sys
from pathlib import Path

import yaml
from packaging.version import Version

SITE = Path(__file__).resolve().parent.parent
STATE = SITE / "data" / "manager" / "release.yml"
REFERENCE = SITE / "docs" / "manager" / "configuration-and-advanced-settings" / "Settings-reference.md"
FA_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
JALALI_MONTHS = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]


def ver(tag):
    return Version(str(tag).lstrip("v"))


def state():
    return yaml.safe_load(STATE.read_text(encoding="utf-8")) if STATE.exists() else {}


def jalali(d):
    """Gregorian date -> (year, month, day) in the Persian calendar."""
    gy, gm, gd = d.year, d.month, d.day
    g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    gy2 = gy + 1 if gm > 2 else gy
    days = 355666 + 365 * gy + (gy2 + 3) // 4 - (gy2 + 99) // 100 + (gy2 + 399) // 400 + gd + g_d_m[gm - 1]
    jy = -1595 + 33 * (days // 12053)
    days %= 12053
    jy += 4 * (days // 1461)
    days %= 1461
    if days > 365:
        jy += (days - 1) // 365
        days = (days - 1) % 365
    jm = 1 + days // 31 if days < 186 else 7 + (days - 186) // 30
    jd = 1 + (days % 31 if days < 186 else (days - 186) % 30)
    return jy, jm, jd


def keys(text):
    return set(re.findall(r"^### .*\{ #(\w+) \}$", text, re.M))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check")
    ap.add_argument("--tag")
    ap.add_argument("--date")
    ap.add_argument("--src")
    a = ap.parse_args()
    st = state()
    if a.check:
        v = ver(a.check)
        print(f"new={'true' if v > ver(st.get('latest', '0')) else 'false'}")
        print(f"settings={'true' if v >= ver(st.get('settings_reference', '0')) else 'false'}")
        return
    if not (a.tag and a.date):
        sys.exit(__doc__)
    v, d = ver(a.tag), datetime.date.fromisoformat(a.date[:10])
    tag = "v" + str(v)
    en_date = f"{d:%B} {d.day}, {d.year}"
    jy, jm, jd = jalali(d)
    fa_date = f"{str(jd).translate(FA_DIGITS)} {JALALI_MONTHS[jm - 1]} {str(jy).translate(FA_DIGITS)} / {d.day} {d:%B} {d.year}"
    fa_date = fa_date.replace(f"{d:%B}", ["ژانویه", "فوریه", "مارس", "آوریل", "مه", "ژوئن", "ژوئیه", "اوت", "سپتامبر", "اکتبر", "نوامبر", "دسامبر"][d.month - 1])
    for name, pattern, new in (
        ("index.md", r"(- \*\*Latest version:\*\* )v[\d.]+\w*( \([^)]*\))", rf"\g<1>{tag} ({en_date})"),
        ("index.fa.md", r"(- \*\*آخرین نسخه:\*\* )v[\d.]+\w*( \([^)]*\))", rf"\g<1>{tag} ({fa_date})"),
    ):
        p = SITE / "docs" / "manager" / name
        s = p.read_text(encoding="utf-8")
        s2, n = re.subn(pattern, new, s, count=1)
        if not n:
            sys.exit(f"{p}: no latest-version line found")
        p.write_text(s2, encoding="utf-8")
    st["latest"], st["date"] = str(v), d.isoformat()
    if a.src and v >= ver(st.get("settings_reference", "0")):
        before = keys(REFERENCE.read_text(encoding="utf-8")) if REFERENCE.exists() else set()
        subprocess.run([sys.executable, str(SITE / "scripts" / "sync_manager_settings.py"), a.src], check=True)
        after = keys(REFERENCE.read_text(encoding="utf-8"))
        st["settings_reference"] = str(v)
        for label, items in (("added", after - before), ("removed", before - after)):
            if items:
                print(f"settings {label}: " + ", ".join(sorted(items)))
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text("# Written by tools/manager_release.py: the Hiddify Manager release the site shows, and the\n"
                     "# version the settings reference (Settings-reference.md) was made from.\n"
                     + yaml.safe_dump(st, sort_keys=False), encoding="utf-8")
    print(f"site now shows {tag} ({d})")


if __name__ == "__main__":
    main()
