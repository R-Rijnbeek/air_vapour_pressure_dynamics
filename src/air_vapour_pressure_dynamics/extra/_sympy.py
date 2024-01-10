# -*- coding: utf-8 -*-

# ====== IMPORTS ===============

from basic_decorators import argument_check

from ..initialize import SETTINGS, sp

# ======= CONSTANTS ============

sympySymbol = sp.Symbol if SETTINGS.SYMPY_DETECTED else None
sympyExpr = sp.Expr if SETTINGS.SYMPY_DETECTED else None

# ======= CLASSES ============

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

# ======= FUNCTIONS ===========

@argument_check(sympyExpr)
def log_sympy(value: sympyExpr) -> sympyExpr :
    return sp.log(value)

def isSympyExpr(value: object) -> bool:
    return SETTINGS.SYMPY_DETECTED and isinstance(value, sp.Expr)

if __name__ == '__main__':
    
    pass