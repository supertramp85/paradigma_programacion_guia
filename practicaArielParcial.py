alumnos = {}
calificaciones = {}

def agregar():
   matricula = int(input("Ingrese matrícula: "))
   nombre = input("Ingrese nombre: ")
   edad = int(input("Ingrese edad: "))
   alumnos[matricula] = {"nombre": nombre, "edad": edad}
   print("Estudiante agregado.")

def contador_estudiantes():
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
    print("Opción 1: Agregar Nuevo Estudiante")
    print("Opción 2: Cantidad de Estudiantes")
    print("Opción 3: Ingresar Calificación")
    print("Opción 4: Promedio de Calificaciones")
    print("Opción 5: Imprimir Lista de Estudiantes")

    opcion = int(input("Ingrese opción: "))

    if opcion == 1:
        agregar()
    elif opcion == 2:
        contador_estudiantes()
    elif opcion == 3:
        registrar_calificaciones()
    elif opcion == 4:
        calcular_promedio()
    elif opcion == 5:
        list_estudiantes()
