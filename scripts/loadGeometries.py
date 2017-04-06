import gzip
import json

geometries = {}

def loadCountries():
    with gzip.open('data/shapes_simplified_low.txt.gz', 'rt') as f:
        print('Loading country border shapes')
        for row in f:
            fields = row.split('\t')
            try:
                geometries[fields[0].strip()] = json.loads(fields[1].strip())
            except:
                print("Skipping line: ")

        f.close()
        print('Done.')

def loadAdmin1Shapes():
    with gzip.open('data/ne_admin1_states_provinces_simplified.geojson.gz', 'rb') as f:
        print('Loading Admin 1 boundary shapes')
        fc = json.loads(f.read().decode('utf8'))
        for feature in fc['features']:
            geonamesId = int(feature['properties']['gn_id'])
            if (geonamesId > 0):
                geometry = feature['geometry']
                geometries[str(geonamesId)] = geometry

def loadGeometries():
    loadCountries()
    loadAdmin1Shapes()
    return geometries
