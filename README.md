# Recogito 2 Gazetteer Package: GeoNames

A gazetteer package for Recogito 2, using a subset of data from GeoNames. The package is based
on the material available through the [GeoNames Download Server](http://www.geonames.org/export/)
and uses the following source files:

* `countryInfo.txt` - countries (without geometry)
* `admin1CodesASCII.txt` - level 1 admin divisions (without geometry)
* `cities1000.txt` - cities with a population > 1000 (with point coordinates)
* `alternateNames.txt` - alternate names with language codes _(note: this file is not included
  in this repository due to filesize restrictions; the script will download it from GeoNames
  automatically)_
* `shapes_simplified_low.txt` - simplified country boundary shapes

The following data sources are used in addition to GeoNames:

* `ne_admin1_states_provinces_simplified.geojson` contains simplified geometries for admin level 1
  regions, derived from [Natural Earth](http://www.naturalearthdata.com/) (thanks to [@kgeographer](http://github.com/kgeographer) for pointing me there!)
* Based on `wikidata_geonames.csv`, the gazetteer package includes concordances between GeoNames
  and Wikidata for 87,548 records

### Releases

| Version | Date       | # of Records | Notes                                       | |
|---------|------------|--------------|---------------------------------------------|-|
|[0.1](https://github.com/pelagios/recogito2-places-geonames/releases/tag/0.1)| 2017-04-04 | 152,249      | Initial release, without Admin 1 boundaries |[geonames-20170404.jsonl.gz](https://github.com/pelagios/recogito2-places-geonames/releases/download/0.1/geonames-20170404.jsonl.gz)|

### Attribution & License

* GeoNames dump files are licensed CC-BY 3.0
* Natural Earth data is in the public domain
* Concordances between GeoNames and Wikidata were extracted from Wikidata by [Michael
  Stoner](https://github.com/michaelstoner) as part of the [PastPlace](http://www.pastplace.org/)
  Global Historical Gazetteer project
* World continent borders are from the [UCLA geoportal](http://gis.ucla.edu/geodata/dataset/continent_ln)
