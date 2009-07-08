#!/usr/bin/env python
from migrate.versioning.shell import main

main(url='postgres://pvoter:pvoter@localhost/pvoter',repository='migrations/')
