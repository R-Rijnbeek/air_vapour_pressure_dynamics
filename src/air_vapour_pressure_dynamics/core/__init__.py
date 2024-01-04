# -*- coding: utf-8 -*-

# ======== IMPORTS ===========

import inspect

from basic_decorators import argument_check

from ..initialize import SETTINGS, np, sp
from ..extra._numpy import UnitNumpyArray
from ..extra._sympy import UnitSympyExpression
from ..extra._float import UnitFloat
from ..calculations import functionList
    
# ======= FUNCTIONS ===========

def inputChanger(arg):
    if isinstance(arg,int):
        return float(arg)
    if ( SETTINGS.NUMPY_DETECTED and isinstance(arg,np.ndarray)):
        return arg.astype(np.float64)
    return arg

def inputAdapter(*args):
    return tuple(inputChanger(arg) for arg in args)

def getFunctionBackName():
    return inspect.currentframe().f_back.f_code.co_name

def _getFunctionByName(functionName):
    return functionList[functionName]["function"]

def _getUnitsByName(functionName):
    return functionList[functionName]["unit"]

def MakeUpOutput(value, functionName):
    if SETTINGS.APPLY_UNITS :
        if isinstance(value, float) :
            return UnitFloat(value, _getUnitsByName(functionName))
        if SETTINGS.NUMPY_DETECTED and isinstance(value, np.ndarray):
            return UnitNumpyArray(value, _getUnitsByName(functionName))
        if SETTINGS.SYMPY_DETECTED and isinstance(value, sp.Expr):
            return UnitSympyExpression(value, _getUnitsByName(functionName))
    return value


def argumentChecker_2var(TEMP, HR, function="density_air"):
    if SETTINGS.ARGUMENT_CHECK :
        formats = [int, float]
        if SETTINGS.NUMPY_DETECTED :
            formats.append(np.ndarray)
        if SETTINGS.SYMPY_DETECTED :
            formats.append(sp.Symbol)
        formats = (tuple(formats),tuple(formats))
        @argument_check(*formats)
        def wrapper(temp, hr):
            return _getFunctionByName(function)(temp, hr)
    else:
        def wrapper(temp, hr):
            return _getFunctionByName(function)(temp, hr)
    (TEMP, HR,) = inputAdapter(TEMP, HR)
    return MakeUpOutput(wrapper(TEMP, HR),function)
    
def argumentChecker_1var(TEMP, function="density_air"):
    if SETTINGS.ARGUMENT_CHECK :
        formats = [int, float]
        if SETTINGS.NUMPY_DETECTED :
            formats.append(np.ndarray)
        if SETTINGS.SYMPY_DETECTED :
            formats.append(sp.Symbol)
        formats = (tuple(formats))
        @argument_check(formats)
        def wrapper(temp):
            return _getFunctionByName(function)(temp)
    else:
        def wrapper(temp):
            return _getFunctionByName(function)(temp)
    (TEMP,) = inputAdapter(TEMP)
    return MakeUpOutput(wrapper(TEMP),function)

if __name__ == '__main__':
    
    pass