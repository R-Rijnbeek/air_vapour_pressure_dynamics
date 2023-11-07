import sympy
from decorators import argument_check

@argument_check((float,int))
def vapourpressure(temp: int | float) -> float:
    temp=float(temp)
    return 10**(8.07131 - (1730.63/(233.426+temp)))*133.322

@argument_check((float,int),(float,int))
def density_air(temp: int | float, rh: int | float) -> float:
    temp=float(temp)
    rh=float(rh)
    return 219.56*(1 +absolutehumidity_kg_air(temp, rh)/1000)/((0.622 + absolutehumidity_kg_air(temp, rh)/1000)*(temp + 273))

@argument_check((float,int),(float,int))
def absolutehumidity_kg_air(temp: int | float,rh: int | float) -> float:
    temp=float(temp)
    rh=float(rh)
    waterdd = vapourpressure(temp)
    return 0.622*waterdd*(rh/100)/(101325. - waterdd*(rh/100))*1000

@argument_check((float,int),(float,int))
def absolutehumidity_m3_air(temp: int | float, rh: int | float) -> float:
    temp=float(temp)
    rh=float(rh)
    return (absolutehumidity_kg_air(temp, rh)*density_air(temp, rh))
    
@argument_check((float,int),(float,int))
def entalpie_kg_air(temp: int | float, rh: int | float) -> float:
    temp=float(temp)
    rh=float(rh)
    return ((1.005*temp) + absolutehumidity_kg_air(temp, rh)*(2500.6 + (1.85*temp))/1000)

@argument_check((float,int),(float,int))
def entalpie_m3_air(temp: int | float, rh: int | float) -> float:
    temp=float(temp)
    rh=float(rh)
    return (entalpie_kg_air(temp, rh)*density_air(temp, rh))
    
@argument_check((float,int),(float, int))
def moisuredeficit_kg_air(temp: int | float,rh: int | float) -> float:
    temp=float(temp)
    rh=float(rh)
    return (absolutehumidity_kg_air(temp, 100.)-absolutehumidity_kg_air(temp, rh))

@argument_check((float,int),(float,int))
def moisuredeficit_m3_air(temp: int | float, rh: int | float) -> float:
    temp=float(temp)
    rh=float(rh)
    return (moisuredeficit_kg_air(temp, rh)*density_air(temp, rh))

@argument_check((float,int),(float,int))
def dew_point_factor(temp: int | float, rh: int | float) -> float:
    temp=float(temp)
    rh=float(rh)
    return (sympy.log(rh/100.) + 17.67*temp/(243.5 + temp))

@argument_check((float,int),(float,int))
def dew_point_temperature(temp: int | float, rh: int | float) -> float:
    temp=float(temp)
    rh=float(rh)
    return (243.5*dew_point_factor(temp, rh))/(17.67 - dew_point_factor(temp, rh))


if __name__ == '__main__':

    try:
        temp = 45.
        rh = 90.

        vp = vapourpressure(temp)
        ad = density_air(temp, rh)
        ab_hu_kg =absolutehumidity_kg_air(temp, rh)
        ab_hu_m3 = absolutehumidity_m3_air(temp, rh)
        en_kg = entalpie_kg_air(temp, rh)
        en_m3 = entalpie_m3_air(temp, rh)
        mois_def_kg = moisuredeficit_kg_air(temp,rh)
        mois_def_m3 = moisuredeficit_m3_air(temp, rh)
        dewpoint = dew_point_factor(temp, rh)
        dewpoint_temp = dew_point_temperature(temp, rh)
        
        print(f"vp => {vp}")
        print(f"ad => {ad}")
        print(f"ab_hu_kg => {ab_hu_kg}")
        print(f"ab_hu_m3 => {ab_hu_m3}")
        print(f"en_kg => {en_kg}")
        print(f"en_m3 => {en_m3}")
        print(f"mois_def_kg => {mois_def_kg}")
        print(f"mois_def_m3 => {mois_def_m3}")
        print(f"dewpoint => {dewpoint}")
        print(f"dewpoint_temp => {dewpoint_temp}")
    except Exception as exc:
        print(exc)
