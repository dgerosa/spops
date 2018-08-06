# SPopS

Data release supporting [arXiv:XXXX.XXXXXX](https://arxiv.org/abs/arXiv:XXXX.XXXX). Here provide our database and a short python code to query it. 

#### Spin orientations of merging black holes formed from the evolution of stellar binaries
We study the expected spin misalignments of merging binary black holes formed in isolation by combining state-of-the-art population synthesis models with efficient post-Newtonian evolutions, thus tracking sources from stellar formation to gravitational-wave detection. We present extensive predictions of the properties of sources detectable by both current and future interferometers. We account for the fact that detectors are more sensitive to spinning black-hole binaries with suitable spin orientations and find that this significantly impacts the population of sources detectable by LIGO, while this is not the case for third-generation detectors. We find that three formation pathways, differentiated by the order of core collapse and common-envelope phases, dominate the observed population, and that their relative importance critically depends on the recoils imparted to black holes at birth. Our models suggest that measurements of the  "effective spin" parameter χeff will allow for powerful constraints. For instance, we find that the role of spin magnitudes and spin directions in χeff can be largely disentangled, and that the symmetry of the effective spin distribution is a robust indicator of the binary's formation history. Our predictions for individual spin directions and their precessional morphologies confirm and extend early toy models, while exploring substantially more realistic and broader sets of initial conditions.  Our main conclusion is that specific subpopulations of black-hole binaries will exhibit distinctive precessional dynamics: these classes include (but are not limited to) sources where stellar tidal interactions act on sufficiently short timescales, and massive binaries produced in pulsational pair-instability supernovae. Measurements of black-hole spin orientations have enormous potential to constrain specific evolutionary processes in the lives of massive binary stars.

### Credit

You are more than welcome to use our database in your research; we kindly ask you to cite our paper above. For questions or bugs, just ask [me](www.davidegerosa.com). Oh, and before you ask, **SPopS** means "**S**pinning black-hole binary **POP**ulation **S**ynthesis".


### Releases

[![DOI](https://zenodo.org/badge/142477838.svg)](https://zenodo.org/badge/latestdoi/142477838)
 Stable version released together with the first arxiv submission of  [arXiv:XXXX.XXXXXX](https://arxiv.org/abs/arXiv:XXXX.XXXX)

### Example

To access the effective spin distribution and the detection rates of one specific model with python:

    import spops
    db=spops.database()
    model = {"kicks":"70", "spins":"collapse", "tides":"time", "detector":"LIGO"}
    var='chieff'
    print db(model,var)  
    var='detectionrate'
    print db(model,var)

### Database

We provide a database in `h5` format containing all population sysnthesis distributions perfomed with [StarTrack](https://www.syntheticuniverse.org/) and post-processed with [precession](https://davidegerosa.com/precession/). 

The database's size is ~400MB, and can be downloaded in the [GitHub release page](https://github.com/dgerosa/spops/releases).

Data are structured in four nested groups acccording to the model options described in [arXiv:XXXX.XXXXXX](https://arxiv.org/abs/arXiv:XXXX.XXXX). These groups are:
  - **kicks**: Available options are `['0','25','50','70','130','200','265']`.
  - **spins**: Available options are `['collapse','max','uniform']`.
  - **tides**: Available options are `['time','alltides','notides']`.
  - **detector**: Available options are `['LIGO','Voyager','CosmicExplorer']`.

Each group contains the following datasets:

  - `Mzams_a`: ZAMS mass of the heavier star (solar masses).
  - `Mzams_b`: ZAMS mass of the lighter star (solar masses).
  - `M_a`: Mass of the black hole formed by the heavier ZAMS star (solar masses).
  - `M_b`: Mass of the black hole formed by the lighter ZAMS star (solar masses).
  - `met`: Metallicity.
  - `path`: Formation pathway, convention in Sec. 2D of our paper.
  - `theta_bSN1_a`: Tilt angle of the object formed by the heavier ZAMS star before the first core collapse.
  - `theta_bSN1_b`: Tilt angle of the object formed by the lighter ZAMS star before the first core collapse.
  - `phi_bSN1_a`: Azimuthal angle of the object formed by the heavier ZAMS star before the first core collapse.
  - `phi_bSN1_b`: Azimuthal angle of the object formed by the lighter ZAMS star before the first core collapse.
  - `theta_aSN1_a`: Tilt angle of the object formed by the heavier ZAMS star after the first core collapse.
  - `theta_aSN1_b`: Tilt angle of the object formed by the lighter ZAMS star after the first core collapse.
  - `phi_aSN1_a`: Azimuthal angle of the object formed by the heavier ZAMS star after the first core collapse.
  - `phi_aSN1_b`: Azimuthal angle of the object formed by the lighter ZAMS star after the first core collapse.
  - `theta_bSN2_a`: Tilt angle of the object formed by the heavier ZAMS star before the second core collapse.
  - `theta_bSN2_b`: Tilt angle of the object formed by the lighter ZAMS star before the second core collapse.
  - `phi_bSN2_a`: Azimuthal angle of the object formed by the heavier ZAMS star before the second core collapse.
  - `phi_bSN2_b`: Azimuthal angle of the object formed by the lighter ZAMS star before the second core collapse.
  - `theta_aSN2_a`: Tilt angle of the object formed by the heavier ZAMS star after the second core collapse.
  - `theta_aSN2_b`: Tilt angle of the object formed by the lighter ZAMS star after the second core collapse.
  - `phi_aSN2_a`: Azimuthal angle of the object formed by the heavier ZAMS star after the second core collapse.
  - `phi_aSN2_b`: Azimuthal angle of the object formed by the lighter ZAMS star after the second core collapse.
  - `tidealign`: boolean flag marking if the stellar spin was realigned by tides.
  - `M`: Black-hole binary total mass (solar masses).
  - `q`: Black-hole binary mass ratio.
  - `chi1`: Spin of the heavier black hole.
  - `chi2`: Spin of the lighter black hole.
  - `chieff`: Black-hole binary effective spin
  - `morph`: Spin morphology (-1: Librating about $0$, 0: Circulating, +1: Librating about $\pi$)
  - `theta1`: Tilt angle of the heavier black hole at 20 Hz.
  - `theta2`: Tilt angle of the heavier black hole at 20 Hz.
  - `deltaphi`: Difference between the azimuthal spin angles at 20 Hz.
  - `detectionrate`: Cumulative detection rate, i.e. the weight of each stellar evolution.


### Python module

We also provide a simple python module to facitate access to our database. `spops` is compatibule with both Python 2 and Python 3 and can installed from the [Python Package index](https://pypi.python.org/pypi/surrkick) using:

    pip install spops
  
To download the database you can either use the link above, or enter a python console and type:
    
    spops.download()
 
By default, this will save the database in the current location. 

The module contains a single class, called `database`. To initialize the class:

    import spops
    db = spops.database(h5filename='spops.h5',h5dir=None)

The input parameters are: 
  
  - `h5filename`: database file name, default is `spops.h5`.
  - `h5dir`: directory of the database; if `None` (default) the code will look for detabase in both the location where the `spops` module is installed (this is `os.path.dirname(os.path.abspath(spops.__file__))`) and the execution location (this is `.`).

The population sysnthesis run of interest can be specified using a python dictionary with the keys as above, so for instance
  
    model = {"kicks":"70", "spins":"collapse", "tides":"time", "detector":"LIGO"}

One can then access the datasets described above by just calling the database class:

    var='chieff'
    print(db(model,var))
  
To list the model options and the available variables use
    
    print(db.options)
    print(db.vars)
  
#### A few technical notes:
  - The `database` class is a [singleton](https://en.wikipedia.org/wiki/Singleton_pattern): only one istance can exist at any time. Multiple calls will return pointers to the same instance. This is done to prevent useless memory allocation. For instance:
    
        db1=spops.database()
        db2=spops.database()
        print(db1==db2)
    
        >>>> True
  
  - We do [lazy loading](https://en.wikipedia.org/wiki/Lazy_loading) here and only read in a dataset when/if the user asks for it.  Moreover, `spops` remembers which dataset have already been loaded, such that each subsequent access is read in from memory, not disk. So for instance:

        from contexttimer import timer
        @timer()
        def read_from_spops(model,var):
            return db(model,var)
        var='Mzams_a'
        read_from_spops(model,var)
        read_from_spops(model,var)
        
        >>>> function read_from_spops execution time: 0.002 
        >>>> function read_from_spops execution time: 0.000 
 
