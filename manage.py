#!/usr/bin/env python
from migrate.versioning.shell import main

main(url='postgres://whoismygov:whoismygov@localhost/whoismygov',repository='migrations/')
