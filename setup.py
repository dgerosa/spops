#python setup.py sdist upload -r test
#python setup.py sdist upload

from setuptools import setup

def get_meta(metaname):
    with open('spops/spops.py') as f:
        for line in f.readlines():
            if "__"+metaname+"__" in line and "__main__" not in line:
                return line.split('"')[1]

setup(
    name=get_meta('name'),
    version=get_meta('version'),
    description=get_meta('description'),
    license=get_meta('license'),
    author=get_meta('author'),
    author_email=get_meta('author_email'),
    url=get_meta('url'),
    long_description="See: `"+get_meta('url')+" <"+get_meta('url')+">`_." ,
    classifiers=[
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='gravitational-wave, black-hole binary',
    packages=[get_meta('name')],
    install_requires=['numpy','h5py','requests','singleton_decorator','contexttimer'],
    include_package_data=True,
    zip_safe=False,
)
