string = input("Enter a string: ")
string = string.lower().replace(" ", "") # convert to lowercase and remove spaces
if string == string[::-1]:
    print("OK")
else:
    print("NOT")
