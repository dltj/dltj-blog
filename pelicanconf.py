""" Configuration file for DLTJ blog
"""

import os
import sys

sys.path.append("./util")
import macros

AUTHOR = "Peter Murray"
SITENAME = "Disruptive Library Technology Jester"
SITEURL = "https://dltj.org"
DEFAULT_CATEGORY = "Meta Category"

PATH = "content"
STATIC_PATHS = ["assets"]
ROOT_CONTENT = "root-content"
EXTRA_PATH_METADATA = {}
static_basedir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), ROOT_CONTENT + os.sep
)
for root, dirs, files in os.walk(static_basedir):
    for file in files:
        dst_path = os.path.relpath(os.path.join(root, file), static_basedir)
        src_path = os.path.join(ROOT_CONTENT, dst_path)
        STATIC_PATHS.append(src_path)
        EXTRA_PATH_METADATA[src_path] = {"path": dst_path}


# Put articles in their own directory, see
# https://github.com/getpelican/pelican/discussions/3362#discussioncomment-9988666
FILENAME_METADATA = r"(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)"
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = "article/{slug}"
ARTICLE_SAVE_AS = "article/{slug}/index.html"

PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}/index.html"

# Top-level category and tag pages are at the index.html
# of a directory (rather than being as `categories.html` and
# `tags.html`)
CATEGORIES_URL = "category"
CATEGORIES_SAVE_AS = "category/index.html"
TAGS_URL = "tag"
TAGS_SAVE_AS = "tag/index.html"

# Actual category and tag pages are subdirectories under
# `category` and `tag` directories
CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"
TAG_URL = "tag/{slug}"
TAG_SAVE_AS = "tag/{slug}/index.html"

TIMEZONE = "US/Eastern"

DEFAULT_LANG = "en"

THEME = "pelican-hyde"
PROFILE_IMAGE = "PMurray_2016_square_98x98.webp"

# These macros are available on all content pages
JINJA_GLOBALS = {
    "image": macros.image,
    "robustlink": macros.robustlink,
    "note": macros.note,
    "thursday_threads_header": macros.thursday_threads_header,
    "thursday_threads_quote": macros.thursday_threads_quote,
    "captioned": macros.captioned,
}

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.fenced_code": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {},
        "markdown.extensions.attr_list": {},
    },
    "output_format": "html5",
}

# PLUGINS = ["jinja2content", "yaml_metadata"]
# PLUGINS = ["zygote_reader"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# BIO
BIO = "Library technologist, open source advocate, striving to think globally while acting locally"

# Menu Items
MENUITEMS = (
    ("Categories", "/category"),
    ("Tags", "/tag"),
    ("Résumé / CV", "/resume"),
)
DISPLAY_PAGES_ON_MENU = False

# Blogroll
LINKS = (
    # ("Pelican", "https://getpelican.com/"),
    # ("Python.org", "https://www.python.org/"),
    # ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    # ("You can modify those links in your config file", "#"),
)

# Social widget
FONT_ACADEMICONS = True
SOCIAL = (
    ("email", "jester@dltj.org"),
    ("mastodon", "https://code4lib.social/@dltj"),
    ("bluesky", "https://bsky.app/profile/dltj.org"),
    # ("pgp", "https://keyoxide.org/hkp/2DA08D6069D2483DE5E537F348E5203C304F1344"),
    ("github", "https://github.com/dltj"),
    ("linkedin", "https://www.linkedin.com/in/DataGazetteer"),
    ("orcid", "https://orcid.org/0000-0003-4284-508X"),
)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

LOAD_CONTENT_CACHE = False
