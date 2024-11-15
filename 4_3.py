# 3 Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). 
# A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

# Función para leer notas del alumno
def leer_notas(cantidad):
    notas = []
    print(f"Introduce las {cantidad} notas del alumno (entre 0 y 10):")
    for i in range(cantidad):
        while True:
            try:
                nota = float(input(f"Nota {i + 1}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 0 y 10. Inténtalo de nuevo.")
            except ValueError:
                print("Entrada no válida. Introduce un número entre 0 y 10.")
    return notas

# Función para calcular la media de las notas
def calcular_media(notas):
    return sum(notas) / len(notas)

# Función para obtener la nota más alta
def calcular_maxima(notas):
    return max(notas)

# Función para obtener la nota más baja
def calcular_minima(notas):
    return min(notas)

# Función principal
def main():
    cantidad_notas = 5
    notas = leer_notas(cantidad_notas)
    nota_media = calcular_media(notas)
    nota_mas_alta = calcular_maxima(notas)
    nota_mas_baja = calcular_minima(notas)

    print("\nResultados:")
    print(f"Notas introducidas: {notas}")
    print(f"Nota media: {nota_media:.2f}")
    print(f"Nota más alta: {nota_mas_alta}")
    print(f"Nota más baja: {nota_mas_baja}")

# Llamar a la función principal
if __name__ == "__main__":
    main()

