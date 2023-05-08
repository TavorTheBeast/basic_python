# Receive input of three-digit number
number = int(input("Enter a three-digit number: "))

# Calculate total number of collected acorns
total = (number // 100) + ((number // 10) % 10) + (number % 10)

# Calculate the number of acorns each pig will get and the remainder
acorns_per_pig = total // 3
remainder = total % 3

# Print the total number of collected acorns, the number of acorns each pig will get, and the remainder
print(f"Total number of collected acorns: {total}")
print(f"Number of acorns each pig will get: {acorns_per_pig}")
print(f"Remainder: {remainder}")

# Determine whether the total number of acorns can be evenly divided among the three pigs
is_divisible = (total % 3 == 0)
print(f"Is divisible by 3: {is_divisible}")





