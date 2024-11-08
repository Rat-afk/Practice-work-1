from random import randint

n = randint(2, 5)
m = randint(2, 5)
oneCount = 0

a = [[] for _ in range(n)]

print("Original array:")

for arr in a:
    for i in range(m):
        randNum = randint(0, 25)

        arr.append(1 if randNum % 2 == 1 else 0)

    print(arr)

print()
print("Changed array:")

for arr in a:
    for i in arr:
        if i == 1:
            oneCount += 1

    arr.append(0 if oneCount % 2 == 0 else 1)

    oneCount = 0

    print(arr)
