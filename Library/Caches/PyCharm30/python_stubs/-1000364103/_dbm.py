# encoding: utf-8
# module _dbm
# from /System/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/lib-dynload/_dbm.so
# by generator 1.135
# no doc
# no imports

# Variables with simple values

library = 'GNU gdbm'

# functions

def open(*args, **kwargs): # real signature unknown
    """
    Return a database object.
    
      filename
        The filename to open.
      flags
        How to open the file.  "r" for reading, "w" for writing, etc.
      mode
        If creating a new file, the mode bits for the new file
        (e.g. os.O_RDWR).
    """
    pass

# classes

from .OSError import OSError

class error(OSError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

