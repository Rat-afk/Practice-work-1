from random import randint, sample

num1 = 10
num2 = 6
n = randint(1, 1000)
lines = 0
quantityOfLuckyNumbers = 0

with open('input.txt', 'w') as file:
    file.write(' '.join(map(str, sample(range(1, 33), num1))) + '\n')

    file.write(str(n) + '\n')

    while lines < n:
        row_numbers = sample(range(1, 33), num2)

        file.write(' '.join(map(str, row_numbers)) + '\n')

        lines += 1

with open('input.txt', 'r') as file:
    nums = list(map(int, file.readline().split()))
    numberOfTickets = int(file.readline())

    with open('output.txt', 'w') as fileOutput:
        for _ in range(numberOfTickets):
            row = list(map(int, file.readline().split()))

            quantityOfLuckyNumbers = sum(1 for x in row if x in nums)

            if quantityOfLuckyNumbers >= 3:
                fileOutput.write("Lucky\n")
            else:
                fileOutput.write("Unlucky\n")

with open('output.txt', 'r') as file:
    print(file.read())
