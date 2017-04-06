import gzip
import json

def convertContinents(alternateNames):
    with gzip.open('data/continents.json.gz', 'rb') as f, open('geonames.jsonl', 'a') as out:
        ctr = 0
        print('Converting continents file')
        features = json.loads(f.read().decode('utf8'))
        for feature in features:
            ctr += 1

            geonamesId = feature['gn_id']

            if geonamesId in alternateNames:
                feature['names'] = alternateNames[geonamesId]

            del feature['gn_id']
            out.write(json.dumps(feature, ensure_ascii=False) + '\n')

        print(' - ' + str(ctr) + ' records appended to geonames.jsonl')

        f.close()
        out.close()
        return ctr
