arr = []
num = 1
sumNums = 0
multNums = 1
elementsCounter = 0
arithmeticMean = 0

print("Enter 0 to stop\n")

while num != 0:
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Invalid value. Please enter a number\n")

        continue

    if num != 0:
        arr.append(num)
        elementsCounter += 1

for i in arr:
    sumNums += i
    multNums *= i
    arithmeticMean = sumNums / elementsCounter

print("\nArray:", arr)
print("Sum of numbers of the array:", sumNums)
print("Mult of numbers of the array:", multNums)
print("Arithmetic mean of numbers of the array:", round(arithmeticMean, 2))
