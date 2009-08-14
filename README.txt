This file is for you to describe the purplevoter application. Typically
you would include information such as the information below:

Installation and Setup
======================

You need PostGIS installed first.

Install ``purplevoter`` using easy_install::

    easy_install purplevoter

Then you are almost ready to go, except you need some data.


Database Bootstrapping
======================

First tweak the development.ini config file as appropriate and then
setup the application.

To set up the database:

First create a postgres user named pvoter. Then:

$ createdb -T template_postgis -O pvoter -E utf8 pvoter

If that doesn't work, eg. on ubuntu systems you may have to first
bootstrap the template_postgis database. See eg Step 4 of:
http://code.djangoproject.com/wiki/GeoDjangoUbuntuInstall

Then try the createdb command again.

Next, fix up some table ownership:

$ psql -c "alter table geometry_columns owner to pvoter;" pvoter
$ psql -c "alter table spatial_ref_sys owner to pvoter;" pvoter


Then to populate the data:

$ source bin/activate
$ paster setup-app development.ini
$ python manage.py version_control
$ python manage.py upgrade


Data Migrations
===============

When adding new data, or modifying existing data, you should provide
migrations so your changes can be reproduced.

You'll want to look up the docs for SQLAlchemy-migrate and learn how
to use the manage.py script and write migrations. You can steal ideas
for migrations by looking at existing scripts. Maybe bad ideas, but
they've worked so far ;-)


