def squared_numbers(start, stop):
    result = []
    while start <= stop:
        result.append(start ** 2)
        start += 1
    print(result)


squared_numbers(-3, 3)