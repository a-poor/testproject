"""
testproject module

Includes some test functions.

"""

from . import mysubmodule


__version__ = "0.0.1"


def make_scale(dstart,dstop,rstart,rstop):
    """
    Create a scale function.

    Creates a function to map a number from a domain to a range.

    Parameters
    ----------
    dstart : int or float
        Domain's start value
    dstop : int or float
        Domain's end value.
    rstart : int or float
        Range's start value
    rstop : int or float
        Range's end value.

    Returns
    -------
    function
        Function taking a number as an argument, that will be mapped from the domain to the range. 
    """
    dextent = dstop - dstart
    rextent = rstop - rstart
    scale_factor = rextent / dextent
    def scale(n):
        return (n - dstart) * scale_factor + rstart
    return scale

