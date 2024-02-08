

prepare:
	apt-get install -y libcairo2-dev libfreetype6-dev libffi-dev libjpeg-dev libpng-dev libz-dev pngquant
	pip install "mkdocs-material[imaging]==9.*" mkdocs-rss-plugin mkdocs-git-revision-date-localized-plugin mkdocs-git-authors-plugin  mkdocs-static-i18n=="1.2.*"

docs:
	mkdocs serve