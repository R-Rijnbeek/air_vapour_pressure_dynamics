# -*- coding: utf-8 -*-
""" Submodule that create and execute an Settings class that is use to configurate the Base Labrary.

    - The global variable that is created is called: SETTINGS

    - It also verify if 'numpy' and/or 'sympy' is installed inthe python environment. And create an statement on the 'Settings' class That can be called to manage the usecases of the whole package when those libraries are installed.Those statements can be called by:

        - numpy: SETTINGS.NUMPY_DETECTED => bool
        - sympy: SETTINGS.SYMPY_DETECTED => bool

    - SETTERS: 

        - Apply argument check to the base functions::

            >>> SETTINGS.ARGUMENT_CHECK = bool

        - Apply units to the results of the base calculations::
        
            >>> SETTINGS.APPLY_UNITS = bool
    
    Please note that this module is private.  All functions and objects
    are available in the main `air_vapour_pressure_dynamics` namespace - use that instead.
"""
# ======== IMPORTS ===========

from basic_decorators import argument_check

# ======= FUNCTIONS ===========

class Settings():
    def __init__(self) -> None:
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

    def numpyCheck(self) -> None:
        try:
            global np
            import numpy as np
            self.setNumpyDetected(True)
            print("Numpy library detected")
        except:
            global np
            np = None
            print("Numpy library not detected")

    def sympyCheck(self) -> None:
        try:
            global sp
            import sympy as sp
            self.setSympyDetected(True)
            print("Sympy library detected")
        except:
            global sp
            sp = None
            print("Sympy library not detected")
    
    def LibraryCheck(self) -> None:
        self.numpyCheck()
        self.sympyCheck()

    @property
    def CERO_LOG(self) -> bool:
        return self._CERO_LOG
    
    @property
    def ARGUMENT_CHECK(self) -> bool:
        return self._ARGUMENT_CHECK
    
    
    @ARGUMENT_CHECK.setter
    @argument_check(object, bool)
    def ARGUMENT_CHECK(self, bool: bool) -> None:
        self._ARGUMENT_CHECK = bool
    
    @property
    def APPLY_UNITS(self) -> bool:
        return self._APPLY_UNITS
    
    @APPLY_UNITS.setter
    @argument_check(object, bool)
    def APPLY_UNITS(self, bool: bool) -> None:
        self._APPLY_UNITS = bool
    
    @property
    def NUMPY_DETECTED(self) -> bool:
        return self._NUMPY_DETECTED
    
    @property
    def SYMPY_DETECTED(self) -> bool:
        return self._SYMPY_DETECTED
    
# ======= EXECUTION ===========
    
SETTINGS = Settings()

if __name__ == '__main__':
    
    pass