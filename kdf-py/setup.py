"""pacpy setup script"""
from setuptools import setup, find_packages

setup(
    name='pykdf',
    version='1.0',
    description="kdf let's you easily share scientific data.",
    long_description = """
    `kdf` is a purposefully simplistic way to share 
    scientific data between programming languages. `kdf` starts 
    with the well supported HDF5 format but then reduces it 
    to a non-hierarchical key-array store. 
    This reduction makes it possible to create a 
    **simple and unified** lowest common demoninator data
     access API for, potentially, all programming languages.
    """,
    url='https://github.com/parenthetical-e/kdf',
    author='Erik Peterson',
    author_email='erik.exists@gmail.com',
    license='MIT',
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='science data interchange',
    packages=find_packages(),
    install_requires=['numpy>=1.8.0','scipy>=0.15.1'],
)
