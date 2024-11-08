from random import uniform

def temp(array, day):
    average = []
    sums = 0

    for i in array:
        for l in i:
            sums += l

        average.append(round((sums / day), 1))

        sums = 0

    return average

def sort(array):
    for i in range (len(array) - 1):
        for l in range(len(array) - 1 - i):
            if array[l] > array[l + 1]:
                array[l], array[l + 1] = array[l + 1], array[l]

    return array

days = 30
months = 12
monthsCounter = 0
sumOfAverTemp = 0
averTempYear = 0
temperature = [[] for i in range(months)]
months_names = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

for arr in temperature:
    if (monthsCounter == 0) or (monthsCounter == 1):
        for j in range(days):
            arr.append(round(uniform(-30.0, -10.0), 1))
    elif (monthsCounter == 2) or (monthsCounter == 3):
        for j in range(days):
            arr.append(round(uniform(5.0, 15.0), 1))
    elif (monthsCounter == 4) or (monthsCounter == 5):
        for j in range(days):
            arr.append(round(uniform(15.0, 25.0), 1))
    elif (monthsCounter == 6) or (monthsCounter == 7):
        for j in range(days):
             arr.append(round(uniform(20.0, 30.0), 1))
    elif (monthsCounter == 8) or (monthsCounter == 9):
        for j in range(days):
            arr.append(round(uniform(0.0, 15.0), 1))
    else:
        for j in range(days):
            arr.append(round(uniform(-5.0, -15.0), 1))

    monthsCounter += 1

print("Temperature for every day of every month:\n")

for i in range(len(temperature)):
    print(months_names[i] + ":")
    print(temperature[i], '\n')

averTemp = temp(temperature, days)

for i in averTemp:
    sumOfAverTemp += i
    averTempYear = round(sumOfAverTemp / monthsCounter, 2)

print("\nAverage temperature for every month:" + '\n' + str(averTemp) + '\n')
print("Sorted array of average temperatures:" + '\n' + str(sort(averTemp)) + '\n')
print("Average temp for the year =" , averTempYear)
