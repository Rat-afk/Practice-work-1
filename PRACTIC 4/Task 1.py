mult = 1

while True:
    try:
        n = int(input("Enter a positive number: "))

        if n <= 0:
            print("Invalid value. Please enter a positive number" + '\n')
        else:
            break
    except ValueError:
        print("Invalid value. Please enter a positive number" + '\n')

for i in range(3, n + 1, 3):
    mult *= i

print("\nMult of natural numbers to", n, "=", mult)
