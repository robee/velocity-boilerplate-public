import logging
import tornado
import tornado.template
import os
from tornado.options import define, options

import environment


# Make filepaths relative to settings.
path = lambda root,*a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))

define("port", default=8888, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
define("debug", default=False, help="debug mode")
tornado.options.parse_command_line()

MEDIA_ROOT = path(ROOT, 'static')
TEMPLATE_ROOT = path(ROOT, 'templates')

# Deployment Configuration
"""DOCUMENTATION TODO"""
class DeploymentType:
    PRODUCTION = "PRODUCTION"
    DEV = "DEV"
    SOLO = "SOLO"
    STAGING = "STAGING"
    dict = {
        SOLO: 1,
        PRODUCTION: 2,
        DEV: 3,
        STAGING: 4
    }

"""DOCUMENTATION TODO"""
if 'DEPLOYMENT_TYPE' in os.environ:
    DEPLOYMENT = os.environ['DEPLOYMENT_TYPE'].upper()
else:
    DEPLOYMENT = DeploymentType.SOLO


"""DOCUMENTATION TODO"""
settings = {}
settings['debug']                   = DEPLOYMENT != DeploymentType.PRODUCTION or options.debug 
settings['static_path']             = MEDIA_ROOT
settings['cookie_secret']           = "your-cookie-secret"
settings['xsrf_cookies']            = True
settings['template_loader']         = tornado.template.Loader(TEMPLATE_ROOT)
settings['login_url']               = '/login'
settings['database_cred']           = 'mysql://username:password@db_host_machine:port_number/database_name'
settings['kissmetrics_key']         =''
settings['kissmetrics_user_id']     =''
settings['mixpanel_token']          ='your mixpanel token'
settings['mixpanel_api_key']        ='your mixpanel_api_key'
settings['mixpanel_api_secret']     ='your mixpanel_api_secret'
settings["facebook_url"]            ='your facebook_url'
settings['facebook_api_key']        ='your facebook_api_key'
settings['facebook_secret']         ='your facebook_secret'
settings['twitter_consumer_key']    ='your twitter consumer key'
settings['twitter_consumer_secret'] ='your twitter consumer secret'
settings['google_analytics_key']    ='your google analytics key'


# if you want Session support thanks to Milan Cermak we have it
# check out sessions.py in /utils for an explanation
settings['session_age']                         =''
settings['session_regeneration_interval']       =''
settings['session_cookie_name']                 =''
settings['session_cookie_path']                 =''
settings['session_cookie_domain']               =''
settings['session_storage']                     =''



