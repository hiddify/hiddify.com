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
tw:
	@npx tailwindcss -i ./input.css -o ./docs/assets/css/site.css

.PHONY: all test clean docs


idx = lunr(ref='location',fields=('title', 'text'),documents={'location':1},languages="fa",)
