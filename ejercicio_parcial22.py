alumnos = {}
calificaciones = {}

def agregar_estudiante(numero, nombre, edad):
    alumnos[numero] = {"nombre": nombre, "edad": edad}

def cantidad_estudiantes():
    return len(alumnos)

def registrar_calificaciones(numero, calificacion):
    if numero in alumnos:
        if numero not in calificaciones:
            calificaciones[numero] = []
        calificaciones[numero].append(calificacion)
    else:
        print("La matrícula no existe.")

def calcular_promedio(numero):
    if numero in calificaciones:
        calif = calificaciones[numero]
        if calif:
            return sum(calif) / len(calif)
    return 0

def listar_estudiantes():
    for numero, estudiante in alumnos.items():
        print(f"Matrícula: {numero}, Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}")

while True:
    print("\nMENU")
    print("Opción 1: Agregar nuevo estudiante")
    print("Opción 2: Cantidad de estudiantes")
    print("Opción 3: Ingresar calificación")
    print("Opción 4: Promedio de calificaciones")
    print("Opción 5: Imprimir lista de estudiantes")
    print("Opción 6: Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        numero = int(input("Ingrese la matrícula: "))
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))
        agregar_estudiante(numero, nombre, edad)

    elif opcion == "2":
        print(f"La escuela tiene {cantidad_estudiantes()} estudiantes.")

    elif opcion == "3":
        numero = int(input("Ingrese la matrícula del estudiante: "))
        calificacion = float(input("Ingrese la calificación: "))
        registrar_calificaciones(numero, calificacion)

    elif opcion == "4":
        numero = int(input("Ingrese la matrícula del estudiante: "))
        promedio = calcular_promedio(numero)
        print(f"El promedio de calificaciones del estudiante es: {promedio:.2f}")

    elif opcion == "5":
        listar_estudiantes()

    elif opcion == "6":
        break

    else:
        print("Opción no válida. Intente de nuevo.")
