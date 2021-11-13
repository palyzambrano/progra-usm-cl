def average(q1, q2, lab):
  """ Nc = (C1 + C2 + C3) / 3 """
  return (q1 + q2 + lab) / 3

def final(avg, lab):
  """ Nf = Nc * 0.7 + Nl * 0.3 """
  return (avg * 0.7) + (lab * 0.3)

q1 = int(input('Ingrese nota certamen 1: '));
q2 = int(input('Ingrese nota certamen 2: '));
lab = int(input('Ingrese nota laboratorio: '));

