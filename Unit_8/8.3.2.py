mariah = {
    "first_name": "Mariah",
    "last_name": "Carey",
    "birth_date": "27.03.1970",
    "hobbies": ["Sing", "Compose", "Act"]
}

# Ask the user for input
choice = int(input("Enter a number between 1 and 7: "))

# Perform the appropriate action based on the user's input
if choice == 1:
    print(mariah["last_name"])
elif choice == 2:
    print(mariah["birth_date"][3:5])
elif choice == 3:
    print(len(mariah["hobbies"]))
elif choice == 4:
    print(mariah["hobbies"][-1])
elif choice == 5:
    mariah["hobbies"].append("Cooking")
    print(mariah["hobbies"])
elif choice == 6:
    birth_date = mariah["birth_date"].split(".")
    birth_tuple = tuple(int(date) for date in birth_date)
    print(birth_tuple)
elif choice == 7:
    birth_year = int(mariah["birth_date"][-4:])
    age = 2023 - birth_year
    mariah["age"] = age
    print(mariah["age"])
else:
    print("Invalid choice!")

