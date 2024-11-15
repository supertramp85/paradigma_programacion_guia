#2. Crea una lista e inicializala con 5 cadenas de caracteres 
# leídas por teclado. Copia los elementos de la lista 
# en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.


def leer_cadenas(n):
    """Lee n cadenas de caracteres ingresadas por teclado y las almacena en una lista."""
    lista = []
    for i in range(n):
        cadena = input(f"Ingrese la cadena {i + 1}: ")
        lista.append(cadena)
    return lista

def invertir_lista(lista):
    """Retorna una nueva lista con los elementos de la lista original en orden inverso."""
    return lista[::-1]

def mostrar_lista(lista):
    """Muestra cada elemento de una lista."""
    for elemento in lista:
        print(elemento)

# Inicializar la lista con 5 cadenas de caracteres leídas por teclado
cadenas = leer_cadenas(5)

# Crear una nueva lista con el orden inverso de las cadenas
cadenas_invertidas = invertir_lista(cadenas)

# Mostrar los elementos de la lista en orden inverso
print("\nLista en orden inverso:")
mostrar_lista(cadenas_invertidas)
