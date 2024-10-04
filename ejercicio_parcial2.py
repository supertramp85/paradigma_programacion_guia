#Teniendo en cuenta los puntos anteriores, resolver el siguiente ejercicio.
#Supongamos que nos encontramos con un cliente que nos solicita un pequeño script para
#realizar el control de stock de su compañía.
#El mismo nos indica que lo que requiere es un proceso que permita realizar la carga de
#distintos productos utilizando como ingreso su nombre y precio. El mismo debe ser
#mostrado por pantalla al usuario luego de su correcto ingreso.
#Por último se nos solicitan 3 datos extra:
#Necesitamos indicar luego de finalizar la carga de productos la cantidad ingresada.
#Necesitamos indicar al usuario, luego de finalizar la carga de productos, cuál es el
#valor total de los productos ingresados.
#Necesitamos indicar al usuario, luego de finalizar la carga de productos, cuál fué el
#producto más barato ingresado y cuál el más caro
#------------------------------------------------------------------------------------------------
producto_mas_barato=None
producto_mas_caro=None
contador=0
producto_total=0
continuar=True

while continuar:
     nombre= input("ingrese nombre del producto o (s) para salir: ")

     if nombre.lower() == 's':
        break
     precio= float(input("ingrese precio: "))

     #acumuladores y contador
     contador += 1
     producto_total += precio
     
     #max y min
     if producto_mas_barato is None or precio < producto_mas_barato:
       producto_mas_barato=precio

     if producto_mas_caro is None or precio > producto_mas_caro:
        producto_mas_caro=precio

print(f"la cantidad de producto ingresada es: {contador}")
print(f"el producto mas caro es: {producto_mas_caro}")
print(f"el producto mas barato es: {producto_mas_barato}")
print(f"el total de productos ingresados es: {producto_total}")
     
    