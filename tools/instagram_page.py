"""Keep docs/instagram (the site's Instagram-style page) in sync with the YouTube channel.

Every long channel video (Shorts are left out on purpose) that is not on the page yet gets a square post image in docs/instagram/img/yt/
and a tile in the grid of index.md and index.fa.md, newest first. Tiles already on the page (hand-made posts,
blog posts) stay as they are, in their place.

usage:  make instagram          (needs: pip install yt-dlp pillow; a Persian-capable font such as Vazirmatn)
"""
import html, io, os, re, subprocess, sys, urllib.request
from PIL import Image, ImageDraw, ImageFilter, ImageFont

CHANNEL = 'https://www.youtube.com/@hiddify'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE_DIR = os.path.join(ROOT, 'docs', 'instagram'); IMG_DIR = os.path.join(PAGE_DIR, 'img', 'yt')
PAGES = [os.path.join(PAGE_DIR, 'index.md'), os.path.join(PAGE_DIR, 'index.fa.md')]
FONT = os.environ.get('INSTAGRAM_FONT', '/usr/share/fonts/truetype/vazirmatn/Vazirmatn-Bold.ttf')
YTDLP = os.environ.get('YTDLP', 'yt-dlp')
SIZE = 640

def channel():
    """[(id, title, kind)] newest first: the channel's long videos only (no Shorts)."""
    out = []
    for tab, kind in (('videos', 'video'),):
        r = subprocess.run([YTDLP, '--flat-playlist', '--extractor-args', 'youtubetab:approximate_date',
                            '--print', '%(id)s\t%(upload_date)s\t%(title)s', f'{CHANNEL}/{tab}'], capture_output=True, text=True)
        for n, l in enumerate(r.stdout.splitlines()):
            if l.count('\t') < 2: continue
            vid, date, title = l.split('\t', 2)
            if not date.isdigit():   # Shorts have no date in the list: ask for it
                q = subprocess.run([YTDLP, '--skip-download', '--print', '%(upload_date)s', f'https://www.youtube.com/shorts/{vid}'],
                                   capture_output=True, text=True).stdout.strip()
                date = q if q.isdigit() else '0'
            out.append((int(date), len(out), vid, title, kind))
    out.sort(key=lambda x: (-x[0], x[1]))          # newest first; the channel's own order for equal dates
    return [(v, t, k) for _, _, v, t, k in out]

def fetch(url):
    try:
        with urllib.request.urlopen(url, timeout=30) as r: return Image.open(io.BytesIO(r.read())).convert('RGB')
    except Exception: return None

def wrap(d, text, font, width, lines=2):
    words, rows, cur = text.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=font) <= width: cur = t
        else:
            rows.append(cur); cur = w
            if len(rows) == lines: break
    if len(rows) < lines and cur: rows.append(cur)
    if len(rows) == lines and ' '.join(rows) != ' '.join(words): rows[-1] = rows[-1].rstrip('.،,') + '…'
    return rows

def play(d, cx, cy, s=1.0):
    w, h = int(96 * s), int(68 * s)
    d.rounded_rectangle((cx - w // 2, cy - h // 2, cx + w // 2, cy + h // 2), int(18 * s), fill=(255, 0, 0))
    t = int(16 * s); d.polygon([(cx - t + 3, cy - t), (cx - t + 3, cy + t), (cx + t + 5, cy)], fill='white')

EMOJI = re.compile('[\U0001F000-\U0001FFFF\u2600-\u27BF\uFE0F\u200d]')

def square(vid, title, kind):
    title = re.sub(r'\s+', ' ', EMOJI.sub(' ', title)).strip()
    if kind == 'short':
        fr = fetch(f'https://i.ytimg.com/vi/{vid}/oar2.jpg') or fetch(f'https://i.ytimg.com/vi/{vid}/hqdefault.jpg')
        w, h = fr.size; s = min(w, h); top = max(0, (h - s) // 3)
        im = fr.crop(((w - s) // 2, top, (w - s) // 2 + s, top + s)).resize((SIZE, SIZE), Image.LANCZOS)
        d = ImageDraw.Draw(im, 'RGBA')
        d.rectangle((0, SIZE - 120, SIZE, SIZE), fill=(0, 0, 0, 150))
        f = ImageFont.truetype(FONT, 28)
        for i, row in enumerate(wrap(d, title, f, SIZE - 60)):
            d.text((SIZE // 2, SIZE - 88 + i * 40), row, font=f, fill='white', anchor='mm')
        play(d, SIZE // 2, SIZE // 2 - 40)
        d.rounded_rectangle((20, 20, 128, 58), 12, fill=(255, 0, 0, 230)); d.text((74, 39), 'Shorts', font=ImageFont.truetype(FONT, 22), fill='white', anchor='mm')
        return im
    th = None
    for q in ('maxresdefault', 'sddefault', 'hqdefault'):
        th = fetch(f'https://i.ytimg.com/vi/{vid}/{q}.jpg')
        if th and th.size[0] > 200: break
    w, h = th.size; t = h * 16 // 9
    if t < w: th = th.crop(((w - t) // 2, 0, (w - t) // 2 + t, h))          # drop the 4:3 bars of small thumbnails
    bg = th.resize((SIZE * h // h * 16 // 9, SIZE), Image.LANCZOS)
    bg = bg.crop(((bg.width - SIZE) // 2, 0, (bg.width - SIZE) // 2 + SIZE, SIZE)).resize((64, 64)).resize((SIZE, SIZE), Image.BILINEAR)
    bg = bg.filter(ImageFilter.GaussianBlur(6)).point(lambda v: int(v * 0.45))
    im = bg.copy(); d = ImageDraw.Draw(im, 'RGBA')
    tw = SIZE - 40; thh = tw * 9 // 16; ty = 70
    m = Image.new('L', (tw, thh), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, tw - 1, thh - 1), 18, fill=255)
    im.paste(th.resize((tw, thh), Image.LANCZOS), (20, ty), m)
    play(d, SIZE // 2, ty + thh // 2, 0.8)
    f = ImageFont.truetype(FONT, 30)
    rows = wrap(d, title, f, SIZE - 60, 3)
    y0 = ty + thh + 30 + (3 - len(rows)) * 22
    for i, row in enumerate(rows):
        d.text((SIZE // 2, y0 + i * 46), row, font=f, fill='white', anchor='mt')
    d.text((SIZE // 2, 32), 'YouTube · Hiddify', font=ImageFont.truetype(FONT, 22), fill=(255, 255, 255, 200), anchor='mm')
    return im

TILE = '''      <a href="{url}" target="_blank" class="post" title="{title}">
        <figure markdown="span">
          <img src="/instagram/img/yt/{vid}.webp" alt="{title}" loading="lazy" decoding="async">
        </figure>
      </a>
'''

def main():
    vids = channel()
    if not vids: sys.exit('could not list the channel (is yt-dlp installed?)')
    os.makedirs(IMG_DIR, exist_ok=True)
    for page in PAGES:
        s = open(page, encoding='utf-8').read()
        have = set(re.findall(r'(?:youtu\.be/|v=|shorts/)([A-Za-z0-9_-]{11})', s))
        new = [(v, t, k) for v, t, k in vids if v not in have]
        if not new: print(os.path.basename(page), 'up to date'); continue
        # tiles of the page, in order: (video id or None, html)
        start = s.index('<div class="grid">') + len('<div class="grid">\n')
        end = s.index('\n    </div>\n  </div>', start)
        tiles = re.findall(r'(?:[ \t]*<!--[^>]*-->\s*)?[ \t]*<a [\s\S]*?</a>\s*', s[start:end])
        tid = lambda t: (re.findall(r'(?:youtu\.be/|v=|shorts/)([A-Za-z0-9_-]{11})', t) or [None])[0]
        order = [v for v, _, _ in vids]
        out = []
        for v, t, k in vids:                                   # channel order; existing tiles keep their own html
            old = [x for x in tiles if tid(x) == v]
            if old:
                out.append(old[0].rstrip() + '\n')
                # blog posts etc. that followed this tile on the page stay right after it
                i = tiles.index(old[0]) + 1
                while i < len(tiles) and tid(tiles[i]) is None: out.append(tiles[i].rstrip() + '\n'); i += 1
            else:
                f = os.path.join(IMG_DIR, v + '.webp')
                if not os.path.exists(f): square(v, t, k).save(f, 'WEBP', quality=82, method=6)
                url = f'https://www.youtube.com/shorts/{v}' if k == 'short' else f'https://www.youtube.com/watch?v={v}'
                out.append(TILE.format(url=url, vid=v, title=html.escape(re.sub(r'\s+', ' ', t).strip(), quote=True)))
        # tiles that are neither channel videos nor placed above (e.g. a blog post at the very top)
        placed = ''.join(out)
        for x in tiles:
            if x.strip() and x.rstrip() not in placed: out.append(x.rstrip() + '\n')
        s = s[:start] + ''.join(out).rstrip('\n') + s[end:]
        open(page, 'w', encoding='utf-8').write(s)
        print(os.path.basename(page), f'+{len(new)} videos')

if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == '--sample':          # --sample <id> <kind> <title>  → /tmp/sample.png
        square(sys.argv[2], sys.argv[4], sys.argv[3]).save('/tmp/mgrshot/sq/sample-' + sys.argv[2] + '.png')
    else: main()
