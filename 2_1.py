
#Ciclistas:La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado).
#Desarrollar un programa que permita cargar, por cada competidor, nombre y tiempo de carrera. Luego se pide:
#a) Determinar y mostrar el nombre del ganador de la carrera.
#b) Ingresar por teclado el tiempo record registrado para dicha carrera. Determinar si el tiempo del ganador es menor
#al tiempo record, mostrar un mensaje.
#c) Calcular y mostrar el tiempo promedio entre todos los ciclistas

# Ingresar el número de competidores
n = int(input("Ingrese el número de competidores: "))

# Inicializar variables
ganador = None
tiempo_total = 0

# Ingresar el tiempo récord
tiempo_record = float(input("Ingrese el tiempo récord de la carrera: "))

# Ciclo para ingresar la información de cada competidor
for i in range(n):
    nombre = input(f"Ingrese el nombre del competidor {i + 1}: ")
    tiempo = float(input(f"Ingrese el tiempo de carrera del competidor {nombre}: "))
    
    # Calcular el tiempo total
    tiempo_total += tiempo
    
    # Determinar al ganador
    if ganador is None or tiempo < ganador["tiempo"]:
        ganador = {"nombre": nombre, "tiempo": tiempo}

# Calcular el tiempo promedio entre todos los ciclistas
tiempo_promedio = tiempo_total / n

# Mostrar resultados
print(f"El ganador de la carrera es {ganador['nombre']} con un tiempo de {ganador['tiempo']} minutos.")

if ganador["tiempo"] < tiempo_record:
    print("¡El ganador superó el tiempo récord!")

print(f"El tiempo promedio entre todos los ciclistas es {tiempo_promedio} minutos.")
