# Classify the triangle based on sides:

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = float(input("Enter side C: "))
if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")