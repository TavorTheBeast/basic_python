def arrow(my_char, max_length):
    # Top half of the arrow
    arrow_top = ""
    for i in range(1, max_length + 1):
        arrow_top += my_char * i + "\n"

    # Bottom half of the arrow
    arrow_bottom = ""
    for i in range(max_length - 1, 0, -1):
        arrow_bottom += my_char * i + "\n"

    # Combining top and bottom half with center line
    arrow = arrow_top + my_char * max_length + "\n" + arrow_bottom
    return arrow



print(arrow('*', 5))