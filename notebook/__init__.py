"""The Jupyter HTML Notebook"""

import os
import signal
import tornado.log as log
import logging
# Packagers: modify this line if you store the notebook static files elsewhere
DEFAULT_STATIC_FILES_PATH = os.path.join(os.path.dirname(__file__), "static")

# Packagers: modify the next line if you store the notebook template files
# elsewhere

# Include both notebook/ and notebook/templates/.  This makes it
# possible for users to override a template with a file that inherits from that
# template.
#
# For example, if you want to override a specific block of notebook.html, you
# can create a file called notebook.html that inherits from
# templates/notebook.html, and the latter will resolve correctly to the base
# implementation.
DEFAULT_TEMPLATE_PATH_LIST = [
    os.path.dirname(__file__),
    os.path.join(os.path.dirname(__file__), "templates"),
]

def sigterm_handler(signal, frame):
    app_log = logging.getLogger('tornado.application')
    app_log.warn('Ignoring sigterm from home thread...')

del os

signal.signal(signal.SIGTERM, sigterm_handler)

from .nbextensions import install_nbextension
from ._version import version_info, __version__
