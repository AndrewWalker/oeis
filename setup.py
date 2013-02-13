from setuptools import setup, find_packages
from oeis import __version__

setup(
    name = "oeis",
    description = "Access to the Online Encylopedia of Integer Sequences",
    version = "0.1",
    author = "Andrew Walker",
    author_email = "walker.ab@gmail.com",
    packages = find_packages(),
    url = "https://github.com/AndrewWalker/oeis.git",
    install_requires = [ 'requests' ],
    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: BSD License',
        'Topic :: Scientific/Engineering :: Mathematics',
    ]
)
