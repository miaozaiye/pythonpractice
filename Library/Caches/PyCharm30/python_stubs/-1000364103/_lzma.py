# encoding: utf-8
# module _lzma
# from /System/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/lib-dynload/_lzma.so
# by generator 1.135
# no doc
# no imports

# Variables with simple values

CHECK_CRC32 = 1
CHECK_CRC64 = 4

CHECK_ID_MAX = 15

CHECK_NONE = 0
CHECK_SHA256 = 10
CHECK_UNKNOWN = 16

FILTER_ARM = 7
FILTER_ARMTHUMB = 8
FILTER_DELTA = 3
FILTER_IA64 = 6
FILTER_LZMA1 = 4611686018427387905
FILTER_LZMA2 = 33
FILTER_POWERPC = 5
FILTER_SPARC = 9
FILTER_X86 = 4

FORMAT_ALONE = 2
FORMAT_AUTO = 0
FORMAT_RAW = 3
FORMAT_XZ = 1

MF_BT2 = 18
MF_BT3 = 19
MF_BT4 = 20
MF_HC3 = 3
MF_HC4 = 4

MODE_FAST = 1
MODE_NORMAL = 2

PRESET_DEFAULT = 6
PRESET_EXTREME = 2147483648

# functions

def is_check_supported(*args, **kwargs): # real signature unknown
    """
    Test whether the given integrity check is supported.
    
    Always returns True for CHECK_NONE and CHECK_CRC32.
    """
    pass

def _decode_filter_properties(*args, **kwargs): # real signature unknown
    """
    Return a bytes object encoding the options (properties) of the filter specified by *filter* (a dict).
    
    The result does not include the filter ID itself, only the options.
    """
    pass

def _encode_filter_properties(*args, **kwargs): # real signature unknown
    """
    Return a bytes object encoding the options (properties) of the filter specified by *filter* (a dict).
    
    The result does not include the filter ID itself, only the options.
    """
    pass

# classes

from .object import object

class LZMACompressor(object):
    """
    LZMACompressor(format=FORMAT_XZ, check=-1, preset=None, filters=None)
    
    Create a compressor object for compressing data incrementally.
    
    format specifies the container format to use for the output. This can
    be FORMAT_XZ (default), FORMAT_ALONE, or FORMAT_RAW.
    
    check specifies the integrity check to use. For FORMAT_XZ, the default
    is CHECK_CRC64. FORMAT_ALONE and FORMAT_RAW do not suport integrity
    checks; for these formats, check must be omitted, or be CHECK_NONE.
    
    The settings used by the compressor can be specified either as a
    preset compression level (with the 'preset' argument), or in detail
    as a custom filter chain (with the 'filters' argument). For FORMAT_XZ
    and FORMAT_ALONE, the default is to use the PRESET_DEFAULT preset
    level. For FORMAT_RAW, the caller must always specify a filter chain;
    the raw compressor does not support preset compression levels.
    
    preset (if provided) should be an integer in the range 0-9, optionally
    OR-ed with the constant PRESET_EXTREME.
    
    filters (if provided) should be a sequence of dicts. Each dict should
    have an entry for "id" indicating the ID of the filter, plus
    additional entries for options to the filter.
    
    For one-shot compression, use the compress() function instead.
    """
    def compress(self, *args, **kwargs): # real signature unknown
        """
        Provide data to the compressor object.
        
        Returns a chunk of compressed data if possible, or b'' otherwise.
        
        When you have finished providing data to the compressor, call the
        flush() method to finish the compression process.
        """
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        """
        Finish the compression process.
        
        Returns the compressed data left in internal buffers.
        
        The compressor object may not be used after this method is called.
        """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, format=None, check=-1, preset=None, filters=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


from .object import object

class LZMADecompressor(object):
    """
    Create a decompressor object for decompressing data incrementally.
    
      format
        Specifies the container format of the input stream.  If this is
        FORMAT_AUTO (the default), the decompressor will automatically detect
        whether the input is FORMAT_XZ or FORMAT_ALONE.  Streams created with
        FORMAT_RAW cannot be autodetected.
      memlimit
        Limit the amount of memory used by the decompressor.  This will cause
        decompression to fail if the input cannot be decompressed within the
        given limit.
      filters
        A custom filter chain.  This argument is required for FORMAT_RAW, and
        not accepted with any other format.  When provided, this should be a
        sequence of dicts, each indicating the ID and options for a single
        filter.
    
    For one-shot decompression, use the decompress() function instead.
    """
    def decompress(self, *args, **kwargs): # real signature unknown
        """
        Provide data to the decompressor object.
        
        Returns a chunk of decompressed data if possible, or b'' otherwise.
        
        Attempting to decompress data after the end of stream is reached
        raises an EOFError.  Any data found after the end of the stream
        is ignored and saved in the unused_data attribute.
        """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    check = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ID of the integrity check used by the input stream."""

    eof = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the end-of-stream marker has been reached."""

    unused_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Data found after the end of the compressed stream."""



from .Exception import Exception

class LZMAError(Exception):
    """ Call to liblzma failed. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

