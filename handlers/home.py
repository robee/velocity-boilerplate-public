from handlers.base import BaseHandler
from models import *

import logging
logger = logging.getLogger('docs.' + __name__)


class HomeHandler(BaseHandler):
    """DOCUMENTATION TODO"""
    def get(self):
        self.render_template("home.html")
