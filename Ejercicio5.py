#QUINTO EJERICIO
#PIDE POR TERMINAL QUE INGRESEN UN NUMERO ENTERO,
#SINO ES ENTERO, ENTONCES IMPRIME UN MENSAJE DE ERROR DICIENDO QUE NO SE ACEPTAN DECIMALES
#ADICIONAL, SI EL NUMERO ES MULTIPLO DE 3, IMPRIME LA PALABRA "FIZZ"
#SI EL NUMERO ES MULTIPLO DE 5, IMPRIME LA PALABRA "BUZZ"
#Y SI ES MULTIPLO DE 15, IMPRIME LA PALABRA "FIZZBUZZ"

entrada = input("Ingresa un número entero: ")
#Comprobamos si hay un punto en la entrada
if "." in entrada:
    print("Error: No se aceptan decimales.")
else:
    numero = int(entrada)  # Convertimos a entero
    if numero % 15 == 0:
        print("fizzbuzz")
    elif numero % 3 == 0:
        print("fizz")
    elif numero % 5 == 0:
        print("buzz")
    else:
        print("El número no es múltiplo de 3, 5 o 15.")