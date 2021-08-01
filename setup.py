from setuptools import find_packages, setup
from olcommon.version import __version__

setup(
    name='multi-validator',
    packages=find_packages(),
    version=__version__,
    description='This will validate multiple data type, i.e. phone number, name, age, ',
    author='Neel Ratan Guria',
    #install_requires=['mongoengine'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
)
