import csv
import json

### Converts admin1CodesASCII.txtfile
def convertAdmin1():

    def convertAdmin1Row(row):
        geonamesId = row[3]
        json = {
            'type': 'FeatureCollection',
            'uri': 'http://sws.geonames.org/' + geonamesId,
            'title': row[1],
            'country_code': row[0][:row[0].index('.')]
        }

        # if geonamesId in alternateNames:
        #    json['names'] = alternateNames[geonamesId]

        return json


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
