from random import randint

maxNum = -10000
maxNumIndex = 0
sumOfNums = 0

while True:
    try:
        n = int(input("Enter a quantity of numbers: "))

        if n < 0:
            print("Invalid value. Please enter a positive number" + '\n')
        else:
            break
    except ValueError:
        print("Invalid value. Please enter a positive number" + '\n')

with open('numsTask4.txt','w') as file:
    for i in range(n):
        file.write(str(randint(-2, 2)) + ' ')

with open('numsTask4.txt','r') as file:
    nums = list(map(int, file.readline().split()))

for i in nums:
    if i > maxNum:
        maxNum = i
        maxNumIndex = nums.index(i)

for i in range (len(nums)):
    if nums[i] - maxNum == -1:
        sumOfNums += nums[i]

print("Array of numbers: " + str(nums) + '\n')
print("Sum of numbers =", sumOfNums)
