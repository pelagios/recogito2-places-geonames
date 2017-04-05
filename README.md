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

### Releases

| Version | Date       | # of Records | Notes           | |
|---------|------------|--------------|-----------------|-|
|0.1      | 2017-04-04 |              | Initial release | |

### Attribution & License

GeoNames dump files are licensed CC-BY 3.0.
