import json
import tornado.web

import logging
from models import *
from sqlalchemy.orm import scoped_session, sessionmaker

logger = logging.getLogger('boilerplate.' + __name__)

class BaseHandler(tornado.web.RequestHandler):
    """A class to collect common handler methods - all other handlers should
    subclass this one.
    """
    @property
    def db(self):
        """DOCUMENTATION TODO"""
        return self.application.db

    def get_current_user(self):
        """DOCUMENTATION TODO"""
        cookie_username = self.get_secure_cookie("user")
        logging.info(cookie_username)
        if not cookie_username: return None
        return get_user(self.db, username=cookie_username)
        
    def render_template(self, template, args={}):
        user = self.get_current_user()
        username = ''
        if user: username = user.username
        google_key = settings['google_analytics_key']
        mixpanel_token = settings['mixpanel_token']
        return self.render( template, 
                            message=self.get_argument('message', default=''),
                            current_user=username, 
                            google_analytics_key=google_key,
                            mixpanel_token=mixpanel_token, 
                            args=args)
        
    def get_current_user(self):
        """DOCUMENTATION TODO"""
        cookie_username = self.get_secure_cookie("user")
        if not cookie_username: return None
        return get_user(self.db, username=cookie_username)
        
    def load_json(self):
        """Load JSON from the request body and store them in
        self.request.arguments, like Tornado does by default for POSTed form
        parameters.

        If JSON cannot be decoded, raises an HTTPError with status 400.
        """
        try:
            self.request.arguments = json.loads(self.request.body)
        except ValueError:
            msg = "Could not decode JSON: %s" % self.request.body
            logger.debug(msg)
            raise tornado.web.HTTPError(400, msg)

    def get_json_argument(self, name, default=None):
        """Find and return the argument with key 'name' from JSON request data.
        Similar to Tornado's get_argument() method.
        """
        if default is None:
            default = self._ARG_DEFAULT
        if not self.request.arguments:
            self.load_json()
        if name not in self.request.arguments:
            if default is self._ARG_DEFAULT:
                msg = "Missing argument '%s'" % name
                logger.debug(msg)
                raise tornado.web.HTTPError(400, msg)
            logger.debug("Returning default argument %s, as we couldn't find "
                    "'%s' in %s" % (default, name, self.request.arguments))
            return default
        arg = self.request.arguments[name]
        logger.debug("Found '%s': %s in JSON arguments" % (name, arg))
        return arg
