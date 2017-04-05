import json
import gzip

geometries = {}

# Many GeoNames GeoJSON shapes don't follow the right-hand rule - fixing this here
# def fixShapes():

def loadGeometries():
    with gzip.open('data/shapes_simplified_low.txt.gz', 'rt') as f:
        print('Loading country border shapes')
        for row in f:
            fields = row.split('\t')
            try:
                geometries[fields[0].strip()] = json.loads(fields[1].strip())
            except:
                print("Skipping line: " + row)

        f.close()
        print('Done.')
        return geometries
