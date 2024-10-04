
#3. Menu de Opciones con secuencias Escribir un programa que le permita al usuario, a través de un menú de opciones, las siguientes operaciones:
#  a) Generar una serie n de números (n ingresado por teclado y validando que sea mayor a cero) y mostrar la suma de los cuadrados 
# b) Ingresar un texto finalizado por un punto y determinar la cantidad de palabras que finalizan con vocales 
# c) Ingresar una serie de números (la carga finaliza con cero) y determinar si hay mayor cantidad de valores pares o de impares 
# d) Salir


opcion = ""

while opcion != "d":
    print("\n--- Menú de Opciones ---")
    print("a) Generar una serie de números y mostrar la suma de los cuadrados.")
    print("b) Ingresar un texto y determinar cuántas palabras terminan con vocal.")
    print("c) Ingresar una serie de números y determinar si hay más pares o impares.")
    print("d) Salir")
    
    opcion = input("\nSeleccione una opción (a, b, c, d): ").lower()

    if opcion == "a":
        # Opción a: Generar una serie de números y mostrar la suma de los cuadrados
        n = int(input("Ingrese un número mayor a cero: "))
        while n <= 0:
            n = int(input("El número debe ser mayor a cero. Ingrese nuevamente: "))
        
        suma_cuadrados = 0
        for i in range(1, n + 1):
            suma_cuadrados += i ** 2
        
        print(f"La suma de los cuadrados de los primeros {n} números es: {suma_cuadrados}")

    elif opcion == "b":
        # Opción b: Determinar cuántas palabras terminan en vocal
        texto = input("Ingrese un texto finalizado por un punto: ").strip()
        while not texto.endswith('.'):
            texto = input("El texto debe finalizar con un punto. Ingrese nuevamente: ")

        vocales = "aeiouAEIOU"
        palabras = texto[:-1].split()  # Remover el punto final y separar palabras
        palabras_con_vocal = 0
        
        for palabra in palabras:
            if palabra[-1] in vocales:
                palabras_con_vocal += 1
        
        print(f"Cantidad de palabras que terminan en vocal: {palabras_con_vocal}")

    elif opcion == "c":
        # Opción c: Determinar si hay más pares o impares
        pares = 0
        impares = 0
        
        while True:
            numero = int(input("Ingrese un número (0 para terminar): "))
            if numero == 0:
                break
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1

        if pares > impares:
            print("Hay más números pares.")
        elif impares > pares:
            print("Hay más números impares.")
        else:
            print("Hay igual cantidad de números pares e impares.")

    elif opcion == "d":
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Intente de nuevo.")
