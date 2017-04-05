import csv
import os.path
import urllib.request
import zipfile

###
# Only names in these languages will be used
#
# Mostly a random, biased selection, but includes the top-ten languages by native speaker:
# https://en.wikipedia.org/wiki/List_of_languages_by_number_of_native_speakers
#
# Leave array empty to use all languages
###
languagesToInclude = [
  'zh', 'es', 'en', 'hi', 'ar', 'pt', 'bn', 'ru', 'ja', 'pa',
  'de', 'fr', 'it', 'el' #
]

alternateNames = {}

###
# Downloads & unpacks the alternateNames.zip file from GeoNames (if needed)
# and parses it into a table GeoNames ID -> names/languages
###
def fetchAndUnpackIfNeeded():
    if not os.path.isfile('data/alternateNames.zip'):
        print('Downloading alternateNames.zip from GeoNames')
        url = 'http://download.geonames.org/export/dump/alternateNames.zip'
        urllib.request.urlretrieve(url, 'data/alternateNames.zip')

    if not os.path.isfile('data/alternateNames.txt'):
        print('Unpacking')
        z = zipfile.ZipFile('data/alternateNames.zip', 'r')
        z.extractall('data')
        z.close()

def loadNames():
    fetchAndUnpackIfNeeded()

    useAllLanguages = len(languagesToInclude) == 0

    def shouldInclude(language):
        if language:
            return useAllLanguages or language in languagesToInclude
        else:
            return True # no language tag - include

    def addName(geonamesId, language, name):
        if name and shouldInclude(language):
            altName = { 'name': name }
            if language:
                altName['language'] = language

            if geonamesId in alternateNames:
                alternateNames[geonamesId].append(altName)
            else:
                alternateNames[geonamesId] = [altName]

    with open('data/alternateNames.txt') as f:
        print('Loading GeoNames alternateNames table')
        names = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
        for row in names:
            if row[2] != 'link':
                addName(row[1], row[2], row[3])

        f.close()
        print('Done.')
        return alternateNames
