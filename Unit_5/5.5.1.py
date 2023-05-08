def is_valid_input(letter_guessed):
    if len(letter_guessed) != 1 or not letter_guessed.isalpha():
        # The guessed letter is not a single English letter
        print(False)

    # The guessed letter is a valid input
    print(True)


is_valid_input('a')

is_valid_input('A')

