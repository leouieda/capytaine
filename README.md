# Capytaine: a Python-based distribution of Nemoh

[![Travis Build Status](https://travis-ci.org/mancellin/capytaine.svg?branch=master)](https://travis-ci.org/mancellin/capytaine)
[![Appveyor Build Status](https://ci.appveyor.com/api/projects/status/github/mancellin/capytaine?branch=master&svg=true)](https://ci.appveyor.com/project/mancellin/capytaine)
[![DOI](https://zenodo.org/badge/103753001.svg)](https://zenodo.org/badge/latestdoi/103753001)

Capytaine is Python package for the simulation of the interaction between water waves and floating bodies in frequency domain.
It is built around a full rewrite of the open source Boundary Element Method (BEM) solver Nemoh for the linear potential flow wave theory.

## Installation

```bash
conda install -c mancellin capytaine
```
See [the documentation](https://ancell.in/capytaine) for more informations.

## License

Copyright (C) 2017-2019, Matthieu Ancellin

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

It is based on [Nemoh](https://lheea.ec-nantes.fr/logiciels-et-brevets/nemoh-presentation-192863.kjsp), which has been developed by Gérard Delhommeau, Aurélien Babarit et al., (École Centrale de Nantes) and is distributed under the Apache License 2.0.

It includes code from [meshmagick](https://github.com/LHEEA/meshmagick/) by François Rongère (École
Centrale de Nantes), licensed under the GNU General Public License (GPL).
