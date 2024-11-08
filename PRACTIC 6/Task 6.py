from random import randint, uniform

nums = [round(uniform(-25.0, 25.0), 2) for _ in range(randint(2, 10))]
posNums = []
negNums = []

print("Original array:", nums)

for num in nums:
    if num < 0:
        negNums.append(num)
    else:
        posNums.append(num)

print("\nArray of positive numbers:", posNums)
print("\nArray of negative numbers:", negNums)
