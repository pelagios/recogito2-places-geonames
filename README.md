# Recogito 2 Gazetteer Package: GeoNames

A gazetteer package for Recogito 2, using a subset of data from GeoNames. The package is based
on the material available through the [GeoNames Download Server](http://www.geonames.org/export/)
and uses the following source files:

* `countryInfo.txt` - countries
* `admin1CodesASCII.txt` - level 1 admin divisions
* `cities1000.txt` - cities with a population > 1000
* `alternateNames.txt` - alternate names with language codes _(note: this file is not included
  in this repository due to filesize restrictions; the script will download it from GeoNames
  automatically)_
* `shapes_simplified_low.txt` - simplified country boundaries
* The package additionally includes Wikidata links for XX,XXX records, base on the file 
  `wikidata_geonames.csv`.

### Releases

| Version | Date       | # of Records | Notes                                       | |
|---------|------------|--------------|---------------------------------------------|-|
|[0.1](https://github.com/pelagios/recogito2-places-geonames/releases/tag/0.1)| 2017-04-04 | 152,242      | Initial release, without Admin 1 boundaries |[geonames-20170404.jsonl.gz](https://github.com/pelagios/recogito2-places-geonames/releases/download/0.1/geonames-20170404.jsonl.gz)|

### Attribution & License

GeoNames dump files are licensed CC-BY 3.0.

Wikidata-GeoNames concordances were extracted from Wikidata by [Michael Stoner](https://github.com/michaelstoner)
as part of the [PastPlace](http://www.pastplace.org/) Global Historical Gazetteer project.
