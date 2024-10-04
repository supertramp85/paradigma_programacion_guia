cantidad_productos = 0
valor_total = 0
producto_mas_barato = None
producto_mas_caro = None

while True:
    nombre = input("Ingrese el nombre del producto (o 's' para terminar): ")

    if nombre.lower() == 's':
        break

    precio = float(input("Ingrese el precio del producto: "))
    
    cantidad_productos += 1
    valor_total += precio

    if producto_mas_barato is None or precio < producto_mas_barato:
        producto_mas_barato = precio

    if producto_mas_caro is None or precio > producto_mas_caro:
        producto_mas_caro = precio

if cantidad_productos == 0:
    print("No se ingresaron productos.")
else:
    print(f"Se ingresaron {cantidad_productos} productos.")
    print(f"El valor total de los productos ingresados es: {valor_total}")
    print(f"El producto más barato tiene un precio de: {producto_mas_barato}")
    print(f"El producto más caro tiene un precio de: {producto_mas_caro}")
