# -*- coding: utf-8 -*-

# ======== IMPORTS ===========

from ..core import (getFunctionBackName, 
                    controller,
                    SETTINGS
                    )

from ..extra._numpy import NumpyArray, UnitNumpyArray
from ..extra._sympy import SympySimbol, SympyExpression, UnitSympyExpression
from ..extra._float import UnitFloat

# ========== SETTERS =========

def setArgumentCheck(bool: bool) -> None:
    SETTINGS.ARGUMENT_CHECK = bool

def setApplyUnits(bool: bool) -> None:
    SETTINGS.APPLY_UNITS = bool

# ======= BASE FUNCTIONS =====

def vapourpressure(temp: int | float | NumpyArray | SympySimbol) -> float | UnitFloat | NumpyArray | UnitNumpyArray | SympyExpression | UnitSympyExpression :
    """
    Function that calculate the vapour pressure of the air with argument the temperature (temp).

    Parameters
    ----------
    temp: temperature in °C

    Inputs => Output
    ----------------
    - setApplyUnits(False)

        - INPUT (float) => OUTPUT (float) 
        - INPUT = (int) => OUTPUT = (float) 
        - INPUT = (numpy.ndarray) => OUTPUT = (numpy.ndarray) 
        - INPUT = (sympy.Simbol) => OUTPUT = (sympy.Expr)
    
    - setApplyUnits(True) => default

        - INPUT (float) => OUTPUT (UnitFloat) 
        - INPUT = (int) => OUTPUT = (UnitFloat) 
        - INPUT = (numpy.ndarray) => OUTPUT = (UnitNumpyArray) 
        - INPUT = (sympy.Simbol) => OUTPUT = (UnitSympyExpression)
    """
    return controller(temp, function=getFunctionBackName())

def density_air(temp: int | float | NumpyArray | SympySimbol, rh: int | float | NumpyArray | SympySimbol) -> float | UnitFloat | NumpyArray | UnitNumpyArray | SympyExpression | UnitSympyExpression :
    """
    Function that calculate the desity of the air kg/m3 witha as argument the temperature (temp) and relative humidity (rh).

    Parameters
    ----------
    - temp: temperature in °C
    - rh: relative humidity in %

    Inputs => Output
    ----------------
    - setApplyUnits(False)

        - INPUT (float) => OUTPUT (float) 
        - INPUT = (int) => OUTPUT = (float) 
        - INPUT = (numpy.ndarray) => OUTPUT = (numpy.ndarray) 
        - INPUT = (sympy.Simbol) => OUTPUT = (sympy.Expr)
    
    - setApplyUnits(True) => default

        - INPUT (float) => OUTPUT (UnitFloat) 
        - INPUT = (int) => OUTPUT = (UnitFloat) 
        - INPUT = (numpy.ndarray) => OUTPUT = (UnitNumpyArray) 
        - INPUT = (sympy.Simbol) => OUTPUT = (UnitSympyExpression)
    """
    return controller(temp, rh, function=getFunctionBackName())

def absolutehumidity_kg_air(temp: int | float | NumpyArray | SympySimbol, rh: int | float | NumpyArray | SympySimbol) -> float | UnitFloat | NumpyArray | UnitNumpyArray | SympyExpression | UnitSympyExpression :
    """
    Function that calculate the absolute humidity of 1 kg the air witha as argument the temperature (temp) and relative humidity (rh).

    Parameters
    ----------
    - temp: temperature in °C
    - rh: relative humidity in %

    Inputs => Output
    ----------------
    - setApplyUnits(False)

        - INPUT (float) => OUTPUT (float) 
        - INPUT = (int) => OUTPUT = (float) 
        - INPUT = (numpy.ndarray) => OUTPUT = (numpy.ndarray) 
        - INPUT = (sympy.Simbol) => OUTPUT = (sympy.Expr)
    
    - setApplyUnits(True) => default

        - INPUT (float) => OUTPUT (UnitFloat) 
        - INPUT = (int) => OUTPUT = (UnitFloat) 
        - INPUT = (numpy.ndarray) => OUTPUT = (UnitNumpyArray) 
        - INPUT = (sympy.Simbol) => OUTPUT = (UnitSympyExpression)
    """
    return controller(temp, rh, function=getFunctionBackName())

def absolutehumidity_m3_air(temp: int | float | NumpyArray | SympySimbol, rh: int | float | NumpyArray | SympySimbol) -> float | UnitFloat | NumpyArray | UnitNumpyArray | SympyExpression | UnitSympyExpression:
    """
    Function that calculate the absolute humidity of 1 cubic meter of air witha as argument the temperature (temp) and relative humidity (rh).

    Parameters
    ----------
    - temp: temperature in °C
    - rh: relative humidity in %

    Inputs => Output
    ----------------
    - setApplyUnits(False)

        - INPUT (float) => OUTPUT (float) 
        - INPUT = (int) => OUTPUT = (float) 
        - INPUT = (numpy.ndarray) => OUTPUT = (numpy.ndarray) 
        - INPUT = (sympy.Simbol) => OUTPUT = (sympy.Expr)
    
    - setApplyUnits(True) => default

        - INPUT (float) => OUTPUT (UnitFloat) 
        - INPUT = (int) => OUTPUT = (UnitFloat) 
        - INPUT = (numpy.ndarray) => OUTPUT = (UnitNumpyArray) 
        - INPUT = (sympy.Simbol) => OUTPUT = (UnitSympyExpression)
    """
    return controller(temp, rh, function=getFunctionBackName())

def entalpie_kg_air(temp: int | float | NumpyArray | SympySimbol, rh: int | float | NumpyArray | SympySimbol) -> float | UnitFloat | NumpyArray | UnitNumpyArray | SympyExpression | UnitSympyExpression :
    """
    Function that calculate the entalpie of 1 kilogram air with as argument the temperature (temp) and relative humidity (rh).
    
    Parameters
    ----------
    - temp: temperature in °C
    - rh: relative humidity in %

    Inputs => Output
    ----------------
    - setApplyUnits(False)

        - INPUT (float) => OUTPUT (float) 
        - INPUT = (int) => OUTPUT = (float) 
        - INPUT = (numpy.ndarray) => OUTPUT = (numpy.ndarray) 
        - INPUT = (sympy.Simbol) => OUTPUT = (sympy.Expr)
    
    - setApplyUnits(True) => default

        - INPUT (float) => OUTPUT (UnitFloat) 
        - INPUT = (int) => OUTPUT = (UnitFloat) 
        - INPUT = (numpy.ndarray) => OUTPUT = (UnitNumpyArray) 
        - INPUT = (sympy.Simbol) => OUTPUT = (UnitSympyExpression)
    """
    return controller(temp, rh, function=getFunctionBackName())

def entalpie_m3_air(temp: int | float | NumpyArray | SympySimbol, rh: int | float | NumpyArray | SympySimbol) -> float | UnitFloat | NumpyArray | UnitNumpyArray | SympyExpression | UnitSympyExpression:
    """
    Function that calculate the entalpie of 1 cubic meter air with as argument the temperature (temp) and relative humidity (rh).

    Parameters
    ----------
    - temp: temperature in °C
    - rh: relative humidity in %

    Inputs => Output
    ----------------
    - setApplyUnits(False)

        - INPUT (float) => OUTPUT (float) 
        - INPUT = (int) => OUTPUT = (float) 
        - INPUT = (numpy.ndarray) => OUTPUT = (numpy.ndarray) 
        - INPUT = (sympy.Simbol) => OUTPUT = (sympy.Expr)
    
    - setApplyUnits(True) => default

        - INPUT (float) => OUTPUT (UnitFloat) 
        - INPUT = (int) => OUTPUT = (UnitFloat) 
        - INPUT = (numpy.ndarray) => OUTPUT = (UnitNumpyArray) 
        - INPUT = (sympy.Simbol) => OUTPUT = (UnitSympyExpression)
    """
    return controller(temp, rh, function=getFunctionBackName())

def moisuredeficit_kg_air(temp: int | float | NumpyArray | SympySimbol, rh: int | float | NumpyArray | SympySimbol) -> float | UnitFloat | NumpyArray | UnitNumpyArray | SympyExpression | UnitSympyExpression:
    """
    Function that calculate the moisure dficit of 1 kg air with as argument the temperature (temp) and relative humidity (rh).
    
    Parameters
    ----------
    - temp: temperature in °C
    - rh: relative humidity in %

    Inputs => Output
    ----------------
    - setApplyUnits(False)

        - INPUT (float) => OUTPUT (float) 
        - INPUT = (int) => OUTPUT = (float) 
        - INPUT = (numpy.ndarray) => OUTPUT = (numpy.ndarray) 
        - INPUT = (sympy.Simbol) => OUTPUT = (sympy.Expr)
    
    - setApplyUnits(True) => default

        - INPUT (float) => OUTPUT (UnitFloat) 
        - INPUT = (int) => OUTPUT = (UnitFloat) 
        - INPUT = (numpy.ndarray) => OUTPUT = (UnitNumpyArray) 
        - INPUT = (sympy.Simbol) => OUTPUT = (UnitSympyExpression)
    """
    return controller(temp, rh, function=getFunctionBackName())

def moisuredeficit_m3_air(temp: int | float | NumpyArray | SympySimbol, rh: int | float | NumpyArray | SympySimbol) -> float | UnitFloat | NumpyArray | UnitNumpyArray | SympyExpression | UnitSympyExpression:
    """
    Function that calculate the moisure dficit of 1 cubic meter air with as argument the temperature (temp) and relative humidity (rh).

    Parameters
    ----------
    - temp: temperature in °C
    - rh: relative humidity in %

    Inputs => Output
    ----------------
    - setApplyUnits(False)

        - INPUT (float) => OUTPUT (float) 
        - INPUT = (int) => OUTPUT = (float) 
        - INPUT = (numpy.ndarray) => OUTPUT = (numpy.ndarray) 
        - INPUT = (sympy.Simbol) => OUTPUT = (sympy.Expr)
    
    - setApplyUnits(True) => default

        - INPUT (float) => OUTPUT (UnitFloat) 
        - INPUT = (int) => OUTPUT = (UnitFloat) 
        - INPUT = (numpy.ndarray) => OUTPUT = (UnitNumpyArray) 
        - INPUT = (sympy.Simbol) => OUTPUT = (UnitSympyExpression)
    """
    return controller(temp, rh, function=getFunctionBackName())

def dew_point_factor(temp: int | float | NumpyArray | SympySimbol, rh: int | float | NumpyArray | SympySimbol) -> float | UnitFloat | NumpyArray | UnitNumpyArray | SympyExpression | UnitSympyExpression:
    """
    Function that calculate the dewpoint factor of air with as argument the temperature (temp) and relative humidity (rh).
    
    Parameters
    ----------
    - temp: temperature in °C
    - rh: relative humidity in %

    Inputs => Output
    ----------------
    - setApplyUnits(False)

        - INPUT (float) => OUTPUT (float) 
        - INPUT = (int) => OUTPUT = (float) 
        - INPUT = (numpy.ndarray) => OUTPUT = (numpy.ndarray) 
        - INPUT = (sympy.Simbol) => OUTPUT = (sympy.Expr)
    
    - setApplyUnits(True) => default

        - INPUT (float) => OUTPUT (UnitFloat) 
        - INPUT = (int) => OUTPUT = (UnitFloat) 
        - INPUT = (numpy.ndarray) => OUTPUT = (UnitNumpyArray) 
        - INPUT = (sympy.Simbol) => OUTPUT = (UnitSympyExpression)
    """
    return controller(temp, rh, function=getFunctionBackName())

def dew_point_temperature(temp: int | float | NumpyArray | SympySimbol, rh: int | float | NumpyArray | SympySimbol) -> float | UnitFloat | NumpyArray | UnitNumpyArray | SympyExpression | UnitSympyExpression:
    """
    Function that calculate the dewpoint temperature of air with as argument the temperature (temp) and relative humidity (rh).

    Parameters
    ----------
    - temp: temperature in °C
    - rh: relative humidity in %

    Inputs => Output
    ----------------
    - setApplyUnits(False)

        - INPUT (float) => OUTPUT (float) 
        - INPUT = (int) => OUTPUT = (float) 
        - INPUT = (numpy.ndarray) => OUTPUT = (numpy.ndarray) 
        - INPUT = (sympy.Simbol) => OUTPUT = (sympy.Expr)
    
    - setApplyUnits(True) => default

        - INPUT (float) => OUTPUT (UnitFloat) 
        - INPUT = (int) => OUTPUT = (UnitFloat) 
        - INPUT = (numpy.ndarray) => OUTPUT = (UnitNumpyArray) 
        - INPUT = (sympy.Simbol) => OUTPUT = (UnitSympyExpression)
    """
    return controller(temp, rh, function=getFunctionBackName())


if __name__ == '__main__':
    
    pass
