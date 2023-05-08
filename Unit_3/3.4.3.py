string = input("Enter a string: ")

length = len(string)
midpoint = length // 2

first_half = string[:midpoint]
second_half = string[midpoint:]

# If the length of the string is odd, the first half will be one character shorter
if length % 2 == 1:
    first_half = first_half[:-1]

result = first_half.lower() + second_half.upper()

print("Result: " + result)
