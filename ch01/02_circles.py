import math

radius = input("Ingrese radio: ")
radius = float(radius)
perimeter = 2 * (math.pi * radius)
area = math.pi * math.pow(radius, 2)

print("Perimetro: " + str(perimeter))
print("Área: " + str(area))
