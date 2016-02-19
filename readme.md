`kdf` is a purposefully simplistic way to share scientific data between programming languages. 

`kdf` starts with the well supported HDF5 format but then reduces it to a non-hierarchical key-array store. This reduction makes it possible to create a **simple and unified** lowest common demoninator data access API for, potentially, all programming languages.

For example, in Python 

```python    
>>> import numpy as np
>>> from kdf import save_kdf, load_kdf
>>> filename = 'demo'
>>> # Make some data
>>> dog = np.ones(1000)
>>> cat = np.random.random(10)
>>> human = 0
>>> # save it
>>> save_kdf(filename, dog=dog, cat=cat, human=human)
>>> # get it back again
>>> data = load_kdf(filename)  # data is a dict of arrays
>>> print(data)
```
    
Whereas in R
    
```r
> library(kdf) 
> filename <- 'demo'
> # Make some data
> dog <- rep(1, 1000)
> cat <- rnorm(10)
> human <- 0
> # save it
> save_kdf(filename, dog=dog, cat=cat, human=human)
> # get it back again
> data <- load_kdf(filename)  # data is a dict of arrays
> print(data)
```

The supported languages are,

 - Python
 - R

TODO:

 - Matlab
 - Julia
 - C
 - C++
 - FORTRAN
 - ?

Pull requests for others are very welcome.


# More detailed aims

1. Create a very simple interface for key-array storage.
2. The function signatures and return values should be as conserved as possible, while staying well within each language's idiom. 
3. There will be two, and only two, functions for every language.      

    - `save_kdf(filename, ...)` saves data, 
    - `load_kdf(filename)` loads it.  

The data is written to a standard `.hdf5` file. Besides the limited API, the only difference between HDF5 and KDF files is that KDF files includes the key value pair, `kdf : 1` which makes is easy to tell KDF files from arbitray HDF files. That said, and by design, KDF files keep the HDF5 extension allowing them to easily read with larger universe of HDF tools. Said another way KDF is a strict subset of HDF.


# Qs

    Use compression, if possible? can detect? Have a flag?


# Examples

## Python 
    
    >>> import numpy as np
    >>> from kdf import save_kdf, load_kdf
    >>> filename = 'demo'
    >>> # Make some data
    >>> dog = np.ones(1000)
    >>> cat = np.random.random(10)
    >>> human = 0
    >>> # save it
    >>> save_kdf(filename, dog=dog, cat=cat, human=human)
    >>> # get it back again
    >>> data = load_kdf(filename)  # data is a dict of arrays
    >>> print(data)
    
## R

    > library(kdf) 
    > filename <- 'demo'
    > # Make some data
    > dog <- rep(1, 1000)
    > cat <- rnorm(10)
    > human <- 0
    > # save it
    > save_kdf(filename, dog=dog, cat=cat, human=human)
    > # get it back again
    > data <- load_kdf(filename)  # data is a dict of arrays
    > print(data)


* And matlab

    TODO

* And Julia

    TODO

