<<<<<<< HEAD
#Ahorros. Escribir un programa en el cual muestre a fin de año el total de ahorro obtenido, si se pide en cada mes el 10% del sueldo ganado.

# Solicitar al usuario el sueldo mensual
sueldo_mensual = float(input("Ingrese su sueldo mensual: "))

# Inicializar el total de ahorro a cero
total_ahorro = 0.0

# Calcular el ahorro mensual durante 12 meses
for mes in range(1, 13):
    ahorro_mensual = sueldo_mensual * 0.10  # 10% del sueldo mensual
    total_ahorro += ahorro_mensual

    # Mostrar el ahorro del mes
    print(f"Mes {mes}: Ahorro mensual = {ahorro_mensual}")

# Mostrar el total de ahorro al final del año
print(f"Total de ahorro al final del año = {total_ahorro}")
=======
#Ahorros. Escribir un programa en el cual muestre a fin de año el total de ahorro obtenido, si se pide en cada mes el 10% del sueldo ganado.

# Solicitar al usuario el sueldo mensual
sueldo_mensual = float(input("Ingrese su sueldo mensual: "))

# Inicializar el total de ahorro a cero
total_ahorro = 0.0

# Calcular el ahorro mensual durante 12 meses
for mes in range(1, 13):
    ahorro_mensual = sueldo_mensual * 0.10  # 10% del sueldo mensual
    total_ahorro += ahorro_mensual

    # Mostrar el ahorro del mes
    print(f"Mes {mes}: Ahorro mensual = {ahorro_mensual}")

# Mostrar el total de ahorro al final del año
print(f"Total de ahorro al final del año = {total_ahorro}")
>>>>>>> 11ad6668f95431f70c296fb159f1e88c352e16d3
