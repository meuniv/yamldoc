## Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Yaml2LMS'
copyright = '2020, Vincent Meunier'
author = 'Vincent Meunier'

pygments_style = 'sphinx'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
import sphinx_rtd_theme

#extensions = [
#    ...
#    "sphinx_rtd_theme",
#]

#html_theme = "sphinx_rtd_theme"

##html_theme = 'msmb_theme'
##import msmb_theme
##html_theme_path = [msmb_theme.get_html_theme_path()]

###html_theme= 'groundwork'

#####html_theme = 'bizstyle'
#import edx_theme
#import os

##extensions = ['edx_theme']

##html_theme = 'edx_theme'
##html_theme_path = [edx_theme.get_html_theme_path()]
#html_favicon = os.path.join(html_theme_path[0], 'edx_theme', 'static', 'css', 'favicon.ico')

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import stanford_theme
    html_theme = 'stanford_theme'
    html_theme_path = [stanford_theme.get_html_theme_path()]

# otherwise, readthedocs.org uses their theme by default, so no need to specify it
import stanford_theme# on_rtd is whether we are on readthedocs.org, this line of rrtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import stanford_theme
    html_theme = 'stanford_theme'
    html_theme_path = [stanford_theme.get_html_theme_path()]

# otherwise, readthedocs.org uses their theme by default, so no need to specify itode grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import stanford_theme
    html_theme = 'stanford_theme'
    html_theme_path = [stanford_theme.get_html_theme_path()]

# otherwise, readthedocs.org uses their theme by default, so no need to specify #html_theme = "stanford_theme"
#html_theme_path = [stanford_theme.get_html_theme_path()]

