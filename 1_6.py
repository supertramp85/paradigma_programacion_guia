# Escribir un programa que pregunte un nombre de usuario, y que después muestre por pantalla si su cantidad de letras es par o impar.


nombre_usuario = input("Ingrese su nombre de usuario: ")

cantidad_letras = len(nombre_usuario)
es_par = cantidad_letras % 2 == 0

mensaje = "par" if es_par else "impar"

print(f"La cantidad de letras en el nombre es {mensaje}.")
