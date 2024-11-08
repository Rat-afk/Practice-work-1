from random import uniform

while True:
    try:
        n = int(input("Enter a quantity of numbers: "))

        if n < 0:
            print("Invalid value. Please enter a positive number" + '\n')
        else:
            break
    except ValueError:
        print("Invalid value. Please enter a positive number" + '\n')

with open('numsTask2.txt','w') as file:
    for i in range(n):
        file.write(str(round(uniform(-25.0, 25.0), 2)) + ';')

with open('numsTask2.txt','r') as file:
    nums = list(map(float, file.readline().split(';')[:-1]))

print("\nArray of numbers:", nums, '\n')

for i in range(len(nums) - 1):
    for j in range(len(nums) - 1 - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print("Sorted array of numbers:", nums)

with open('numsTask2.txt','w') as file:
    for i in nums:
        file.write(str(i) + ';')
