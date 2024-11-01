# Check if a number is within a specified range:


num = int(input("Enter a number: "))
start = int(input("Enter a range start: "))
end = int(input("Enter a range end: "))
if start <= num <= end:
    print("Within range")
else:
    print("Out of range")