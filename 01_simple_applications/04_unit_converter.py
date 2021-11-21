# http://progra.usm.cl/apunte/ejercicios/1/conversion-unidades-longitud.html

CENTIMETER_INCH = 2.54

longitude = input('Ingrese longitud: ')
inches = float(longitude) / CENTIMETER_INCH

print(f'{longitude} cm = {inches} in')
