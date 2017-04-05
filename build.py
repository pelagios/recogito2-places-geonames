import os
from scripts.loadNames import loadNames
from scripts.loadGeometries import loadGeometries
from scripts.convertCountries import convertCountries
from scripts.convertAdmin1 import convertAdmin1
from scripts.convertCities import convertCities

try:
    os.remove('geonames.jsonl')
except OSError:
    pass

names = loadNames()
shapes = loadGeometries()
print('Starting conversion...')
convertCountries(names, shapes)
convertAdmin1(names, shapes)
convertCities(names)
print('Done.')
