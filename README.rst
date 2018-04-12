sphinxcontrib-cacoo
====================
This Sphinx extension allows you to embed diagrams on cacoo_ into your document::

  .. image:: https://cacoo.com/diagrams/EWHRuF5Kox1AnyNL

  .. figure:: https://cacoo.com/diagrams/EWHRuF5Kox1AnyNL

     caption of figure

.. _cacoo: https://cacoo.com/

Setting
=======

Install
-------

::

   $ pip install sphinxcontrib-cacoo


Configure Sphinx
----------------

Add ``sphinxcontrib.cacoo`` to ``extensions`` at `conf.py`::

   extensions += ['sphinxcontrib.cacoo']

And set your API key to ``cacoo_apikey``::

   cacoo_apikey = 'your apikey'


Usage
=====

Please give an URL of caoo diagrams to image_ or figure_ directives
as an argument::

  .. image:: https://cacoo.com/diagrams/EWHRuF5Kox1AnyNL

  .. figure:: https://cacoo.com/diagrams/EWHRuF5Kox1AnyNL

     caption of figure

.. _image: http://docutils.sourceforge.net/docs/ref/rst/directives.html#image
.. _figure: http://docutils.sourceforge.net/docs/ref/rst/directives.html#figure

Directives
==========

For backward compatibility, this extension provides following two dirctives.

`.. cacoo-image:: [URL]`

  This directive insert a diagram into the document.
  If your diagram has multiple sheets, specify sheetid after ``#``.

  Examples::

    .. cacoo-image:: https://cacoo.com/diagrams/EWHRuF5Kox1AnyNL

    .. cacoo-image:: https://cacoo.com/diagrams/mb53vvmYG38QGUPf#37D74

  Options are same as `image directive`_ .

`.. cacoo-figure:: [URL]`

  This directive insert a diagram and its caption into the document.

  Examples::

    .. cacoo-figure:: https://cacoo.com/diagrams/EWHRuF5Kox1AnyNL

       Structure of this system

  Options are same as `figure directive`_ .

.. _image directive: http://docutils.sourceforge.net/docs/ref/rst/directives.html#image
.. _figure directive: http://docutils.sourceforge.net/docs/ref/rst/directives.html#figure

Configuration Options
======================

**cacoo_apikey**

  The API key for cacoo_ 


Repository
==========

https://github.com/tk0miya/sphinxcontrib-cacoo
