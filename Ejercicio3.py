#TERCER EJERCICIO
#PIDE UN NUMERO AL USUARIO POR TERMINAL
#Y DETERMINA SI ES UN NUMERO PAR O IMPAR
Entrada = (input("Ingresa un número entero: "))
if "." in Entrada:
    print("Error: No se aceptan decimales.")
else:
    numero = int(Entrada)
#Verificamos si es par o impar
    if numero % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")