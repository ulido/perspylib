import numpy as np

def tuplify(value):
    if isinstance(value, dict):
        return tuple(sorted([(tuplify(k), tuplify(v)) for k,v in value.iteritems()]))
    elif isinstance(value, list):
        return tuple([tuplify(x) for x in value])
    elif isinstance(value, np.ndarray):
        return tuple([tuplify(x) for x in value])
    else:
        return value
