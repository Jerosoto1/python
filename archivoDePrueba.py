#Test Invetory

#Here we are burning the dictionary list so that it is not empty and we add some products to it.
inventory = [
    {"name":"nails","price":5000,"quantity":22},
    {"name":"milk", "price":3200,"quantity":24},
    {"name":"coffe","price":2000,"quantity":12},
    {"name":"rice","price":2200,"quantity":46},
    {"name":"candy","price":500,"quantity":100},
    {"name": "oil", "price": 12000, "quantity": 24}
]



#Here we are giving you a function so that when you enter numbers that are not valid, it asks you to enter a negative number.
def input_num(prompt, tipo=float):
    while True:
        entrance = input(prompt)
        try:
            valor = tipo(entrance)
            if valor <= 0:
                print("Must be a positive number!.")
                continue
            return valor
        except ValueError:
            print("\nInvalid entry. Please enter a valid number.")


#Here we create a function so that you can add product and in case you want to enter a product that already exists, it will tell you a message that the product already exists.
def add_product(name, price, quantity):
    for product in inventory:
        if product["name"].lower() == name.lower():  
            print("\nThe product already exists in the inventory.")
            return
    inventory.append({"name": name, "price": round(price, 2), "quantity": int(quantity)})
    print(f"\nProduct '{name}' successfully added with price ${price:.2f} and quantity {quantity}.")


#Here we make a new function so that the user can check if the product is available or, if so, print a message that it is not found.
def search_product(name):
    for product in inventory:
        if product["name"].lower() == name.lower():  
            print(f"\n{product['name']} | Price: ${product['price']:.2f} | Quantity: {product['quantity']}")
            return
    print("\nproduct not found.")


#Here by performing this function we can easily update the price of the product.
def update_price(name, new_price):
    for product in inventory:
        if product["name"].lower() == name.lower():
            product["price"] = round(new_price, 2)
            print(f"\nPrice of '{name}' updated to ${new_price:.2f}.")
            return
    print("\nproduct not found.")

#Here we perform a function so that products can be easily removed from the inventory.
def del_product(name):
    for product in inventory:
        if product["name"].lower() == name.lower():
            inventory.remove(product)
            print(f"The Product '{name}' was removed from inventory.")
            return
    print("\nProduct not found.")

#Here with this function what we do is calculate the total value of the inventory
def total_inventory_value():
    total = sum(product["price"] * product["quantity"] for product in inventory)
    print(f"\nTotal inventory value: ${total:.2f}")


#Here we create the menu with a function so that when you need to call it, it can be done much faster.
def menu ():
    while True: 
        print ("\n°°° Menu °°°\n")
        print ("1. Add product")
        print ("2. Search product")
        print ("3. Update price")
        print ("4. Delete product from inventory")
        print ("5. Calculate the price of inventory")
        print ("\n6. Exit-> \n")
        
        option = input("Choose an option (1-6): ")



        #Here we call the function and ask it for the requirements to add the product
        if option == "1":
            name = input("\nProduct title: ").strip()
            price = input_num("Price: ")
            quantity = input_num("Quantity: ", int)
            add_product(name, price, quantity)



        #Here we just tell it to call the function and give the name of the product to search for.
        elif option == "2":
            name = input ("Give me the name of the product to search for it: ")
            search_product(name)



        #Here we ask the user to enter the name of the product to update its price
        elif option == "3":
            name = input("product title to update: ").strip()
            new_price = input_num("New price: ")
            update_price(name, new_price)



        #Here we ask for the name of the peoduct to remove it from the inventory
        elif option == "4":
            name = input ("product title to delete: ")
            del_product(name)



        #Here we only call the function to know how much the entire inventory is worth.
        elif option == "5":
            total_inventory_value()



        #Here we simply break the program and get out of it
        elif option == "6":
            print ("\n  °°° Exiting program... °°° \n")
            break 
        else:
            print ("\nInvalid option. Please choose between 1 and 6\n")

if __name__ == "__main__":
    menu()