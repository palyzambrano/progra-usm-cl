hours_now = int(input('Hora actual: '))
hours_to_add = int(input('Cantidad de horas: '))
time_then = ((hours_now + hours_to_add) % 12) % 12

print(f'En {hours_to_add} horas, el reloj marcara las {time_then}')
