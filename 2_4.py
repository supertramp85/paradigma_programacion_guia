#4. Decimal a Hexadecimal: Generar n números aleatorios entre el rango de 5000 y 450000, por cada uno de ellos mostrar y generar el numero hexadecimal


import random

# Solicitar el número de valores a generar
n = int(input("Ingrese la cantidad de números a generar: "))

# Generar y mostrar los números aleatorios con su equivalente hexadecimal
for i in range(n):
    numero_aleatorio = random.randint(5000, 450000)
    hexadecimal = hex(numero_aleatorio)
    print(f"Número: {numero_aleatorio} -> Hexadecimal: {hexadecimal}")
