import math

a = float(input('Ingrese cateto a: '))
b = float(input('Ingrese cateto b: '))
hypotenuse = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

print(f'La hipotenusa es {hypotenuse}')
