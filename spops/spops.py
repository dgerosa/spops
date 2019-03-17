'''
SPopS: Spinning black-hole binary Population Synthesis
Data release supporting Gerosa et al 2018 `Spin orientations of merging black holes formed from the evolution of stellar binaries'.
Data release supporting Gerosa et al 2019 `Multiband gravitational-wave event rates and stellar physics'.
See https://github.com/dgerosa/spops
'''

from __future__ import print_function
import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
import os,sys
import numpy as np
import h5py
from singleton_decorator import singleton

if __name__!="__main__":
    __name__            = "spops"
__version__             = "0.2.1"
__description__         = "Database of population synthesis simulations of spinning black-hole binaries"
__license__             = "MIT"
__author__              = "Davide Gerosa"
__author_email__        = "dgerosa@caltech.edu"
__url__                 = "https://github.com/dgerosa/spops"


@singleton
class database(object):
    ''' Access the database of black-hole binary populations by Gerosa et al. 2018.
    Usage:  db=spops.database()
            db(model,variable)
    where e.g.
        model= {'kicks':'70','tides':'time','spins':'collapse','detector':'LIGO'}
        variable = 'Mzams_a'
    '''

    def __init__(self,h5filename='spops.h5',h5dir=None):
        ''' Initialize class. Note this class is a singleton: only one istance can exist at any time. Multiple calls return pointers to the same instance.'''

        if h5dir==None:
            for trydir in ['.',os.path.dirname(os.path.abspath(__file__))]:
                self.filename = trydir+'/'+h5filename
                if os.path.isfile(h5filename):
                    break
        else:
            self.filename = h5dir+'/'+h5filename

        if not os.path.isfile(self.filename):
            raise ValueError("h5 database not found. Use spops.download(outfile=None)") # Write download message here!

        self.f = h5py.File(self.filename,'r')

        # Models available
        self.options={}
        self.options['kicks'] = sorted(['0','25','50','70','130','200','265'])
        self.options['spins'] = sorted(['collapse','max','uniform'])
        self.options['tides'] = sorted(['time','alltides','notides'])
        self.options['detector'] = sorted(['LIGO','Voyager','CosmicExplorer','LISA','LISALIGO','LISACosmicExplorer'])
        self.options['Tobs'] = sorted(['10','4'])
        self.options['SNRthr'] = sorted(['4','8'])

        # Labes available
        self.labels={}
        self.labels['ST'] = ['Mzams_a','Mzams_b','M_a','M_b','met','zmer','path']
        self.labels['PN'] = ['M','q','chi1','chi2', 'chieff','morph','theta1','theta2','deltaphi','tidealign']
        self.labels['rates'] = ['SNR','detectionrate']
        self.vars = sorted(self.labels['ST']+self.labels['PN']+self.labels['rates'],key= lambda s:s.lower())

        # Empty dictionary to store which info have been loaded already
        self.stored={}


    def freeze(self, dict):
        ''' Utility to create a dictionary key from another dictionary'''

        # See https://stackoverflow.com/questions/13264511/typeerror-unhashable-type-dict
        return frozenset(dict.items())


    def checkkeys(self,which,model):
        ''' Sanity check on the key in the `which` category provided by `model`'''
        if which not in model.keys():
            raise ValueError("Missing key, "+which)
        elif model[which] not in self.options[which]:
            raise ValueError("Available "+which+" keys are "+str(self.options[which]))


    def __call__(self,model,var):
        ''' Load data only if necessary '''

        # You're loading a ST variable
        if var in self.labels['ST']:
            # Check the necessary keys are there
            self.checkkeys('kicks',model)
            # Load only if needed
            storedict={'kicks':model['kicks'],'var':var}
            if self.freeze(storedict) not in self.stored.keys():
                loaded = self.f['ST'][model['kicks']][var]
                self.stored[self.freeze(storedict)] = np.array(loaded[:])

        # You're loading a ST variable
        elif var in self.labels['PN']:
            # Check the necessary keys are there
            self.checkkeys('kicks',model)
            self.checkkeys('spins',model)
            self.checkkeys('tides',model)
            storedict={'kicks':model['kicks'],'spins':model['spins'],'tides':model['tides'],'var':var}
            if self.freeze(storedict) not in self.stored.keys():
                loaded = self.f['PN'][model['kicks']][model['spins']][model['tides']][var]
                self.stored[self.freeze(storedict)] = np.array(loaded[:])

        # You're loading a rates variable
        elif var in self.labels['rates']:
            self.checkkeys('kicks',model)
            self.checkkeys('detector',model)

            if "LISA" not in model['detector']:
                self.checkkeys('spins',model)
                self.checkkeys('tides',model)
                storedict={'kicks':model['kicks'],'spins':model['spins'],'tides':model['tides'],'detector':model['detector'],'var':var}
                if self.freeze(storedict) not in self.stored.keys():
                    loaded = self.f['ground'][model['kicks']][model['spins']][model['tides']][model['detector']][var]
                    self.stored[self.freeze(storedict)] = np.array(loaded[:])

            else:
                self.checkkeys('Tobs',model)
                self.checkkeys('SNRthr',model)
                storedict={'kicks':model['kicks'],'Tobs':model['Tobs'],'SNRthr':model['SNRthr'],'detector':model['detector'],'var':var}
                if self.freeze(storedict) not in self.stored.keys():
                    loaded = self.f['space'][model['kicks']][model['Tobs']][model['SNRthr']][model['detector']][var]
                    self.stored[self.freeze(storedict)] = np.array(loaded[:])

        else:
            raise ValueError("Variable not available, check self.labels")

        return self.stored[self.freeze(storedict)]



if __name__ == "__main__":

    db=database()
    model = {"kicks":"70", "spins":"collapse", "tides":"time", "detector":"LIGO"}
    var='chieff'
    print(db(model,var))
    var='detectionrate'
    print(db(model,var))

    model = {"kicks":"70", "spins":"collapse", "tides":"time", "detector":"LISACosmicExplorer", "Tobs":"10", "SNRthr":"8"}
    var='q'
    print(db(model,var))
    var='detectionrate'
    print(db(model,var))

    db1=database()
    db2=database()
    print(db1==db2)

    from contexttimer import timer
    @timer()
    def read_from_spops(model,var):
        return db(model,var)
    var='Mzams_a'
    read_from_spops(model,var)
    read_from_spops(model,var)

    print(db.options)
    print(db.vars)
