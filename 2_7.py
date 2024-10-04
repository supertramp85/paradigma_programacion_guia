#7.Complejo de cines Desarrollar un programa que permita procesar funciones de un complejo de cines. 
#Por cada función se conoce:cantidad de espectadores y descuento(S/N).La carga termina cuando la cantidad de espectadores sea igual a
#0(cero).El programa deberá:Calcular la recaudación total del complejo,considerando que el valor de la entrada e sde$50en los días con 
#descuento y $75 en los días sin descuento.Determinar cuántas funciones con descuentos efectuaron y qué porcentaje representan sobre el total de 
#funciones


# Inicializar variables
recaudacion_total = 0
funciones_con_descuento = 0
total_funciones = 0

# Ciclo para procesar cada función
while True:
    # Solicitar la cantidad de espectadores
    espectadores = int(input("Ingrese la cantidad de espectadores (0 para terminar): "))
    
    # Condición de salida del ciclo
    if espectadores == 0:
        break
    
    # Solicitar si hay descuento o no
    descuento = input("¿Hay descuento? (S/N): ").strip().upper()
    
    # Determinar el precio de la entrada según el descuento
    if descuento == 'S':
        precio_entrada = 50
        funciones_con_descuento += 1  # Contar función con descuento
    else:
        precio_entrada = 75
    
    # Calcular la recaudación de la función
    recaudacion_funcion = espectadores * precio_entrada
    recaudacion_total += recaudacion_funcion
    
    # Contar la función procesada
    total_funciones += 1

# Mostrar resultados
if total_funciones > 0:
    porcentaje_descuento = (funciones_con_descuento / total_funciones) * 100
    print(f"\nRecaudación total del complejo: ${recaudacion_total}")
    print(f"Total de funciones con descuento: {funciones_con_descuento}")
    print(f"Porcentaje de funciones con descuento: {porcentaje_descuento:.2f}%")
else:
    print("No se procesaron funciones.")
