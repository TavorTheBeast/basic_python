def are_files_equal(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        if f1.read() == f2.read():
            return True
        else:
            return False


print(are_files_equal("c:\vacation.txt", "c:\work.txt"))