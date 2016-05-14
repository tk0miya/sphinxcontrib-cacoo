# -*- coding: utf-8 -*-

import sys
from mock import patch
from sphinx_testing import with_app

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest


class TestSphinxcontrib(unittest.TestCase):
    @patch('sphinxcontrib.cacoo.urlopen')
    @with_app(buildername='html', srcdir="tests/examples/basic", copy_srcdir_to_tmpdir=True)
    def test_cacoo(self, app, status, warnings, urlopen):
        app.build()
        print(status.getvalue(), warnings.getvalue())

        html = (app.outdir / 'index.html').read_text()
        self.assertRegexpMatches(html, '<img alt="(_images/cacoo-.*)" src="\\1" />')
