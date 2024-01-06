# -*- coding: utf-8 -*-

# ====== IMPORTS ===============

from basic_decorators import argument_check

from ..initialize import SETTINGS, np

# ======= CONSTANTS ============

numpyArray = np.ndarray if (SETTINGS.NUMPY_DETECTED) else None
numpyFloat64 = np.float64 if (SETTINGS.NUMPY_DETECTED) else None

# ======= CLASSES ==============

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


# ======= FUNCTIONS ============

@argument_check(np.ndarray)
def log_numpy(value: np.ndarray) -> np.ndarray:
    return np.log(value)

def isNumpyValue(value: object) -> bool:
    return SETTINGS.NUMPY_DETECTED and isinstance(value, np.ndarray)

if __name__ == '__main__':
    
    pass