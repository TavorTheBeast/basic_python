# Accept a character from the user
user_input = input("Enter a character: ")

# Check if the input is a single English letter
if len(user_input) == 1 and user_input.isalpha() and user_input.isascii():
    # If it is, print it to the screen in lowercase
    print(user_input.lower())
# Check if the input is a string of letters with more than one letter
elif len(user_input) > 1 and user_input.isalpha():
    print("E1")
# Check if the input is a character that is not an English letter
elif len(user_input) == 1 and not user_input.isalpha() and user_input.isascii():
    print("E2")
# Check if the input is a letter string that has more than one character and also contains non-English characters
elif len(user_input) > 1 and not user_input.isalpha():
    print("E3")
else:
    print("Invalid input")
