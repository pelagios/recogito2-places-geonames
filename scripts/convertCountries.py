import csv
import json

### Converts contryInfo.txt file
def convertCountries(alternateNames, shapes, wikidata):

    def convertCountriesRow(row):
        if len(row) is not 19:
            print ('Invalid countries record: ' + str(row))

        geonamesId = row[16]
        record = {
            'type': 'FeatureCollection',
            'uri': 'http://sws.geonames.org/' + geonamesId,
            'title': row[4],
            'country_code': row[0],
            'population': int(row[7])
        }

        if geonamesId in alternateNames:
            record['names'] = alternateNames[geonamesId]

        if geonamesId in shapes:
            record['features'] = [{
                'geometry': shapes[geonamesId]
            }]

        if geonamesId in wikidata:
            record['close_matches'] = wikidata[geonamesId]

        return record

    with open('data/countryInfo.txt', 'rt') as countries, open('geonames.jsonl', 'a') as out:
        ctr = 0
        print('Converting countries file')

        reader = csv.reader(filter(lambda row: row[0] != '#', countries), delimiter='\t')
        for row in reader:
            ctr += 1
            out.write(json.dumps(convertCountriesRow(row), ensure_ascii=False) + '\n')
        print(' - ' + str(ctr) + ' records appended to geonames.jsonl')

        countries.close()
        out.close()

        return ctr
