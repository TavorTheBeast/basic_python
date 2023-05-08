def count_chars(my_str):
    # Remove all spaces from the string
    my_str = my_str.replace(' ', '')

    # Initialize an empty dictionary
    char_dict = {}

    # Loop through each character in the string
    for char in my_str:
        # If the character is not already in the dictionary, add it
        if char not in char_dict:
            char_dict[char] = [1]
        # If the character is already in the dictionary, increment its count
        else:
            char_dict[char].append(1)

    # Return the dictionary
    print(char_dict)


magic_str = "abra cadabra"
count_chars(magic_str)