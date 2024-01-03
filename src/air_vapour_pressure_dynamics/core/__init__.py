# -*- coding: utf-8 -*-

# ======== IMPORTS ===========

import inspect
import math

from basic_decorators import argument_check

from ..initialize import SETTINGS, np, sp
from ..extra._numpy import UnitNumpyArray
from ..extra._sympy import UnitSympyExpression
from ..extra._float import UnitFloat
    
# ======= FUNCTIONS ===========

def inputChanger(arg):
    if isinstance(arg,int):
        return float(arg)
    if ( SETTINGS.NUMPY_DETECTED and isinstance(arg,np.ndarray)):
        return arg.astype(np.float64)
    return arg

def inputAdapter(*args):
    return tuple(inputChanger(arg) for arg in args)

def LOG(value):
    if SETTINGS.NUMPY_DETECTED and isinstance(value, np.ndarray):
        return np.log(value)
    if SETTINGS.SYMPY_DETECTED and isinstance(value, sp.Expr):
        return sp.log(value)
    if value < SETTINGS.CERO_LOG :
        value = SETTINGS.CERO_LOG
    return math.log(value)

def _vapourpressure(temp: int | float) -> UnitFloat:
    return 10**(8.07131 - (1730.63/(233.426+temp)))*133.322

def _density_air(temp: int | float, rh: int | float) -> UnitFloat:
    return 219.56*(1 +_absolutehumidity_kg_air(temp, rh)/1000)/((0.622 + _absolutehumidity_kg_air(temp, rh)/1000)*(temp + 273))

def _absolutehumidity_kg_air(temp: int | float,rh: int | float) -> UnitFloat:
    waterdd = _vapourpressure(temp)
    return (0.622*waterdd*(rh/100)/(101325. - waterdd*(rh/100))*1000)

def _absolutehumidity_m3_air(temp: int | float, rh: int | float) -> UnitFloat:
    return (_absolutehumidity_kg_air(temp, rh)*_density_air(temp, rh))
    
def _entalpie_kg_air(temp: int | float, rh: int | float) -> UnitFloat:
    return ((1.005*temp) + _absolutehumidity_kg_air(temp, rh)*(2500.6 + (1.85*temp))/1000)

def _entalpie_m3_air(temp: int | float, rh: int | float) -> UnitFloat:
    return (_entalpie_kg_air(temp, rh)*_density_air(temp, rh))
    
def _moisuredeficit_kg_air(temp: int | float,rh: int | float) -> UnitFloat:
    return (_absolutehumidity_kg_air(temp, 100.)-_absolutehumidity_kg_air(temp, rh))

def _moisuredeficit_m3_air(temp: int | float, rh: int | float) -> UnitFloat:
    return (_moisuredeficit_kg_air(temp, rh)*_density_air(temp, rh))

def _dew_point_factor(temp: int | float, rh: int | float) -> UnitFloat:
    return (LOG(rh/100.) + 17.67*temp/(243.5 + temp))

def _dew_point_temperature(temp: int | float, rh: int | float) -> UnitFloat:
    return (243.5*_dew_point_factor(temp, rh))/(17.67 - _dew_point_factor(temp, rh))


functionList = {
    "vapourpressure": {"function":_vapourpressure, "unit": "Pa"},
    "density_air" : {"function":_density_air, "unit": "kg/m^3"},
    "absolutehumidity_kg_air" : {"function":_absolutehumidity_kg_air, "unit": "g/Kg"},
    "absolutehumidity_m3_air" : {"function":_absolutehumidity_m3_air, "unit": "g/m³"},
    "entalpie_kg_air" : {"function":_entalpie_kg_air, "unit": "KJ/Kg"},
    "entalpie_m3_air" : {"function":_entalpie_m3_air, "unit": "KJ/m³"},
    "moisuredeficit_kg_air" : {"function":_moisuredeficit_kg_air, "unit": "gr/Kg"},
    "moisuredeficit_m3_air" : {"function":_moisuredeficit_m3_air, "unit": "gr/m³"},
    "dew_point_factor" : {"function":_dew_point_factor, "unit": ""},
    "dew_point_temperature": {"function":_dew_point_temperature, "unit": "°C"},
}

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