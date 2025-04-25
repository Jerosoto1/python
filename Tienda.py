#Al usuario: Nombre del producto
        #   Precio unitario
        #   Cantidad de productos
        #   POrcentaje de descuento
#Validae: Que el precio y cantidad sean numeros positivos
        # QUe el descuetno este entre 0 y 100
        # Calcular: El costo sin descuetno
        # El descuento(si aplica)
        # COSTO FINAL 


#Solicita el nombre del producto
producto = input("Ingrese el nombre del producto: ")

#Solicita el precio del producto
while True:
    try:
      precio = float(input("Ingrese el precio del producto: "))
      if precio <= 0:
         print("El precio debe ser numero positivo")
      else:
         break
    except ValueError:
       print("INGRESA UN NUMERO VALIDO")


#Solicita la cantidad de productos
while True:
   try:
      cantidad = int(input("Ingresa la cantidad de productos: "))
      if cantidad <= 0:
         print("la cantidad debe ser un numero positivo")
      else:
         break
   except ValueError:
      print("Porfavor ingrese un numero entero valido")

#SOlicitar descuento
