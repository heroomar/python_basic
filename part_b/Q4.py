# Print the multiplication table of a given number.


num = int(input("Enter number: "))

for x in xrange(1,11):
	print(f"{num} X {x} = {num*x}")