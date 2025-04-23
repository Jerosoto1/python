#CUARTO EJECICIO
#PIDE UN NUMERO AL USUARIO POR TERMINAL
#Y DETERMINA SI ES UN NUMERO PRIMO
numero = int(input("Ingresa un número: "))
if numero < 2:
    print("No es primo.")
else:
    esprimo = True
    i = 2

    while i < numero:
        if numero % i == 0:   # Si se divide exacto con otro número
            esprimo = False  # entonces no es primo
            break             # salimos del ciclo
        i = i + 1             # seguimos probando con el siguiente número

    if esprimo:
        print("El número es primo.")
    else:
        print("El número no es primo.")