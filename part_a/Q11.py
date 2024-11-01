# Check if a number is a multiple of both 3 and 5:

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Multiple of both 3 and 5")
else:
    print("Not a multiple of both")