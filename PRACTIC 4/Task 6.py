from math import sqrt

top = 2
bottom = -3
baseOfTriangle = 4
left = -(sqrt((top + abs(bottom) ** 2) + (baseOfTriangle / 2) ** 2))
right = abs(left)

try:
    a = float(input("Enter a coordinate a: "))
    b = float(input("Enter a coordinate b: "))
except ValueError:
    print("Invalid value. Please enter a number" + '\n')
    a = float(input("Enter a coordinate a: "))
    b = float(input("Enter a coordinate b: "))

if (a <= right) and (a >= left) and (b <= top) and (b >= bottom):
    print("The point is located in the area")
else:
    print("The point is outside the area")