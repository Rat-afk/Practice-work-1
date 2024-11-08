arr = []
counter = 0

while True:
    try:
        num = int(input("Enter a star number: "))

        break
    except ValueError:
        print("Invalid value. Please enter a number", '\n')

while counter != 100:
    arr.append(num)

    num -= 3
    counter += 1

print("\nArray of decreasing numbers:")
print(arr)
