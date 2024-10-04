# Sueldos y aguinaldo
#Ingresar por teclado los sueldos de un vendedor, correspondientes al primer semestre del año y luego:
#a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período.
#b) Determinar en qué mes recibió el sueldo más bajo del período.
#c) Informar el sueldo promedio del semestre.
# Inicializar variables
sueldo_mayor = 0
sueldo_menor = None
total_sueldos = 0
mes_menor = 0

# Ciclo para ingresar los sueldos del primer semestre (6 meses)
for mes in range(1, 7):
    sueldo = float(input(f"Ingrese el sueldo del mes {mes}: "))

    # Sumar el sueldo al total
    total_sueldos += sueldo

    # Determinar el sueldo mayor
    if sueldo > sueldo_mayor:
        sueldo_mayor = sueldo

    # Determinar el sueldo menor
    if sueldo_menor is None or sueldo < sueldo_menor:
        sueldo_menor = sueldo
        mes_menor = mes

# Calcular aguinaldo (la mitad del sueldo mayor)
aguinaldo = sueldo_mayor / 2

# Calcular promedio de los sueldos
promedio = total_sueldos / 6

# Mostrar resultados
print(f"El aguinaldo es de: {aguinaldo}")
print(f"El sueldo más bajo fue de: {sueldo_menor} en el mes {mes_menor}")
print(f"El sueldo promedio del semestre es: {promedio}")
