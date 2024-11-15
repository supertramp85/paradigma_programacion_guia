#1.Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10)
#  y posteriormente muestre en 
# pantalla cada elemento de la lista junto con su cuadrado y su cubo.


import random

def generar_lista(n, inicio=1, fin=10):
    """Genera una lista de n números aleatorios entre inicio y fin."""
    return [random.randint(inicio, fin) for _ in range(n)]

def calcular_cuadrado_y_cubo(numero):
    """Devuelve una tupla con el cuadrado y el cubo de un número dado."""
    cuadrado = numero ** 2
    cubo = numero ** 3
    return cuadrado, cubo

def mostrar_resultados(lista):
    """Muestra cada número de la lista junto con su cuadrado y su cubo."""
    for numero in lista:
        cuadrado, cubo = calcular_cuadrado_y_cubo(numero)
        print(f"Número: {numero}, Cuadrado: {cuadrado}, Cubo: {cubo}")

# Inicializar la lista con 10 valores aleatorios del 1 al 10
valores = generar_lista(10)
mostrar_resultados(valores)
