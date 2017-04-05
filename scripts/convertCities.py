import csv
import gzip
import json

### Converts cities TSV file
def convertCities(alternateNames, wikidata):

    def convertCitiesRow(row):
        if len(row) is not 19:
            print ('Invalid cities record: ' + str(row))
        else:
            geonamesId = row[0]
            lat = float(row[4])
            lon = float(row[5])

            if row[0] in alternateNames:
                names = alternateNames[row[0]]
            else:
                namesFromCSV = filter(None, [ x.strip() for x in row[3].split(',') ])
                names = [ { 'name': n } for n in namesFromCSV ]

            record = {
                'type': 'FeatureCollection',
                'uri': 'http://sws.geonames.org/' + geonamesId,
                'title': row[1],
                'names': names,
                'features': [{ 'geometry': { 'type': 'Point', 'coordinates': [ lon, lat ] } }],
                'reprPoint': [ lon, lat ],
                'country_code': row[8],
                'population': int(row[14]),
                'last_changed_at': row[18]
            }

            if geonamesId in wikidata:
                record['close_matches'] = wikidata[geonamesId]

            return record

    with gzip.open('data/cities1000.txt.gz', 'rt') as cities, open('geonames.jsonl', 'a') as out:
        ctr = 0
        print('Converting cities file')
        reader = csv.reader(cities, delimiter='\t', quoting=csv.QUOTE_NONE)
        for row in reader:
            ctr += 1
            out.write(json.dumps(convertCitiesRow(row), ensure_ascii=False) + '\n')
        print(' - ' + str(ctr) + ' records appended to geonames.jsonl')

        cities.close()
        out.close()

        return ctr
