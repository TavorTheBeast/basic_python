def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        old_letters_guessed_sorted = sorted(old_letters_guessed)
        print("X\n" + "->".join(old_letters_guessed_sorted))
        return False

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


old_letters = ['a', 'p', 'c', 'f']
try_update_letter_guessed('A', old_letters)