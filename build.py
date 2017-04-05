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

ctr = 0

names = loadNames()
shapes = loadGeometries()

print('Starting conversion...')
ctr += convertCountries(names, shapes)
ctr += convertAdmin1(names, shapes)
ctr += convertCities(names)
print('Done.')
print(str(ctr) + ' records total')
