def print_products(products):
    print("Shopping list:")
    print(", ".join(products))

def print_num_products(products):
    print("Number of products:", len(products))

def is_product_on_list(products):
    product = input("Enter a product: ")
    if product in products:
        print("Yes, {} is on the list".format(product))
    else:
        print("No, {} is not on the list".format(product))

def print_num_occurrences(products):
    product = input("Enter a product: ")
    count = products.count(product)
    print("{} appears {} time(s) in the list".format(product, count))

def delete_product(products):
    product = input("Enter a product to delete: ")
    if product in products:
        products.remove(product)
        print("{} removed from the list".format(product))
    else:
        print("{} is not in the list".format(product))

def add_product(products):
    product = input("Enter a product to add: ")
    products.append(product)
    print("{} added to the list".format(product))

def print_invalid_products(products):
    invalid_products = [p for p in products if len(p) < 3 or not p.isalpha()]
    if invalid_products:
        print("Invalid products:", ", ".join(invalid_products))
    else:
        print("There are no invalid products in the list")

def remove_duplicates(products):
    products_set = set(products)
    products.clear()
    products.extend(products_set)
    print("Duplicates removed")

def main():
    products_str = input("Enter a list of products (separated by commas): ")
    products = products_str.split(",")

    while True:
        print("\nMain menu:")
        print("1. Print the list of products")
        print("2. Print the number of products in the list")
        print("3. Check if a product is on the list")
        print("4. Count the number of occurrences of a product")
        print("5. Delete a product from the list")
        print("6. Add a product to the list")
        print("7. Print invalid products")
        print("8. Remove duplicates from the list")
        print("9. Exit")

        choice = int(input("Enter a choice (1-9): "))

        if choice == 1:
            print_products(products)
        elif choice == 2:
            print_num_products(products)
        elif choice == 3:
            is_product_on_list(products)
        elif choice == 4:
            print_num_occurrences(products)
        elif choice == 5:
            delete_product(products)
        elif choice == 6:
            add_product(products)
        elif choice == 7:
            print_invalid_products(products)
        elif choice == 8:
            remove_duplicates(products)
        elif choice == 9:
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again")


main()
