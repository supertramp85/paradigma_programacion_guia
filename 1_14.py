#Suma - División - Potencia Se necesita desarrollar un programa que permita calcular la suma de tres números. Si el resultado es mayor a 10 dividir por 2 
#(mostrar su resultado sin decimales), en caso contrario elevar el resultado al cubo.

# Solicitar al usuario tres números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

# Calcular la suma de los tres números
suma = numero1 + numero2 + numero3

# Verificar si la suma es mayor que 10
if suma > 10:
    # Dividir el resultado por 2 y mostrar el resultado sin decimales
    resultado = int(suma / 2)
    print(f"La suma es mayor que 10. Resultado: {resultado}")
else:
    # Elevar el resultado al cubo
    resultado = suma ** 3
    print(f"La suma no es mayor que 10. Resultado al cubo: {resultado}")

