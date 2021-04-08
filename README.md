# findCPcli

[![PyPI version](https://badge.fury.io/py/findCPcli.svg)](https://badge.fury.io/py/findCPcli) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Build Status](https://travis-ci.org/findCP/findCPcli.svg?branch=master)](https://travis-ci.org/findCP/findCPcli) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=findCP_findCPcli&metric=alert_status)](https://sonarcloud.io/dashboard?id=findCP_findCPcli) [![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg)](https://github.com/RichardLitt/standard-readme) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Source
## Table of Contents
- [Install](#Install)
- [Run](#Run)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Install
```
$ pip install findCPcli
```

## Run
```sh
$ findCPcli [-h] [-v] -i <input file> [-o <output file>]
                 [-cp <output file>] [-swD <output file>] [-sF <output file>]
                 [-swDF <output file>]

                       
optional arguments:
  -h, --help           show this help message and exit
  -v, --verbose        Print feedback while running.
  -i <input file>      Input metabolic model. Allowed file formats: .xml .json
                       .yml
  -o <output file>     Output spreadsheet file with results. Allowed file
                       formats: .xls .xlsx .ods
  -cp <output file>    Output spreadsheet file with growth dependent
                       chokepoints. Allowed file formats: .xls .xlsx .ods
  -swD <output file>   Save output model without Dead End Metabolites. Allowed
                       file formats: .xml .json .yml
  -sF <output file>    Save output model with reactions bounds updated with
                       Flux Variability Analysis. Allowed file formats: .xml
                       .json .yml
  -swDF <output file>  Save output model with reactions bounds updated with
                       Flux Variability Analysis and without Dead End
                       Metabolites. Allowed file formats: .xml .json .yml
  -objective <reaction id>
                        Reaction id to be used as objective function with Flux
                        Balance Analysis
```


## Maintainers

[@alexOarga](https://github.com/alexOarga)

## Contributing

Feel free to dive in! [Open an issue](https://github.com/findCP/findCPcli/issues/new) or submit PRs.

Standard Readme follows the [Contributor Covenant](http://contributor-covenant.org/version/1/3/0/) Code of Conduct.

## License

[GPL](LICENSE) © Alex Oarga


