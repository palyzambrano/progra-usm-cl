# http://progra.usm.cl/apunte/ejercicios/1/circulos.html

from math import pi, pow

radius = input("Ingrese radio: ")
radius = float(radius)
perimeter = 2 * (pi * radius)
area = pi * pow(radius, 2)

print("Perimetro: " + str(perimeter))
print("Área: " + str(area))
