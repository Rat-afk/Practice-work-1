arr = []
maxLen = 1
maxLenWord = ''
minLen = 10000
minLenWord = ''
element = ' '

print("Enter nothing to stop\n")

while element != '':
    element = input('Enter a text: ')

    if element != '':
        arr.append(element)

for i in range(len(arr)):
    if len(arr[i]) > maxLen:
        maxLen = len(arr[i])
        maxLenWord = arr[i]

    if len(arr[i]) < minLen:
        minLen = len(arr[i])
        minLenWord = arr[i]

print("\nArray:", arr)
print("Max length of the text:", maxLen, "(" + maxLenWord + ")")
print("Min length of the text:", minLen, "(" + minLenWord + ")")
