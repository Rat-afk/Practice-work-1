from random import randint

minNum = 10000
minNumIndex = 0
multOfNums = 1

while True:
    try:
        n = int(input("Enter a quantity of numbers: "))

        if n < 0:
            print("Invalid value. Please enter a positive number" + '\n')
        else:
            break
    except ValueError:
        print("Invalid value. Please enter a positive number" + '\n')

with open('numsTask1.txt','w') as file:
    for i in range(n):
        file.write(str(randint(-25, 25)) + ' ')

with open('numsTask1.txt','r') as file:
    nums = list(map(int, file.readline().split()))

for i in nums:
    if i < minNum:
        minNum = i
        minNumIndex = nums.index(i)

for i in range (len(nums)):
    if i > minNumIndex:
        multOfNums *= nums[i]

print("\nArray of numbers: " + str(nums) + '\n')
print("Mult of numbers after the minimum number =", multOfNums)
