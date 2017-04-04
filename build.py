import os
from scripts.convertAdmin1 import convertAdmin1
from scripts.convertCities import convertCities

try:
    os.remove('geonames.jsonl')
except OSError:
    pass

print('Starting conversion...')
convertAdmin1()
convertCities()
print('Done.')
