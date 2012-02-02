from handlers.base import BaseHandler
from utils import markdown
from models import *
import tornado.web

import logging
logger = logging.getLogger('boilerplate.' + __name__)


class ReadmeHandler(BaseHandler):
    """DOCUMENTATION TODO"""
    
    @tornado.web.authenticated
    def get(self):
        html_readme = markdown.markdown_path("README.md")
        self.render_template("readme.html", args={'readme':html_readme})
