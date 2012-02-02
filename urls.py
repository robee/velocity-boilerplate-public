from handlers.home import HomeHandler
from handlers.readme import ReadmeHandler
from handlers.login import *
from handlers.dbadmin import *


"""DOCUMENTATION TODO"""
url_patterns = [
    (r"/", HomeHandler),
    (r"/register", RegistrationHandler),
    (r"/account", UserAccountHandler),
    (r"/update_email", EmailUpdateHandler),
    (r"/password_reset", PasswordResetHandler ),
    (r"/login", LoginHandler),
    (r"/logout", LogoutHandler),
    (r"/readme", ReadmeHandler),
    (r"/facebook", FacebookGraphLoginHandler),
    (r"/db/create", CreateDatabaseHandler),
    (r"/db/delete", DeleteDatabaseHandler),
    (r"/db/flush", FlushDatabaseHandler),
    (r"/db/test", TestDatabaseHandler),
]
