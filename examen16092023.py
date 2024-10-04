contador_venta = 0
contador_auto = 0
contador_camioneta = 0
contador_camion = 0
precio_mayor_veh = None
precio_menor_veh = None

auto_total = 0
camioneta_total = 0
camion_total = 0

for _ in range(12):
    print("Ingrese 1 para autos, 2 para salir:")
    ingreso = input("Ingrese opción: ")

    if ingreso == "2":
        break

    if ingreso == "1":
        tipo = int(input("Ingrese tipo (1 para autos, 2 para camiones, 3 para camionetas): "))
        precio = float(input("Ingrese precio: "))
        mes = int(input("Ingrese mes: "))
        contador_venta += 1

        if tipo == 1:
            auto_total += precio
            contador_auto += 1
        elif tipo == 2:
            camioneta_total += precio
            contador_camioneta += 1
        elif tipo == 3:
            camion_total += precio
            contador_camion += 1

        if precio_mayor_veh is None or precio > precio_mayor_veh:
            precio_mayor_veh = precio

        if precio_menor_veh is None or precio < precio_menor_veh:
            precio_menor_veh = precio

total_ventas = auto_total + camioneta_total + camion_total

mejor_venta = None

if auto_total > camioneta_total and auto_total > camion_total:
    mejor_venta = "auto"
elif camion_total > camioneta_total and camion_total > auto_total:
    mejor_venta = "camión"
elif camioneta_total > auto_total and camioneta_total > camion_total:
    mejor_venta = "camioneta"

print("Tipo:", tipo)
print("Precio:", precio)
print("Mejor venta:", mejor_venta)
print("Contador de ventas:", contador_venta)
print("Precio mayor:", precio_mayor_veh)
print("Precio menor:", precio_menor_veh)
print("Total de ventas:", total_ventas)

print("GRACIAS")
