# http://progra.usm.cl/apunte/ejercicios/1/que-nota-necesito.html

TERMS_THIRD_PART = 60

term_01 = input('Ingrese nota certamen 1: ')
term_02 = input('Ingrese nota certamen 2: ')
lab = input('Ingrese nota laboratorio: ')

term_01 = int(term_01)
term_02 = int(term_02)
lab = int(lab)

required_note = (((TERMS_THIRD_PART - lab * 0.3) * 3) / 0.7 - term_01 - term_02)
required_note = round(required_note)

print(f'Necesita nota {required_note} en el certamen 3')
