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


Production Deployment
=====================

We might eventually use mod_wsgi. For now, we run Paste under the
control of supervisord, and assume you can set up Apache or similar to
reverse-proxy it.

The source includes a supervisord.conf suitable for running the paste
server under the control of supervisord, which will restart it if it
ever crashes.  To use supervisord::

* I assume you've built in a virtualenv as described above.

* Edit supervisord.conf; in the [supervisord] section, set the
  "directory" setting to the full path of the parent directory of your
  virtualenv.

* Edit production.ini as desired.

* In the parent of the virtualenv, create an etc/ subdirectory
  and symlink both production.ini and supervisord.conf into it.

  Also create a logs/ subdirectory.


Then you can run $VIRTUALENV/bin/supervisord to start things up.

To shut down, run this:
 $VIRTUALENV/bin/supervisorctl shutdown.

To restart the paste server, run:

 $VIRTUALENV/bin/supervisorctl restart pvoter


