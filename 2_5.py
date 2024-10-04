#5.Analisis de Texto
#El usuario ingresa una frase al comenzar el programa, la misma no puede tener longitud cero. La frase finaliza con
#un punto, y las palabras están separadas por espacios únicamente.
#Se debe mostrar:
#a) Ver el porcentaje de vocales respecto del total de letras de la frase.
#b) La longitud promedio de las palabras
#c) La longitud de la palabra mas larga del texto
#c) Cantidad de palabras que comienzan con "ta"

# Ingreso de la frase
while True:
    frase = input("Ingrese una frase que termine con punto: ")
    if len(frase) > 1 and frase.endswith('.'):
        break
    print("La frase no puede estar vacía y debe terminar con un punto.")

# Inicialización de variables
frase = frase[:-1]  # Remover el punto final
palabras = frase.split()

total_letras = 0
total_vocales = 0
longitud_total_palabras = 0
palabra_mas_larga = 0
palabras_comienzan_con_ta = 0

# Definir las vocales
vocales = "aeiouAEIOU"

# Recorrer cada palabra
for palabra in palabras:
    longitud_palabra = len(palabra)
    longitud_total_palabras += longitud_palabra
    total_letras += longitud_palabra

    # Contar vocales en la palabra
    for letra in palabra:
        if letra in vocales:
            total_vocales += 1

    # Verificar si la palabra es la más larga
    if longitud_palabra > palabra_mas_larga:
        palabra_mas_larga = longitud_palabra

    # Verificar si la palabra comienza con "ta"
    if palabra.lower().startswith("ta"):
        palabras_comienzan_con_ta += 1

# Calcular el porcentaje de vocales respecto al total de letras
porcentaje_vocales = (total_vocales / total_letras) * 100

# Calcular la longitud promedio de las palabras
promedio_longitud_palabras = longitud_total_palabras / len(palabras)

# Mostrar los resultados
print(f"Porcentaje de vocales respecto al total de letras: {porcentaje_vocales:.2f}%")
print(f"Longitud promedio de las palabras: {promedio_longitud_palabras:.2f}")
print(f"Longitud de la palabra más larga: {palabra_mas_larga}")
print(f"Cantidad de palabras que comienzan con 'ta': {palabras_comienzan_con_ta}")
