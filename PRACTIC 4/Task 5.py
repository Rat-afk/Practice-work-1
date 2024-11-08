top = 4
bottom = -2
right = 3
left = -1

while True:
    try:
        a = float(input("Enter a coordinate a: "))
        b = float(input("Enter a coordinate b: "))

        break
    except ValueError:
        print("Invalid value. Please enter a number" + '\n')

if (a < right) and (a > left) and (b < top) and (b > bottom):
    print("The point is located in the area")
elif ((a == right) and (b <= top) and (b >= bottom)) or ((a == left) and (b <= top) and (b >= bottom))\
        or ((b == top) and (a <= right) and (a >= left)) or ((b == bottom) and (a <= right) and (a >= left)):
    print("The point is on the boundary of the area")
else:
    print("The point is outside the area")
