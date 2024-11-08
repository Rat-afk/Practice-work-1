from random import randint

def water(arr):
    volume = 0
    left = 0
    right = len(arr) - 1

    while left < right:
        if height[left] < height[right]:
            h = height[left]
        else:
            h = height[right]

        width = right - left

        area = width * h

        if volume < area:
            volume = area

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return volume

while True:
    try:
        i = int(input("Enter a quantity of numbers: "))

        break
    except ValueError:
        print("Invalid value. Please enter a number", '\n')

with open('water.txt', 'w') as file:
    for j in range(i):
        file.write(str(randint(-25, 25)) + ' ')

with open('water.txt', 'r') as file:
    height = list(map(int, file.readline().split()))

print("\nheight =", height, '\n')
print("Max volume =", water(height))
