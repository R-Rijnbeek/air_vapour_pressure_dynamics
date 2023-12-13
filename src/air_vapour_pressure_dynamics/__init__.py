# -*- coding: utf-8 -*-
"""
air_vapour_pressure_dynamics: Repository with the basic functions related with the temperature, relative humidity, absolute humidity and entalpy of the air with the different variable transformations
"""
__author__  = "Robert Rijnbeek"
__email__   = "robert270384@gmail.com"
__version__ = "1.4.1"

# ======== IMPORTS ===========

import math
from basic_decorators import argument_check, type_arguments_for_all

import inspect

# ======= GLOBAL VARIABLES ====

ARGUMENT_CHECK = True

# ======= BASE FUNCTIONS =====

@argument_check(bool)
def setArgumentCheck(bool):
    global ARGUMENT_CHECK
    ARGUMENT_CHECK = bool

class UnitFloat(float):
    @argument_check(object, float, str)
    def __new__(self, value, unit=None):
       return float.__new__(self, value)
    
    @argument_check(object ,float, str)
    def __init__(self, value, unit=None):
        self.unit = unit

@argument_check((float,int))
def vapourpressure(temp: int | float) -> UnitFloat:
    """
    Function that calculate the vapour pressure of the air with argument the temperature (temp).
    """
    temp=float(temp)
    return UnitFloat(10**(8.07131 - (1730.63/(233.426+temp)))*133.322,"Pa")

def _density_air(temp: int | float, rh: int | float) -> UnitFloat:
    """
    Function that calculate the desity of the air kg/m3 witha as argument the temperature (temp) and relative humidity (rh).
    """
    temp=float(temp)
    rh=float(rh)
    return UnitFloat(219.56*(1 +_absolutehumidity_kg_air(temp, rh)/1000)/((0.622 + _absolutehumidity_kg_air(temp, rh)/1000)*(temp + 273)),"kg/m^3")

def _absolutehumidity_kg_air(temp: int | float,rh: int | float) -> UnitFloat:
    """
    Function that calculate the absolute humidity of 1 kg the air witha as argument the temperature (temp) and relative humidity (rh).
    """
    temp=float(temp)
    rh=float(rh)
    waterdd = vapourpressure(temp)
    return UnitFloat((0.622*waterdd*(rh/100)/(101325. - waterdd*(rh/100))*1000),"g/Kg")

def _absolutehumidity_m3_air(temp: int | float, rh: int | float) -> UnitFloat:
    """
    Function that calculate the absolute humidity of 1 cubic meter of air witha as argument the temperature (temp) and relative humidity (rh).
    """
    temp=float(temp)
    rh=float(rh)
    return UnitFloat((_absolutehumidity_kg_air(temp, rh)*_density_air(temp, rh)),"g/m³")
    
def _entalpie_kg_air(temp: int | float, rh: int | float) -> UnitFloat:
    """
    Function that calculate the entalpie of 1 kilogram air with as argument the temperature (temp) and relative humidity (rh).
    """
    temp=float(temp)
    rh=float(rh)
    return UnitFloat(((1.005*temp) + _absolutehumidity_kg_air(temp, rh)*(2500.6 + (1.85*temp))/1000),"KJ/Kg")

def _entalpie_m3_air(temp: int | float, rh: int | float) -> UnitFloat:
    """
    Function that calculate the entalpie of 1 cubic meter air with as argument the temperature (temp) and relative humidity (rh).
    """
    temp=float(temp)
    rh=float(rh)
    return UnitFloat((_entalpie_kg_air(temp, rh)*_density_air(temp, rh)),"KJ/m³")
    
def _moisuredeficit_kg_air(temp: int | float,rh: int | float) -> UnitFloat:
    """
    Function that calculate the moisure dficit of 1 kg air with as argument the temperature (temp) and relative humidity (rh).
    """
    temp=float(temp)
    rh=float(rh)
    return UnitFloat((_absolutehumidity_kg_air(temp, 100.)-_absolutehumidity_kg_air(temp, rh)),"gr/Kg")

def _moisuredeficit_m3_air(temp: int | float, rh: int | float) -> UnitFloat:
    """
    Function that calculate the moisure dficit of 1 cubic meter air with as argument the temperature (temp) and relative humidity (rh).
    """
    temp=float(temp)
    rh=float(rh)
    return UnitFloat((_moisuredeficit_kg_air(temp, rh)*_density_air(temp, rh)),"gr/m³")

def _dew_point_factor(temp: int | float, rh: int | float) -> UnitFloat:
    """
    Function that calculate the dewpoint factor of air with as argument the temperature (temp) and relative humidity (rh).
    """
    temp=float(temp)
    rh=float(rh)
    return UnitFloat((math.log(rh/100.) + 17.67*temp/(243.5 + temp)), "")

def _dew_point_temperature(temp: int | float, rh: int | float) -> UnitFloat:
    """
    Function that calculate the dewpoint temperature of air with as argument the temperature (temp) and relative humidity (rh).
    """
    temp=float(temp)
    rh=float(rh)
    return UnitFloat((243.5*_dew_point_factor(temp, rh))/(17.67 - _dew_point_factor(temp, rh)),"°C")


functionList = {
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

def argumentChecker(TEMP, HR, function="density_air"):
    if ARGUMENT_CHECK :
        @argument_check((int,float),(int,float))
        def wrapper(temp, hr):
            return functionList[function](temp, hr)
        return wrapper(TEMP, HR)
    else:
        def wrapper(temp, hr):
            return functionList[function](temp, hr)
        return wrapper(TEMP, HR)
    
def getFunctionBackName():
    return inspect.currentframe().f_back.f_code.co_name


def density_air(temp,hr):
    return argumentChecker(temp,hr, function=getFunctionBackName())

def absolutehumidity_kg_air(temp,hr):
    return argumentChecker(temp,hr, function=getFunctionBackName())

def absolutehumidity_m3_air(temp,hr):
    return argumentChecker(temp,hr, function=getFunctionBackName())

def entalpie_kg_air(temp,hr):
    return argumentChecker(temp,hr, function=getFunctionBackName())

def entalpie_m3_air(temp,hr):
    return argumentChecker(temp,hr, function=getFunctionBackName())

def moisuredeficit_kg_air(temp,hr):
    return argumentChecker(temp,hr, function=getFunctionBackName())

def moisuredeficit_m3_air(temp,hr):
    return argumentChecker(temp,hr, function=getFunctionBackName())

def dew_point_factor(temp,hr):
    return argumentChecker(temp,hr, function=getFunctionBackName())

def dew_point_temperature(temp,hr):
    return argumentChecker(temp,hr, function=getFunctionBackName())


if __name__ == '__main__':

    setArgumentCheck(True)

    temp = 25
    hr = 90
    print(f"""
    {density_air(temp,hr),
    absolutehumidity_kg_air(temp,hr) ,
    absolutehumidity_m3_air(temp,hr),
    entalpie_kg_air(temp,hr),
    entalpie_m3_air(temp,hr),
    moisuredeficit_kg_air(temp,hr),
    moisuredeficit_m3_air(temp,hr),
    dew_point_factor(temp,hr),
    dew_point_temperature(temp,hr)}
          """)