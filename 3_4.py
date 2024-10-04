#4. Secuencia numérica Ingresar una secuencia de números, de a uno por vez, la carga finaliza cuando el usuario ingresa el cero. Determinar 
#a) Porcentaje que representan los números divisibles por 3 sobre el total de números ingresados en la secuencia 
#b) Determinar la cantidad de números que son el cuadrado del número anterior 
#c) Determinar la posición del mayor elemento impar de la secuencia 

# Inicializar variables
total_numeros = 0
divisibles_por_tres = 0
cantidad_cuadrados = 0
mayor_impar = None
posicion_mayor_impar = -1
posicion_actual = 0
numero_anterior = None

# Iniciar el ciclo para ingresar los números
while True:
    numero = int(input("Ingrese un número (0 para finalizar): "))
    
    if numero == 0:
        break
    
    total_numeros += 1
    posicion_actual += 1

    # a) Contar cuántos números son divisibles por 3
    if numero % 3 == 0:
        divisibles_por_tres += 1

    # b) Verificar si el número es el cuadrado del número anterior
    if numero_anterior is not None and numero == numero_anterior ** 2:
        cantidad_cuadrados += 1

    # c) Verificar si el número es impar y es el mayor
    if numero % 2 != 0:
        if mayor_impar is None or numero > mayor_impar:
            mayor_impar = numero
            posicion_mayor_impar = posicion_actual
    
    # Guardar el número actual como anterior para la próxima iteración
    numero_anterior = numero

# Mostrar los resultados
if total_numeros > 0:
    porcentaje_divisibles = (divisibles_por_tres / total_numeros) * 100
    print(f"\nPorcentaje de números divisibles por 3: {porcentaje_divisibles:.2f}%")
else:
    print("\nNo se ingresaron números.")

print(f"Cantidad de números que son el cuadrado del número anterior: {cantidad_cuadrados}")

if mayor_impar is not None:
    print(f"El mayor número impar es {mayor_impar} y está en la posición {posicion_mayor_impar}")
else:
    print("No se ingresaron números impares.")
