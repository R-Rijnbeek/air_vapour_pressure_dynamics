# -*- coding: utf-8 -*-

from air_vapour_pressure_dynamics import (vapourpressure, 
                                          density_air, 
                                          absolutehumidity_kg_air, 
                                          absolutehumidity_m3_air, 
                                          entalpie_kg_air, 
                                          entalpie_m3_air, 
                                          moisuredeficit_kg_air, 
                                          moisuredeficit_m3_air, 
                                          dew_point_factor, 
                                          dew_point_temperature
                                          )

def numpy_test_Process(temp, rh):
    vp = vapourpressure(temp)
    ad = density_air(temp, rh)
    ab_hu_kg = absolutehumidity_kg_air(temp, rh)
    ab_hu_m3 = absolutehumidity_m3_air(temp, rh)
    en_kg = entalpie_kg_air(temp, rh)
    en_m3 = entalpie_m3_air(temp, rh)
    mois_def_kg = moisuredeficit_kg_air(temp,rh)
    mois_def_m3 = moisuredeficit_m3_air(temp, rh)
    dewpoint = dew_point_factor(temp, rh)
    dewpoint_temp = dew_point_temperature(temp, rh)
    print(  f"""vp => {vp}\nad => {ad}\nab_hu_kg => {ab_hu_kg}\nab_hu_m3 => {ab_hu_m3}\nen_kg => {en_kg}\nen_m3 => {en_m3}\nmois_def_kg => {mois_def_kg}\nmois_def_m3 => {mois_def_m3}\ndewpoint => {dewpoint}\ndewpoint_temp => {dewpoint_temp}\n""")
    return True






if __name__ == '__main__':

    try:
        import numpy as np
        temp = np.random.uniform(low=0., high=50., size=(50,))
        rh = np.random.uniform(low=0., high=100., size=(50,))

        numpy_test_Process(temp,rh)


    except Exception as exc:
        print(f"{exc}")
