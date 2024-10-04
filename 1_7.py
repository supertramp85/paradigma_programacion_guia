#Ingresar la cantidad de números de la sucesión de Fibonacci a mostrar

# Solicitar al usuario la cantidad de números a mostrar
n = int(input("Ingrese la cantidad de números de la sucesión de Fibonacci a mostrar: "))

# Verificar si el usuario ingresó un número válido
if n <= 0:
    print("Por favor, ingrese un número positivo.")
else:
    # Inicializar los primeros dos números de la sucesión de Fibonacci
    fib1, fib2 = 0, 1
    count = 0

    # Mostrar los primeros n números de la sucesión de Fibonacci
    print("Sucesión de Fibonacci con", n, "números:")
    while count < n:
        print(fib1, end=" ")
        fib1, fib2 = fib2, fib1 + fib2
        count += 1
