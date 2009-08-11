#!/usr/bin/env python

# Also worth experimenting with if it ends up easier to load data from xml:
# shp2text --gpx nycc.shp 0 0

import subprocess

sql, stderr = subprocess.Popen(
    'shp2pgsql -a -s 9102718 nybb.shp  -g geometry boroughs',
    shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

# Quick-n-dirty string munging to hack the raw sql into a form that we
# can use.

for line in sql.split('\n'):
    try:
        cols, values = line.split(' VALUES ', 1)
    except ValueError:
        print line
        continue
    cols = cols.replace('INSERT INTO "boroughs"',
                        'INSERT INTO "districts"')
    cols = cols.replace('"borocode","boroname","shape_leng","shape_area",',
                        'state, district_type, level_name, district_name, ')
    #print cols
    values = values.strip().lstrip('(').rstrip(');')
    values = values.split(',', 4)
    assert len(values) == 5
    geom = values[-1]
    
    state = 'NY'
    district_type = 'Borough'
    district_name = values[1].strip("'") #'District %s' % values[0].strip("'")
    level_name = 'City'
    #print district
    values = [repr(x.strip("'").strip('"'))
              for x in [state, district_type, level_name, district_name, geom]]
    values = ', '.join(values)

    line = '%s VALUES (%s);' % (cols, values)
    print line
