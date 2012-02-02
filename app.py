#!/usr/bin/env python

import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options
from sqlalchemy.orm import scoped_session, sessionmaker
from utils.mixpanel import Mixpanel



from models import *  # import the engine to bind
from settings import settings
from urls import url_patterns

class VelocityBoilerplate(tornado.web.Application):
    """DOCUMENTATION TODO"""
    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, **settings)
        self.db = scoped_session(sessionmaker(bind=engine))
        self.mixpanel = Mixpanel(settings['mixpanel_token'], 1, 1)
        
    def log_request(self, handler):
            """Override the original log_request to include a call to Mixpanel recording the time
            """
            if "log_function" in self.settings:
                self.settings["log_function"](handler)
                return
            if handler.get_status() < 400:
                log_method = logging.info
            elif handler.get_status() < 500:
                log_method = logging.warning
            else:
                log_method = logging.error
            request_time = 1000.0 * handler.request.request_time()
            log_method("%d %s %.2fms", handler.get_status(), handler._request_summary(), request_time)
            
            """ Use the mixpanel object in the application to send a log with the time to mixpanel"""
            self.mixpanel.track_event(
                            handler._request_summary(), 
                            properties={
                                'request_time':request_time}, 
                            )
    


def main():
    app = VelocityBoilerplate()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
