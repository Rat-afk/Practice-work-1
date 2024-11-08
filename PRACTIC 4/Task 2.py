from random import uniform

sumOfNumbers = 0

while True:
    try:
        n = int(input("Enter a quantity of numbers: "))

        if n < 0:
            print("Invalid value. Please enter a positive number" + '\n')
        else:
            break
    except ValueError:
        print("Invalid value. Please enter a positive number" + '\n')

with open('numsTask2.txt', 'w') as file:
    for i in range(n):
        file.write(str(round(uniform(-25.0, 25.0 ), 2)) + ';')

with open('numsTask2.txt', 'r') as file:
    nums = list(map(float, file.readline().split(';')[:-1]))

    for i in nums:
        if i > 0:
            sumOfNumbers += i

print("\nArray:", nums, '\n')
print("Sum of positive numbers of the array =", round(sumOfNumbers, 2))
