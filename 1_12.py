# Crear un conversor de pies y pulgadas a centímetros

# Solicitar al usuario la cantidad de pies y pulgadas
pies = float(input("Ingrese la cantidad de pies: "))
pulgadas = float(input("Ingrese la cantidad de pulgadas: "))

# Convertir pies y pulgadas a centímetros
pulgadas_totales = (pies * 12) + pulgadas  # Convertir pies a pulgadas y sumar las pulgadas
centimetros = pulgadas_totales * 2.54  # Convertir pulgadas a centímetros

# Mostrar el resultado
print(f"{pies} pies y {pulgadas} pulgadas son equivalentes a {centimetros} centímetros.")
