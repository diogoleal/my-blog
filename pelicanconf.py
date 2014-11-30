#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Diogo Leal'
AUTHOR_EMAIL = u'diogo@diogoleal.com'
SITENAME = u'Diogo Leal'
SITEURL = u'http://diogoleal.github.io'

PATH = u'content'
TIMEZONE = u'America/Sao_Paulo'
DEFAULT_LANG = u'pt'

FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DISQUS_SITENAME = u'diogoleal'
#DISQUS_DISPLAY_COUNTS = True

TWITTER_USERNAME = u'diogoleal'

LINKS = (('Nostalgia Games', 'http://ngcast.com.br/'),)

USE_PAGER = True
DISPLAY_ARTICLE_INFO_ON_INDEX = False

SOCIAL = (
    ('github', 'https://github.com/diogoleal/'),
    ('twitter', 'https://twitter.com/diogoleal'),
    ('google+', 'https://plus.google.com/+DiogoLealAndrade/posts'),
    ('linkedin', 'https://www.linkedin.com/in/diogoleal'),
    ('reddit', 'https://www.reddit.com/user/diogoleal/'),
#    ('rss', 'feeds/all.atom.xml'),
    )

THEME='pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
TAG_CLOUD_STEPS = 8
TAG_CLOUD_MAX_ITEMS = 15
DISPLAY_CATEGORIES_ON_SIDEBAR = False

ADDTHIS_PROFILE = 'ra-545fa8ff1081873a'

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['./plugins']

PLUGINS = [
        'summary',
        'feed_summary',
        'gravatar',
        'pelican_youtube',
        'pelican_vimeo',
        'sitemap',
    ]


SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

RELATIVE_URLS = True
