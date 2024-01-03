# -*- coding: utf-8 -*-

# ====== IMPORTS ===============

import sys
sys.path.append('.')
from src.air_vapour_pressure_dynamics import (  
#from air_vapour_pressure_dynamics import ( 
                                            density_air, 
                                            setArgumentCheck,
                                            setApplyUnits
                                            )

# ====== FUNCTION DEFINITION ====

def testProcess_1():
    try:
        temp = 25.
        rh = "90"
        setArgumentCheck(False)
        setApplyUnits(False)
        dens = density_air(temp, rh)
        print(f"It is not suppose to do the calculation {dens}")
        return False
    except Exception as exc:
        print(exc)
        print("TEST 1 SUCCESFUL")
        return True
    
def testProcess_2():
    try:
        temp = 25
        rh = 90
        dens = density_air(temp, rh)
        dens_unit = dens.unit
        return False
    except Exception as exc:
        print(exc)
        print("TEST 2 SUCCESFUL")
        return True
    
def testProcess_3():
    try:
        temp = 25
        rh = 90
        setApplyUnits(True)
        dens = density_air(temp, rh)
        dens_unit = dens.unit
        print(dens_unit)
        print("TEST 3 SUCCESFUL")
        return True
    except Exception as exc:
        print(exc)
        return False

def testProcess_4():
    try:
        temp = 25
        rh = "90"
        setArgumentCheck(True)
        density_air(temp, rh)
        return False
    except Exception as exc:
        print(exc)
        print("TEST 4 SUCCESFUL")
        return True
    
def testProcess_5():
    try:
        setArgumentCheck("Trues")
        return False
    except Exception as exc:
        print(exc)
        print("TEST 5 SUCCESFUL")
        return True

def testProcess_6():
    try:
        setArgumentCheck("Trues")
        return False
    except Exception as exc:
        print(exc)
        print("TEST 6 SUCCESFUL")
        return True
    
def testProcess_7():
    try:
        temp = "John"
        rh = "Doe"
        setArgumentCheck(False)
        density_air(temp, rh)
        return False
    except Exception as exc:
        print(exc)
        print("TEST 7 SUCCESFULL")
        return True
    
def settings_test_process():
    try:
        t1 = testProcess_1()
        t2 = testProcess_2()
        t3 = testProcess_3()
        t4 = testProcess_4()
        t5 = testProcess_5()
        t6 = testProcess_6()
        t7 = testProcess_7()
        if (t1 and t2 and t3 and t4 and t5 and t6 and t7):
            print("Settings test Process pass successfully!!" )
            return True
        else:
            print("WARNING: Settings test Process does not pass.")
            return False
    except Exception as exc:
        print(f"ERROR: {exc}")
        return False

    
if __name__ == '__main__':

    settings_test_process()