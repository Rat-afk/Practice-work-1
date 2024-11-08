a = 0
num = 0
sumOfNums = 0

while True:
    try:
        while a <= 0:
            a = int(input("Enter a positive number a: "))

            if a == 0:
                print("Invalid value. Divide by 0", '\n')

                continue
            elif a < 0:
                print("Invalid value. Please enter a positive number", '\n')

                continue

        break

    except ValueError:
        print("Invalid value. Please enter a positive number" + '\n')

print("\nEnter a negative number to stop", '\n')

while num >= 0:
    num = int(input("Enter a positive number: "))

    if num % a == 0:
        sumOfNums += num

print("Sum of numbers =", sumOfNums)
