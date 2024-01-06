# -*- coding: utf-8 -*-
""" air_vapour_pressure_dynamics: 
    =============================

    Repository with the basic functions related with the temperature, relative humidity, absolute humidity and entalpy of the air.

    How it work:
    -----------

    1. Importing specific functions::

        >>> from air_vapour_pressure_dynamics import vapourpressure, absolutehumidity_kg_air,....

    2. Importing the whole package::

        >>> import air_vapour_pressure_dynamics

    Setters:
    --------

    - put or remove argument validation::

        >>> setArgumentCheck(bool)

    - Put or remove Units to results of validation::

        >>> setApplyUnits(bool)

    Examples:
    ---------

    - Basic Example::

        >>> from air_vapour_pressure_dynamics import absolutehumidity_kg_air
        >>> temp = 25.5
        >>> rh = 86.8
        >>> absolutehumidity_kg_air(temp, rh)

        >>> 17.83208626438017

    - Get units of calculation::
        
        >>> ....
        >>> temp = 25.5
        >>> rh = 86.8
        >>> ab_hu = absolutehumidity_kg_air(temp, rh)
        >>> ab_hu.units

        >>> 'g/Kg'

    Compatibility:
    --------------
    - Numpy
    - Sympy

    But it is not neccesary to install those packages if you are going to use it only with generic integers or float numbers

    Content:
    --------

    - Functions:

        - vapourpressure(temp)
        - density_air(temp, rh)
        - absolutehumidity_kg_air(temp, rh)
        - absolutehumidity_m3_air(temp, rh)
        - entalpie_kg_air(temp, rh)
        - entalpie_m3_air(temp, rh)
        - moisuredeficit_kg_air(temp, rh)
        - moisuredeficit_m3_air(temp, rh)
        - dew_point_factor(temp, rh)
        - dew_point_temperature(temp, rh)

    - Setters:

        - setApplyUnits(bool)
        - setArgumentCheck(bool)

"""
__author__  = "Robert Rijnbeek"
__email__   = "robert270384@gmail.com"
__version__ = "1.8.8"

# ======== IMPORTS ===========

from .base import *

__all__ = [ # SETTINGS
            "setArgumentCheck", 
            "setApplyUnits",
            # CORE FUNCTIONS
            "vapourpressure",
            "density_air",
            "absolutehumidity_kg_air",
            "absolutehumidity_m3_air",
            "entalpie_kg_air",
            "entalpie_m3_air",
            "moisuredeficit_kg_air",
            "moisuredeficit_m3_air",
            "dew_point_factor",
            "dew_point_temperature"
            ]

if __name__ == '__main__':
    
    pass
