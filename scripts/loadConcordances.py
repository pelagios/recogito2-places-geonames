import csv
import gzip

concordances = {}

def loadConcordances():
    with gzip.open('data/concordances.csv.gz', 'rt') as f:
        print('Loading concordance list')
        rows = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        next(rows) # Skip header
        for row in rows:
            wikidata  = row[0]
            geonames  = row[1]
            viaf      = 'http://viaf.org/viaf/' + row[4] if len(row[4]) == 9 else False

            concordances[geonames] = [ wikidata ]

            if (viaf != False):
              concordances[geonames].append(viaf)

        f.close()
        print('Done.')
        return concordances
