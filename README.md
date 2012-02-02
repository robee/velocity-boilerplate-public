Velocity-Boilerplate -- jumpstart webdev
===============================================================================

## Description


## Setup Instructions


    1. Install python
    2. install virtualenv
    3. Create a virtualenv called yourapp and put it in your /envs directory (virtualenv --no-site-packages foobar)
    4. Activate the virtualenv you just created
    5. pip install mysql-python
    6. pip install SQLAlchemy
    7. pip install nginx
    8. pip install simplejson
    9. pip install tornado
    
    (Assumes you already have a MySQL database somewhere)


## Integrations

### Server Side

[Tornado 2.2](http://www.tornadoweb.org/)

MySQL

python-mysql

SQLAlchemy

Kissmetrics (src: [Greplin](http://github.com/greplin))

Mixpanel (src: [Greplin](http://github.com/greplin))

Stripe (src: [Greplin](http://github.com/greplin))

Python-Markdown (src: [trentm](https://github.com/trentm/python-markdown2))

Tornado-sessions (src: [Milan Cermak](mailto:milan.cermak@gmail.com))

simplejson

### Client Side

Twitter Boostrap

Zocial CSS3 Buttons

HTML5 Boilerplate (this may be removed for redundancy)

JQuery

Modernizer

Mixpanel Analytics

Google Analytics


## Directory Structure

    velocity-boilerplate/
        app.py
        environment.py
        fabfile.py
        models.py
        settings.py
        urls.py
        documents/
            home.md
        handlers/
            base.py
            dbadmin.py
            home.py
            login.py
            readme.py
        requirements/
            common.txt
            dev.txt
            production.txt
        logconfig/
            dictconfig.py
            logconfig.py
        static/
            404.html
            apple-touch*.png
            crossdomain.xml
            favicon.ico
            humans.txt
            robots.txt
            boostrap/
                css/
                img/
                js/
            build/
            css/
            js/
            img/
            type/
        templates/
            base.html
            account.html
            dbadmin.html
            home.html
            login.html
            readme.html
            register.html


### app.py
The main Tornado application, and also a runnable file that starts the Tornado 
server.

DOCUMENTATION TODO

### environment.py

DOCUMENTATION TODO

### fabfile.py

We use [Fabric](http://fabfile.org/) to deploy to remote servers in development,
staging and production environments. The boilerplate Fabfile is quite thin, as
most of the commands are imported from [buedafab](https://github.com/bueda/ops),
a collection of our Fabric utilities.


### models.py
A place to store the SQLAlchemy models.

DOCUMENTATION TODO

### settings.py
A place to collect application settings ala Django. There's undoubtedly a better
way to do this, considering all of the flak Django is taking lately for this
global configuration. For now, it works.


### urls.py

DOCUMENTATION TODO

### documents/
    
DOCUMENTATION TODO
    
#### home.md

DOCUMENTATION TODO

### handlers/
All of your Tornado RequestHandlers go in this directory.

Everything in this directory is added to the `PYTHONPATH` when the
`environment.py` file is imported.

#### base.py

DOCUMENTATION TODO

#### dbadmin.py

DOCUMENTATION TODO

#### home.py

DOCUMENTATION TODO

#### login.py

DOCUMENTATION TODO

#### readme.py

DOCUMENTATION TODO

### requirements/

pip requirements files, optionally one for each app environment. The
`common.txt` is installed in every case.

Our Fabfile (see below) installs the project's dependencies from these files.
It's an attempt to standardize the location for dependencies like Rails'
`Gemfile`. We also specifically avoid listing the dependencies in the README of
the project, since a list there isn't checked programmatically or ever actually
installed, so it tends to quickly become out of date.


#### common.txt

DOCUMENTATION TODO

#### dev.txt

DOCUMENTATION TODO

#### production.txt

DOCUMENTATION TODO

### logconfig/
An extended version of the
[log_settings](https://github.com/jbalogh/zamboni/blob/master/log_settings.py)
module from Mozilla's [zamboni](https://github.com/jbalogh/zamboni).

This package includes an `initialize_logging` method meant to be called from the
project's `settings.py` that sets Python's logging system. The default for
server deployments is to log to syslog, and the default for solo development is
simply to log to the console. 

All of your loggers should be children of your app's root logger (defined in
`settings.py`). This works well at the top of every file that needs logging:

    import logging
    logger = logging.getLogger('five.' + __name__)



#### dictconfig.py

DOCUMENTATION TODO

#### logconfig.py

DOCUMENTATION TODO

### static/

DOCUMENTATION TODO

### templates/

DOCUMENTATION TODO

#### base.html

DOCUMENTATION TODO

#### *.html

DOCUMENTATION TODO

#### TODO


- Documentation
- Unit tests
- Integrate S3 storage 
- automate deployment
- some form validation or WTForms
- integrate survey monkey
- integrate Database cacheing ( memcached or redis?)
- Celery integration
- set up unit testing and integrate with automation
- continuous deployment integration
- document system - fix the readme


### Related Projects

[buedafab](https://github.com/bueda/ops)
[django-boilerplate](https://github.com/bueda/django-boilerplate)
[python-webapp-etc](https://github.com/bueda/python-webapp-etc)
[comrade](https://github.com/bueda/django-comrade)

## Acknowledgements

The is is a fork of the [buedafab](https://github.com/bueda) [tornado-boilerplate](https://github.com/bueda/tornado-boilerplate) project and
the majority of the code written here is from them


## Contributing

If you have improvements or bug fixes:

* Fork the repository on GitHub
* File an issue for the bug fix/feature request in GitHub
* Create a topic branch
* Push your modifications to that branch
* Send a pull request

## Authors
* Ross Robinson (http://www.rossrobinson.org)