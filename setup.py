#python setup.py sdist upload -r test
#python setup.py sdist upload

from setuptools import setup

# Extract version
def get_version():
    with open('surrkick/surrkick.py') as f:
        for line in f.readlines():
            if "__version__" in line:
                return line.split('"')[1]

def setup_package():

    metadata = dict(
        name='spops',
        version=get_version(),
        description='Database of population synthesis simulations of spinning black-hole binaries',
        long_description="See: `github.com/dgerosa/spops <https://github.com/dgerosa/spops>`_." ,
        classifiers=[
            'Topic :: Scientific/Engineering :: Astronomy',
            'Topic :: Scientific/Engineering :: Physics',
            'Topic :: Scientific/Engineering :: Mathematics',
            'Intended Audience :: Science/Research',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.7',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
        keywords='gravitational-wave, black-hole binary',
        url='https://github.com/dgerosa/spops',
        author='Davide Gerosa',
        author_email='dgerosa@caltech.edu',
        license='MIT',
        packages=['spops'],
        install_requires=['numpy','h5py','singleton_decorator','contexttimer'],
        include_package_data=True,
        zip_safe=False,
    )

    setup(**metadata)


if __name__ == '__main__':

    setup_package()
