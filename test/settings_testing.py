# -*- coding: utf-8 -*-

# ====== IMPORTS ===============

from air_vapour_pressure_dynamics import ( density_air, 
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
        density_air(temp, rh)
        return False
    except Exception as exc:
        print("TEST SUCCESFUL")
        return True
    
if __name__ == '__main__':

    testProcess_1()