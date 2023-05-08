def sort_words(file_path):
    with open(file_path) as f:
        words = f.read().split()
        sorted_words = sorted(set(words))
        print(sorted_words)

def reverse_lines(file_path):
    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            print(line.strip()[::-1])

def print_last_lines(file_path, n):
    with open(file_path) as f:
        lines = f.readlines()
        last_n_lines = lines[-n:]
        for line in last_n_lines:
            print(line.strip())

file_path = input("Enter file path: ")
operation = input("Enter operation name (sort, rev, last): ")

if operation == "sort":
    sort_words(file_path)
elif operation == "rev":
    reverse_lines(file_path)
elif operation == "last":
    n = int(input("Enter number of last lines to print: "))
    print_last_lines(file_path, n)
else:
    print("Invalid operation name")



