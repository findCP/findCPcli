[![PyPI version](https://badge.fury.io/py/findCPcli.svg)](https://badge.fury.io/py/findCPcli) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Build Status](https://travis-ci.org/findCP/findCPcli.svg?branch=master)](https://travis-ci.org/findCP/findCPcli) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=findCP_findCPcli&metric=alert_status)](https://sonarcloud.io/dashboard?id=findCP_findCPcli) [![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg)](https://github.com/RichardLitt/standard-readme) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## findCPcli - find ChokePoint reactions in genome-scale metabolic models

```findCPcli``` is a command line python-tool for the computation of chokepoint rections in genome-scale metabolic models. 
The main purspose is to provide a tool to compute the chokepoints of the topology of the metabolic network, as well as considering also the dynamic information of the network.

findCPcli takes as inputs SBML files of genome-scale models and  provides as output spreadsheet files with the results of the chokepoint computation. 

The computation of chokepoints can also be exploited via [findCPcore](https://github.com/findCP/findCPcore) which is used by findCPcli. 
[findCPcore](https://github.com/findCP/findCPcore) documentation can be found at [readthedocs](https://findcpcore.readthedocs.io/en/latest/).

For citation purposes please refer to:

Oarga et al.. "Growth Dependent Computation of Chokepoints in Metabolic Networks." International Conference on Computational Methods in Systems Biology. Springer, Cham, 2020. https://doi.org/10.1007/978-3-030-60327-4_6


## Table of Contents
- [Install](#Install)
- [Documentation and Examples](#Documentation and Examples)
- [Tool parameters](#Tool parameters)  
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Install
```findCPcli``` can be installed via **pip**:
```
$ pip install findCPcli
```

## Documentation and Examples

**Chokepoint reactions** are those reactions that are either the unique consumer of a given metabolite or the only producer of a metabolite. 

**Dead-End Metabolites (DEM)**  are those metabolites that are not produced or consumed by any reaction.

### Compute chokepoints

findcpcli allows, from a model in SBML format, the generation of a spreadsheet with the computation of chokepoints and other points of interest of the model (such as dead-end metabolites, essential reactions and essential genes).

```sh
$ findCPcli -i model.xml -o generate_output.xls 
```

The previous command produces a spreadsheet file containing the following sheets:
 - ```model_info```: general model information.
 - ```reactions```: list of reactions of the model
- ```metabolites```: list of metabolites of the model
- ```genes```: list of genes of the model
- ```reactions_FVA```: Upper and lower flux bound of each reaction obtained with Flux Variability Analysis.
- ```metabolites_FVA```: Upper and lower flux bound of each reaction obtained with Flux Variability Analysis grouped by metabolite.
- ``` reversible_reactions ```:  List of reversible reactions of the model before and after FVA refinement.
- ```chokepoints```: Chokepoint reactions and the metabolite/s they produce/consume. Chokepoints are computed in 4 different models:
  1. Input model
  2. Model without DEM.
  3. Model refined with FVA.
  4. Model refined with FVA and without DEM.
- ``` dead-end ```:  Dead-end metabolites before and after FVA refinement.
- ``` essential genes ```: List of essential genes of the model. Essential genes are computed in the 4 previously listed models.
- ``` essential reactions ```: List of essential reactions of the model. Essential reactions are computed in the 4 previously listed models.
- ``` comparison ```: Comparison of chokepoint, essential reactions and essential gene reactions in the 4 previously listed models.
- ``` summary ```:  Comparison the size of the previous sets and their intersections.


### Compute growth dependent chokepoints

findcpcli allows, from a model in SBML format, to calculate how refining the model with different values of the fraction of the optimum with FVA affects the number of chokepoints
(i.e. [Growth Dependant Chokepoints](https://doi.org/10.1007/978-3-030-60327-4_6)).
, reversible and non reversible reactions and dead reactions (i.e. reactions with upper and lower bound equal to 0).
The tool produces a spreadsheet file showing how the size of this set varies.

```sh
$ findCPcli -i model.xml -cp generate_output.xls 
```

### Remove Dead-End Metabolites

The following command exports a new generated model withoud Dead-End Metabolites from an input SBML model.

```sh
$ findCPcli -i model.xml -swD new_model.xml
```

### Refine model with FVA
findcpcli can generate a new model in which the flux bounds of the reactions have been updated with the values obtained in the computation of FVA . 
In this way the model can receive a different topology and the number of chokepoints, essential reactions or dead reactions, among others, can vary.


```sh
$ findCPcli -i model.xml -sF new_model.xml
```

Alternatively a new model can be generated refined with FVA and with DEMs removed after.

```sh
$ findCPcli -i model.xml -swDF new_model.xml
```

## Tool parameters
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

findCPcli is released under [GPLv3 license](LICENSE).


