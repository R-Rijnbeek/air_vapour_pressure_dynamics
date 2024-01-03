import sys
sys.path.append('.')
from src.air_vapour_pressure_dynamics import (  absolutehumidity_m3_air )

print(absolutehumidity_m3_air(20,90))