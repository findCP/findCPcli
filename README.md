[![PyPI version](https://badge.fury.io/py/findCPcli.svg)](https://badge.fury.io/py/findCPcli) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![CI-CD](https://github.com/findCP/findCPcli/actions/workflows/main.yml/badge.svg)](https://github.com/findCP/findCPcli/actions/workflows/main.yml) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=findCP_findCPcli&metric=alert_status)](https://sonarcloud.io/dashboard?id=findCP_findCPcli) [![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg)](https://github.com/RichardLitt/standard-readme) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## findCPcli - find ChokePoint reactions in genome-scale metabolic models

```findCPcli``` is a command line python-tool for the computation of chokepoint reactions in genome-scale metabolic models. 
The main purpose of the tool is to compute chokepoints by taking into account both the topology and the dynamic information of the network. In addition to the computation of chokepoints, findCPcli can compute and remove dead-end metabolites, find essential reactions and update the flux bounds of the reactions according to the results of Flux Variability Analysis. 

findCPcli takes as input an SBML files of genome-scale models, and provides as output a spreadsheet file with the results of the chokepoint computation.

**Chokepoint reactions:** Chokepoint reactions are those reactions that are either the unique consumer or the only producer of a given metabolite. findCPcli makes use of the flux bounds of the model to determine consumer and producer reactions, and in turn, to compute chokepoint reactions.

**Dead-End Metabolites (DEM):** Dead-end metabolites are those metabolites that are not produced or consumed by any reaction.

**Essential Reactions:** A reaction is considered an essential reaction if its deletion, this is, restricting its flux to zero, causes the objective (e.g. cellular growth) to be zero.


_Figure:_ Chokepoint reactions and dead-end metabolites example:
![Chokepoint reactions and Dead-end metabolites example](docs/chokepoints_example.png)

The computation of chokepoints can also be exploited programmatically via the [Low Level API](#low-level-api) which is based on [COBRApy](https://github.com/opencobra/cobrapy).


## Table of Contents
- [License](#license)
- [Pseudocode](#pseudocode)
- [Install](#Install)
- [Documentation](#documentation)
- [Tool parameters](#tool-parameters)
- [Low Level API](#low-level-api)
- [Maintainers](#maintainers)
- [Contributing](#contributing)


## License

findCPcli is released under [GPLv3 license](LICENSE).


For citation purposes please refer to:

Oarga et al. **Growth Dependent Computation of Chokepoints in Metabolic Networks.** International Conference on Computational Methods in Systems Biology. Springer, Cham, 2020. https://doi.org/10.1007/978-3-030-60327-4_6


## Install
```findCPcli``` can be installed via **pip** package manager:
```shell
$ pip install findCPcli
```

## Documentation

Documentation is available at [readthedocs](https://findcpcli.readthedocs.io/en/latest/) and can also be [downloaded](https://findcpcli.readthedocs.io/_/downloads/en/latest/pdf/). 
The previous links include examples and descriptions of the operations that can be performed with the tool.

## Tool parameters

More information about the parameters of the tool can be obtained by executing ``findCPcli -h``. 
For a detailes description of the operations see the [documentation](https://findcpcli.readthedocs.io/en/latest/). 

```shell
$ findCPcli [-h] [-v] [-l] -i <input file> [-o <output file>]
                 [-cp <output file>] [-swD <output file>] [-sF <output file>]
                 [-swDF <output file>] [-objective <reaction id>]
                 [-fraction <fraction>]
                       
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
  -fraction <fraction>  Fraction of optimum growth to be used in Flux
                        Variability Analysis. Value must be beetwen 0.0 and
                        1.0
```

## Low Level API

The computation of chokepoints can also be exploited via [findCPcore](https://github.com/findCP/findCPcore) which is used by findCPcli. 
[findCPcore](https://github.com/findCP/findCPcore) documentation can be found at [readthedocs](https://findcpcore.readthedocs.io/en/latest/).

Example of network refinement and chokepoint computation:
```python
from findCPcore import CobraMetabolicModel

model = CobraMetabolicModel("aureus.xml")

# update flux bounds with FVA
model.fva(update_flux=True)

# compute chokepoints
model.find_chokepoints()

# get chokepoints
model.chokepoints()
```

## Maintainers

[@alexOarga](https://github.com/alexOarga)

## Contributing

Feel free to dive in! [Open an issue](https://github.com/findCP/findCPcli/issues/new) or submit PRs.

Standard Readme follows the [Contributor Covenant](http://contributor-covenant.org/version/1/3/0/) Code of Conduct.




