# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'BeProudガイド'
copyright = '2024, BeProud members'
author = 'BeProud members'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_revealjs",
    "myst_parser",
    "sphinxext.opengraph",
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

html_logo = "_static/logo.png"

html_theme_options = {
    "source_repository": "https://github.com/beproud/beproud-guide/",
    "source_branch": "master",
    "source_directory": "",
}

# sphinxext-opengraph
# ogp_site_url = "https://guide.beproud.jp/"
ogp_site_url = "https://beproud-guide.readthedocs.io/"

ogp_social_cards = {
    "enable": True,
    "image": "_static/logo.png",
    "font": "Noto Sans CJK JP",
}

# macOSとWindows用のフォント設定
if sys.platform == "darwin":
    ogp_social_cards["font"] = "Hiragino Maru Gothic Pro"
elif sys.platform == "win32":
    ogp_social_cards["font"] = "MS Gothic"


# -- for revealjs --------
# https://github.com/attakei/sphinx-revealjs/blob/master/demo/revealjs4/conf.py
revealjs_style_theme = "white"
revealjs_script_conf = {
    "controls": True,
    "progress": False,
    "history": True,
    "center": True,
    "transition": "none",
}

revealjs_script_plugins = [
    {
        "name": "RevealNotes",
        "src": "revealjs/plugin/notes/notes.js",
    },
    {
        "name": "RevealHighlight",
        "src": "revealjs/plugin/highlight/highlight.js",
    },
]

revealjs_static_path = html_static_path

revealjs_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.10.0/styles/github.min.css",
    'slides.css',
]
