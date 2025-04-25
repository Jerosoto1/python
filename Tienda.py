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
product = input("Ingrese el nombre del producto: ")

#Solicita el precio del producto
while True:
    try:
      price = float(input("Ingrese el precio del producto: "))
      if price <= 0:
         print("El precio debe ser numero positivo")
      else:
         break
    except ValueError:
       print("INGRESA UN NUMERO VALIDO")


#Solicita la cantidad de productos 
while True:
   try:
      quantity = int(input("Ingresa la cantidad de productos: "))
      if quantity <= 0:
         print("la cantidad debe ser un numero positivo")
      else:
         break
   except ValueError:
      print("Porfavor ingrese un numero entero valido")

#SOlicitar descuento 
while True:
   try:
      discount = float(input("Ingresa cuanto descuento quieres aplicar del (0 a 100): "))
      if discount < 0 or discount > 100: 
         print("El descuento debe de estar de 0 a 100")
      else:
         break
   except ValueError:
      print("Por favor, ingresa un numero valido.")

#Calcula el costo todal sin descuento
CostWithoutDiscount = price * quantity

#Aplicar el descuento
DiscountAmount = CostWithoutDiscount * (discount / 100)
FinalCost = CostWithoutDiscount - DiscountAmount

#Mostrar el resultado con dos decimales
print(f"Producto: {product}")
print(f"costo total (con descuento): ${FinalCost:.2f}")
