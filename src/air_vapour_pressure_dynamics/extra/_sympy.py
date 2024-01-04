# -*- coding: utf-8 -*-

# ====== IMPORTS ===============

from basic_decorators import argument_check

from ..initialize import SETTINGS, sp

# ======= FUNCTIONS ===========

if SETTINGS.SYMPY_DETECTED :
    class UnitSympyExpression(sp.UnevaluatedExpr):

        @argument_check(object, sp.Expr, str)
        def __new__(self, value, unit=None):
            return sp.UnevaluatedExpr.__new__(self, value)
        
        @argument_check(object, sp.Expr, str)
        def __init__(self, value, unit=None):
            self.unit = unit
            super()
else:
    class UnitSympyExpression():
        pass

class SympySimbol():
    """sympy Simbol: sympy.Simbol"""
    pass
class SympyExpression():
    """sympy Expression: sympy.Expr"""
    pass

def log_sympy(value):
    return sp.log(value)

def isSympyExpr(value):
    return SETTINGS.SYMPY_DETECTED and isinstance(value, sp.Expr)

if __name__ == '__main__':
    
    pass