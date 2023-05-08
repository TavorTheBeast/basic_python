def format_list(my_list):
    even_indices = range(0, len(my_list), 2)  # get the even indices
    formatted_str = ", ".join(my_list[i] for i in even_indices)  # join even-indexed strings with a comma and space
    return f"{formatted_str} and {my_list[-1]}"  # add the last string preceded by 'and'

# example usage
my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
formatted_str = format_list(my_list)
print(formatted_str)  # "apple, cherry and date"

