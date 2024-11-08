from random import randint

def nums(size, start, end):
    arr = [randint(start, end) for _ in range(size)]

    prnt(arr)

def prnt(arr):
    print("\nArray:", arr)

    for i in arr:
        print(arr.index(i), "->", i)

arrSize = 0
startOfRandom = 0
endOfRandom = 0

while True:
    try:
        arrSize = int(input("Enter the size of the array: "))
        startOfRandom = int(input("Enter the starting number: "))
        endOfRandom = int(input("Enter the ending number: "))

        break
    except ValueError:
        print("Invalid value. Please enter a number\n")

nums(arrSize, startOfRandom, endOfRandom)
