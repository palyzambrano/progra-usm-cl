# http://progra.usm.cl/apunte/ejercicios/1/pitagoras.html

from math import pow, sqrt

a = float(input('Ingrese cateto a: '))
b = float(input('Ingrese cateto b: '))
hypotenuse = sqrt(pow(a, 2) + pow(b, 2))

print(f'La hipotenusa es {hypotenuse}')
