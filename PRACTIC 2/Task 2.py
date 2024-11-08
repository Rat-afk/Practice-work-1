arr = []

while True:
    try:
        endOfArray = int(input("Enter a number of end of the array: "))

        break
    except ValueError:
        print("Invalid value. Please enter a number", '\n')

for i in range(1, endOfArray + 1, 2):
    arr.append(i)

print("\nArray of odd numbers:")
print(arr)
