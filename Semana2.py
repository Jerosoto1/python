# # House = {
# #     "Cuartos" : 4,
# #     "Baños" : 2,
# #     "Address" : "calle64",
# # }

# # print(House)
# # House["Baños"] = "4"
# # House["Cuartos"] = "7"
# # House["Address"] = "CALLE 55 #36A"
# # del House["Address"]

# # House["City"] = "Itagui"

# # for info,Pr in House.items():
# #     print(f"{info}: {Pr}")


# # Crear un lista y contar cuantos nombres hay repetidos.
# # Nombres = ["Jero", "Sofia", "Sara", "Jero", "Ana", "Salome", "Mariana", "Sofia", "Jero"]
# # counterName={}

# # for nombre in Nombres:
# #     if nombre in counterName:
# #         counterName[nombre] += 1
# #     else: 
# #         counterName[nombre] =1

# # print(counterName)




# #Crea un diccionario llamado auto que contenga: Marca,Modelo,Año,
# # Cambaiar el modelo del auto a otro diferente,Agrega un nuevo color al diccionario
# #Elimina la clave año,Imprime todas lasclaves del diccionario usando un bucle for
# #IMprime todos los valores del diccionario usando un bucle for
# # Auto = {
# #     "Marca" : "Tesla",
# #     "Modelo" : "Model X",
# #     "Año" : "2015"

# # }

# # print(Auto)
# # Auto["Modelo"] = "Model Y"
# # print(Auto)
# # Auto["Color"] = "Azul Oscuro"
# # print(Auto)
# # del Auto["Año"]
# # print(Auto)

# # for Key,Value in Auto.items():
# #     print(f" {Value} ")





# ##Crea un diccionario paises donde las claves sean nombres de paises y los valores-
# # #-las capitales, 
# country = {
#     "Colombia" : "Bogota",
#     "Brasil" : "Brasilia",
#     "Chile" : "Santiago",
#     "Perú" : "Lima",
#     "Argentina" : "Buenos Aires",
#     "Ecuador" : "Quito",
#     "Venezuela": ["Caracas", "Marcaibo", "Barquisimeto", "Aragua"]
# }

# nombre = "Araguas444"
# flag = False
# for i in range(0, len(country["Venezuela"])):
#     if country["Venezuela"][i] == nombre:
#         flag = True
#         print("Lo encontré")
#         break

# if flag == False:
#     print("No lo encontré, mardito")

flag = False
while True:
    nombre = input("CUal es su nombre: ")

    if nombre == "alberto":
        flag = True

    if flag == True:
        break
        
    age = input("ingrese su edad")
    print(age)

    print("Sos  un Mardito")




# # dicts = {
# #     0: "Mateo",
# #     1.5: "Monsalve",
# #     (2, 3): "27",
# #     "alias": "Mateo"
# # }

# # list_brands = ["Bajaj", "Susuki", "BMW", "Yamaha"]
# # nombre = "Yamaha"
# # for brand in list_brands:
# #     if nombre == brand:
# #         print("Existe!")
# #     else:
# #         print("No existe!")


# ciudades = {}
# for pais,ciudad in country.items():
#     #print(pais, ciudad)
#     ciudades[ciudad] = pais 
# print(ciudades)


# #Escribe un programa que pregunte al usuario un pais y devuelva su capital(si existe)

# pais = input("Dime algun pais: ")
# if pais in country:
#     print(country[pais])
# else:
#     print("No existe")



# #Invierte el diccionario paises, es decir, que las capitales sean las claves y
# #los países los valores.

# ciudad = input("Dime una capital: ")
# if ciudad in ciudades:
#     print(ciudades[ciudad])
# else:
#     print("NO HAY PUTO") 



# #Crea un diccionario de estudiantes donde las claves sean los nombres y los valores sus notas finales.
# #Después imprime los nombres de los estudiantes que aprobaron (nota mayor o igual a 6