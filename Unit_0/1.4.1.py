import random

print("Welcome to the Hangman game!")
print("  _    _ ")
print(" | |  | |")
print(" | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __")
print(" |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
print(" | |  | | (_| | | | | (_| | | | | | | (_| | | | |")
print(" |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
print("                      __/ |                       ")
print("                     |___/                        ")

attempts = random.randint(5, 10)
print("You have", attempts, "guessing attempts to save the hangman!")
