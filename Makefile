

prepare:
	pip install "mkdocs-material[imaging]==9.2.5" mkdocs-rss-plugin mkdocs-git-revision-date-localized-plugin mkdocs-git-authors-plugin  git+https://github.com/hiddify/mkdocs-static-i18n mkdocs-awesome-pages-plugin mkdocs-nav-weight
	sudo apt-get install -y libcairo2-dev libfreetype6-dev libffi-dev libjpeg-dev libpng-dev libz-dev pngquant

docs:
	@mkdocs serve --no-livereload

.PHONY: all test clean docs

