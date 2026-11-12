#!/usr/bin/env python3
"""Keep the YouTube video cards on the app and manager guide pages in sync with the channel.

- Reads the channel's long videos (videos tab, newest first) with yt-dlp, or from --list FILE
  (lines "id|upload_date|duration|title").
- App guide pages (docs/app/index*.md): the video group is rebuilt with every app video, newest first.
- Manager guide pages (docs/manager/index*.md): each existing video group is sorted newest first;
  a new manager video that is not on the page yet is added to the top of the first group.
- Existing cards are kept as they are (their thumbnails too); new cards get a 480x270 thumbnail in
  docs/assets/youtube/<id>.jpg.
"""
import re, sys, subprocess, urllib.request, io, os, argparse
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = 'https://www.youtube.com/@hiddify/videos'
APP_RE = re.compile(r'(اپ هیدیفای|هیدیفای‌اپ|HiddifyApp|Hiddify ?5|Hiddify Next|HiddifyNG|HiddifyN\b|Hiddify ?N |HiddifyCli|کِ?لش|هیدیفای اندروید|Clash|Hiddify android|تلویزیون|فیلترشکن رایگان هیدیفای|اینترنت آزاد رایگان با Hiddify|کانفیگ رایگان وارپ)', re.I)
APP_EXCLUDE = re.compile(r'(منیجر|Manager|پنل هیدیفای در نسخه دسکتاپ برنامه نکوری)', re.I)

def channel(listfile=None):
    if listfile:
        lines = open(listfile, encoding='utf-8').read().splitlines()
    elif os.environ.get('YT_SOURCE') == 'rss':                 # GitHub Action: the RSS feed, no yt-dlp
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from yt_channel import long_videos
        lines = ['|'.join((v, d, '', t)) for v, d, t in long_videos()]
    else:
        yd = os.environ.get('YTDLP', 'yt-dlp')
        lines = subprocess.run([yd, '--flat-playlist', '--extractor-args', 'youtubetab:approximate_date',
                                '--print', '%(id)s|%(upload_date)s|%(duration)s|%(title)s', CH],
                               capture_output=True, text=True, check=True).stdout.splitlines()
    vids = []
    for l in lines:
        p = l.split('|', 3)
        if len(p) == 4 and p[0]: vids.append({'id': p[0], 'title': p[3].strip()})
    return vids

def is_app(v): return bool(APP_RE.search(v['title'])) and not APP_EXCLUDE.search(v['title'])

def esc(s): return s.replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;')

def card(v):
    t = esc(v['title'])
    return (f'            <a href="https://www.youtube.com/watch?v={v["id"]}" title="{t}">\n'
            f'              <div class="relative p-2 flex justify-center items-center">\n'
            f'                <img src="/assets/youtube/{v["id"]}.jpg" alt="{t}"\n'
            f'                  class="md:max-h-[103px] w-full md:max-w-[184px] rounded-xl" decoding="async" loading="lazy" />\n'
            f'                <img src="/assets/play-icon.svg" class="absolute" decoding="async" loading="lazy" />\n'
            f'              </div>\n'
            f'            </a>\n')

def thumb(vid):
    out = os.path.join(ROOT, 'docs/assets/youtube', vid + '.jpg')
    if os.path.exists(out): return
    from PIL import Image
    for q in ('maxresdefault', 'hqdefault'):
        try:
            data = urllib.request.urlopen(f'https://i.ytimg.com/vi/{vid}/{q}.jpg', timeout=30).read()
            im = Image.open(io.BytesIO(data)).convert('RGB')
            w, h = im.size; th = w * 9 // 16
            if h > th: im = im.crop((0, (h - th) // 2, w, (h - th) // 2 + th))
            im.resize((480, 270), Image.LANCZOS).save(out, quality=88); return
        except Exception: continue

BLOCK = re.compile(r'[ \t]*<a href="https://www\.youtube\.com/watch\?v=([\w-]+)"[^>]*>.*?</a>\n', re.S)

def groups(s):
    """Runs of consecutive video cards: list of (start, end, [(id, text)])."""
    out = []; cur = None
    for m in BLOCK.finditer(s):
        if cur and s[cur[1]:m.start()].strip() == '':
            cur[1] = m.end(); cur[2].append((m.group(1), m.group(0)))
        else:
            if cur: out.append(cur)
            cur = [m.start(), m.end(), [(m.group(1), m.group(0))]]
    if cur: out.append(cur)
    return out

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--list'); a = ap.parse_args()
    vids = channel(a.list); order = {v['id']: i for i, v in enumerate(vids)}; by = {v['id']: v for v in vids}
    app = [v for v in vids if is_app(v)]
    for fn in ('docs/app/index.fa.md', 'docs/app/index.md'):
        p = os.path.join(ROOT, fn); s = open(p, encoding='utf-8').read(); g = groups(s)
        if not g: continue
        st, en, items = g[0]; have = dict(items)
        ids = [v['id'] for v in app] + [i for i, _ in items if i not in order]
        new = ''.join(have.get(i) or card(by[i]) for i in ids)
        for i in ids:
            if i not in have: thumb(i)
        s = s[:st] + new + s[en:]; open(p, 'w', encoding='utf-8').write(s)
        print(fn, len(ids), 'videos,', sum(i not in have for i in ids), 'new')
    for fn in ('docs/manager/index.fa.md', 'docs/manager/index.md'):
        p = os.path.join(ROOT, fn); s = open(p, encoding='utf-8').read()
        on_page = set(BLOCK.findall(s)); added = []
        for st, en, items in reversed(groups(s)):
            items = sorted(items, key=lambda it: order.get(it[0], 10**6))
            s = s[:st] + ''.join(t for _, t in items) + s[en:]
        fa = fn.endswith('.fa.md')
        newm = [v for v in vids if not is_app(v) and v['id'] not in on_page
                and v['id'] not in open(os.path.join(ROOT, 'docs/manager/index.md' if fa else 'docs/manager/index.fa.md'), encoding='utf-8').read()
                and (bool(re.search('[؀-ۿ]', v['title'])) == fa)]
        if newm:
            g = groups(s); st = g[0][0]
            s = s[:st] + ''.join(card(v) for v in newm) + s[st:]
            for v in newm: thumb(v['id'])
        open(p, 'w', encoding='utf-8').write(s)
        print(fn, 'sorted;', len(newm), 'new')
main()
