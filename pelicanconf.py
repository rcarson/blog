#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITENAME = 'Robert Carson'
SITEURL = ''

AUTHOR = 'Robert Carson'
AUTHOR_URL = False
AUTHOR_SAVE_AS = False
AUTHORS_URL = False
AUTHORS_SAVE_AS = False

PDF_GENERATOR = False

PAGE_PATHS = ['pages']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

CATEGORY_SAVE_AS = 'blog/{slug}/idex.html'
CATEGORY_URL = 'blog/{slug}/'

ARCHIVES_SAVE_AS = 'blog/archives/index.html'

TAG_SAVE_AS = False
TAG_URL = False

#INDEX_SAVE_AS = 'blog/index.html'

PATH = 'content'

TIMEZONE = 'America/Tijuana'

DEFAULT_LANG = 'en'

DEFAULT_DATE_FORMAT = '%A %B %d, %Y'

DEFAULT_PAGENATION = 5

DEFAULT_CATEGORY = 'Uncategorized'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/rcarson'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
