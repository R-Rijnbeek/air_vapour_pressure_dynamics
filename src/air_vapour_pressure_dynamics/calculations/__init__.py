import math
from ..initialize import SETTINGS, np, sp

def LOG(value):
    if SETTINGS.NUMPY_DETECTED and isinstance(value, np.ndarray):
        return np.log(value)
    if SETTINGS.SYMPY_DETECTED and isinstance(value, sp.Expr):
        return sp.log(value)
    if value < SETTINGS.CERO_LOG :
        value = SETTINGS.CERO_LOG
    return math.log(value)

def _vapourpressure(temp: int | float) -> float:
    return 10**(8.07131 - (1730.63/(233.426+temp)))*133.322

def _density_air(temp: int | float, rh: int | float) -> float:
    return 219.56*(1 +_absolutehumidity_kg_air(temp, rh)/1000)/((0.622 + _absolutehumidity_kg_air(temp, rh)/1000)*(temp + 273))

def _absolutehumidity_kg_air(temp: int | float,rh: int | float) -> float:
    waterdd = _vapourpressure(temp)
    return (0.622*waterdd*(rh/100)/(101325. - waterdd*(rh/100))*1000)

def _absolutehumidity_m3_air(temp: int | float, rh: int | float) -> float:
    return (_absolutehumidity_kg_air(temp, rh)*_density_air(temp, rh))
    
def _entalpie_kg_air(temp: int | float, rh: int | float) -> float:
    return ((1.005*temp) + _absolutehumidity_kg_air(temp, rh)*(2500.6 + (1.85*temp))/1000)

def _entalpie_m3_air(temp: int | float, rh: int | float) -> float:
    return (_entalpie_kg_air(temp, rh)*_density_air(temp, rh))
    
def _moisuredeficit_kg_air(temp: int | float,rh: int | float) -> float:
    return (_absolutehumidity_kg_air(temp, 100.)-_absolutehumidity_kg_air(temp, rh))

def _moisuredeficit_m3_air(temp: int | float, rh: int | float) -> float:
    return (_moisuredeficit_kg_air(temp, rh)*_density_air(temp, rh))

def _dew_point_factor(temp: int | float, rh: int | float) -> float:
    return (LOG(rh/100.) + 17.67*temp/(243.5 + temp))

def _dew_point_temperature(temp: int | float, rh: int | float) -> float:
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