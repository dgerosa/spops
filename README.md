# spops

Data release supporting [arXiv:XXXX.XXXXXX](https://arxiv.org/abs/arXiv:XXXX.XXXX). Here provide our database and a short python code to query it.

#### Spin orientations of merging black holes formed from the evolution of stellar binaries
We study the expected spin misalignments of merging binary black holes formed in isolation by combining state-of-the-art population synthesis models with efficient post-Newtonian evolutions, thus tracking sources from stellar formation to gravitational-wave detection. We present extensive predictions of the properties of sources detectable by both current and future interferometers. We account for the fact that detectors are more sensitive to spinning black-hole binaries with suitable spin orientations and find that this significantly impacts the population of sources detectable by LIGO, while this is not the case for third-generation detectors. We find that three formation pathways, differentiated by the order of core collapse and common-envelope phases, dominate the observed population, and that their relative importance critically depends on the recoils imparted to black holes at birth. Our models suggest that measurements of the “effective spin” parameter χeff will allow for powerful constraints. For instance, we find that the role of spin magnitudes and spin directions in χeff can be largely disentangled, and that the symmetry of the effective spin distribution is a robust indicator of the binary’s formation history. Our predictions for individual spin directions and their precessional morphologies confirm and extend early toy models, while exploring substantially more realistic and broader sets of initial conditions. Our main conclusion is that specific subpopulations of black-hole binaries will exhibit distinctive precessional dynamics: these classes include (but are not limited to) sources where stellar tidal interactions act on sufficiently small timescales, and massive binaries produced in pair-instability supernovae. Measurements of black-hole spin orientations have enormous potential to constrain specific evolutionary processes in the lives of massive binary stars.

### Credit

You are more than welcome to use our database in your research; we kindly ask you to cite our paper above. For questions or bugs, just ask [me](www.davidegerosa.com).

### Releases

ZENODOBADGE Stable version released together with the first arxiv submission of  [arXiv:XXXX.XXXXXX](https://arxiv.org/abs/arXiv:XXXX.XXXX)

### Database

We provide a database in `h5` format containing all population sysnthesis distributions perfomed with [StarTrack](https://www.syntheticuniverse.org/) and post-processed with [precession](https://davidegerosa.com/precession/). 

The database's size is ~400MB, and can be downloaded in the GitHub release page.

Data are structured in four nested groups acccording to the model options described in [arXiv:XXXX.XXXXXX](https://arxiv.org/abs/arXiv:XXXX.XXXX). These groups are:
  - `kicks`. Available options are `['0','25','50','70','130','200','265']`
  - `spins`. Available options are `['collapse','max','uniform']`
  - `tides`. Available options are `['time','alltides','notides']`
  - `detector`. Available options are `['LIGO','Voyager','CosmicExplorer']`

Each group contains the following datasets:





### Python module

We also provide a simple python module, called `spops`, to facitate access to our database. `spops` is compatibule with both Python 2 and Python 3 and can installed from the [Python Package index](https://pypi.python.org/pypi/surrkick) using:

  pip install spops
 
