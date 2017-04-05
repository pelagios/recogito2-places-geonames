import os.path
import urllib.request
import zipfile

###
# Downloads & unpacks the alternateNames.zip file from GeoNames (if needed)
# and parses it into a table GeoNames ID -> names/languages
###
def fetchAndUnpackIfNeeded():
    if not os.path.isfile('data/alternateNames.zip'):
        print('Downloading alternatNames.zip from GeoNames')
        url = 'http://download.geonames.org/export/dump/alternateNames.zip'
        urllib.request.urlretrieve(url, 'data/alternateNames.zip')

    if not os.path.isfile('data/alternateNames.txt'):
        print('Unpacking')
        z = zipfile.ZipFile('data/alternateNames.zip', 'r')
        z.extractall('data')
        z.close()

def loadNames():
    fetchAndUnpackIfNeeded()
