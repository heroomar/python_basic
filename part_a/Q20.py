# Check if a string is uppercase, lowercase, or a mix:

string = input("Enter a string: ")
if string.isupper():
    print("Uppercase")
elif string.islower():
    print("Lowercase")
else:
    print("Mixed case")