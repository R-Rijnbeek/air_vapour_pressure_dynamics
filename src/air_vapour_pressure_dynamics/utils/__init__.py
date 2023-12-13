# -*- coding: utf-8 -*-

# ======== IMPORTS ===========

import inspect

import math

from basic_decorators import argument_check

# ======= GLOBAL VARIABLES ====

ARGUMENT_CHECK = True
APPLY_UNITS = True

# ======= FUNCTIONS ===========

@argument_check(bool)
def setArgCheck(bool: bool) -> None:
    global ARGUMENT_CHECK
    ARGUMENT_CHECK = bool

@argument_check(bool)
def setApplyU(bool: bool) -> None:
    global APPLY_UNITS
    APPLY_UNITS = bool

class UnitFloat(float):
    @argument_check(object, float, str)
    def __new__(self, value, unit=None):
       return float.__new__(self, value)
    
    @argument_check(object ,float, str)
    def __init__(self, value, unit=None):
        self.unit = unit


def _vapourpressure(temp: int | float) -> UnitFloat:
    temp=float(temp)
    return 10**(8.07131 - (1730.63/(233.426+temp)))*133.322

def _density_air(temp: int | float, rh: int | float) -> UnitFloat:
    temp=float(temp)
    rh=float(rh)
    return 219.56*(1 +_absolutehumidity_kg_air(temp, rh)/1000)/((0.622 + _absolutehumidity_kg_air(temp, rh)/1000)*(temp + 273))

def _absolutehumidity_kg_air(temp: int | float,rh: int | float) -> UnitFloat:
    temp=float(temp)
    rh=float(rh)
    waterdd = _vapourpressure(temp)
    return (0.622*waterdd*(rh/100)/(101325. - waterdd*(rh/100))*1000)

def _absolutehumidity_m3_air(temp: int | float, rh: int | float) -> UnitFloat:
    temp=float(temp)
    rh=float(rh)
    return (_absolutehumidity_kg_air(temp, rh)*_density_air(temp, rh))
    
def _entalpie_kg_air(temp: int | float, rh: int | float) -> UnitFloat:
    temp=float(temp)
    rh=float(rh)
    return ((1.005*temp) + _absolutehumidity_kg_air(temp, rh)*(2500.6 + (1.85*temp))/1000)

def _entalpie_m3_air(temp: int | float, rh: int | float) -> UnitFloat:
    temp=float(temp)
    rh=float(rh)
    return (_entalpie_kg_air(temp, rh)*_density_air(temp, rh))
    
def _moisuredeficit_kg_air(temp: int | float,rh: int | float) -> UnitFloat:
    temp=float(temp)
    rh=float(rh)
    return (_absolutehumidity_kg_air(temp, 100.)-_absolutehumidity_kg_air(temp, rh))

def _moisuredeficit_m3_air(temp: int | float, rh: int | float) -> UnitFloat:
    temp=float(temp)
    rh=float(rh)
    return (_moisuredeficit_kg_air(temp, rh)*_density_air(temp, rh))

def _dew_point_factor(temp: int | float, rh: int | float) -> UnitFloat:
    temp=float(temp)
    rh=float(rh)
    return (math.log(rh/100.) + 17.67*temp/(243.5 + temp))

def _dew_point_temperature(temp: int | float, rh: int | float) -> UnitFloat:
    temp=float(temp)
    rh=float(rh)
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

def MakeUpOutput(float, functionName):
    if APPLY_UNITS :
       return UnitFloat(float,_getUnitsByName(functionName))
    return float


def argumentChecker_2var(TEMP, HR, function="density_air"):
    if ARGUMENT_CHECK :
        @argument_check((int,float),(int,float))
        def wrapper(temp, hr):
            return _getFunctionByName(function)(temp, hr)
    else:
        def wrapper(temp, hr):
            return _getFunctionByName(function)(temp, hr)
    return MakeUpOutput(wrapper(TEMP, HR),function)
    
def argumentChecker_1var(TEMP, function="density_air"):
    if ARGUMENT_CHECK :
        @argument_check((int,float))
        def wrapper(temp):
            return _getFunctionByName(function)(temp)
    else:
        def wrapper(temp):
            return _getFunctionByName(function)(temp)
    return MakeUpOutput(wrapper(TEMP),function)