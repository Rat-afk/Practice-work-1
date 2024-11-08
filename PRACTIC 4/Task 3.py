from random import randint

ratioOfNumbers = 0
maxNumber = -10000
minNumber = 10000

while True:
    try:
        n = int(input("Enter a quantity of numbers: "))

        if n < 0:
            print("Invalid value. Please enter a positive number" + '\n')
        else:
            break
    except ValueError:
        print("Invalid value. Please enter a positive number" + '\n')

with open('numsTask3.txt', 'w') as file:
    for i in range(n):
        if i < n - 1:
            file.write(str(randint(-25, 25)) + ',')
        else:
            file.write(str(randint(-25, 25)))

with open('numsTask3.txt', 'r') as file:
    nums = list(map(int, file.readline().split(',')))

    for i in nums:
        if i > maxNumber:
            maxNumber = i
        if i < minNumber:
            minNumber = i

    ratioOfNumbers = maxNumber - minNumber

print()
print("Array:", nums, '\n')
print("Ratio between max number and min number of the array =", ratioOfNumbers)
