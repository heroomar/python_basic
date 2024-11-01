# Check if a year is a century year:

year = int(input("Enter a year: "))
if year % 100 == 0:
    print("Century Year")
else:
    print("Not a Century Year")