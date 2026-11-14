#!/usr/bin/env python3
"""Add the channel's new videos to the app and manager guide pages.

- Reads the channel's long videos (videos tab, newest first) with yt-dlp, or from --list FILE
  (lines "id|upload_date|duration|title"), or from the RSS feed (YT_SOURCE=rss, in the GitHub Action).
- A video that is on neither guide page yet goes to the top of the first category of its page in
  data/guides/app.yml or data/guides/manager.yml (app videos on both languages of the app page;
  manager videos on the page of their title's language). Move it to another category if needed.
- Its title goes to data/guides/videos.yml and its 480x270 thumbnail to docs/assets/youtube/<id>.jpg.
- Then the pages are rebuilt (tools/guide_page.py).
"""
import re, sys, subprocess, urllib.request, io, os, argparse, json
import yaml
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

DATA = os.path.join(ROOT, 'data', 'guides')


def on_pages():
    """Every video id already on a guide page."""
    ids = set()
    for page in ('app', 'manager'):
        d = yaml.safe_load(open(os.path.join(DATA, page + '.yml'), encoding='utf-8'))
        for c in d['categories']:
            for lang in ('fa', 'en'):
                ids.update(c.get('videos', {}).get(lang) or [])
        ids.update((d.get('legacy') or {}).get('videos') or [])
    return ids


def prepend(page, lang, vid):
    """Put vid first in the videos of the first category of data/guides/<page>.yml (language lang)."""
    p = os.path.join(DATA, page + '.yml'); s = open(p, encoding='utf-8').read()
    m = re.search(rf'(?m)^      {lang}: \[(.*)\]$', s)          # the first category's list
    ids = [x.strip() for x in m.group(1).split(',') if x.strip()]
    s = s[:m.start()] + f'      {lang}: [' + ', '.join([vid] + ids) + ']' + s[m.end():]
    open(p, 'w', encoding='utf-8').write(s)


def add_title(vid, title):
    p = os.path.join(DATA, 'videos.yml')
    with open(p, 'a', encoding='utf-8') as f:
        f.write(f'{json.dumps(vid)}: {json.dumps(title, ensure_ascii=False)}\n')


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

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--list'); a = ap.parse_args()
    have = on_pages(); new = []
    for v in reversed(channel(a.list)):           # oldest first, so the newest ends up on top
        if v['id'] in have:
            continue
        if is_app(v):
            prepend('app', 'fa', v['id']); prepend('app', 'en', v['id'])
        else:
            prepend('manager', 'fa' if re.search('[\u0600-\u06FF]', v['title']) else 'en', v['id'])
        add_title(v['id'], v['title']); thumb(v['id']); new.append(v)
    for v in reversed(new):
        print(f"new {'app' if is_app(v) else 'manager'} video: {v['title']} ({v['id']})")
    print(len(new), 'new videos')
    subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'guide_page.py')], check=True)


if __name__ == '__main__':
    main()
