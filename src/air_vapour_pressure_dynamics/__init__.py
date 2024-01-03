# -*- coding: utf-8 -*-
"""
air_vapour_pressure_dynamics: Repository with the basic functions related with the temperature, relative humidity, absolute humidity and entalpy of the air with the different variable transformations
"""
__author__  = "Robert Rijnbeek"
__email__   = "robert270384@gmail.com"
__version__ = "1.8.4"

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
