"""The Hiddify channel's latest LONG videos from YouTube's public RSS feed (no API key, no yt-dlp).

The feed lists the 15 newest uploads, Shorts included. A Short answers /shorts/<id> itself (200);
a long video is redirected to /watch (303). Used by the scheduled GitHub Action (YT_SOURCE=rss),
where yt-dlp is often blocked."""
import urllib.request, urllib.error, xml.etree.ElementTree as ET

CHANNEL_ID = 'UCxrmeMvVryNfB4XL35lXQNg'   # youtube.com/@hiddify
FEED = f'https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}'
NS = {'a': 'http://www.w3.org/2005/Atom', 'yt': 'http://www.youtube.com/xml/schemas/2015'}
UA = {'User-Agent': 'Mozilla/5.0 (hiddify.com docs sync)', 'Cookie': 'CONSENT=YES+1; SOCS=CAI'}

class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k): return None

def is_short(vid):
    op = urllib.request.build_opener(_NoRedirect)
    try:
        return op.open(urllib.request.Request(f'https://www.youtube.com/shorts/{vid}', headers=UA), timeout=30).status == 200
    except urllib.error.HTTPError as e:
        return False if e.code in (301, 302, 303, 307, 308) else None

def long_videos():
    """[(id, 'YYYYMMDD', title)] newest first, long videos only."""
    root = ET.fromstring(urllib.request.urlopen(urllib.request.Request(FEED, headers=UA), timeout=30).read())
    out = []
    for e in root.findall('a:entry', NS):
        vid = e.find('yt:videoId', NS).text
        title = e.find('a:title', NS).text or ''
        date = (e.find('a:published', NS).text or '')[:10].replace('-', '')
        if is_short(vid) is False:          # unknown (None) is skipped too: better late than a Short on the page
            out.append((vid, date, title))
    return out

if __name__ == '__main__':
    for v in long_videos(): print('|'.join(v))
