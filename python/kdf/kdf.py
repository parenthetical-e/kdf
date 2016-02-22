import h5py
import os
import numpy as np


def save_kdf(filename, *args, **kwds):
    """Save several arrays into a single HDF5 filename.

    Parameters
    ----------
    filename : str or filename
        The filename name (string) where the data will be saved. 
    data : dict, optional
        A data structure to write to file
    kwds : Keyword arguments, optional
        Key-array[-like] pairs 
        (e.g. a=np.asarray([1,2,3]), b=10, c=['i', 'd'))
    
    Note
    ----
    Can't provide both a dict and keywords. Only one or the 
    other is acceptable.

    Returns
    -------
    None
    """
    filename = str(filename)
    if not filename.endswith(('.hdf5', '.h5', '.he5')):
        filename += '.hdf5'

    # Overwrite without warning
    if os.path.isfile(filename):
        os.remove(filename)

    fi = h5py.File(filename, 'w')

    # Look for args
    if len(args) > 0:
        if len(kwds) > 0:
            raise ValueError("Can't provide both a dict and keys")
        if len(args) == 1:
            towrite = args[0]  # Assume arg[0] is dict-like
        else:
            raise ValueError("Can only pass one dataset.")
    # args was empty, so we're writing kwds
    else:
        towrite = kwds  

    for k, v in towrite.items():
        path = "/{}".format(k)
        fi.create_dataset(path, data=v)
    
    fi.create_dataset('kdf', data=1)
    fi.close()


def load_kdf(filename):
    """Load arrays stored with `save_kdf`.

    Note: Not for use with arbitrary HDF5 datastores.

    Parameters
    ----------
    filename : str 
        The filename (string) where the data was saved. 

    Returns
    -------
    A dict of the stored arrays. 
    """

    fi = h5py.File(filename, 'r')

    # Check for a kdf flag, and that it is 1. 
    try:
        fi['kdf']
    except:
        raise IOError("{} is not a kdf file".format(filename))
    if fi['hdf'] != 1:
        raise IOError("{} is not a kdf file".format(filename))

    # Parse the loaded into a dict, and we're done here.
    loaded = {}
    for k, v in fi.iteritems():
        if k == "kdf":
            continue

        loaded[k] = v.value

    return loaded

