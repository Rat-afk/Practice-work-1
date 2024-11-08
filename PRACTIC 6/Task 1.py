arr = ['apple', 'cube', 'fireplace', 'heroic', 'work']
oddWords = []

with open('numsTask1.txt', 'w') as file:
    for word in arr:
        file.write(str(word) + ' ')

print("The array of words:")

with open('numsTask1.txt', 'r') as file:
    words = list(map(str, file.readline().split()))

    print(words, '\n')

    for word in words:
        if len(word) % 2 == 1:
            oddWords.append(word)

print("The words of odd length:")
print(oddWords)
