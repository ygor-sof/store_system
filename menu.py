from products import register_product
from products import products

def main_menu():
    main_option = 0

    while main_option != 5:
        print("")
        print("1 - register products")
        print("2 - products")
        print("3 - exit")
        option = int(input("select Option: "))
        if option == 1:
            print("register")
            register_product()
            print(products)

        elif option == 2:
            print(products)

        print("exit!")