from handlers.base import BaseHandler
from models import *
from utils import hasher
import simplejson as json
import tornado.escape
import tornado.auth

import logging
logger = logging.getLogger('docs.' + __name__)


class LoginHandler(BaseHandler):
    
    
    def get(self):
        """DOCUMENTATION TODO"""
        if self.get_current_user():
            self.redirect('/')
        else:
            self.render_template("login.html")
        
    def post(self):
        """DOCUMENTATION TODO"""
        form_password = self.get_argument("password", default='')
        form_username = self.get_argument("username", default='')
        user = get_user(self.db, username=form_username)
        
        if(user != None and user.password == pass_hash(form_password)):
            self.set_secure_cookie("user", user.username)
            self.redirect('/readme')
        else:
            msg = tornado.escape.url_escape("Username/Password is incorrect")
            self.redirect('/login?message=%s'%msg)

class LogoutHandler(BaseHandler):

    def post(self):
        """DOCUMENTATION TODO"""
        self.set_secure_cookie("user", '')
        self.redirect('/')


class UserAccountHandler(BaseHandler):

   
    def get(self):
        """DOCUMENTATION TODO"""
        email = self.get_current_user().email
        current_email = email if email != '' else 'No Current Email'
        self.render_template("account.html", args={'email':current_email})


class PasswordResetHandler(BaseHandler):

    def post(self):
        """DOCUMENTATION TODO"""
        new_password = self.get_argument("new_password", default='')
        old_password = self.get_argument("old_password", default='')
        current_user = self.get_current_user()

        if(pass_hash(old_password) == current_user.password):
            current_user.password = pass_hash(new_password)
            msg = tornado.escape.url_escape("Password has been reset")
            self.redirect('/account?message=%s'%msg)
        else:
            msg = tornado.escape.url_escape("Error: Could not reset password")
            self.redirect('/account?message=%s'%msg)


class EmailUpdateHandler(BaseHandler):

    def post(self):
        """DOCUMENTATION TODO"""
        new_email = self.get_argument("new_email", default='')
        existing_user = get_user(self.db, email=new_email)
        if existing_user != None:
            msg = tornado.escape.url_escape("Error: Email Address already in use")
            self.redirect('/account?message=%s'%msg)
        user = self.get_current_user()
        user.email = new_email
        commit(self.db, [user])
        self.redirect('/account')
        

class RegistrationHandler(BaseHandler):
    
    
    def get(self):
        """DOCUMENTATION TODO"""
        self.render_template("register.html")
    
    
    def post(self):
        """DOCUMENTATION TODO"""
        form_password = self.get_argument("password", default='')
        form_username = self.get_argument("username", default='')
        form_email = self.get_argument("email", default='')
        email_user = get_user(self.db, email=form_email)
        username_user = get_user(self.db, username=form_username)
        
        if form_password == '' or form_username == '' or form_email == '':
            msg = tornado.escape.url_escape("Please complete the form, I mean come on. :(")
            self.redirect('/register?message=%s'%msg)
        elif get_user(self.db, email=form_email):
            msg = tornado.escape.url_escape("Email Address already in use.")
            self.redirect('/register?message=%s'%msg)   
        elif get_user(self.db, username=form_username):
            msg = tornado.escape.url_escape("Username already in use.")
            self.redirect('/register?message=%s'%msg)
        else:
            user = create_user(form_username,form_email, form_password)
            commit(self.db, [user])
            self.redirect('/login')
        

class FacebookGraphLoginHandler(LoginHandler, tornado.auth.FacebookGraphMixin):
    @tornado.web.asynchronous
    def get(self):
        """DOCUMENTATION TODO"""
        if self.get_argument("code", False):
            self.get_authenticated_user(
                redirect_uri=self.settings["facebook_url"],
                client_id= self.settings["facebook_api_key"],
                client_secret= self.settings["facebook_secret"],
                code=self.get_argument("code"),
                callback=self.async_callback(self._on_login))
            return
        self.authorize_redirect(redirect_uri=self.settings["facebook_url"],
                              client_id=self.settings["facebook_api_key"],
                              extra_params={"scope": "read_stream,offline_access"})

    def _on_login(self, user):
        """{
                'picture': u'https://fbcdn-profile-a.akamaihd.net/hprofile-ak-snc4/41515_736450341_5786550_q.jpg', 
                'first_name': u'Ross', 
                'last_name': u'Robinson', 
                'name': u'Ross Robinson', 
                'locale': u'en_US', 
                'session_expires': ['5176599'], 
                'access_token': 'access TOKEN', 
                'link': u'http://www.facebook.com/mr.rossrobinson', 
                'id': u'736450341'
            }"""
        
        # Grab the username and password (access_token) from the facebook response
        username = user['name']
        password = user['access_token']
        
        # create a new user using the Facebook details
        new_user = create_user(username=username,email='', password=password, account_type='Facebook', details=json.dumps(user))
        
        commit(self.db, [new_user])
        self.set_secure_cookie("user", username)
        self.redirect('/readme')
        

