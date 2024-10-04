<<<<<<< HEAD
 #Galería de Arte Una galería de arte desea preparar un catálogo de sus cuadros más famosos. Se realiza una prueba con tres cuadros y por cada uno se
# ingresa el año en que fue creado. El programa deberá verificar si todos los cuadros son anteriores al siglo XX (El siglo XX es el siglo pasado. 
#Se inició en el año 1901 y terminó en el año 2000). Determinar cuántos tienen antigüedad inferior a 10 años. Si no hay ninguno, imprimir el mensaje “Renovar stock”.

# Solicitar al usuario el año de creación de los tres cuadros
cuadro1 = int(input("Ingrese el año de creación del primer cuadro: "))
cuadro2 = int(input("Ingrese el año de creación del segundo cuadro: "))
cuadro3 = int(input("Ingrese el año de creación del tercer cuadro: "))

# Solicitar al usuario el año de creación de cada cuadro
cuadro1 = int(input("Ingrese el año de creación del primer cuadro: "))
cuadro2 = int(input("Ingrese el año de creación del segundo cuadro: "))
cuadro3 = int(input("Ingrese el año de creación del tercer cuadro: "))

# Verificar si todos los cuadros son anteriores al siglo XX (1901-2000)
if cuadro1 < 1901 and cuadro2 < 1901 and cuadro3 < 1901:
    print("Todos los cuadros son anteriores al siglo XX.")
    
    # Calcular cuántos cuadros tienen menos de 10 años de antigüedad
    anio_actual = 2023  # Año actual
    cuadros_menos_10_anios = 0

    if anio_actual - cuadro1 < 10:
        cuadros_menos_10_anios += 1
    if anio_actual - cuadro2 < 10:
        cuadros_menos_10_anios += 1
    if anio_actual - cuadro3 < 10:
        cuadros_menos_10_anios += 1

    if cuadros_menos_10_anios > 0:
        print(f"{cuadros_menos_10_anios} cuadro(s) tiene(n) menos de 10 años de antigüedad.")
    else:
        print("Ningún cuadro tiene menos de 10 años de antigüedad.")
else:
    print("Al menos uno de los cuadros no es anterior al siglo XX (1901-2000). Renovar stock.")

    
=======
 #Galería de Arte Una galería de arte desea preparar un catálogo de sus cuadros más famosos. Se realiza una prueba con tres cuadros y por cada uno se
# ingresa el año en que fue creado. El programa deberá verificar si todos los cuadros son anteriores al siglo XX (El siglo XX es el siglo pasado. 
#Se inició en el año 1901 y terminó en el año 2000). Determinar cuántos tienen antigüedad inferior a 10 años. Si no hay ninguno, imprimir el mensaje “Renovar stock”.

# Solicitar al usuario el año de creación de los tres cuadros
cuadro1 = int(input("Ingrese el año de creación del primer cuadro: "))
cuadro2 = int(input("Ingrese el año de creación del segundo cuadro: "))
cuadro3 = int(input("Ingrese el año de creación del tercer cuadro: "))

# Solicitar al usuario el año de creación de cada cuadro
cuadro1 = int(input("Ingrese el año de creación del primer cuadro: "))
cuadro2 = int(input("Ingrese el año de creación del segundo cuadro: "))
cuadro3 = int(input("Ingrese el año de creación del tercer cuadro: "))

# Verificar si todos los cuadros son anteriores al siglo XX (1901-2000)
if cuadro1 < 1901 and cuadro2 < 1901 and cuadro3 < 1901:
    print("Todos los cuadros son anteriores al siglo XX.")
    
    # Calcular cuántos cuadros tienen menos de 10 años de antigüedad
    anio_actual = 2023  # Año actual
    cuadros_menos_10_anios = 0

    if anio_actual - cuadro1 < 10:
        cuadros_menos_10_anios += 1
    if anio_actual - cuadro2 < 10:
        cuadros_menos_10_anios += 1
    if anio_actual - cuadro3 < 10:
        cuadros_menos_10_anios += 1

    if cuadros_menos_10_anios > 0:
        print(f"{cuadros_menos_10_anios} cuadro(s) tiene(n) menos de 10 años de antigüedad.")
    else:
        print("Ningún cuadro tiene menos de 10 años de antigüedad.")
else:
    print("Al menos uno de los cuadros no es anterior al siglo XX (1901-2000). Renovar stock.")
>>>>>>> 11ad6668f95431f70c296fb159f1e88c352e16d3
