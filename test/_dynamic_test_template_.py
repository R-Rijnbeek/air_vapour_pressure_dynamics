import sys
sys.path.append('.')
from src.air_vapour_pressure_dynamics import (  absolutehumidity_kg_air )

print(absolutehumidity_kg_air( 25.5, 86.8))