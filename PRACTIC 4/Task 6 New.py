def vector_cross_mult(x1, y1, x2, y2):
    return x1 * y2 - y1 * x2

def is_point_in_triangle(a_cor, b_cor):
    x1, y1 = 0, 2
    x2, y2 = -2, -3
    x3, y3 = 2, -3

    cross1 = vector_cross_mult(x2 - x1, y2 - y1, a_cor - x1, b_cor - y1)
    cross2 = vector_cross_mult(x3 - x2, y3 - y2, a_cor - x2, b_cor - y2)
    cross3 = vector_cross_mult(x1 - x3, y1 - y3, a_cor - x3, b_cor - y3)

    return (cross1 >= 0 and cross2 >= 0 and cross3 >= 0) or \
        (cross1 <= 0 and cross2 <= 0 and cross3 <= 0)

while True:
    try:
        a = float(input("Enter a coordinate a: "))
        b = float(input("Enter a coordinate b: "))

        break
    except ValueError:
        print("Invalid value. Please enter a number" + '\n')

if is_point_in_triangle(a, b):
    print("The point is located in the area")
else:
    print("The point is outside the area")
