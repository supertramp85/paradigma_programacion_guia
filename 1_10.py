<<<<<<< HEAD
#Crear un conversor de dólares a pesos y pesos a dólares, donde se ingrese por teclado el valor del peso actual

# Solicitar al usuario el valor actual del peso
valor_peso_actual = float(input("Ingrese el valor actual del peso: "))

# Solicitar al usuario que elija la dirección de conversión
print("Seleccione la dirección de conversión:")
print("1. Dólares a Pesos")
print("2. Pesos a Dólares")
opcion = int(input("Ingrese 1 o 2 para seleccionar la dirección de conversión: "))

# Verificar la opción seleccionada y realizar la conversión
if opcion == 1:
    # Conversión de Dólares a Pesos
    dolares = float(input("Ingrese la cantidad de dólares a convertir: "))
    pesos = dolares * valor_peso_actual
    print(f"{dolares} dólares son equivalentes a {pesos} pesos.")
elif opcion == 2:
    # Conversión de Pesos a Dólares
    pesos = float(input("Ingrese la cantidad de pesos a convertir: "))
    dolares = pesos / valor_peso_actual
    print(f"{pesos} pesos son equivalentes a {dolares} dólares.")
else:
    print("Opción no válida. Por favor, seleccione 1 o 2 para la dirección de conversión.")
=======
#Crear un conversor de dólares a pesos y pesos a dólares, donde se ingrese por teclado el valor del peso actual

# Solicitar al usuario el valor actual del peso
valor_peso_actual = float(input("Ingrese el valor actual del peso: "))

# Solicitar al usuario que elija la dirección de conversión
print("Seleccione la dirección de conversión:")
print("1. Dólares a Pesos")
print("2. Pesos a Dólares")
opcion = int(input("Ingrese 1 o 2 para seleccionar la dirección de conversión: "))

# Verificar la opción seleccionada y realizar la conversión
if opcion == 1:
    # Conversión de Dólares a Pesos
    dolares = float(input("Ingrese la cantidad de dólares a convertir: "))
    pesos = dolares * valor_peso_actual
    print(f"{dolares} dólares son equivalentes a {pesos} pesos.")
elif opcion == 2:
    # Conversión de Pesos a Dólares
    pesos = float(input("Ingrese la cantidad de pesos a convertir: "))
    dolares = pesos / valor_peso_actual
    print(f"{pesos} pesos son equivalentes a {dolares} dólares.")
else:
    print("Opción no válida. Por favor, seleccione 1 o 2 para la dirección de conversión.")
>>>>>>> 11ad6668f95431f70c296fb159f1e88c352e16d3
