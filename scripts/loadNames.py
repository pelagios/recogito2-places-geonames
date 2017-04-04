import urllib.request

###
# Downloads & unpacks the alternateNames.zip file from GeoNames (if needed)
# and parses it into a table GeoNames ID -> names/languages
###
def fetchIfNeeded():
    url = 'http://download.geonames.org/export/dump/alternateNames.zip'
    urllib.request.urlretrieve(url, 'data/alternateNames.zip')
