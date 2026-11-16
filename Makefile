prepare:
	pip install "mkdocs-material[imaging]==9.2.5" mkdocs-rss-plugin mkdocs-git-revision-date-localized-plugin mkdocs-git-authors-plugin   mkdocs-awesome-pages-plugin mkdocs-nav-weight nltk mkdocs-include-markdown-plugin  mkdocs-exclude
	pip install -U --force-reinstall git+https://github.com/hiddify/mkdocs-static-i18n  git+https://github.com/hiddify/mkdocs git+https://github.com/hiddify/lunr.py

	sudo apt-get install -y libcairo2-dev libfreetype6-dev libffi-dev libjpeg-dev libpng-dev libz-dev pngquant

# local dev env with uv + free-threaded python in ./venv
prepare-uv:
	uv venv --python 3.14t venv
	uv pip install --python venv/bin/python "mkdocs-material==9.2.5" pillow cairosvg mkdocs-rss-plugin mkdocs-git-revision-date-localized-plugin mkdocs-git-authors-plugin mkdocs-awesome-pages-plugin mkdocs-nav-weight nltk mkdocs-include-markdown-plugin mkdocs-exclude \
		"mkdocs-static-i18n @ git+https://github.com/hiddify/mkdocs-static-i18n" "mkdocs @ git+https://github.com/hiddify/mkdocs" "lunr @ git+https://github.com/hiddify/lunr.py"

MKDOCS := $(if $(wildcard venv/bin/mkdocs),venv/bin/mkdocs,mkdocs)

docs:
	@$(MKDOCS) serve --no-livereload

live:
	@env DEV=true GIT_PLUGINS=false $(MKDOCS) serve --dirtyreload
# the "All settings" reference of Hiddify Manager, from its code (MANAGER=path of a Hiddify-Manager checkout with submodules)
MANAGER ?= ../Hiddify-Manager
manager-settings:
	python3 scripts/sync_manager_settings.py $(MANAGER)

# merge hiddify-sing-box's docs/hiddify into docs/core (SINGBOX=path of a hiddify-sing-box checkout)
SINGBOX ?= ../hiddify-sing-box
core-docs:
	python3 scripts/sync_core_docs.py $(SINGBOX)

PY = $(if $(wildcard venv/bin/python),venv/bin/python,python3)

# The app and manager guide pages are built from data/guides/*.yml:
#   guide-pages: rebuild them; guides: add articles they do not list yet; youtube: add new channel videos
guide-pages:
	@$(PY) tools/guide_page.py

guides:
	@$(PY) tools/guide_links.py

# one spelling for Persian words written in several ways (tools/fa_spelling.py)
spelling:
	@$(PY) tools/fa_spelling.py

# Instagram-style page (docs/instagram): add every YouTube channel video that is not there yet (needs yt-dlp)
youtube: instagram
	@$(PY) tools/youtube_sections.py

instagram:
	@$(if $(wildcard venv/bin/python),venv/bin/python,python3) tools/instagram_page.py

tw:
	@npx tailwindcss -i ./input.css -o ./docs/assets/css/site.css

.PHONY: all test clean docs core-docs manager-settings instagram youtube guides guide-pages spelling


idx = lunr(ref='location',fields=('title', 'text'),documents={'location':1},languages="fa",)
