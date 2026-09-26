products = {}

def register_product():
    code = len(products) + 1
    name = input("Product Name: ")
    stock = 0

    products[code] = {
        "name": name,
        "stock": stock
    }
