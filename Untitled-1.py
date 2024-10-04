alumnos = {1: {"nombre": "pedro", "edad": 25}}
calificaciones = {}

def agregar_estudiante():
    matricula = int(input("Ingrese matrícula: "))
    nombre = input("Ingrese nombre: ")
    edad = int(input("Ingrese edad: "))
    alumnos[matricula] = {"nombre": nombre, "edad": edad}
    print("Estudiante agregado.")

def cantidad_estudiante():
    cantidad = len(alumnos)
    print("Cantidad de estudiantes registrados:", cantidad)

def registrar_calificaciones():
    matricula = int(input("Ingrese matrícula del estudiante: "))
    if matricula in alumnos:
        calificacion = float(input("Ingrese calificación: "))
        if matricula not in calificaciones:
            calificaciones[matricula] = []
        calificaciones[matricula].append(calificacion)
        print("Calificación registrada.")
    else:
        print("El estudiante no existe.")

def calcular_promedio():
    matricula = int(input("Ingrese matrícula del estudiante: "))
    if matricula in calificaciones:
        promedio = sum(calificaciones[matricula]) / len(calificaciones[matricula])
        print("Promedio de calificaciones:", promedio)
    else:
        print("El estudiante no tiene calificaciones registradas.")

def list_estudiantes():
    print("Lista de estudiantes:")
    for matricula, info in alumnos.items():
        print(f"Matrícula: {matricula}, Nombre: {info['nombre']}, Edad: {info['edad']}")

while True:
    print("MENU")
    print("Opción 1: Agregar nuevo estudiante")
    print("Opción 2: Cantidad de estudiantes")
    print("Opción 3: Ingresar calificación")
    print("Opción 4: Promedio de calificaciones")
    print("Opción 5: Imprimir lista de estudiantes")

    opcion = int(input("Ingrese opción: "))

    if opcion == 1:
        agregar_estudiante()
    elif opcion == 2:
        cantidad_estudiante()
    elif opcion == 3:
        registrar_calificaciones()
    elif opcion == 4:
        calcular_promedio()
    elif opcion == 5:
        list_estudiantes()
