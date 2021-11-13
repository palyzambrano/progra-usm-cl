def invert_number(num):
  result = ''
  length = len(str(num))

  for _ in range(length):
    result += str(int(num % 10))
    num /= 10

  return result

num = input('Ingrese numero: ')
result = invert_number(int(num))

print(result)
