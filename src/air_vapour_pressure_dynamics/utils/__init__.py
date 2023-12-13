# -*- coding: utf-8 -*-

# ======== IMPORTS ===========

import inspect

import math

from basic_decorators import argument_check

# ======= GLOBAL VARIABLES ====

ARGUMENT_CHECK = True

# ======= FUNCTIONS ===========

@argument_check(bool)
def setArgCheck(bool: bool) -> None:
    global ARGUMENT_CHECK
    ARGUMENT_CHECK = bool

class UnitFloat(float):
    @argument_check(object, float, str)
    def __new__(self, value, unit=None):
       return float.__new__(self, value)
    
    @argument_check(object ,float, str)
    def __init__(self, value, unit=None):
        self.unit = unit


def _vapourpressure(temp: int | float) -> UnitFloat:
    temp=float(temp)
    return UnitFloat(10**(8.07131 - (1730.63/(233.426+temp)))*133.322,"Pa")

def _density_air(temp: int | float, rh: int | float) -> UnitFloat:
    temp=float(temp)
    rh=float(rh)
    return UnitFloat(219.56*(1 +_absolutehumidity_kg_air(temp, rh)/1000)/((0.622 + _absolutehumidity_kg_air(temp, rh)/1000)*(temp + 273)),"kg/m^3")

def _absolutehumidity_kg_air(temp: int | float,rh: int | float) -> UnitFloat:
    temp=float(temp)
    rh=float(rh)
    waterdd = _vapourpressure(temp)
    return UnitFloat((0.622*waterdd*(rh/100)/(101325. - waterdd*(rh/100))*1000),"g/Kg")

def _absolutehumidity_m3_air(temp: int | float, rh: int | float) -> UnitFloat:
    temp=float(temp)
    rh=float(rh)
    return UnitFloat((_absolutehumidity_kg_air(temp, rh)*_density_air(temp, rh)),"g/m³")
    
def _entalpie_kg_air(temp: int | float, rh: int | float) -> UnitFloat:
    temp=float(temp)
    rh=float(rh)
    return UnitFloat(((1.005*temp) + _absolutehumidity_kg_air(temp, rh)*(2500.6 + (1.85*temp))/1000),"KJ/Kg")

def _entalpie_m3_air(temp: int | float, rh: int | float) -> UnitFloat:
    temp=float(temp)
    rh=float(rh)
    return UnitFloat((_entalpie_kg_air(temp, rh)*_density_air(temp, rh)),"KJ/m³")
    
def _moisuredeficit_kg_air(temp: int | float,rh: int | float) -> UnitFloat:
    temp=float(temp)
    rh=float(rh)
    return UnitFloat((_absolutehumidity_kg_air(temp, 100.)-_absolutehumidity_kg_air(temp, rh)),"gr/Kg")

def _moisuredeficit_m3_air(temp: int | float, rh: int | float) -> UnitFloat:
    temp=float(temp)
    rh=float(rh)
    return UnitFloat((_moisuredeficit_kg_air(temp, rh)*_density_air(temp, rh)),"gr/m³")

def _dew_point_factor(temp: int | float, rh: int | float) -> UnitFloat:
    temp=float(temp)
    rh=float(rh)
    return UnitFloat((math.log(rh/100.) + 17.67*temp/(243.5 + temp)), "")

def _dew_point_temperature(temp: int | float, rh: int | float) -> UnitFloat:
    temp=float(temp)
    rh=float(rh)
    return UnitFloat((243.5*_dew_point_factor(temp, rh))/(17.67 - _dew_point_factor(temp, rh)),"°C")


functionList = {
    "vapourpressure": _vapourpressure,
    "density_air" : _density_air,
    "absolutehumidity_kg_air" : _absolutehumidity_kg_air,
    "absolutehumidity_m3_air" : _absolutehumidity_m3_air,
    "entalpie_kg_air" : _entalpie_kg_air,
    "entalpie_m3_air" : _entalpie_m3_air ,
    "moisuredeficit_kg_air" : _moisuredeficit_kg_air,
    "moisuredeficit_m3_air" : _moisuredeficit_m3_air,
    "dew_point_factor" : _dew_point_factor,
    "dew_point_temperature": _dew_point_temperature,
}

def getFunctionBackName():
    return inspect.currentframe().f_back.f_code.co_name

def argumentChecker_2var(TEMP, HR, function="density_air"):
    if ARGUMENT_CHECK :
        @argument_check((int,float),(int,float))
        def wrapper(temp, hr):
            return functionList[function](temp, hr)
        return wrapper(TEMP, HR)
    else:
        def wrapper(temp, hr):
            return functionList[function](temp, hr)
        return wrapper(TEMP, HR)
    
def argumentChecker_1var(TEMP, function="density_air"):
    if ARGUMENT_CHECK :
        @argument_check((int,float))
        def wrapper(temp):
            return functionList[function](temp)
        return wrapper(TEMP)
    else:
        def wrapper(temp):
            return functionList[function](temp)
        return wrapper(TEMP)