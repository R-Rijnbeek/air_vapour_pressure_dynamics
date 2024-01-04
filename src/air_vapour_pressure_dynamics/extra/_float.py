# -*- coding: utf-8 -*-

# ====== IMPORTS ===============

import math
from basic_decorators import argument_check

# ======= FUNCTIONS ===========

class UnitFloat(float):
    @argument_check(object, float, str)
    def __new__(self, value, unit=None):
       return float.__new__(self, value)
    
    @argument_check(object ,float, str)
    def __init__(self, value, unit=None):
        self.unit = unit

def log_float(value):
    return math.log(value)

if __name__ == '__main__':
    
    pass