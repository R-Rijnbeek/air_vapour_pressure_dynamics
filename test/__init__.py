from numpy_testing import numpy_test_Process
from settings_testing import settings_test_process
from calculation_testing import calculation_test_Process
from sympy_testing import sympy_test_Process


def global_test_Process():
    try:
        test1 = calculation_test_Process()
        test2 = settings_test_process()
        test3 = numpy_test_Process()
        test4 = sympy_test_Process()
        if test1 and test2 and test3 and test4 :
            print("INFO: Global Test Process pass succesfully!!")
            return True
        else:
            print("WARNING: Global test process does not pass. Look log foe ore info")
            return False
    except Exception as exc:
        print(f"ERROR: {exc}")
        return False
    

if __name__ == '__main__':

    global_test_Process()

