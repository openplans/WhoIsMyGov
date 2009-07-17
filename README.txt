This file is for you to describe the purplevoter application. Typically
you would include information such as the information below:

Installation and Setup
======================

You need PostGIS installed first.

Install ``purplevoter`` using easy_install::

    easy_install purplevoter

Tweak the development.ini config file as appropriate and then setup the
application::

    paster setup-app development.ini

Then you are ready to go, except you need some data.

Data Bootstrapping
=================

You should be able to bootstrap the database by doing:

$ source bin/activate
$ python manage.py upgrade

You may need to initialize the 'pvoter' database first, I forget the exact
postgres commands for doing it right, sorry.  You'll probably also need to
grant all rights in that database to 'pvoter'.  Most of the problems I had were
due to insufficient privileges on that user.

Data Migrations
===============

When adding new data, 
You'll want to look up the docs for SQLAlchemy-migrate.  If you need to add to
the database, the nice thing to do is add a script to migrations/ by
using the manage script as per those docs.  You can steal ideas how to get
things done by looking at existing scripts. Maybe bad ideas, but they've worked
so far ;-)


