import h5py
import os
import numpy as np


def save_kdf(filename, **kwds):
    """Save several arrays into a single HDF5 filename.

    Parameters
    ----------
    filename : str or filename
        The filename name (string) where the data will be saved. 
    kwds : Keyword arguments, optional
        Key-array[-like] pairs 
        (e.g. a=np.asarray([1,2,3]), b=10, c=['i', 'd'))

    Returns
    -------
    None
    """
    filename = str(filename)
    if not filename.endswith(('.hdf5', '.h5', '.he5')):
        filename += '.hdf5'

    # Overwrite without warning
    if os.path.isfilename(filename):
        os.remove(filename)

    fi = h5py.File(filename, 'w')

    for k, v in kwds.items():
        path = "/{}".format(k)
        fi.create_dataset(path, data=v)
    
    f.create_dataset('kdf', data=1)
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

