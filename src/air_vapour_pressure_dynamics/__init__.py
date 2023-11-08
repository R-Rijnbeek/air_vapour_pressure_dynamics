# -*- coding: utf-8 -*-
"""
air_vapour_pressure_dynamics: Repository with the basic functions related with the temperature, relative humidity, absolute humidity and entalpy of the air with the different variable transformations
"""
__author__  = "Robert Rijnbeek"
__email__   = "robert270384@gmail.com"
__version__ = "1.0.0"

# ======== IMPORTS ===========

import math

# ======== DECORATORS ========

def argument_check(*types_args,**types_kwargs):
    """
    INFORMATION: Standard decorator with arguments that is used to verify the agument (arg) or opttion arguments (kwargs) 
                 of linked function. If the decorator see an not valid argument or kwarg in the funcion. 
                 There will be generate an exception with the explanation with the argument that is not correct.
    INPUT: 
        - *types_args: Tuple of arguments where eatch argument can will be a a type (simple object type) or types of 
                       object types (when you define a tuple of objects). Or if it is defined as an list. Those values of the list 
                       are the option of the values thay those arguments can will be.
        - **types_kwargs: dict of kwargs where eatch argument can will be a a type (simple object type) or types of object types 
                          (when you define a tuple of objects). Or if it is defined as an list for a key of a dict. The keyvalue of a
                          dict must be in the defined list liked to that veyvalue.
    OUTPUT:
        - ERROR: EXECUTION OF THE LINKED FUNCTION
        - NO ERROR: A DEFINED EXCEPTION

    """
    def check_accepts(f):
        def function_wrapper(*args, **kwargs):
            assert len(args) is len(types_args), f"In function '{f.__name__}{args}' and option values: {kwargs}, lenght of argumnets {args} is not the same as types_args {types_args}"
            for (arg, type_arg) in zip(args, types_args):
                if isinstance(type_arg,list):
                    assert arg in type_arg, f"In function '{f.__name__}{args}' and option values: {kwargs}, argument {arg} is not in list {type_arg}" 
                else:
                    assert isinstance(arg, type_arg), f"In function '{f.__name__}{args}' and option values: {kwargs}, arg {arg} does not match {type_arg}" 
            for kwarg,value in kwargs.items():
                assert kwarg in types_kwargs , f"In function '{f.__name__}{args}' and option values: {kwargs}, the kwarg ('{kwarg}':{value}) is not a valid option value" 
                espected_format = types_kwargs[kwarg]
                if isinstance(espected_format,list): 
                    assert value in espected_format, f"In function '{f.__name__}{args}' and option values: {kwargs}, the kwarg value ('{kwarg}':{value}) is not in list {espected_format}" 
                else:
                    assert isinstance(value, espected_format), f"In function '{f.__name__}{args}' and option values: {kwargs}, kwarg value ('{kwarg}':{value}) does not match with {espected_format}" 
            return f(*args, **kwargs)
        function_wrapper.__name__ = f.__name__
        return function_wrapper
    return check_accepts 


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