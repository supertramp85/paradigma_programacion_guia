# Diccionario con los socios fundadores
socios = {
    1: {"nombre": "Amanda Núñez", "ingreso": "17/03/2009", "cuota_al_dia": True},
    2: {"nombre": "Bárbara Molina", "ingreso": "17/03/2009", "cuota_al_dia": True},
    3: {"nombre": "Lautaro Campos", "ingreso": "17/03/2009", "cuota_al_dia": True}
}

# Función para cargar un nuevo socio
def agregar_socio(numero, nombre, ingreso, cuota_al_dia):
    socios[numero] = {"nombre": nombre, "ingreso": ingreso, "cuota_al_dia": cuota_al_dia}

# Función para informar la cantidad de socios
def cantidad_socios():
    return len(socios)

# Función para registrar el pago de cuotas de un socio
def pagar_cuotas(numero):
    if numero in socios:
        socios[numero]["cuota_al_dia"] = True

# Función para modificar la fecha de ingreso de todos los socios
def modificar_fecha_ingreso(fecha_original, fecha_nueva):
    for numero, socio in socios.items():
        if socio["ingreso"] == fecha_original:
            socio["ingreso"] = fecha_nueva

# Función para dar de baja a un socio
def dar_de_baja(nombre_apellido):
    for numero, socio in socios.items():
        if socio["nombre"] == nombre_apellido:
            del socios[numero]
            break

# Función para imprimir el listado completo de socios
def imprimir_socios():
    for numero, socio in socios.items():
        print(f"Socio nº{numero}, {socio['nombre']}, ingresó: {socio['ingreso']}, cuota al día: {socio['cuota_al_dia']}")

# Menú principal
while True:
    print("\nMenú Principal:")
    print("1. Agregar un nuevo socio")
    print("2. Informar cantidad de socios")
    print("3. Registrar pago de cuotas")
    print("4. Modificar fecha de ingreso")
    print("5. Dar de baja a un socio")
    print("6. Imprimir listado de socios")
    print("7. Salir")
    
    opcion = input("Elija una opción: ")
    
    if opcion == "1":
        numero = int(input("Ingrese el número de socio: "))
        nombre = input("Ingrese el nombre y apellido del socio: ")
        ingreso = input("Ingrese la fecha de ingreso (ddmmaaaa): ")
        cuota_al_dia = input("¿Cuota al día? (s/n): ").lower() == "s"
        agregar_socio(numero, nombre, ingreso, cuota_al_dia)
    elif opcion == "2":
        print(f"El club tiene {cantidad_socios()} socios.")
    elif opcion == "3":
        numero = int(input("Ingrese el número de socio que ha pagado todas las cuotas adeudadas: "))
        pagar_cuotas(numero)
    elif opcion == "4":
        fecha_original = input("Ingrese la fecha de ingreso original que desea modificar: ")
        fecha_nueva = input("Ingrese la nueva fecha de ingreso (ddmmaaaa): ")
        modificar_fecha_ingreso(fecha_original, fecha_nueva)
    elif opcion == "5":
        nombre_apellido = input("Ingrese el nombre y apellido del socio que desea dar de baja: ")
        dar_de_baja(nombre_apellido)
    elif opcion == "6":
        imprimir_socios()
    elif opcion == "7":
        break
    else:
        print("Opción no válida. Intente de nuevo.")
