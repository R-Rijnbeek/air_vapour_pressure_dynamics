# -*- coding: utf-8 -*-

# ======== IMPORTS ===========

import inspect

from basic_decorators import argument_check

from ..initialize import SETTINGS
from ..calculations import FUNCTION_CONFIG
from ..extra._numpy import UnitNumpyArray, isNumpyValue, numpyArray, numpyFloat64
from ..extra._sympy import UnitSympyExpression, isSympyExpr, sympySymbol
from ..extra._float import UnitFloat
    
# ======= FUNCTIONS ===========

def _inputChanger(arg):
    if isinstance(arg,int):
        return float(arg)
    if ( isNumpyValue(arg) ):
        return arg.astype(numpyFloat64)
    return arg

def _inputAdapter(*args):
    return tuple(_inputChanger(arg) for arg in args)

def _getFunctionByName(functionName):
    return FUNCTION_CONFIG[functionName]["function"]

def _getUnitsByName(functionName):
    return FUNCTION_CONFIG[functionName]["unit"]

def _makeUpOutput(value, functionName):
    if SETTINGS.APPLY_UNITS :
        if isinstance(value, float) :
            return UnitFloat(value, _getUnitsByName(functionName))
        if isNumpyValue(value):
            return UnitNumpyArray(value, _getUnitsByName(functionName))
        if isSympyExpr(value):
            return UnitSympyExpression(value, _getUnitsByName(functionName))
    return value

def _getFunctionBackName_X2():
    return inspect.currentframe().f_back.f_back.f_code.co_name

def controller(*args):
    function = _getFunctionBackName_X2()
    argument_lenght = len(args)
    if (0 < argument_lenght < 3 ):

        if SETTINGS.ARGUMENT_CHECK :

            formats = [int, float]
            if SETTINGS.NUMPY_DETECTED :
                formats.append(numpyArray)
            if SETTINGS.SYMPY_DETECTED :
                formats.append(sympySymbol)
            formats = tuple(tuple(formats) for i in range(argument_lenght))

            @argument_check(*formats)
            def wrapper(*arguments):
                return _getFunctionByName(function)(*arguments)
        else:
            def wrapper(*arguments):
                return _getFunctionByName(function)(*arguments)
            
        ARGS = _inputAdapter(*args)
        return _makeUpOutput(wrapper(*ARGS),function)

    else:
        raise AssertionError("number of argument must be 1 or 2")

if __name__ == '__main__':
    
    pass