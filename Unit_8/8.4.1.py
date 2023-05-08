HANGMAN_PHOTOS = {
    1: """
    x-------x
    """,
    2: """
    x-------x
    |
    |
    |
    |
    |
    """,
    3: """
    x-------x
    |       |
    |       0
    |
    |
    |
    """,
    4: """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,
    5: """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """,
    6: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """,
    7: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """
}

def print_hangman(num_of_tries):
    if num_of_tries <= 0:
        print(HANGMAN_PHOTOS[1])
    elif num_of_tries >= 7:
        print(HANGMAN_PHOTOS[7])
    else:
        print(HANGMAN_PHOTOS[num_of_tries])


num_of_tries = 7
print_hangman(num_of_tries)