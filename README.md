# findCPcli

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

# Source
## Table of Contents
- [Run](#Run)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Run
```sh
$ python3 main/CLI/findCP.py [-h] [-v] -i <input file> [-o <output file>]
                 [-cp <output file>] [-swD <output file>] [-sF <output file>]
                 [-swDF <output file>]

                       
optional arguments:
  -h, --help           show this help message and exit
  -v, --verbose        Print feedback while running.
  -i <input file>      Input metabolic model. Allowed file formats: .xml .json
                       .yml
  -o <output file>     Output spreadsheet file with results. Allowed file
                       formats: .xls .xlsx .ods
  -cp <output file>    Output spreadsheet file with chokepoints sensibility
                       analysis. Allowed file formats: .xls .xlsx .ods
  -swD <output file>   Save output model without Dead End Metabolites. Allowed
                       file formats: .xml .json .yml
  -sF <output file>    Save output model with reactions bounds updated with
                       Flux Variability Analysis. Allowed file formats: .xml
                       .json .yml
  -swDF <output file>  Save output model with reactions bounds updated with
                       Flux Variability Analysis and without Dead End
                       Metabolites. Allowed file formats: .xml .json .yml
```


## Maintainers

[@alexOarga](https://github.com/alexOarga)

## Contributing

Feel free to dive in! [Open an issue](https://github.com/findCP/findCP/issues/new) or submit PRs.

Standard Readme follows the [Contributor Covenant](http://contributor-covenant.org/version/1/3/0/) Code of Conduct.

## License

[MIT](LICENSE) © Alex Oarga
