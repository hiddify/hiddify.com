"""The About us page (docs/about-us.md and .fa.md), same structure in both languages.
    python3 tools/about_page.py      writes the two pages (story, numbers, teams, join, support)
The timeline is the blog: every published post (date, title, description, colour and icon from its category)
plus a few Hiddify Manager milestones that have no post (EXTRA). hooks/about_timeline.py calls timeline_html()
at every build, so a new blog post shows up on the About page by itself, with no edit here.
Styles: docs/assets/css/about.css (loaded only on that page)."""
import glob
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'


def _icons():
    import material
    base = os.path.dirname(material.__file__)
    for d in ('templates/.icons/material', '.icons/material'):
        if os.path.isdir(os.path.join(base, d)):
            return os.path.join(base, d) + '/'
    raise FileNotFoundError('Material icons not found')


MI = _icons()
FA_DIGITS = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
FA_MONTHS = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']
EN_MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


def mi(n):
    s = open(MI + n + '.svg').read()
    return s.replace('<svg ', '<svg aria-hidden="true" ', 1).strip()


def g2j(gy, gm, gd):
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
    if days < 186:
        jm, jd = 1 + days // 31, 1 + days % 31
    else:
        jm, jd = 7 + (days - 186) // 30, 1 + (days - 186) % 30
    return jy, jm, jd




def post(name, lang):
    f = ROOT + f'docs/blog/posts/{name}.{"fa.md" if lang == "fa" else "md"}'
    s = open(f, encoding='utf-8').read()
    d = re.search(r'^date:\s*(\S+)', s, re.M).group(1)
    m = re.search(r'^slug:\s*(\S+)', s, re.M)
    slug = m.group(1) + '/' if m else ''   # a post without a slug lives at its date (its address must not change)
    return d, ('/fa' if lang == 'fa' else '') + f'/blog/{d.replace("-", "/")}/{slug}'


def date_label(d, lang):
    y, m, dd = map(int, d.split('-'))
    if lang == 'fa':
        jy, jm, jd = g2j(y, m, dd)
        return f'{jd} {FA_MONTHS[jm - 1]} {jy}'.translate(FA_DIGITS), str(jy).translate(FA_DIGITS)
    return f'{EN_MONTHS[m - 1]} {dd}, {y}', str(y)


# The timeline is the blog (user 2026-11-17: «بر اساس پستهای بلاگ»): every published post, with its own
# date, title and description; colour and icon from its category; each point links to its post.
CAT = {'Manager': ('server-network', '#455fe9'), 'App': ('cellphone', '#8b5cf6'), 'Project': ('lightbulb-on-outline', '#14b8a6'),
       'Hello': ('cake-variant-outline', '#ec4899'), 'Anniversary': ('cake-variant-outline', '#ec4899')}


EXTRA = [
    ('2022-09-26', 'https://github.com/hiddify/Hiddify-Manager/commits/main/?since=2022-09-26&until=2022-09-27', 'flag-variant-outline', '#455fe9',
     ('اولین کد هیدیفای', 'ریپوی سرور هیدیفای (آن زمان hiddify-config، امروز Hiddify-Manager) در گیت‌هاب ساخته شد.'),
     ('The first Hiddify code', 'The Hiddify server repository (then hiddify-config, today Hiddify-Manager) is created on GitHub.')),
    ('2024-03-02', 'https://github.com/hiddify/hiddifypanel/blob/main/HISTORY.md', 'debug-step-over', '#64748b',
     ('هیدیفای‌منیجر ۸.۸.۹۹ و پرش به ۱۰', 'آخرین نسخهٔ ۸. نسخهٔ ۹ منتشر نشد: نسخهٔ بعدی ۱۰.۱۰ بود تا پنل و سرور یک شماره داشته باشند.'),
     ('Hiddify Manager 8.8.99, and the jump to 10', 'The last 8.x. There was no 9: the next version was 10.10, so the panel and the server share one number.')),
]


def front(s, key):
    m = re.search(rf'^{key}:\s*(.+)$', s, re.M)
    v = m.group(1).strip() if m else ''
    return json.loads(v) if v.startswith('"') else v


def short(text, n=120):
    text = re.sub(r'\s+', ' ', text).strip()
    if len(text) <= n:
        return text
    cut = text[:n].rsplit(' ', 1)[0].rstrip('،,:;؛ ')
    return cut + '…'


def timeline(lang):
    out = []
    for f in sorted(glob.glob(ROOT + 'docs/blog/posts/*.fa.md')):
        base = f[:-6]
        f = base + ('.fa.md' if lang == 'fa' else '.md')
        s = open(f, encoding='utf-8').read()
        if re.search(r'^draft:\s*true', s, re.M):
            continue
        cat = re.search(r'^categories:\s*\n\s*-\s*(\S+)', s, re.M)
        icon, col = CAT.get(cat.group(1) if cat else '', ('newspaper-variant-outline', '#64748b'))
        title = re.search(r'^#\s+(.+)$', s, re.M).group(1).strip()
        title = re.sub(r'\s*[\U0001F300-\U0001FAFF\u2600-\u27BF]+\s*$', '', title)
        name = base.rsplit('/', 1)[1]
        desc = front(s, 'description')
        d, url = post(name, lang)
        out.append((d, url, icon, col, title, short(desc)))
    # Hiddify Manager milestones that have no blog post of their own
    for d, url, icon, col, fa, en in EXTRA:
        title, line = fa if lang == 'fa' else en
        out.append((d, url, icon, col, title, line))
    return sorted(out)


T = {
    'fa': dict(
        title='درباره ما', desc='داستان هیدیفای، از اولین قدم تا امروز؛ تیم‌ها و راه‌های همکاری.',
        eyebrow='داستان هیدیفای', h1='راهکار آزادی اینترنت',
        story=['در ایران، دسترسی به اینترنت به‌شدت سانسور می‌شود، و پس از مرگ <a href="https://en.wikipedia.org/wiki/Death_of_Mahsa_Amini">مهسا امینی</a> و اعتراض‌های پس از آن بیشتر هم شد. از آن زمان، مردم عادی برای رسیدن به اینترنت آزاد با محدودیت روبه‌رو هستند.',
               'پروژهٔ هیدیفای راه‌هایی ساده و کم‌هزینه برای رسیدن به اینترنت بدون محدودیت به مردم می‌دهد.'],
        f_hidden='مخفی', f_simple='ساده', f_hiddify='هیدیفای',
        nums=[('calendar-star', 'از ۱۴۰۱', 'کنار شما'), ('source-commit', '+۱۳ هزار', 'کامیت در گیت‌هاب'),
              ('shield-star-outline', '+۳۰', 'پروتکل'), ('lock-open-variant-outline', '۱۰۰٪', 'متن‌باز')],
        tl_h='از اولین قدم تا امروز', tl_sub='داستان هیدیفای در بلاگ، از اولین قدم تا امروز. هر نقطه را بزنید تا پست کاملش را بخوانید.', read='خواندن پست',
        teams_h='تیم‌های ما', teams_sub='هیدیفای را گروهی از داوطلبان می‌سازند.',
        teams=[('code-braces', '#455fe9', 'توسعه', 'توسعه‌دهندگان ما با <a href="https://github.com/hiddify/Hiddify-Manager">هیدیفای‌منیجر</a> و <a href="https://github.com/hiddify/hiddify-app">اپ هیدیفای</a> رویاهای ما را به واقعیت تبدیل می‌کنند.'),
               ('palette-outline', '#ec4899', 'طراحی', 'طراحان ما تصویرهای چشم‌نواز می‌سازند و تجربهٔ کاربری محصولات هیدیفای را با تست با کاربران بهتر می‌کنند.'),
               ('play-box-multiple-outline', '#f59e0b', 'محتوا', 'محتوای آموزشی و خواندنی، از <a href="/fa/manager/">آموزش‌های کامل</a> تا <a href="https://www.youtube.com/@hiddify">ویدیوهای یوتیوب</a>، را ما گردآوری می‌کنیم.'),
               ('lifebuoy', '#10b981', 'پشتیبانی کاربران', 'ما همیشه برای جواب دادن به پرسش‌های شما در <a href="https://t.me/hiddify_board">گروه تلگرام</a> در دسترس هستیم.')],
        join_h='به ما بپیوندید', join_sub='ما همیشه دنبال متخصصانی هستیم که به بهتر شدن هیدیفای کمک کنند. رزومهٔ خود را برایمان بفرستید.',
        roles=[('code-braces', '#455fe9', 'تیم توسعه', 'دنبال توسعه‌دهندگان پایتون، کاتلین و فلاتر هستیم تا با هم آیندهٔ هیدیفای را بسازیم.', ['Python', 'Kotlin', 'Flutter']),
               ('video-outline', '#f59e0b', 'تیم محتوا', 'اگر در ساخت و ویرایش ویدیو برای یوتیوب و محتوای تصویری برای شبکه‌های اجتماعی مهارت دارید، به ما بپیوندید.', ['YouTube', 'ویرایش ویدیو']),
               ('draw', '#ec4899', 'تیم طراحی', 'دنبال یک متخصص طراحی UX/UI هستیم تا تجربهٔ کاربران را در همهٔ محصولات هیدیفای بهتر کند.', ['UX', 'UI'])],
        mail='ایمیل بزنید',
        sup_h='می‌خواهید از هیدیفای حمایت کنید؟',
        sup_t='ساده‌ترین راه، زدن ستاره در گیت‌هاب ماست. همهٔ کار ما داوطلبانه است و کمک‌های مالی هم صرف توسعهٔ پروژه می‌شود.',
        star='ستاره در گیت‌هاب', donate='حمایت مالی', donate_url='/fa/donation-and-support/',
    ),
    'en': dict(
        title='About us', desc='The story of Hiddify, from the first step to today; our teams and how to join.',
        eyebrow='The story of Hiddify', h1='Internet Freedom Solution',
        story=["In Iran, internet access is heavily censored, even more so after <a href=\"https://en.wikipedia.org/wiki/Death_of_Mahsa_Amini\">Mahsa Amini's</a> death and the protests that followed. Since then, everyday people have faced restrictions in reaching the open internet.",
               'The Hiddify project gives people simple and affordable ways to reach the unrestricted internet.'],
        f_hidden='Hidden', f_simple='Simple', f_hiddify='Hiddify',
        nums=[('calendar-star', 'Since 2022', 'by your side'), ('source-commit', '13k+', 'commits on GitHub'),
              ('shield-star-outline', '30+', 'protocols'), ('lock-open-variant-outline', '100%', 'open source')],
        tl_h='From the first step to today', tl_sub='The story of Hiddify on our blog, from the first step to today. Tap any point to read the full post.', read='Read the post',
        teams_h='Our teams', teams_sub='Hiddify is built by a group of volunteers.',
        teams=[('code-braces', '#455fe9', 'Development', 'Our developers bring our vision to life through <a href="https://github.com/hiddify/Hiddify-Manager">Hiddify Manager</a> and the <a href="https://github.com/hiddify/hiddify-app">Hiddify app</a>.'),
               ('palette-outline', '#ec4899', 'Design', 'Our designers create beautiful visuals and improve the experience of Hiddify products through testing with users.'),
               ('play-box-multiple-outline', '#f59e0b', 'Content', 'We put together helpful content, from <a href="/manager/">our full tutorials</a> to <a href="https://www.youtube.com/@hiddify">YouTube videos</a>.'),
               ('lifebuoy', '#10b981', 'User support', 'We are always there to answer your questions in our <a href="https://t.me/hiddify_board">Telegram group</a>.')],
        join_h='Join us', join_sub='We are always looking for specialists to help make Hiddify better. Send us your resume.',
        roles=[('code-braces', '#455fe9', 'Development team', "We're looking for Python, Kotlin and Flutter developers to build the future of Hiddify with us.", ['Python', 'Kotlin', 'Flutter']),
               ('video-outline', '#f59e0b', 'Content team', 'If you are good at making and editing videos for YouTube and visual content for social media, join us.', ['YouTube', 'Video editing']),
               ('draw', '#ec4899', 'Design team', 'We are looking for a UX/UI design expert to improve the experience of users across all Hiddify products.', ['UX', 'UI'])],
        mail='Email us',
        sup_h='Want to support Hiddify?',
        sup_t='The easiest way is to star us on GitHub. All of our work is voluntary, and donations are spent on developing the project.',
        star='Star on GitHub', donate='Donate', donate_url='/donation-and-support/',
    ),
}


def timeline_html(lang):
    """The <li> items of the timeline (year labels and one card per event), newest last."""
    t = T[lang]
    items, last_year = '', None
    tl = timeline(lang)
    for i, (d, url, ic, col, title, line) in enumerate(tl):
        label, year = date_label(d, lang)
        if year != last_year:
            items += f'<li class="hi-ab-year"><span>{year}</span></li>'
            last_year = year
        now = ' now' if i == len(tl) - 1 else ''
        items += (f'<li class="hi-ab-ev{now}" style="--c:{col}"><a href="{url}"><i class="hi-ab-dot">{mi(ic)}</i>'
                  f'<span class="hi-ab-card"><time datetime="{d}">{label}</time><b>{title}</b><span>{line}</span>'
                  f'<em>{t["read"]} {mi("arrow-left" if lang == "fa" else "arrow-right")}</em></span></a></li>')
    return items


def page(lang):
    t = T[lang]
    story = ''.join(f'<p>{p}</p>' for p in t['story'])
    nums = ''.join(f'<div class="hi-ab-num"><i>{mi(ic)}</i><b>{v}</b><span>{l}</span></div>' for ic, v, l in t['nums'])
    items = timeline_html(lang)
    teams = ''.join(f'<div class="hi-ab-team" style="--c:{c}"><i>{mi(ic)}</i><b>{h}</b><p>{p}</p></div>' for ic, c, h, p in t['teams'])
    roles = ''.join(f'<div class="hi-ab-role" style="--c:{c}"><i>{mi(ic)}</i><div><b>{h}</b><p>{p}</p>'
                    f'<span class="hi-ab-tags">{"".join(f"<span>{x}</span>" for x in tags)}</span></div></div>'
                    for ic, c, h, p, tags in t['roles'])
    return f'''---
title: {t['title']}
description: {json.dumps(t['desc'], ensure_ascii=False)}
hide:
  - toc
  - feedback
comments: false
weight: 5
---

<link rel="stylesheet" href="/assets/css/about.css">

<p class="hi-ab-eyebrow">{t['eyebrow']}</p>

# {t['h1']}

<div class="hi-ab" markdown="0">
<div class="hi-ab-story">{story}</div>
<div class="hi-ab-formula" aria-label="{t['f_hidden']} + {t['f_simple']} = {t['f_hiddify']}">
<span class="hi-ab-f"><i>{mi('eye-off-outline')}</i>{t['f_hidden']}</span><span class="hi-ab-op">+</span>
<span class="hi-ab-f"><i>{mi('gesture-tap')}</i>{t['f_simple']}</span><span class="hi-ab-op">=</span>
<span class="hi-ab-f res"><i><img src="/assets/logos/hiddify-mark-white.svg" alt=""></i>{t['f_hiddify']}</span>
</div>
<div class="hi-ab-nums">{nums}</div>

<h2 id="timeline">{t['tl_h']}</h2>
<p class="hi-ab-sub">{t['tl_sub']}</p>
<ol class="hi-ab-tl">{items}</ol>

<h2 id="teams">{t['teams_h']}</h2>
<p class="hi-ab-sub">{t['teams_sub']}</p>
<div class="hi-ab-teams">{teams}</div>

<h2 id="join">{t['join_h']}</h2>
<p class="hi-ab-sub">{t['join_sub']}</p>
<div class="hi-ab-roles">{roles}</div>
<div class="hi-ab-mail"><a class="hi-ab-btn pri" href="mailto:contribute@hiddify.com">{mi('email-fast-outline')}{t['mail']}</a><code dir="ltr">contribute@hiddify.com</code></div>

<div class="hi-ab-support">
<div><h2 id="support">{t['sup_h']}</h2><p>{t['sup_t']}</p></div>
<div class="hi-ab-sbtn"><a class="hi-ab-btn star" href="https://github.com/hiddify/Hiddify-Manager">{mi('star-outline')}{t['star']}</a><a class="hi-ab-btn pri" href="{t['donate_url']}">{mi('hand-heart-outline')}{t['donate']}</a></div>
</div>
</div>
'''


if __name__ == '__main__':
    open(ROOT + 'docs/about-us.fa.md', 'w', encoding='utf-8').write(page('fa'))
    open(ROOT + 'docs/about-us.md', 'w', encoding='utf-8').write(page('en'))
    print('wrote docs/about-us.md and docs/about-us.fa.md')
