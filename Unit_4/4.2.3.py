temperature = input("Enter a temperature with a suffix of C or F: ")

if temperature[-1].lower() == "c":
    celsius = float(temperature[:-1])
    fahrenheit = (celsius * 9/5) + 32
    print(str(fahrenheit) + "F")
elif temperature[-1].lower() == "f":
    fahrenheit = float(temperature[:-1])
    celsius = (fahrenheit - 32) * 5/9
    print(str(celsius) + "C")
else:
    print("Invalid input")
