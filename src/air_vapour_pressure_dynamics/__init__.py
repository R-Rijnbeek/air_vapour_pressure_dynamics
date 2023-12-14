# -*- coding: utf-8 -*-
"""
air_vapour_pressure_dynamics: Repository with the basic functions related with the temperature, relative humidity, absolute humidity and entalpy of the air with the different variable transformations
"""
__author__  = "Robert Rijnbeek"
__email__   = "robert270384@gmail.com"
__version__ = "1.6.1"

# ======== IMPORTS ===========

if __package__ is None or __package__ == '':
    # uses current directory visibility
    from utils import ( getFunctionBackName, 
                        argumentChecker_2var, 
                        argumentChecker_1var, 
                        setArgCheck,
                        setApplyU,
                        UnitFloat
                        )
else:
    # uses current package visibility
    from .utils import (getFunctionBackName, 
                        argumentChecker_2var, 
                        argumentChecker_1var, 
                        setArgCheck,
                        setApplyU,
                        UnitFloat
                        )

# ========== SETTERS =========

def setArgumentCheck(bool: bool) -> None:
    setArgCheck(bool)

def setApplyUnits(bool: bool) -> None:
    setApplyU(bool)

# ======= BASE FUNCTIONS =====

def vapourpressure(temp: int | float) -> UnitFloat | float:
    """
    Function that calculate the vapour pressure of the air with argument the temperature (temp).
    """
    return argumentChecker_1var(temp, function=getFunctionBackName())

def density_air(temp: int | float, rh: int | float) -> UnitFloat | float:
    """
    Function that calculate the desity of the air kg/m3 witha as argument the temperature (temp) and relative humidity (rh).
    """
    return argumentChecker_2var(temp, rh, function=getFunctionBackName())

def absolutehumidity_kg_air(temp: int | float, rh: int | float) -> UnitFloat | float:
    """
    Function that calculate the absolute humidity of 1 kg the air witha as argument the temperature (temp) and relative humidity (rh).
    """
    return argumentChecker_2var(temp, rh, function=getFunctionBackName())

def absolutehumidity_m3_air(temp: int | float, rh: int | float) -> UnitFloat | float:
    """
    Function that calculate the absolute humidity of 1 cubic meter of air witha as argument the temperature (temp) and relative humidity (rh).
    """
    return argumentChecker_2var(temp, rh, function=getFunctionBackName())

def entalpie_kg_air(temp: int | float, rh: int | float) -> UnitFloat | float:
    """
    Function that calculate the entalpie of 1 kilogram air with as argument the temperature (temp) and relative humidity (rh).
    """
    return argumentChecker_2var(temp, rh, function=getFunctionBackName())

def entalpie_m3_air(temp: int | float, rh: int | float) -> UnitFloat | float:
    """
    Function that calculate the entalpie of 1 cubic meter air with as argument the temperature (temp) and relative humidity (rh).
    """
    return argumentChecker_2var(temp, rh, function=getFunctionBackName())

def moisuredeficit_kg_air(temp: int | float, rh: int | float) -> UnitFloat | float:
    """
    Function that calculate the moisure dficit of 1 kg air with as argument the temperature (temp) and relative humidity (rh).
    """
    return argumentChecker_2var(temp, rh, function=getFunctionBackName())

def moisuredeficit_m3_air(temp: int | float, rh: int | float) -> UnitFloat | float:
    """
    Function that calculate the moisure dficit of 1 cubic meter air with as argument the temperature (temp) and relative humidity (rh).
    """
    return argumentChecker_2var(temp, rh, function=getFunctionBackName())

def dew_point_factor(temp: int | float, rh: int | float) -> UnitFloat | float:
    """
    Function that calculate the dewpoint factor of air with as argument the temperature (temp) and relative humidity (rh).
    """
    return argumentChecker_2var(temp, rh, function=getFunctionBackName())

def dew_point_temperature(temp: int | float, rh: int | float) -> UnitFloat | float:
    """
    Function that calculate the dewpoint temperature of air with as argument the temperature (temp) and relative humidity (rh).
    """
    return argumentChecker_2var(temp, rh, function=getFunctionBackName())


if __name__ == '__main__':

   pass
