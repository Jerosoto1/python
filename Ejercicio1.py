#PRIMER EJERCICIO:
#VAN A SOLICITAR LA EDAD DE 2 PERSONAS
#VAN A GUARDAR LAS EDAD EN VARIABLES
#VAN A VALIDAR QUIEN ES MAYOR QUE EL OTRO
#ADICIONAL, QUIEN ES MAYOR DE EDAD

edad1 = int(input("Ingresa la primera edad: "))
edad2 = int(input("Ingresa la segunda edad: "))

#Comparar edades
if edad1 > edad2:
    print("La primera persona es mayor.")
elif edad1 < edad2:
    print("La segunda persona es mayor.")
else:
    print("Ambas personas tienen la misma edad.")

#Verificar si son mayores de edad
if edad1 >= 18:
    print("La primera persona es mayor de edad.")
else:
    print("La primera persona es menor de edad.")

if edad2 >= 18:
    print("La segunda persona es mayor de edad.")
else:
    print("La segunda persona es menor de edad.")