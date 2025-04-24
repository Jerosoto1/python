#PALINDROMO #PALABRAS IMPARES #TERMINACION MISMA LETRA
#OSO

#ANA
Palindromo1 = input("Ingrese un palindromo: ")

longitud = len(Palindromo1)

if longitud %2 == 0:
    print("No es un palindromo")
    exit()

alreves = Palindromo1[::-1]
print(alreves)

if Palindromo1 == alreves: 
    print("ES PALINDROMO")
else:
    print("No es palindromo")
    
#Como meter todo en un while
#PYTHON TUTOR