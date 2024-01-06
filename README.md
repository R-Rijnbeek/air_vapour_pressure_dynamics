# Air Vapour Pressure Dynamics

Repository with the basic functions related with the temperature, relative humidity, absolute humidity and entalpy of the air.

## How it work:

1. Create en python environent and install the package using de command:
    ````
    pip install air_vapour_pressure_dynamics
    ````
2. Once you get installed the package you can import the packahe in the python module by:
    ````python
    from air_vapour_pressure_dynamics import vapourpressure, absolutehumidity_kg_air,....
    ````
    or 

    ````python
    import air_vapour_pressure_dynamics
    ````

## Setters:

1. put or remove argument validation::
    ````python
    setArgumentCheck(bool)
    ````
2. Put or remove Units to results of validation::
    ````python
    setApplyUnits(bool)
    ````

## Examples:

### Basic Example::
````python
from air_vapour_pressure_dynamics import absolutehumidity_kg_air
temp = 25.5
rh = 86.8
absolutehumidity_kg_air(temp, rh)

17.83208626438017
````

### Get units of calculation::
````python
from air_vapour_pressure_dynamics import absolutehumidity_kg_air
temp = 25.5
rh = 86.8
ab_hu = absolutehumidity_kg_air(temp, rh)
ab_hu.units

'g/Kg'
````
## Compatibility:

* Numpy
* Sympy

But it is not neccesary to install those packages if you are going to use it only with generic integers or float numbers

## Content:

* Functions:

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

* Setters:

    - setApplyUnits(bool)
    - setArgumentCheck(bool)


And that it!!