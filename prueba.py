# Inicialización con los datos de los socios fundadores
socios = {
    1: {"nombre": "Amanda Núñez", "fecha_ingreso": "17/03/2009", "cuota_al_dia": True},
    2: {"nombre": "Bárbara Molina", "fecha_ingreso": "17/03/2009", "cuota_al_dia": True},
    3: {"nombre": "Lautaro Campos", "fecha_ingreso": "17/03/2009", "cuota_al_dia": True}
}

def agregar_socio():
    numero = int(input("Ingrese el número del socio: "))
    nombre = input("Ingrese el nombre y apellido del socio: ")
    fecha_ingreso = input("Ingrese la fecha de ingreso (ddmmaaaa): ")
    cuota_al_dia = input("¿Cuota al día? (s/n): ").lower() == "s"
    
    socios[numero] = {"nombre": nombre, "fecha_ingreso": fecha_ingreso, "cuota_al_dia": cuota_al_dia}

def cantidad_socios():
    print(f"El club tiene {len(socios)} socios.")

def pagar_cuotas():
    numero = int(input("Ingrese el número del socio que ha pagado todas las cuotas adeudadas: "))
    if numero in socios:
        socios[numero]["cuota_al_dia"] = True
        print("Las cuotas han sido pagadas.")
    else:
        print("El número de socio no existe.")

def modificar_fecha_ingreso():
    fecha_original = "13/03/2018"
    nueva_fecha = "14/03/2018"
    
    for numero, socio in socios.items():
        if socio["fecha_ingreso"] == fecha_original:
            socio["fecha_ingreso"] = nueva_fecha

def dar_de_baja():
    nombre = input("Ingrese el nombre y apellido del socio que desea dar de baja: ")
    
    socios_a_eliminar = [numero for numero, socio in socios.items() if socio["nombre"] == nombre]
    
    if socios_a_eliminar:
        for numero in socios_a_eliminar:
            del socios[numero]
        print(f"{len(socios_a_eliminar)} socio(s) han sido dados de baja.")
    else:
        print("No se encontró ningún socio con ese nombre.")

def imprimir_listado():
    print("Listado de socios:")
    for numero, socio in socios.items():
        estado_cuota = "al día" if socio["cuota_al_dia"] else "pendiente"
        print(f"Socio nº{numero}, {socio['nombre']}, ingresó: {socio['fecha_ingreso']}, Cuota: {estado_cuota}")

while True:
    print("MENU")
    print("1. Agregar socio")
    print("2. Informar cantidad de socios")
    print("3. Registrar pago de cuotas")
    print("4. Modificar fecha de ingreso")
    print("5. Dar de baja a un socio")
    print("6. Imprimir listado completo")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        agregar_socio()
    elif opcion == "2":
        cantidad_socios()
    elif opcion == "3":
        pagar_cuotas()
    elif opcion == "4":
        modificar_fecha_ingreso()
    elif opcion == "5":
        dar_de_baja()
    elif opcion == "6":
        imprimir_listado()
    elif opcion == "7":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
