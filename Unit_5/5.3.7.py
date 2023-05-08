def chocolate_maker(small, big, x):
    # Calculate the maximum length of a line that can be created using the given chocolate cubes
    max_line_length = small + big * 5

    # Check if it is possible to create a line of length x
    if max_line_length >= x and (x % 5) <= small:
        print(True)
    else:
        print(False)


chocolate_maker(3, 1, 8)

chocolate_maker(3, 1, 9)

chocolate_maker(3, 2, 10)