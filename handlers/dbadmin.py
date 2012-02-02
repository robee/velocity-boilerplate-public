from handlers.base import BaseHandler
from utils import markdown
from models import *
import tornado.web

import logging
logger = logging.getLogger('boilerplate.' + __name__)


class CreateDatabaseHandler(BaseHandler):
    """DOCUMENTATION TODO"""
    
    def get(self):
        
        """Defined in Models - creates all the models in the database """
        create_all()
        
        admin = create_user( username    = 'admin', 
                            email       = 'admin@tornadoboilerplate.com',
                            password    = 'adminpass'
                          )
        guest = create_user( username    = 'guest', 
                            email       = 'guest@tornadoboilerplate.com',
                            password    = 'guestpass'
                          )
        commit(self.db, [admin, guest])
        self.render_template("dbadmin.html", args={'users':[], 'operation':"Create Database"})


class DeleteDatabaseHandler(BaseHandler):
    """DOCUMENTATION TODO"""

    def get(self):
        drop_all()
        self.render_template("dbadmin.html", args={'users':[], 'operation':"Delete Database"})

class FlushDatabaseHandler(BaseHandler):
    """DOCUMENTATION TODO"""

    def get(self):
        drop_all()
        create_all()
        self.render_template("dbadmin.html", args={'users':[], 'operation':"Flush Database"})

class TestDatabaseHandler(BaseHandler):
    """DOCUMENTATION TODO"""

    def get(self):
        admin = get_user(self.db, username='admin')
        guest = get_user(self.db, username='guest')
        
        admin.email = admin.email + 'X'
        guest.email = guest.email + 'X'
        
        commit(self.db, [admin, guest])
        
        self.render_template("dbadmin.html", args={'operation':"Test Database", 'users':[admin, guest]})

