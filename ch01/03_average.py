labels = ["Primera", "Segunda", "Tercera", "Cuarta"] 
average = 0.0

for label in labels:
  value = input(f"{label} nota: ")
  value = float(value)
  average += value

print("El promedio es: " + str(average / len(labels)))
