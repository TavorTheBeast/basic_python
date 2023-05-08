def last_early(my_str):
    last_char = my_str[-1]
    if last_char in my_str[:-1]:
        print(True)
    else:
        print(False)

last_early("happy birthday")