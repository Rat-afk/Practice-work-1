from random import randint

minNum = 0
minNumNumber = 0
arr = [randint(1,100) for i in range(10)]

for i in arr:
    if i > minNum:
        minNum = i

for i in range(len(arr)):
    if arr[i] < minNum:
        minNum = int(arr[i])

        minNumNumber = i + 1

print("Array:", arr)
print("Number of minimal element of the array:", minNumNumber)
