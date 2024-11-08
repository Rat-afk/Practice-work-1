from random import uniform

def temp(array, day):
    average = {}
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
monthsNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
temperature = {}
temperatures = []

for i in range(months):
    if (i == 0) or (i == 1):
        for j in range(days):
            temperatures.append((uniform(-30.0, -10.0), 1))
    elif (i == 2) or (i == 3):
        for j in range(days):
            temperatures.append((uniform(5.0, 15.0), 1))
    elif (i == 4) or (i == 5):
        for j in range(days):
            temperatures.append(round(uniform(15.0, 25.0), 1))
    elif (i == 6) or (i == 7):
        for j in range(days):
             temperatures.append(round(uniform(20.0, 30.0), 1))
    elif (i == 8) or (i == 9):
        for j in range(days):
            temperatures.append(round(uniform(0.0, 15.0), 1))
    else:
        for j in range(days):
            temperatures.append(round(uniform(-5.0, -15.0), 1))

    temperature[months] = temperatures

print("Temperature for every day of every month:")

for arr in temperature:
    print(arr)

averTemp = temp(temperature, days)

print()
print("Average temperature for every month:" + '\n' + str(averTemp) + '\n')
print("Sorted array of average temperatures:" + '\n' + str(sort(averTemp)) + '\n')