def sort_prices(list_of_tuples):
    sorted_list = sorted(list_of_tuples, key=lambda x: float(x[1]), reverse=True)
    print(sorted_list)

products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
sort_prices(products)