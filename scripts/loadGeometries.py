import json
import gzip

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

def loadGeometries():
    loadCountries()

    # TODO load Admin1 shapes
    
    return geometries
