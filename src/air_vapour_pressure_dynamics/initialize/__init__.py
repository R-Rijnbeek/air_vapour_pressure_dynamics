# -*- coding: utf-8 -*-

# ======== IMPORTS ===========

from basic_decorators import argument_check

# ======= FUNCTIONS ===========

class Settings():
    def __init__(self):
        self._CERO_LOG = 0.0001
        self._ARGUMENT_CHECK = True
        self._APPLY_UNITS = True
        self._NUMPY_DETECTED = False
        self._SYMPY_DETECTED = False
        self.LibraryCheck()

    @argument_check(object, bool)
    def setNumpyDetected(self, bool:bool) -> None:
        self._NUMPY_DETECTED = bool

    @argument_check(object, bool)
    def setSympyDetected(self, bool:bool) -> None:
        self._SYMPY_DETECTED = bool

    def numpyCheck(self):
        try:
            global np
            import numpy as np
            self.setNumpyDetected(True)
            print("Numpy library detected")
        except:
            print("Numpy library not detected")

    def sympyCheck(self):
        try:
            global sp
            import sympy as sp
            self.setSympyDetected(True)
            print("Sympy library detected")
        except:
            print("Sympy library not detected")
    
    def LibraryCheck(self):
        self.numpyCheck()
        self.sympyCheck()

    @property
    def CERO_LOG(self):
        return self._CERO_LOG
    
    @property
    def ARGUMENT_CHECK(self):
        return self._ARGUMENT_CHECK
    
    
    @ARGUMENT_CHECK.setter
    @argument_check(object, bool)
    def ARGUMENT_CHECK(self, bool: bool):
        self._ARGUMENT_CHECK = bool
    
    @property
    def APPLY_UNITS(self):
        return self._APPLY_UNITS
    
    @APPLY_UNITS.setter
    @argument_check(object, bool)
    def APPLY_UNITS(self, bool: bool):
        self._APPLY_UNITS = bool
    
    @property
    def NUMPY_DETECTED(self):
        return self._NUMPY_DETECTED
    
    @property
    def SYMPY_DETECTED(self):
        return self._SYMPY_DETECTED
    
# ======= EXECUTION ===========
    
SETTINGS = Settings()

if __name__ == '__main__':
    
    pass