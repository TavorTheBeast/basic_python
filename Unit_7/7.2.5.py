def sequence_del(my_str):
    # Initialize the result string with the first character of the input string
    result = my_str[0]

    # Iterate over the characters of the input string, skipping the first one
    for i in range(1, len(my_str)):
        # If the current character is different from the previous one, add it to the result
        if my_str[i] != my_str[i - 1]:
            result += my_str[i]

    print(result)


sequence_del("ppyyyyythhhhhooonnnnn")