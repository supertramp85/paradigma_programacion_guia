#1-Comisión de vendedores Una empresa debe calcular el total de comisiones que debe abonar por ventas realizadas por sus vendedores, para ello les solicita 
# un sistemita que le permita calcular dichos montos. Se tiene conocimiento que la empresa tiene cuatro categorías de vendedores(1 a 4).Usted debe solicitar 
# el ingreso de la categoría del vendedor y el total de la venta(el proceso termina cuando se ingrese una categoría igual a cero) y acumular las comisiones de 
# las ventas rendidas por los vendedores de diferentes en base a los siguientes cálculos: 
#Categoría1:cobra una comisión de 10% 
#Categoría2: cobra una comisión de 25% 
#Categoría3:cobra una comisión de 30% 
#Categoría4:cobra una comisión de 40% 
#Una vez procesadas todas las ventas mostrar el total de comisiones a pagar por cada categoría de vendedor es que en el la empresa junto con el total general


# Inicializar las variables para acumular las comisiones por categoría
comision_cat1 = 0
comision_cat2 = 0
comision_cat3 = 0
comision_cat4 = 0

# Inicializar la variable para el total general de comisiones
total_general = 0

# Ciclo para ingresar las ventas de los vendedores
while True:
    # Solicitar la categoría del vendedor
    categoria = int(input("Ingrese la categoría del vendedor (1-4) o 0 para terminar: "))
    
    # Verificar si se debe terminar el proceso
    if categoria == 0:
        break
    
    # Solicitar el total de la venta
    venta = float(input("Ingrese el total de la venta: "))
    
    # Calcular la comisión según la categoría
    if categoria == 1:
        comision = venta * 0.10  # 10%
        comision_cat1 += comision
    elif categoria == 2:
        comision = venta * 0.25  # 25%
        comision_cat2 += comision
    elif categoria == 3:
        comision = venta * 0.30  # 30%
        comision_cat3 += comision
    elif categoria == 4:
        comision = venta * 0.40  # 40%
        comision_cat4 += comision
    else:
        print("Categoría inválida. Por favor, ingrese una categoría entre 1 y 4.")
        continue  # Salta al siguiente ciclo sin acumular comisiones
    
    # Acumular la comisión al total general
    total_general += comision

# Mostrar los resultados finales
print("\n--- Resultados de Comisiones ---")
print(f"Total de comisiones para Categoría 1: ${comision_cat1:.2f}")
print(f"Total de comisiones para Categoría 2: ${comision_cat2:.2f}")
print(f"Total de comisiones para Categoría 3: ${comision_cat3:.2f}")
print(f"Total de comisiones para Categoría 4: ${comision_cat4:.2f}")
print(f"Total general de comisiones: ${total_general:.2f}")
