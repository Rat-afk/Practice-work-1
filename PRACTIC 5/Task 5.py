from random import randint

minNum = 10000
minNumIndex = 0
maxNum = -10000
maxNumIndex = 0
sumOfNums = 0
quantOfNums = 0

while True:
    try:
        n = int(input("Enter a quantity of numbers: "))

        if n < 0:
            print("Invalid value. Please enter a positive number" + '\n')
        else:
            break
    except ValueError:
        print("Invalid value. Please enter a positive number" + '\n')

with open('numsTask5.txt','w') as file:
    for i in range(n):
        file.write(str(randint(-25, 25)) + ' ')

with open('numsTask5.txt','r') as file:
    nums = list(map(int, file.readline().split()))

for i in nums:
    if i < minNum:
        minNum = i
        minNumIndex = nums.index(i)

    if i > maxNum:
        maxNum = i
        maxNumIndex = nums.index(i)

for i in range (len(nums)):
    if ((i < minNumIndex) and (i > maxNumIndex)) or ((i > minNumIndex) and (i < maxNumIndex)):
        sumOfNums += nums[i]
        quantOfNums += 1

print("\nArray of numbers: " + str(nums) + '\n')

try:
    print("Arithmetic mean of numbers between minimum number and maximum number =", round((sumOfNums / quantOfNums), 2))
except ZeroDivisionError:
    print("Division by zero occurs")
