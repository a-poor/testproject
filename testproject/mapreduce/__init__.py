"""
testproject.mapreduce module

Functions to help with mapping, filtering, and reduceing iterables.

"""

def map_(fn,itr):
    """
    Map fn onto itr.

    Generator function that transforms itr
    using supplied function.

    Parameters
    ----------
    fn : function
        Function to be mapped onto itr.
    itr : iterable
        Iterable to be transformed.

    Yields
    -------
    iterable
        Result of mapping fn onto itr. 
    """
    for value in itr:
        yield fn(value)

def filter_(fn,itr):
    """
    Filters itr using fn.

    Generator function that yield values
    from itr for which fn evaluates
    to True.

    Parameters
    ----------
    fn : function
        Function to be mapped onto itr.
    itr : iterable
        Iterable to be transformed.

    Yields
    -------
    iterable
        Result of mapping fn onto itr.
    """
    for value in itr:
        if fn(value):
            yield value

def reduce_(fn,itr,start=None):
    """
    Reduce itr using fn.

    Use fn to reduce itr.

    Parameters
    ----------
    fn : function
        Function taking two arguments, the aggregator and the next value.
    itr : iterable
        Iterable to be reduced.
    start : iterable, optional
        Optional starting value for the aggregator function.

    Returns
    -------
    any
        Result of reduce function.
    """
    itr = iter(itr)
    if start is None:
        l = next(itr)
    else:
        l = start
    for r in itr:
        l = fn(l,r)
    return l
