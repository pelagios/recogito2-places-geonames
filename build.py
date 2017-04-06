import os
from scripts.loadNames import loadNames
from scripts.loadGeometries import loadGeometries
from scripts.loadWikidataIds import loadWikidataIds
from scripts.convertContinents import convertContinents
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
wikidata = loadWikidataIds()

print('Starting conversion...')
ctr += convertContinents(names)
ctr += convertCountries(names, shapes, wikidata)
ctr += convertAdmin1(names, shapes, wikidata)
ctr += convertCities(names, wikidata)
print('Done.')
print(str(ctr) + ' records total')
