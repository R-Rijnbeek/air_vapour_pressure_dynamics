# -*- coding: utf-8 -*-

# ====== IMPORTS ===============

from _test_settings_ import USE_INSTALLED_PACKAGE

if USE_INSTALLED_PACKAGE :
    from air_vapour_pressure_dynamics import *
else:
    import sys
    sys.path.append('.')
    from src.air_vapour_pressure_dynamics import *


# ====== FUNCTION DEFINITION ====

def testValues(temp, rh):

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

def calculation_test_Process():
    data_sets = [
                    (25,90),
                    (25.,90.),
                    (23, 40),
                    ("25","90"),
                    (True, False)
                ]
    for (temp, rh) in data_sets:
        try:
            testValues(temp,rh)
        except Exception as exc:
            print(f"{exc}\n")

    print("TEST SUCCESFULL!!")
    return True


if __name__ == '__main__':

    calculation_test_Process()