def ten(n):
    if n % 2 == 0 and n % 10 == 0:
        print("The number", n, "is even and multiples of 10")
    elif n % 2 == 0 and n % 10 != 0:
        print("The number", n, "is even but not multiples of 10")
    else:
        print("The number", n, "is not even and not multiples of 10")

while True:
    try:
        num = int(input("Enter a number: "))

        break
    except ValueError:
        print("Invalid value. Please enter a number" + '\n')

ten(num)
