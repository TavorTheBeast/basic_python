def func(num1, num2):
    """
    Returns the sum of two numbers.

    Parameters:
    num1 (int): The first number to be added.
    num2 (int): The second number to be added.

    Returns:
    int: The sum of the two numbers.
    """
    return num1 + num2

def main():
    # Call the function func with arguments 3 and 4 and print the result
    result = func(3, 4)
    print(result)

if __name__ == "__main__":
    main()


help(func)
