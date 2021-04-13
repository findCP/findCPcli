[![PyPI version](https://badge.fury.io/py/findCPcli.svg)](https://badge.fury.io/py/findCPcli) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Build Status](https://travis-ci.org/findCP/findCPcli.svg?branch=master)](https://travis-ci.org/findCP/findCPcli) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=findCP_findCPcli&metric=alert_status)](https://sonarcloud.io/dashboard?id=findCP_findCPcli) [![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg)](https://github.com/RichardLitt/standard-readme) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## findCPcli - find ChokePoint reactions in genome-scale metabolic models

```findCPcli``` is a command line python-tool for the computation of chokepoint rections in genome-scale metabolic models. 
The main purspose is to provide a tool to compute the chokepoints of the topology of the metabolic network, as well as considering also the dynamic information of the network.

findCPcli takes as inputs SBML files of genome-scale models and  provides as output spreadsheet files with the results of the chokepoint computation. 

The computation of chokepoints can also be exploited via [findCPcore](https://github.com/findCP/findCPcore) wich is used by findCPcli. 
[findCPcore](https://github.com/findCP/findCPcore) documentation can be found at [readthedocs](https://findcpcore.readthedocs.io/en/latest/).

For citation purposes please refer to:

Oarga et al.. "Growth Dependent Computation of Chokepoints in Metabolic Networks." International Conference on Computational Methods in Systems Biology. Springer, Cham, 2020. https://doi.org/10.1007/978-3-030-60327-4_6


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
$ findCPcli [-h] [-v] [-l] -i <input file> [-o <output file>]
                 [-cp <output file>] [-swD <output file>] [-sF <output file>]
                 [-swDF <output file>]

                       
optional arguments:
  -h, --help           show this help message and exit
  -v, --verbose        Print feedback while running.
  -l, --license        View license info.
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


