#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"100Shapes"
SITENAME = u"100shapes.com"
SITEURL = ''

PRODUCTION = False

ARTICLE_SAVE_AS = 'blog/{date:%Y}-{date:%m}-{slug}.html'
ARTICLE_URL = ARTICLE_SAVE_AS

PAGE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'

# Turn off things we don't want
AUTHOR_SAVE_AS = False
CATEGORY_SAVE_AS = False
CATEGORY_FEED_ATOM = False
# FEED_ATOM = False

ARTICLE_DIR = 'posts/'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = False

THEME = 'ohs-pelican-theme'

DIRECT_TEMPLATES = ('index', 'blog_index', 'sitemap',)
BLOG_INDEX_SAVE_AS = 'blog/index.html'
SITEMAP_SAVE_AS = 'sitemap.xml'

FILES_TO_COPY = (
	('extras/CNAME', 'CNAME'),
	('extras/README.md', 'README.md'),
)
STATIC_PATHS = ('assets',)

# PLUGIN_PATH = "/Users/michele/Projects/100shapes.com/plugins"

PLUGINS = ('ohs_plugins.gravatar_plus', 'ohs_plugins.related_posts')

ASSET_URL = '/static/assets'


DELETE_OUTPUT_DIRECTORY = False

WEBASSETS = True
