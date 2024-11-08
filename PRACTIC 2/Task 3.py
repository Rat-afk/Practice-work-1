while True:
    try:
        n = int(input("Enter array size: "))

        if n < 0:
            print("Invalid value. Please enter a positive number" + '\n')
        else:
            break
    except ValueError:
        print("Invalid value. Please enter a positive number" + '\n')

print("Array of the numbers:")

matrix = [[1] * n for _ in range(n)]

for i in range(1, n):
    for j in range(1, n):
        matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

for arr in matrix:
    print(arr)
