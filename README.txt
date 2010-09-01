====================
About WhoIsMyGov
====================

This is the software behind http://whoismygov.org.

It provides a web UI and a web service that can be used to look up
federal, state, and (when we have the data) local elected officials
and candidates.

Installation and Setup
======================

Prerequisites
-------------

You need PostGIS (http://postgis.refractions.net/) installed first.

We recommend installing Purplevoter in a virtualenv
(http://pypi.python.org/pypi/virtualenv). 

Get the Source
---------------

You can use Git to get the source code, like so::

$ git clone git@github.com:openplans/WhoIsMyGov.git

Install
-------

Install the software; if using virtualenv, be sure to activate the
virtualenv first. Then::

$ python setup.py develop

Then you are almost ready to go, except you need some data.


Database Bootstrapping
----------------------
 
First tweak the development.ini config file as appropriate and then
setup the application.

To set up the database:

First create a postgres user named whoismygov::

$ createuser -s whoismygov

Then::

$ createdb -T template_postgis -O whoismygov -E utf8 whoismygov

If that doesn't work, eg. on ubuntu systems you may have to first
bootstrap the template_postgis database. See eg Step 4 of:
http://code.djangoproject.com/wiki/GeoDjangoUbuntuInstall

Then try the createdb command again.

Next, fix up some table ownership::

$ psql -c "alter table geometry_columns owner to whoismygov;" whoismygov
$ psql -c "alter table spatial_ref_sys owner to whoismygov;" whoismygov


Then to populate the data, first be sure you have activated your
virtualenv if using one, then::

$ paster setup-app --name=whoismygov development.ini
$ python manage.py version_control
$ python manage.py upgrade

Start the Dev Server
--------------------

Start it like any other Pylons app::

$ paster serve development.ini


Development Notes
=================

See DEVELOPMENT_NOTES.txt.


Deployment Notes
================

We might eventually use mod_wsgi. For now, we (OpenPlans) run Paste under
the control of supervisord (http://supervisord.org/), and assume you
can set up Apache or another web server to reverse-proxy it.

The source includes a supervisord.conf suitable for running the paste
server under the control of supervisord, which will restart it if it
ever crashes.  To use supervisord:

* I assume you've built in a virtualenv as described above.

* Edit supervisord.conf; in the [supervisord] section, set the
  "directory" setting to the full path of the parent directory of your
  virtualenv.

* Edit production.ini as desired.

* In the parent of the virtualenv, create an etc/ subdirectory
  and symlink both production.ini and supervisord.conf into it.

* Also create a logs/ subdirectory.


Then you can run $VIRTUALENV/bin/supervisord to start things up.

To shut down, run this::

 $VIRTUALENV/bin/supervisorctl shutdown.

To restart the paste server, run::

 $VIRTUALENV/bin/supervisorctl restart whoismygov


History
=========

Originally created by Anil Makhijani under the name PurpleVoter, it is
being developed currently by OpenPlans (http://openplans.org).

Code was initially hosted at http://bitbucket.org/anil/purplevoter and
then forked to http://bitbucket.org/slinkp/purplevoter and then
converted to Git and imported to http://github.com/openplans/WhoIsMyGov.

Much development work was done in partnership with Transportation
Alternatives (http://www.transalt.org/) for their Candidate Survey
site ( http://tacandidatesurvey.org/ ).

For more info, contact Paul Winkler (pw @ openplans.org).


How It Works
=============

See DEVELOPMENT_NOTES.txt for more info.

