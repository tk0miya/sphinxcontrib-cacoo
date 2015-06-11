# -*- coding: utf-8 -*-
#
# argdoc documentation build configuration file, created by
# sphinx-quickstart on Fri Dec  5 11:55:54 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import unittest
import datetime
import argdoc


# -- General configuration ------------------------------------------------

# set up substitutions file for automated crossreferences
rst_prolog = """
.. include:: /class_substitutions.txt
.. include:: /script_substitutions.txt
.. include:: /links.txt
"""

# Moving master_doc outside of index.rst allows us to keep the same sidebar
# for all pages. It also prevents circular import errors and behaves more 
# like a typical sidebar
master_doc = 'master_toctree'

# ignore package prefix when alphabetizing index
modindex_common_prefix = ["argdoc."]

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'argdoc.ext',
    #'sphinx.ext.coverage',
    #'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'numpydoc', 
    #'sphinx.ext.inheritance_diagram'
    ]



# theming, compatibility both for local and builds on readthedocs -------------

# code from http://read-the-docs.readthedocs.org/en/latest/theme.html
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


# sphinx autodoc config -------------------------------------------------------

autodoc_default_flags = [
    "show-inheritance",
    "undoc-members",
    "special-members",
    "private-members",
    "inherited-members",
]
autodoc_member_order = "bysource"

# never document these methods/attributes
exclude_always = {
    "__class__",
    "__delattr__",
    "__dict__",
    "__format__",
    "__hash__",
    "__iter__",
    "__module__",
    "__new__",
    "__reduce__",
    "__reduce_ex__",
    "__repr__",
    "__sizeof__",
    "__subclasshook__",
    "__weakref__",
    "__del__"
}

# document these only if their docstrings don't match those of their base classes
exclude_if_no_redoc_base_classes = [object]
exclude_if_no_redoc = {
    "__init__",
    "__getattribute__",
    "__setattribute__",
    "__getattr__",
    "__setattr__",
    "__getitem__",
    "__setitem__",
    "__str__",
    "next",
    "__next__",
    "close",
}


def autodoc_skip_member(app,what,name,obj,skip,options):
    """Do not generate documentation for functions/methods/classes/objects that
    either:
    
        1.  Appear above ``exclude_always``

        2.  Have an attribute called ``argdoc_skipdoc`` set to *True*
        
        3.  Have the same docstring as the method with the same name defined in 
            a base class that appears in ``exclude_if_no_redoc_base_classes``
    
    Parameters
    ----------
    app
        Sphinx application
    
    what : str
        Type of object (e.g. "module", "function", "class")
    
    name : str
        Fully-qualified name of object
    
    obj : object
        Object to skip or not
    
    skip : bool
        Whether or not Sphinx would skip this, given pre-set options
    
    options : object
        Options given to the directive, whose boolean properties are set to True
        if their corresponding flag was given in the directive
    
    
    Returns
    -------
    bool
        True if object should be skipped, False otherwise
    """
    if skip == False:
        if name in exclude_always:
            skip = True
        elif getattr(obj,"argdoc_skipdoc",False) == True:
            skip = True
        elif name in exclude_if_no_redoc:
            for cls in exclude_if_no_redoc_base_classes:
                if isinstance(obj,cls):
                    try:
                        base_doc = getattr(cls,name).__doc__
                    except AttributeError:
                        base_doc = ""
                    skip |= obj.__doc__ == base_doc
    return skip


def setup(app):
    """Activate custom event handlers for autodoc"""
    app.connect("autodoc-skip-member",autodoc_skip_member)


# intersphinx config ------------------------------------------------------------
intersphinx_mapping = { "python" : ("http://docs.python.org",None),
                        "pip"    : ("https://pip.pypa.io/en/stable",None),
                        }

# other -------------------------------------------------------------------------


# General information about the project.
project = u'argdoc'
copyright = u'2014, Joshua G. Dunn'

# Short version number, for |version|
version = str(argdoc.__version__)
# The full version, including alpha/beta/rc tags, for |release|
release = "%s-r%s" % (argdoc.__version__,str(datetime.date.today()).replace("-","_"))


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'


#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}



# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'argdoc_doc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'argdoc.tex', u'argdoc Documentation',
   u'Joshua G. Dunn', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'argdoc', u'argdoc Documentation',
     [u'Joshua G. Dunn'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'argdoc', u'argdoc Documentation',
   u'Joshua G. Dunn', 'argdoc', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

