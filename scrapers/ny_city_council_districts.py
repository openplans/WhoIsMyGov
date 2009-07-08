#!/usr/bin/env python

# Also worth experimenting with if it ends up easier to load data from xml:
# shp2text --gpx nycc.shp 0 0

import subprocess

sql, stderr = subprocess.Popen(
    'shp2pgsql -a -s 9102718 nycc.shp  -g geometry districts',
    shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

# Quick-n-dirty string munging to hack the raw sql into a form that we
# can use.

for line in sql.split('\n'):
    try:
        cols, values = line.split(' VALUES ', 1)
    except ValueError:
        print line
        continue
    cols = cols.replace('"coundist","shape_leng","shape_area",',
                        'state, district_type, level_name, district_name, ')
    #print cols
    values = values.strip().lstrip('(').rstrip(');')
    values = values.split(',', 4)
    assert len(values) == 4
    geom = values[-1]
    state = 'NY'
    district_type = 'City Council'
    district_name = 'District %s' % values[0].strip("'")
    level_name = 'City'
    #print district
    values = [repr(x.strip("'").strip('"'))
              for x in [state, district_type, level_name, district_name, geom]]
    values = ', '.join(values)

    line = '%s VALUES (%s);' % (cols, values)
    print line
