#!/usr/bin/env python3
"""Keep data/guides/versions.yml at the latest STABLE release of Hiddify Manager and the Hiddify app.

tools/guide_page.py compares each video's (and article's) version with these: when the major version
goes up, older ones get the "Earlier version" badge by themselves. Run daily by .github/workflows/
youtube-sync.yml (through tools/youtube_sections.py). Without network the file stays as it is.
"""
import json, os, re, urllib.request, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE = os.path.join(ROOT, "data", "guides", "versions.yml")
REPOS = {"manager": "hiddify/Hiddify-Manager", "app": "hiddify/hiddify-app"}


def load():
    import yaml
    if os.path.exists(FILE):
        return yaml.safe_load(open(FILE, encoding="utf-8")) or {}
    return {}


def latest(repo):
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}/releases/latest",
                                 headers={"Accept": "application/vnd.github+json", "User-Agent": "hiddify-docs"})
    tok = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if tok:
        req.add_header("Authorization", f"Bearer {tok}")
    tag = json.load(urllib.request.urlopen(req, timeout=30))["tag_name"]
    return re.sub(r"^v", "", tag)


def update():
    cur = load(); new = dict(cur)
    for key, repo in REPOS.items():
        try:
            new[key] = latest(repo)
        except Exception as e:  # keep the old value
            print(f"versions: {key}: {e}")
    if new != cur:
        lines = ["# Latest stable releases; written by tools/versions.py. Used for the 'Earlier version' badges.",
                 *(f'{k}: "{new[k]}"' for k in REPOS if k in new),
                 f'checked: "{datetime.date.today()}"']
        open(FILE, "w", encoding="utf-8").write("\n".join(lines) + "\n")
        print("versions:", {k: new.get(k) for k in REPOS})
    return new


def major(v):
    m = re.match(r"\d+", str(v))
    return int(m.group()) if m else 0


if __name__ == "__main__":
    update()
