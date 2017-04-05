import csv
import gzip

concordances = {}

def loadWikidataIds():
    with gzip.open('data/wikidata_geonames.csv.gz', 'rt') as f:
        print('Loading GeoNames->Wikidata concordances')
        rows = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        next(rows) # Skip header
        for row in rows:
            wikidata  = row[0]
            wikipedia = row[1]
            geonames  = row[4]

            concordances[geonames] = [
                'http://www.wikidata.org/wiki/Q' + wikidata,
                wikipedia
            ]

        f.close()
        print('Done.')
        return concordances
