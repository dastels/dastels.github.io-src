#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dave Astels'
SITENAME = 'The Curmudgeoclast'
SITESUBTITLE ='Thoughts, projects, and ramblings of Dave Astels'
#SITEURL = 'daveastels.com'

PATH = 'content'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Adafruit', 'http://adafruit.com'),
         ('HackSpace Magazine', 'https://hackspace.raspberrypi.org/'),
         ('Python.org', 'http://python.org/'),
         ('Pelican', 'http://getpelican.com/'),)


# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/dastels', 'fab fa-twitter-square fa-fw fa-lg'),
          ('Facebook', 'http://www.facebook.com/dastels', 'fab fa-facebook-square fa-fw fa-lg'),
          ('Linkedin', 'https://www.linkedin.com/in/dastels/', 'fab fa-linkedin fa-fw fa-lg'),
          ('Instagram', 'https://www.instagram.com/dastels', 'fab fa-instagram fa-fw fa-lg'),
          ('dastels on adafruit discord', 'http://adafru.it/discord', 'fab fa-discord fa-fw fa-lg'),
          ('BitBucket', 'http://bitbucket.org/dastels', 'fab fa-bitbucket fa-fw fa-lg'),
          ('GitHub', 'http://github.com/dastels', 'fab fa-github-square fa-fw fa-lg'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "/home/dastels/Projects/Personal/pelican-themes/voidy-bootstrap"

PLUGIN_PATHS = ['/home/dastels/Projects/Personal/pelican-plugins']
PLUGINS = ['tag_cloud']

TAG_CLOUD_STEPS = 4

DEFAULT_METADATA = {
    'status': 'draft',
}

# voidy theme settings

SIDEBAR = "sidebar.html"
CUSTOM_SIDEBAR_MIDDLES = ("sb_tagcloud.html", "sb_links.html",)
