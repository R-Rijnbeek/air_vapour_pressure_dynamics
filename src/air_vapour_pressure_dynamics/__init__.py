# -*- coding: utf-8 -*-
"""
air_vapour_pressure_dynamics: Repository with the basic functions related with the temperature, relative humidity, absolute humidity and entalpy of the air with the different variable transformations
"""
__author__  = "Robert Rijnbeek"
__email__   = "robert270384@gmail.com"
__version__ = "1.3.0"

# ======== IMPORTS ===========

import math
from basic_decorators import argument_check

# ======= BASE FUNCTIONS =====


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

@argument_check((float,int),(float,int))
def density_air(temp: int | float, rh: int | float) -> UnitFloat:
    """
    Function that calculate the desity of the air kg/m3 witha as argument the temperature (temp) and relative humidity (rh).
    """
    temp=float(temp)
    rh=float(rh)
    return UnitFloat(219.56*(1 +absolutehumidity_kg_air(temp, rh)/1000)/((0.622 + absolutehumidity_kg_air(temp, rh)/1000)*(temp + 273)),"kg/m^3")

@argument_check((float,int),(float,int))
def absolutehumidity_kg_air(temp: int | float,rh: int | float) -> UnitFloat:
    """
    Function that calculate the absolute humidity of 1 kg the air witha as argument the temperature (temp) and relative humidity (rh).
    """
    temp=float(temp)
    rh=float(rh)
    waterdd = vapourpressure(temp)
    return UnitFloat((0.622*waterdd*(rh/100)/(101325. - waterdd*(rh/100))*1000),"g/Kg")

@argument_check((float,int),(float,int))
def absolutehumidity_m3_air(temp: int | float, rh: int | float) -> UnitFloat:
    """
    Function that calculate the absolute humidity of 1 cubic meter of air witha as argument the temperature (temp) and relative humidity (rh).
    """
    temp=float(temp)
    rh=float(rh)
    return UnitFloat((absolutehumidity_kg_air(temp, rh)*density_air(temp, rh)),"g/m³")
    
@argument_check((float,int),(float,int))
def entalpie_kg_air(temp: int | float, rh: int | float) -> UnitFloat:
    """
    Function that calculate the entalpie of 1 kilogram air with as argument the temperature (temp) and relative humidity (rh).
    """
    temp=float(temp)
    rh=float(rh)
    return UnitFloat(((1.005*temp) + absolutehumidity_kg_air(temp, rh)*(2500.6 + (1.85*temp))/1000),"KJ/Kg")

@argument_check((float,int),(float,int))
def entalpie_m3_air(temp: int | float, rh: int | float) -> UnitFloat:
    """
    Function that calculate the entalpie of 1 cubic meter air with as argument the temperature (temp) and relative humidity (rh).
    """
    temp=float(temp)
    rh=float(rh)
    return UnitFloat((entalpie_kg_air(temp, rh)*density_air(temp, rh)),"KJ/m³")
    
@argument_check((float,int),(float, int))
def moisuredeficit_kg_air(temp: int | float,rh: int | float) -> UnitFloat:
    """
    Function that calculate the moisure dficit of 1 kg air with as argument the temperature (temp) and relative humidity (rh).
    """
    temp=float(temp)
    rh=float(rh)
    return UnitFloat((absolutehumidity_kg_air(temp, 100.)-absolutehumidity_kg_air(temp, rh)),"gr/Kg")

@argument_check((float,int),(float,int))
def moisuredeficit_m3_air(temp: int | float, rh: int | float) -> UnitFloat:
    """
    Function that calculate the moisure dficit of 1 cubic meter air with as argument the temperature (temp) and relative humidity (rh).
    """
    temp=float(temp)
    rh=float(rh)
    return UnitFloat((moisuredeficit_kg_air(temp, rh)*density_air(temp, rh)),"gr/m³")

@argument_check((float,int),(float,int))
def dew_point_factor(temp: int | float, rh: int | float) -> UnitFloat:
    """
    Function that calculate the dewpoint factor of air with as argument the temperature (temp) and relative humidity (rh).
    """
    temp=float(temp)
    rh=float(rh)
    return UnitFloat((math.log(rh/100.) + 17.67*temp/(243.5 + temp)), "")

@argument_check((float,int),(float,int))
def dew_point_temperature(temp: int | float, rh: int | float) -> UnitFloat:
    """
    Function that calculate the dewpoint temperature of air with as argument the temperature (temp) and relative humidity (rh).
    """
    temp=float(temp)
    rh=float(rh)
    return UnitFloat((243.5*dew_point_factor(temp, rh))/(17.67 - dew_point_factor(temp, rh)),"°C")


if __name__ == '__main__':

    pass