# -*- coding: utf-8 -*-

# ====== IMPORTS ===============

#import sys
#sys.path.append('.')
#from src.air_vapour_pressure_dynamics import (  
from air_vapour_pressure_dynamics import (
                                            vapourpressure, 
                                            density_air, 
                                            absolutehumidity_kg_air, 
                                            absolutehumidity_m3_air, 
                                            entalpie_kg_air, 
                                            entalpie_m3_air, 
                                            moisuredeficit_kg_air, 
                                            moisuredeficit_m3_air, 
                                            dew_point_factor, 
                                            dew_point_temperature,
                                            setApplyU
                                            )

# ====== FUNCTION DEFINITION ====

def importSympy():
    try:
        global sp
        import sympy as sp
        return True
    except Exception as exc:
        print(f"Sympy is not installed in the Python Environment. The test is useless without the installation of 'sympy': {exc}")
        return False
    
def CreateTestData():
    temp = sp.Symbol("temp")
    rh = sp.Symbol("rh")
    return temp, rh

def sympyCalculations(temp, rh):
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
    print("sympy Calculation process pass succesfuly\n")
    return True

def sympyApplyUnits(temp, rh):
    try:
        abs_Humidity_kg = absolutehumidity_kg_air(temp, rh)
        print(abs_Humidity_kg.unit)
        test1 = True
    except:
        test1 = False

    try:
        setApplyU(False)
        abs_Humidity_kg = absolutehumidity_kg_air(temp, rh)
        print(abs_Humidity_kg.unit)
        test2 = False
    except Exception as exc:
        print(f"Expected error: {exc}")
        test2 = True

    try:
        setApplyU(True)
        abs_Humidity_kg = absolutehumidity_kg_air(temp, rh)
        print(abs_Humidity_kg.unit)
        test3 = True
    except:
        test3 = False
    
    if test1 and test2 and test3 :
        print("sympyApplyUnits pass the test!!")
        return True
    else:
        print("sympyApplyUnits does not pass the test")
        return False


def sympy_test_Process():
    try:
        if importSympy():
            temp, rh = CreateTestData()
            test1 = sympyCalculations(temp, rh)
            test2 = sympyApplyUnits(temp, rh)
            if test1 and test2:
                print("sympy test Process pass successfully!!" )
                return True
            else:
                print("WARNING: sympy test process does not pass")
                return False
        else:
            print("Test Pass succesfully without the sympy installation")
            return True
    except Exception as exc:
        print(f"ERROR: unespected Error: {exc}")
        return False

if __name__ == '__main__':

    sympy_test_Process()