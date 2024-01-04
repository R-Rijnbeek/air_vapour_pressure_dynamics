import sys
sys.path.append('.')
from src.air_vapour_pressure_dynamics.core import (  argumentChecker )
from src.air_vapour_pressure_dynamics import (  vapourpressure )

print(vapourpressure(10))