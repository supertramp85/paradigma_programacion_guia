<<<<<<< HEAD
#Se desea un programa que: solicite al usuario un nombre, un apellido y el dominio y luego, proponga una dirección de mail para el nombre y apellido ingresado de acuerdo a las siguientes reglas: Componer la dirección de correo de la siguiente manera: @ Por ejemplo para Nombre = Felipe, Apellido= Steffolani y Dominio= umet.edu.ar la dirección de mail sería: fsteffolani@umet.edu.ar. Pero si la primera primera letra del nombre y la primera letra del apellido son la misma entonces uƟlizar: .@ Por ejemplo para Nombre= Soledad, Apellido= Steffolani y Dominio= colegiorosarito.edu.ar la dirección de mail sería:
#soledad.steffolani@umet.edu.ar

# Solicitar al usuario un nombre, un apellido y un dominio
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
dominio = input("Ingrese el dominio: ")

# Comprobar si la primera letra del nombre y del apellido son iguales
if nombre[0] == apellido[0]:
    # Usar .@ como separador si las primeras letras son iguales
    direccion_email = f"{nombre.lower()}.{apellido.lower()}{dominio}"
else:
    # Usar la primera letra del nombre como separador si son diferentes
    direccion_email = f"{nombre[0].lower()}{apellido.lower()}{dominio}"

# Mostrar la dirección de correo electrónico resultante
print("La dirección de correo electrónico sugerida es:", direccion_email)
=======
#Se desea un programa que: solicite al usuario un nombre, un apellido y el dominio y luego, proponga una dirección de mail para el nombre y apellido ingresado de acuerdo a las siguientes reglas: Componer la dirección de correo de la siguiente manera: @ Por ejemplo para Nombre = Felipe, Apellido= Steffolani y Dominio= umet.edu.ar la dirección de mail sería: fsteffolani@umet.edu.ar. Pero si la primera primera letra del nombre y la primera letra del apellido son la misma entonces uƟlizar: .@ Por ejemplo para Nombre= Soledad, Apellido= Steffolani y Dominio= colegiorosarito.edu.ar la dirección de mail sería:
#soledad.steffolani@umet.edu.ar

# Solicitar al usuario un nombre, un apellido y un dominio
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
dominio = input("Ingrese el dominio: ")

# Comprobar si la primera letra del nombre y del apellido son iguales
if nombre[0] == apellido[0]:
    # Usar .@ como separador si las primeras letras son iguales
    direccion_email = f"{nombre.lower()}.{apellido.lower()}{dominio}"
else:
    # Usar la primera letra del nombre como separador si son diferentes
    direccion_email = f"{nombre[0].lower()}{apellido.lower()}{dominio}"

# Mostrar la dirección de correo electrónico resultante
print("La dirección de correo electrónico sugerida es:", direccion_email)
>>>>>>> 11ad6668f95431f70c296fb159f1e88c352e16d3
