#6. Mostrar por pantalla el promedio de los números ingresados por teclado. Se deja de pedir que el usuario agregue números una vez ingrese 0 (cero).


# Inicializar variables
suma = 0
contador = 0

# Ciclo para ingresar números hasta que se ingrese un 0
while True:
    numero = float(input("Ingrese un número (0 para terminar): "))
    
    if numero == 0:
        break
    
    suma += numero
    contador += 1

# Verificar si se ingresaron números para evitar división por cero
if contador > 0:
    promedio = suma / contador
    print(f"El promedio de los números ingresados es: {promedio}")
else:
    print("No se ingresaron números.")
