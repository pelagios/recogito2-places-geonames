import csv
import json

### Converts admin1CodesASCII.txtfile
def convertAdmin1(alternateNames, shapes):

    def convertAdmin1Row(row):
        geonamesId = row[3]
        record = {
            'type': 'FeatureCollection',
            'uri': 'http://sws.geonames.org/' + geonamesId,
            'title': row[1],
            'country_code': row[0][:row[0].index('.')]
        }

        if geonamesId in alternateNames:
            record['names'] = alternateNames[geonamesId]

        return record


    with open('data/admin1CodesASCII.txt', 'rt') as admin1, open('geonames.jsonl', 'a') as out:
        ctr = 0
        print('Converting Admin1 file')
        reader = csv.reader(admin1, delimiter='\t')
        for row in reader:
            ctr += 1
            out.write(json.dumps(convertAdmin1Row(row), ensure_ascii=False) + '\n')
        print(' - ' + str(ctr) + ' records appended to geonames.jsonl')

        admin1.close()
        out.close()

        return ctr
