def distance(num1, num2, num3):
    if abs(num1 - num2) <= 1 and abs(num1 - num3) >= 2 and abs(num2 - num3) >= 2:
        print(True)
    elif abs(num1 - num3) <= 1 and abs(num1 - num2) >= 2 and abs(num3 - num2) >= 2:
        print(True)
    else:
        print(False)


distance(1, 2, 10)