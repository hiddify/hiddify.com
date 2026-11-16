#!/usr/bin/env python3
"""Write the "All settings" reference of Hiddify Manager from the panel's source code.

    python3 scripts/sync_manager_settings.py <Hiddify-Manager checkout>     (make manager-settings)

Reads, in <checkout>/services/panel/src/hiddifypanel (the HiddifyPanel submodule):
- models/config_enum.py: every setting, its category, its type and what saving it needs
  (nothing, Apply, or Reinstall);
- panel/commercial/restapi/v2/admin/settings_api.py: which settings are shown without "advanced";
- panel/settings_form.py and the enum types: the choices of the select settings;
- translations.i18n/en.json and fa.json: the names and descriptions shown in the panel.
and writes docs/manager/configuration-and-advanced-settings/Settings-reference.md and .fa.md, one
section per settings group, in the panel's order, with an anchor per setting (#<setting_key>) so the
panel and other articles can link to one setting. The version comes from <checkout>/VERSION.
Don't edit the two pages by hand: run this again (the release workflow does it for each release).
"""
import html
import json
import re
import sys
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
OUT = SITE / "docs" / "manager" / "configuration-and-advanced-settings" / "Settings-reference"
PANEL_ARTICLE = "How-to-configure-Hiddify-panel-properly.md"

T = {
    "en": {
        "title": "All Hiddify Manager settings",
        "intro": "Every option of the panel's **Settings** page, in the panel's order, with the panel's own "
                 "explanation. This page is made from the panel's code for Hiddify Manager **v{version}**, so it "
                 "lists exactly what that version has.",
        "how": "**How to use it:** in the panel, open **Settings**. The common settings are shown first; turn on "
               "**Show Advanced Settings** to see the others (the ones marked *advanced* here). The search box at "
               "the top of the Settings page finds any setting by its name. For a tour of the whole panel, see "
               "[the panel guide]({panel}).",
        "after": "After saving",
        "after_nothing": "takes effect at once",
        "after_apply": "needs **Apply changes**",
        "after_reinstall": "needs **Reinstall**",
        "type": "Type",
        "bool": "on / off",
        "select": "a choice",
        "text": "text",
        "number": "number",
        "advanced": "advanced",
        "choices": "Choices",
        "count": "{n} settings",
        "companion": "Set inside the editor of [{owner}](#{key}).",
        "notes": {"parent_panel": "Shown only on a node: a panel that is linked to a parent panel."},
        "auto": "Made automatically from the panel's code (scripts/sync_manager_settings.py). Do not edit by hand.",
    },
    "fa": {
        "title": "همهٔ تنظیمات هیدیفای‌منیجر",
        "intro": "همهٔ گزینه‌های صفحهٔ **تنظیمات** پنل، به ترتیب خود پنل و با توضیح خود پنل. این صفحه از روی کد "
                 "هیدیفای‌منیجر **نسخهٔ {version}** ساخته شده و دقیقاً همان چیزی را دارد که آن نسخه دارد.",
        "how": "**روش استفاده:** در پنل، **تنظیمات** را باز کنید. تنظیمات رایج اول نشان داده می‌شوند؛ برای دیدن بقیه "
               "(آن‌هایی که این‌جا *پیشرفته* علامت خورده‌اند) **نمایش تنظیمات پیشرفته** را روشن کنید. کادر جستجوی "
               "بالای صفحهٔ تنظیمات هر تنظیمی را با نامش پیدا می‌کند. برای آشنایی با کل پنل، "
               "[راهنمای پیکربندی پنل]({panel}) را ببینید.",
        "after": "بعد از ذخیره",
        "after_nothing": "همان لحظه اعمال می‌شود",
        "after_apply": "**اعمال تغییرات** لازم است",
        "after_reinstall": "**نصب دوباره** لازم است",
        "type": "نوع",
        "bool": "روشن / خاموش",
        "select": "انتخابی",
        "text": "متن",
        "number": "عدد",
        "advanced": "پیشرفته",
        "choices": "گزینه‌ها",
        "count": "{n} تنظیم",
        "companion": "داخل ویرایشگر [{owner}](#{key}) تنظیم می‌شود.",
        "notes": {"parent_panel": "فقط در پنل نود دیده می‌شود: پنلی که به یک پنل مرکزی وصل است."},
        "auto": "این صفحه خودکار از کد پنل ساخته می‌شود (scripts/sync_manager_settings.py). دستی ویرایشش نکنید.",
    },
}
FA_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")


def flat(d, prefix=""):
    out = {}
    for k, v in d.items():
        if isinstance(v, dict):
            out.update(flat(v, prefix + k + "."))
        else:
            out[prefix + k] = v
    return out


def md(text):
    """The panel's (small) HTML to Markdown, on one paragraph per <br>."""
    s = str(text or "")
    s = re.sub(r"<a [^>]*href=['\"]([^'\"]+)['\"][^>]*>(.*?)</a>", lambda m: f"[{m.group(2).strip()}]({m.group(1)})", s, flags=re.S)
    s = re.sub(r"<br\s*/?>|</p>|</li>", "\n", s)
    s = re.sub(r"<li>", "- ", s)
    s = re.sub(r"</?(b|strong)>", "**", s)
    s = re.sub(r"</?(i|em)>", "*", s)
    s = re.sub(r"</?code>", "`", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    lines = [l.strip() for l in s.split("\n")]
    return "\n\n".join(l for l in lines if l)


def parse(panel):
    enum = (panel / "models" / "config_enum.py").read_text(encoding="utf-8")
    cat_block = re.search(r"class ConfigCategory\(StrEnum\):(.*?)\n\n", enum, re.S).group(1)
    categories = re.findall(r"^\s+(\w+)\s*=\s*auto\(\)", cat_block, re.M)
    settings = []
    # settings the panel creates (init_db.py, comments left out): a setting that is only declared is not shown
    init_db = (panel / "panel" / "init_db.py").read_text(encoding="utf-8")
    created = set(re.findall(r"ConfigEnum\.(\w+)", "\n".join(l.split("  #")[0] for l in init_db.splitlines())))
    for m in re.finditer(r"^\s{4}(\w+)\s*=\s*_(Bool|Str|Int|Typed)ConfigDscr\((.*)\)\s*(?:#.*)?$", enum, re.M):
        key, kind, args = m.groups()
        if key not in created:
            continue
        parts = [a.strip() for a in args.split(",")]
        ctype = None
        if kind == "Typed":
            ctype, parts = parts[0], parts[1:]
        # "ConfigCategory.hidden if <env> else ConfigCategory.general": the usual case is the else one
        cat = (re.search(r"else ConfigCategory\.(\w+)", args) or re.search(r"ConfigCategory\.(\w+)", args)).group(1)
        mode = next((p.split(".")[-1] for p in parts[1:] if p.startswith("ApplyMode.")), "nothing")
        settings.append({"key": key, "kind": kind, "ctype": ctype, "cat": cat, "mode": mode})
    api_file = panel / "panel" / "commercial" / "restapi" / "v2" / "admin" / "settings_api.py"
    api = api_file.read_text(encoding="utf-8") if api_file.exists() else ""   # older versions: no "advanced" split
    ess = re.search(r"ESSENTIAL_KEYS = frozenset\((.*?)\)\n", api, re.S)
    essential = set(re.findall(r"ConfigEnum\.(\w+)", ess.group(1))) if ess else None
    comp = re.search(r"COMPANION_OF = \{(.*?)\n\}", api, re.S)
    companions = dict(re.findall(r"ConfigEnum\.(\w+):\s*ConfigEnum\.(\w+)", comp.group(1))) if comp else {}
    form = (panel / "panel" / "settings_form.py").read_text(encoding="utf-8")
    choices = {}
    for blk in re.finditer(r"c\.key == ConfigEnum\.(\w+)(?: or c\.key == ConfigEnum\.(\w+))?:(.*?)(?=\n\s*elif |\n\s*else:)", form, re.S):
        code = "\n".join(l for l in blk.group(3).splitlines() if not l.strip().startswith("#") and ".append(" not in l)
        if "SelectField" not in code:
            continue
        found = re.findall(r'\("([^"]+)",\s*(?:Markup\()?(?:_\()?"([^"]+)"', code)
        if found:
            for k in filter(None, blk.group(1, 2)):
                choices[k] = found
    # HEnum types: their members, labelled config.<key>.<member>
    for s in settings:
        if s["ctype"] and s["key"] not in choices:
            cls = re.search(rf"class {re.escape(s['ctype'])}\((?:\w*Enum|HEnum)\):(.*?)\n\n", enum, re.S)
            if cls:
                members = re.findall(r"^\s+(\w+)\s*=", cls.group(1), re.M)
                choices[s["key"]] = [(x, f"config.{s['key']}.{x}") for x in members]
    tr = panel / "translations.i18n"
    texts = {lang: flat(json.loads((tr / f"{lang}.json").read_text(encoding="utf-8"))) for lang in ("en", "fa")}
    return categories, settings, essential, choices, texts, companions


def write(lang, version, categories, settings, essential, choices, texts, companions):
    t, tx, en = T[lang], texts[lang], texts["en"]

    def tr(key, default=""):
        return tx.get(key) or en.get(key) or default

    num = (lambda s: str(s).translate(FA_DIGITS)) if lang == "fa" else str
    shown = [s for s in settings if s["cat"] not in ("hidden",) and tr(f"config.{s['key']}.label")]
    out = [
        "---",
        f"title: {t['title']}",
        "comments: true",
        "---",
        "",
        f"<!-- {t['auto']} -->",
        "",
        f"# {t['title']}",
        "",
        t["intro"].format(version=num(version)),
        "",
        t["how"].format(panel=PANEL_ARTICLE),
        "",
    ]
    for cat in categories:
        rows = [s for s in shown if s["cat"] == cat]
        if not rows:
            continue
        out += [f"## {md(tr(f'config.{cat}.label', cat))} {{ #{cat} }}", ""]
        desc = md(tr(f"config.{cat}.description"))
        if desc:
            out += [desc, ""]
        out += [f"*{t['count'].format(n=num(len(rows)))}*", ""]
        for s in rows:
            k = s["key"]
            label = md(tr(f"config.{k}.label", k))
            out += [f"### {label} {{ #{k} }}", ""]
            d = md(tr(f"config.{k}.description"))
            if d:
                out += [d, ""]
            kind = "select" if k in choices else {"Bool": "bool", "Int": "number"}.get(s["kind"], "text")
            meta = [f"{t['type']}: {t[kind]}", f"{t['after']}: {t['after_' + {'apply_config': 'apply'}.get(s['mode'], s['mode'])]}"]
            if essential is not None and k not in essential:
                meta.append(f"*{t['advanced']}*")
            out += [" · ".join(meta), ""]
            if k in companions:
                owner = md(tr(f"config.{companions[k]}.label", companions[k]))
                out += [t["companion"].format(owner=owner, key=companions[k]), ""]
            if k in t["notes"]:
                out += [t["notes"][k], ""]
            if choices.get(k):
                items = [tr(lbl, lbl) if lbl.startswith(("config.", "lang.", "lib.")) else tr(lbl, lbl) for _, lbl in choices[k]]
                out += [f"{t['choices']}: " + "، ".join(md(i) for i in items) if lang == "fa" else f"{t['choices']}: " + ", ".join(md(i) for i in items), ""]
    return "\n".join(out).rstrip() + "\n", len(shown)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    root = Path(sys.argv[1])
    panel = root / "services" / "panel" / "src" / "hiddifypanel"
    if not (panel / "models" / "config_enum.py").is_file():
        sys.exit(f"{panel} has no models/config_enum.py: give a Hiddify-Manager checkout with its submodules")
    version = (root / "VERSION").read_text().strip() if (root / "VERSION").is_file() else "?"
    data = parse(panel)
    for lang in ("en", "fa"):
        text, n = write(lang, version, *data)
        if lang == "fa":
            sys.path.insert(0, str(SITE / "tools"))
            from fa_spelling import fix
            text = fix(text)
        path = OUT.with_suffix(".fa.md" if lang == "fa" else ".md")
        path.write_text(text, encoding="utf-8")
        print(f"{path.relative_to(SITE)}: {n} settings, v{version}")


if __name__ == "__main__":
    main()
