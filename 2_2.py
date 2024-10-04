#Secuencia de impares
#Cargar por teclado dos números, e imprimir los números impares que se encuentran comprendidos entre ellos, en forma ascendente y descendente


# Ingresar dos números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Determinar el rango de números (ascendente)
if num1 < num2:
    start = num1
    end = num2
else:
    start = num2
    end = num1

# Imprimir números impares en forma ascendente
print("Números impares en forma ascendente:")
for i in range(start, end + 1):
    if i % 2 != 0:
        print(i)

# Imprimir números impares en forma descendente
print("\nNúmeros impares en forma descendente:")
for i in range(end, start - 1, -1):
    if i % 2 != 0:
        print(i)
