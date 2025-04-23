while True:
    try:

        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))


        suma = num1 + num2


        print("El total es:", suma)
        break
    except ValueError:
        print("No hay error entonces ingrese un numero válido.")