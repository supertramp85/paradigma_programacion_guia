#Ciclistas:La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado).
#Desarrollar un programa que permita cargar, por cada competidor, nombre y tiempo de carrera. Luego se pide:
#a) Determinar y mostrar el nombre del ganador de la carrera.
#b) Ingresar por teclado el tiempo record registrado para dicha carrera. Determinar si el tiempo del ganador es menor
#al tiempo record, mostrar un mensaje.
#c) Calcular y mostrar el tiempo promedio entre todos los ciclistas


# Ingresar el número de competidores
n = int(input("Ingrese el número de competidores: "))

# Inicializar variables
ganador_nombre = ""
ganador_tiempo = None
tiempo_total = 0

# Ingresar el tiempo récord
tiempo_record = float(input("Ingrese el tiempo récord de la carrera: "))

# Ciclo para ingresar la información de cada competidor
for i in range(n):
    nombre = input("Ingrese el nombre del competidor: ")
    tiempo = float(input(f"Ingrese el tiempo de {nombre}: "))

    # Sumar el tiempo al total
    tiempo_total += tiempo

    # Determinar si es el ganador (menor tiempo)
    if ganador_tiempo is None or tiempo < ganador_tiempo:
        ganador_tiempo = tiempo
        ganador_nombre = nombre

# Calcular el promedio de los tiempos
promedio = tiempo_total / n

# Mostrar el nombre del ganador y su tiempo
print("El ganador de la carrera es", ganador_nombre, "con un tiempo de", ganador_tiempo, "minutos.")

# Verificar si el ganador rompió el récord
if ganador_tiempo < tiempo_record:
    print("¡El ganador superó el tiempo récord!")

# Mostrar el tiempo promedio de los ciclistas
print("El tiempo promedio entre todos los ciclistas es", promedio, "minutos.")



