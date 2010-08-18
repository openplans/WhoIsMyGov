New York State boundaries.
The JSON file was created like:

$ wget http://www.census.gov/geo/cob/bdy/st/st00shp/st36_d00_shp.zip
$ unzip st36_d00_shp.zip
$ ogr2ogr -s_srs "EPSG:4326" -f GeoJSON st36_d00.json st36_d00.shp

Based on http://www.census.gov/geo/www/cob/st_metadata.html
it looks like the data was already in the correct lat/lon projection 
(EPSG:4326).
