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

def importNumpy():
    try:
        global np
        import numpy as np
        return True
    except Exception as exc:
        print(f"Numpy is not installed in the Python Environment. The test is useless without the installation of 'numpy': {exc}")
        return False
    
def CreateTestData():
    temp = np.random.uniform(low=0., high=50., size=(50,))
    rh = np.random.uniform(low=0., high=100., size=(50,))
    return temp, rh

def numpyCalculations(temp, rh):
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
    print("numpy Calculation process pass succesfuly\n")
    return True

def numpyApplyUnits(temp, rh):
    try:
        abs_Humidity_kg = absolutehumidity_kg_air(temp, rh)
        print(abs_Humidity_kg.unit)
        test1 = True
    except:
        test1 = False

    try:
        setApplyUnits(False)
        abs_Humidity_kg = absolutehumidity_kg_air(temp, rh)
        print(abs_Humidity_kg.unit)
        test2 = False
    except Exception as exc:
        print(f"Expected error: {exc}")
        test2 = True

    try:
        setApplyUnits(True)
        abs_Humidity_kg = absolutehumidity_kg_air(temp, rh)
        print(abs_Humidity_kg.unit)
        test3 = True
    except:
        test3 = False
    
    if test1 and test2 and test3 :
        print("numpyApplyUnits pass the test!!")
        return True
    else:
        print("numpyApplyUnits does not pass the test")
        return False


def numpy_test_Process():
    try:
        if importNumpy():
            temp, rh = CreateTestData()
            test1 = numpyCalculations(temp, rh)
            test2 = numpyApplyUnits(temp, rh)
            if test1 and test2:
                print("Numpy test Process pass successfully!!" )
                return True
            else:
                print("WARNING: Numpy test process does not pass")
                return False
        else:
            print("Test Pass succesfully without the numpy installation")
            return True
    except Exception as exc:
        print(f"ERROR: unespected Error: {exc}")
        return False

if __name__ == '__main__':

    numpy_test_Process()
