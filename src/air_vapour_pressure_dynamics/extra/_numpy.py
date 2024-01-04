# -*- coding: utf-8 -*-

# ====== IMPORTS ===============

from basic_decorators import argument_check

from ..initialize import SETTINGS, np

# ======= FUNCTIONS ===========

if SETTINGS.NUMPY_DETECTED :
    class UnitNumpyArray(np.ndarray):

        @argument_check(object, np.ndarray, str)
        def __new__(cls, value, unit=None):
            return np.asarray(value).view(cls)
        
        @argument_check(object , np.ndarray, str)
        def __init__(self, value, unit=None):
            self.unit = unit
else:
    class UnitNumpyArray():
        pass

class NumpyArray():
    """numpy array value: numpy.ndarray"""
    pass

def log_numpy(value):
    return np.log(value)

if __name__ == '__main__':
    
    pass