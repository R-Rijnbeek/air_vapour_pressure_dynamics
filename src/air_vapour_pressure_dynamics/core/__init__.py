# -*- coding: utf-8 -*-

# ======== IMPORTS ===========

import inspect

from basic_decorators import argument_check

from ..initialize import SETTINGS
from ..extra._numpy import UnitNumpyArray, isNumpyValue, numpyArray, numpyFloat64
from ..extra._sympy import UnitSympyExpression, isSympyExpr, sympySymbol
from ..extra._float import UnitFloat
from ..calculations import functionList
    
# ======= FUNCTIONS ===========

def inputChanger(arg):
    if isinstance(arg,int):
        return float(arg)
    if ( isNumpyValue(arg) ):
        return arg.astype(numpyFloat64)
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
        if isNumpyValue(value):
            return UnitNumpyArray(value, _getUnitsByName(functionName))
        if isSympyExpr(value):
            return UnitSympyExpression(value, _getUnitsByName(functionName))
    return value


def argumentChecker_2var(TEMP, HR, function="density_air"):
    if SETTINGS.ARGUMENT_CHECK :
        formats = [int, float]
        if SETTINGS.NUMPY_DETECTED :
            formats.append(numpyArray)
        if SETTINGS.SYMPY_DETECTED :
            formats.append(sympySymbol)
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
            formats.append(numpyArray)
        if SETTINGS.SYMPY_DETECTED :
            formats.append(sympySymbol)
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