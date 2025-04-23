#SEGUNDO EJERCICIO:
#SOLICITA EL NOMBRE, EDAD Y NOTAS DE UNIVERSIDAD DE UNA PERSONA
#VAS A PEDIR UN TOTAL DE 5 NOTAS
#VAS A CALCULAR EL PROMEDIO DE NOTAS
#Y SI EL PROMEDIO ES INFERIOR DE 3, ENTONCES IMPRIME POR CONSOLA QUE PERDIO LA MATERIA,
#SI ES MAYOR O IGUAL A 3, ENTONCES IMPRIME GANASTE
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")

#Pedimos 5 notas y las sumamos
nota1 = float(input("Ingresa la nota 1: "))
nota2 = float(input("Ingresa la nota 2: "))
nota3 = float(input("Ingresa la nota 3: "))
nota4 = float(input("Ingresa la nota 4: "))
nota5 = float(input("Ingresa la nota 5: "))

#Calculamos el promedio
promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print("Promedio:", promedio)

#Verificamos si ganó o perdió
if promedio >= 3:
    print("Ganaste")
else:
    print("Perdiste la materia.")