GeoJSON files containing various New York State shapes from census.gov
for import scripts to use.

Based on http://www.census.gov/geo/www/cob/st_metadata.html
it looks like the data was already in the correct lat/lon projection 
(EPSG:4326).

New York State boundaries.
=============================

The GeoJSON file st36_d00.json was created like so:

$ wget http://www.census.gov/geo/cob/bdy/st/st00shp/st36_d00_shp.zip
$ unzip st36_d00_shp.zip
$ ogr2ogr -s_srs "EPSG:4326" -f GeoJSON st36_d00.json st36_d00.shp


New York Assembly districts (2006)
========================================
I created sl36_d11.json like so:

$ wget http://www.census.gov/geo/cob/bdy/sl/sl06shp/sl36_d11_shp.zip
$ unzip sl36_d11_shp.zip
$ ogr2ogr -s_srs EPSG:4326 -f GeoJSON sl36_d11.json sl36_d11.shp

New York Senate districts (2006)
========================================
I created su36_d11.json like so:

$ wget http://www.census.gov/geo/cob/bdy/su/su06shp/su36_d11_shp.zip
$ unzip su36_d11_shp.zip
$ ogr2ogr -s_srs EPSG:4326 -f GeoJSON su36_d11.json su36_d11.shp
