# -*- coding: utf-8 -*-
import os
import re
from hashlib import sha1
from email.utils import parsedate
from time import mktime

from docutils.parsers.rst.directives.images import Image
from sphinx.directives.patches import Figure
from sphinx.transforms.post_transforms.images import ImageConverter
from sphinx.util import logging
from sphinx.util import requests
from sphinx.util.osutil import ensuredir

logger = logging.getLogger(__name__)

CACOO_BASEURI = 'https://cacoo.com/diagrams/'


def cacoo_url_to_diagramid(url):
    return re.sub('https://cacoo\.com/diagrams/', '', url)


class Cacoo(object):
    def __init__(self, apikey):
        self.apikey = apikey

    def get_image_info(self, diagramid):
        URLBASE = "https://cacoo.com/api/v1/diagrams/%s.json?apiKey=%s"
        diagramid = re.sub('[#-].*', '', diagramid)  # remove sheetid
        url = URLBASE % (diagramid, self.apikey)
        return requests.get(url).json()

    def get_last_modified(self, diagramid):
        image_info = self.get_image_info(diagramid)
        return mktime(parsedate(image_info['updated']))

    def get_image(self, diagramid):
        URLBASE = "https://cacoo.com/api/v1/diagrams/%s.png?apiKey=%s"
        diagramid = diagramid.replace('#', '-')
        url = URLBASE % (diagramid, self.apikey)
        return requests.get(url).content


class CacooImageConverter(ImageConverter):
    def match(self, node):
        return node.get('uri', '').startswith(CACOO_BASEURI)

    def handle(self, node):
        # type: (nodes.Node) -> None
        try:
            cacoo = Cacoo(self.config.cacoo_apikey)
            diagramid = cacoo_url_to_diagramid(node['uri'])
            image = cacoo.get_image(diagramid)

            ensuredir(os.path.join(self.imagedir, 'cacoo'))
            digest = sha1(image).hexdigest()

            path = os.path.join(self.imagedir, 'cacoo', digest + '.png')
            self.env.original_image_uri[path] = node['uri']

            with open(path, 'wb') as f:
                f.write(image)

            node['candidates'].pop('?')
            node['candidates']['image/png'] = path
            node['uri'] = path
            self.app.env.images.add_file(self.env.docname, path)
        except Exception:
            logger.warning('Fail to download cacoo image: %s (check your cacoo_apikey or diagramid)', node['uri'])
            return False


def setup(app):
    app.add_config_value('cacoo_apikey', None, 'html')
    app.add_post_transform(CacooImageConverter)

    # for backward compatibility
    app.add_directive('cacoo-image', Image)
    app.add_directive('cacoo-figure', Figure)
