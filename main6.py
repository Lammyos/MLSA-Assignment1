# A simple inventory system
inventory = {}


def add_product():
    global name, quantity, price, category, threshold, sales
    name = input("Enter the product's name: ").upper()
    quantity = input("Enter the product's quantity: ")
    price = input("Enter the product's price: ")
    category = input("Enter the product's category: ").title()
    threshold = input("Enter the product's threshold: ")
    sales = input("Enter the product's sales: ")

    inventory[name] = {
    "quantity": quantity,
    "price": price, 
    "category": category, 
    "threshold": threshold,
    "sales": sales
    }
    print("Product have been added successfully.")


def remove_product():
    name2 = input("Enter name of product to be removed: ").upper()
    if name2 in inventory:
        del inventory[name2]
        print("Product has been deleted successfully.")
    else:
        print("Sorry, Product is not in inventory.")


def update_quantity():
    global price, category, threshold, sales
    name3 = input("Enter product name: ").upper()
    if name3 in inventory:
        quantity = inventory[name3]["quantity"]
        print(f"{name3}'s old quantity is {quantity}")
        new_quantity = input("Enter the new quatity of the product: ")
        inventory[name3] = {
            "quantity": new_quantity,
            "price": price, 
            "category": category, 
            "threshold": threshold,
            "sales": sales
        }
        print("Product's quantity has been updated succesfully.")
    else:
        print("Sorry, Product is not in the inventory.")


def search_product():
    name4 = input("Enter product's name: ").upper()
    if name4 in inventory:
        result = inventory[name4]
        print(result)
    else:
        print("Sorry, Product is not in inventory.")


while True:
    print("Do you want to:"
          "\n1. Add new products."
          "\n2. Remove existing products."
          "\n3. Update product quantities."
          "\n4. Search for a product."
          "\n5. Display the entire inventory."
          "\n6. Exit inventory. ")
    opt = input("Enter option by number: ")
    if opt == "1":
        add_product()
        print("Anything else?")
    elif opt == "2":
        remove_product()
        print("Anything else?")
    elif opt == "3":
        update_quantity()
        print("Anything else?")
    elif opt == "4":
        search_product()
        print("Anything else?")
    elif opt == "5":
        if inventory == {}:
            print("There is nothing in the inventory.")
        else:
            print(inventory)
        print("Anything else?")
    elif opt == "6":
        print("Thank you and Goodbye.")
        break
    else:
        print("Option not recognised. Try again.")
        

