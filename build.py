import os
from scripts.convertCountries import convertCountries
from scripts.convertAdmin1 import convertAdmin1
from scripts.convertCities import convertCities
from scripts.loadNames import loadNames

try:
    os.remove('geonames.jsonl')
except OSError:
    pass

names = loadNames()
print('Starting conversion...')
convertCountries(names)
convertAdmin1(names)
convertCities(names)
print('Done.')
