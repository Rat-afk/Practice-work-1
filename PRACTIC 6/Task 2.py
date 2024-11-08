arr = ['apple', 'cube', 'fireplace', 'heroic', 'work']

with open('numsTask2.txt', 'w') as file:
    for word in arr:
        file.write(str(word) + '\n')

print("Words:")

with open('numsTask2.txt', 'r') as file:
    words = list(map(str, file.read().split()))

print(" ".join(map(str, words)))
