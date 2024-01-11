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

def importSympy():
    try:
        global sp
        import sympy as sp
        return True
    except Exception as exc:
        print(f"Sympy is not installed in the Python Environment. The test is useless without the installation of 'sympy': {exc}")
        return False


def calculationProcess():

    setApplyUnits(False)

    x = 1.5
    delta_x = 0.2
    y = 2.4
    delta_y = -0.2

    X = sp.Symbol("X")
    Y = sp.Symbol("Y")

    diff_method_by_X = sp.diff(absolutehumidity_kg_air(X,Y),X)
    diff_method_by_Y = sp.diff(absolutehumidity_kg_air(X,Y),Y)

    delta_Temp_contribution = sp.N(diff_method_by_X.subs([(X, x), (Y, y)]))
    delta_RH_contribution = sp.N(diff_method_by_Y.subs([(X, x), (Y, y)]))

    result = delta_Temp_contribution * delta_x + delta_RH_contribution * delta_y

    return float(result)

if __name__ == '__main__':
    
    importSympy()
    print(calculationProcess())