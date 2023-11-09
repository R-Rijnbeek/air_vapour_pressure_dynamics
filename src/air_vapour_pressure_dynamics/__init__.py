# -*- coding: utf-8 -*-
"""
air_vapour_pressure_dynamics: Repository with the basic functions related with the temperature, relative humidity, absolute humidity and entalpy of the air with the different variable transformations
"""
__author__  = "Robert Rijnbeek"
__email__   = "robert270384@gmail.com"
__version__ = "1.1.0"

# ======== IMPORTS ===========

import math
from basic_decorators import argument_check

# ======= BASE FUNCTIONS =====

@argument_check((float,int))
def vapourpressure(temp: int | float) -> float:
    """
    Function that calculate the vapour presure of the air witha as argument the temperature (temp).
    """
    temp=float(temp)
    return 10**(8.07131 - (1730.63/(233.426+temp)))*133.322

@argument_check((float,int),(float,int))
def density_air(temp: int | float, rh: int | float) -> float:
    """
    Function that calculate the desity of the air kg/m3 witha as argument the temperature (temp) and relative humidity (rh).
    """
    temp=float(temp)
    rh=float(rh)
    return 219.56*(1 +absolutehumidity_kg_air(temp, rh)/1000)/((0.622 + absolutehumidity_kg_air(temp, rh)/1000)*(temp + 273))

@argument_check((float,int),(float,int))
def absolutehumidity_kg_air(temp: int | float,rh: int | float) -> float:
    """
    Function that calculate the absolute humidity of 1 kg the air witha as argument the temperature (temp) and relative humidity (rh).
    """
    temp=float(temp)
    rh=float(rh)
    waterdd = vapourpressure(temp)
    return 0.622*waterdd*(rh/100)/(101325. - waterdd*(rh/100))*1000

@argument_check((float,int),(float,int))
def absolutehumidity_m3_air(temp: int | float, rh: int | float) -> float:
    """
    Function that calculate the absolute humidity of 1 cubic meter of air witha as argument the temperature (temp) and relative humidity (rh).
    """
    temp=float(temp)
    rh=float(rh)
    return (absolutehumidity_kg_air(temp, rh)*density_air(temp, rh))
    
@argument_check((float,int),(float,int))
def entalpie_kg_air(temp: int | float, rh: int | float) -> float:
    """
    Function that calculate the entalpie of 1 kilogram air with as argument the temperature (temp) and relative humidity (rh).
    """
    temp=float(temp)
    rh=float(rh)
    return ((1.005*temp) + absolutehumidity_kg_air(temp, rh)*(2500.6 + (1.85*temp))/1000)

@argument_check((float,int),(float,int))
def entalpie_m3_air(temp: int | float, rh: int | float) -> float:
    """
    Function that calculate the entalpie of 1 cubic meter air with as argument the temperature (temp) and relative humidity (rh).
    """
    temp=float(temp)
    rh=float(rh)
    return (entalpie_kg_air(temp, rh)*density_air(temp, rh))
    
@argument_check((float,int),(float, int))
def moisuredeficit_kg_air(temp: int | float,rh: int | float) -> float:
    """
    Function that calculate the moisure dficit of 1 kg air with as argument the temperature (temp) and relative humidity (rh).
    """
    temp=float(temp)
    rh=float(rh)
    return (absolutehumidity_kg_air(temp, 100.)-absolutehumidity_kg_air(temp, rh))

@argument_check((float,int),(float,int))
def moisuredeficit_m3_air(temp: int | float, rh: int | float) -> float:
    """
    Function that calculate the moisure dficit of 1 cubic meter air with as argument the temperature (temp) and relative humidity (rh).
    """
    temp=float(temp)
    rh=float(rh)
    return (moisuredeficit_kg_air(temp, rh)*density_air(temp, rh))

@argument_check((float,int),(float,int))
def dew_point_factor(temp: int | float, rh: int | float) -> float:
    """
    Function that calculate the dewpoint factor of air with as argument the temperature (temp) and relative humidity (rh).
    """
    temp=float(temp)
    rh=float(rh)
    return (math.log(rh/100.) + 17.67*temp/(243.5 + temp))

@argument_check((float,int),(float,int))
def dew_point_temperature(temp: int | float, rh: int | float) -> float:
    """
    Function that calculate the dewpoint temperature of air with as argument the temperature (temp) and relative humidity (rh).
    """
    temp=float(temp)
    rh=float(rh)
    return (243.5*dew_point_factor(temp, rh))/(17.67 - dew_point_factor(temp, rh))


if __name__ == '__main__':

    pass