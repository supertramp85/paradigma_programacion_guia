<<<<<<< HEAD
 #Jornal de un Operario
#Se necesita desarrollar un programa para el área de recursos humanos de una empresa que permita informar el jornal de un 
#determinado operario. Usted deberá cargar por teclado el código de turno
#que el operario trabajó ese día (1- representa Diurno y 2- representa Nocturno) y la cantidad de horas trabajadas.
#La política de trabajo en la empresa es que los operarios de la misma pueden trabajar en el turno diurno o nocturno. 
#Si un operario trabaja en el turno nocturno el pago es 40.60 pesos la hora, si lo hace en el turno diurno cobra 35.50 pesos la hora.


# Solicitar al usuario el código de turno (1 para Diurno, 2 para Nocturno)
codigo_turno = int(input("Ingrese el código de turno (1 para Diurno, 2 para Nocturno): "))

# Solicitar al usuario la cantidad de horas trabajadas
horas_trabajadas = float(input("Ingrese la cantidad de horas trabajadas: "))

# Definir las tarifas por hora para cada turno
tarifa_diurno = 35.50
tarifa_nocturno = 40.60

# Calcular el jornal según el código de turno y las horas trabajadas
if codigo_turno == 1:
    jornal = horas_trabajadas * tarifa_diurno
    print(f"El jornal del operario en el turno diurno es: ${jornal:.2f}")
elif codigo_turno == 2:
    jornal = horas_trabajadas * tarifa_nocturno
    print(f"El jornal del operario en el turno nocturno es: ${jornal:.2f}")
else:
    print("Código de turno no válido. Por favor, ingrese 1 para Diurno o 2 para Nocturno.")
=======
 #Jornal de un Operario
#Se necesita desarrollar un programa para el área de recursos humanos de una empresa que permita informar el jornal de un 
#determinado operario. Usted deberá cargar por teclado el código de turno
#que el operario trabajó ese día (1- representa Diurno y 2- representa Nocturno) y la cantidad de horas trabajadas.
#La política de trabajo en la empresa es que los operarios de la misma pueden trabajar en el turno diurno o nocturno. 
#Si un operario trabaja en el turno nocturno el pago es 40.60 pesos la hora, si lo hace en el turno diurno cobra 35.50 pesos la hora.


# Solicitar al usuario el código de turno (1 para Diurno, 2 para Nocturno)
codigo_turno = int(input("Ingrese el código de turno (1 para Diurno, 2 para Nocturno): "))

# Solicitar al usuario la cantidad de horas trabajadas
horas_trabajadas = float(input("Ingrese la cantidad de horas trabajadas: "))

# Definir las tarifas por hora para cada turno
tarifa_diurno = 35.50
tarifa_nocturno = 40.60

# Calcular el jornal según el código de turno y las horas trabajadas
if codigo_turno == 1:
    jornal = horas_trabajadas * tarifa_diurno
    print(f"El jornal del operario en el turno diurno es: ${jornal:.2f}")
elif codigo_turno == 2:
    jornal = horas_trabajadas * tarifa_nocturno
    print(f"El jornal del operario en el turno nocturno es: ${jornal:.2f}")
else:
    print("Código de turno no válido. Por favor, ingrese 1 para Diurno o 2 para Nocturno.")
>>>>>>> 11ad6668f95431f70c296fb159f1e88c352e16d3
