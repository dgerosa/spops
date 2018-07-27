#python setup.py sdist upload -r test
#python setup.py sdist upload

from setuptools import setup
import spops


setup(
    name=spops.__name__,
    version=spops.__version__,
    description=spops.__description__,
    license=spops.__license__,
    author=spops.__author__,
    author_email=spops.__author_email__,
    url=spops.__url__,
    long_description="See: `"+spops.__url__+" <"+spops.__url__+">`_." ,
    classifiers=[
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='gravitational-wave, black-hole binary',
    packages=[spops.__name__],
    install_requires=['numpy','h5py','requests','singleton_decorator','contexttimer'],
    include_package_data=True,
    zip_safe=False,
)
