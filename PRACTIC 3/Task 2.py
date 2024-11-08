from random import randint

while True:
    try:
        n = int(input("Enter a quantity of numbers: "))

        break
    except ValueError:
        print("Invalid value. Please enter a number", '\n')

with open('nums.txt', 'w') as file:
    for i in range(n):
        file.write(str(randint(-25, 25)) + ' ')

with open('nums.txt', 'r') as file:
    nums = list(map(int, file.readline().split()))

print("\nOriginal list:", nums)

nums = [i for i in nums if i % 2 != 0]

with open('nums.txt', 'w') as file:
    file.seek(0)
    file.truncate()

    for i in nums:
        file.write(str(i) + ' ')

print("Changed list:", nums)
