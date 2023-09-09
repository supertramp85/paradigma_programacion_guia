#Multiplicación. Ingresar un número cualquiera por teclado y que muestre su respectiva tabla del 1 al 10

# Solicitar al usuario un número
numero = int(input("Ingrese un número: "))

# Mostrar la tabla de multiplicación del número del 1 al 10
print(f"Tabla de multiplicación del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
