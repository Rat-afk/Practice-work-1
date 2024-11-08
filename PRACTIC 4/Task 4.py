from random import randint

quantOfNeiNum = 0

while True:
    try:
        n = int(input("Enter a quantity of numbers: "))

        if n < 0:
            print("Invalid value. Please enter a positive number" + '\n')
        else:
            break
    except ValueError:
        print("Invalid value. Please enter a positive number" + '\n')

with open('numsTask4.txt', 'w') as file:
    for i in range(n):
        if i < n - 1:
            file.write(str(randint(-2, 2)) + ' ')
        else:
            file.write(str(randint(-2, 2)))

with open('numsTask4.txt', 'r') as file:
    nums = list(map(int, file.readline().split()))

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            quantOfNeiNum += 1

print()
print("Array:", nums, '\n')
print("Quantity of neighboring numbers in the array =", quantOfNeiNum)
