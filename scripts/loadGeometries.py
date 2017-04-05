import json
import shapely
from shapely.geometry import mapping, shape
import gzip

geometries = {}

def loadGeometries():
    with gzip.open('data/shapes_simplified_low.txt.gz', 'rt') as f:
        print('Loading country border shapes')

        # Skip header
        it = iter(f)
        next(it)

        for row in it:
            fields = row.split('\t')
            try:
                geometries[fields[0].strip()] = json.loads(fields[1].strip())
            except:
                print("Skipping line: ")

        f.close()
        print('Done.')
        return geometries
