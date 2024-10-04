# Sueldos y aguinaldo
#Ingresar por teclado los sueldos de un vendedor, correspondientes al primer semestre del año y luego:
#a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período.
#b) Determinar en qué mes recibió el sueldo más bajo del período.
#c) Informar el sueldo promedio del semestre.

opcion=0
sueldo=0
mes=0
sueldo_menor=None
sueldo_mayor=None
total_sueldos=0

while True:
    print("1 ingrese sueldo , 2 salir")
    opcion= int( input("ingrese opcion"))
    if opcion == 2:
        break
    if opcion == 1 :
       for primersemestre in range (1,7):
        print (f"mes: {primersemestre}")    
       sueldo= float(input("ingrese sueldo: "))  

       if sueldo_mayor > sueldo:
          sueldo_mayor=sueldo
          mes_mayor=mes

       if sueldo_menor < sueldo:
          sueldo_menor = sueldo 
          mes_menor = mes  
    #total      
    total_sueldos += sueldo

    print (primersemestre)
    print (sueldo)

aguinaldo= sueldo_mayor /2
promedio= total_sueldos/6

print(f"El aguinaldo es de : {aguinaldo}")
print(f"El sueldo menor fue de : {sueldo_menor}")
print(f"El promedio es de : {promedio}")



