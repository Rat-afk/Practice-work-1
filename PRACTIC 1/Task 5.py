text = input("Enter your text: ")
wordsCount = 0

for i in range(len(text.split())):
    wordsCount += 1

print("\nStart " + text + " End\n")
print("Count of words:", wordsCount)
