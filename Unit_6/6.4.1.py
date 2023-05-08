def check_valid_input(letter_guessed, old_letters_guessed):
    # Check if letter_guessed is a valid input
    if len(letter_guessed) != 1 or not letter_guessed.isalpha():
        print(False)

    # Check if letter_guessed was already guessed before
    elif letter_guessed in old_letters_guessed:
        print(False)

    # Otherwise, return True (valid input)
    else:
        print(True)


old_letters = ['a', 'b', 'c']
check_valid_input('C', old_letters)