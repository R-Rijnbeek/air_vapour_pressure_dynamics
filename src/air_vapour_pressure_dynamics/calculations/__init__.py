# -*- coding: utf-8 -*-

# ======== IMPORTS ===========

from ..initialize import SETTINGS
from ..extra._float import log_float
from ..extra._numpy import NumpyArray, log_numpy, isNumpyValue
from ..extra._sympy import SympyExpression, SympySimbol, log_sympy, isSympyExpr


# ======= FUNCTIONS ===========

def LOG(value):
    if isNumpyValue(value):
        return log_numpy(value)
    if isSympyExpr(value):
        return log_sympy(value)
    if value < SETTINGS.CERO_LOG :
        value = SETTINGS.CERO_LOG
    return log_float(value)

def _vapourpressure(temp: int | float | NumpyArray | SympySimbol) -> float | NumpyArray | SympyExpression:
    return 10**(8.07131 - (1730.63/(233.426+temp)))*133.322

def _density_air(temp: int | float | NumpyArray | SympySimbol, rh: int | float | NumpyArray | SympySimbol) -> float | NumpyArray | SympyExpression:
    return 219.56*(1 +_absolutehumidity_kg_air(temp, rh)/1000)/((0.622 + _absolutehumidity_kg_air(temp, rh)/1000)*(temp + 273))

def _absolutehumidity_kg_air(temp: int | float | NumpyArray | SympySimbol, rh: int | float | NumpyArray | SympySimbol) -> float | NumpyArray | SympyExpression:
    waterdd = _vapourpressure(temp)
    return (0.622*waterdd*(rh/100)/(101325. - waterdd*(rh/100))*1000)

def _absolutehumidity_m3_air(temp: int | float | NumpyArray | SympySimbol, rh: int | float | NumpyArray | SympySimbol) -> float | NumpyArray | SympyExpression:
    return (_absolutehumidity_kg_air(temp, rh)*_density_air(temp, rh))
    
def _entalpie_kg_air(temp: int | float | NumpyArray | SympySimbol, rh: int | float | NumpyArray | SympySimbol) -> float | NumpyArray | SympyExpression:
    return ((1.005*temp) + _absolutehumidity_kg_air(temp, rh)*(2500.6 + (1.85*temp))/1000)

def _entalpie_m3_air(temp: int | float | NumpyArray | SympySimbol ,rh: int | float | NumpyArray | SympySimbol) -> float | NumpyArray | SympyExpression:
    return (_entalpie_kg_air(temp, rh)*_density_air(temp, rh))
    
def _moisuredeficit_kg_air(temp: int | float | NumpyArray | SympySimbol, rh: int | float | NumpyArray | SympySimbol) -> float | NumpyArray | SympyExpression:
    return (_absolutehumidity_kg_air(temp, 100.)-_absolutehumidity_kg_air(temp, rh))

def _moisuredeficit_m3_air(temp: int | float | NumpyArray | SympySimbol, rh: int | float | NumpyArray | SympySimbol) -> float | NumpyArray | SympyExpression:
    return (_moisuredeficit_kg_air(temp, rh)*_density_air(temp, rh))

def _dew_point_factor(temp: int | float | NumpyArray | SympySimbol, rh: int | float | NumpyArray | SympySimbol) -> float | NumpyArray | SympyExpression:
    return (LOG(rh/100.) + 17.67*temp/(243.5 + temp))

def _dew_point_temperature(temp: int | float | NumpyArray | SympySimbol, rh: int | float | NumpyArray | SympySimbol) -> float | NumpyArray | SympyExpression:
    return (243.5*_dew_point_factor(temp, rh))/(17.67 - _dew_point_factor(temp, rh))

# ======= CONFIGURATION DICT ===========

FUNCTION_CONFIG = {
    "vapourpressure": {
        "function":_vapourpressure, 
        "unit": "Pa"
        },
    "density_air" : {
        "function":_density_air,
        "unit": "kg/m^3"
        },
    "absolutehumidity_kg_air" : {
        "function":_absolutehumidity_kg_air, 
        "unit": "g/Kg"
        },
    "absolutehumidity_m3_air" : {
        "function":_absolutehumidity_m3_air, 
        "unit": "g/m³"
        },
    "entalpie_kg_air" : {
        "function":_entalpie_kg_air,
        "unit": "KJ/Kg"
        },
    "entalpie_m3_air" : {
        "function":_entalpie_m3_air, 
        "unit": "KJ/m³"
        },
    "moisuredeficit_kg_air" : {
        "function":_moisuredeficit_kg_air, 
        "unit": "gr/Kg"
        },
    "moisuredeficit_m3_air" : {
        "function":_moisuredeficit_m3_air, 
        "unit": "gr/m³"
        },
    "dew_point_factor" : {
        "function":_dew_point_factor, 
        "unit": ""
        },
    "dew_point_temperature": {
        "function":_dew_point_temperature, 
        "unit": "°C"
        }
}

if __name__ == '__main__':
    
    pass