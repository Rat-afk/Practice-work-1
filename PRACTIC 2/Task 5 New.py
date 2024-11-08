from random import uniform

months_names = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def generate_monthly_temperatures(days = 30):
    temperature_dict = {}

    for i, month_n in enumerate(months_names):
        if i in (0, 1):
            temperatures = [round(uniform(-30.0, -10.0), 1) for _ in range(days)]
        elif i in (2, 3):
            temperatures = [round(uniform(5.0, 15.0), 1) for _ in range(days)]
        elif i in (4, 5):
            temperatures = [round(uniform(15.0, 25.0), 1) for _ in range(days)]
        elif i in (6, 7):
            temperatures = [round(uniform(20.0, 30.0), 1) for _ in range(days)]
        elif i in (8, 9):
            temperatures = [round(uniform(0.0, 15.0), 1) for _ in range(days)]
        else:
            temperatures = [round(uniform(-5.0, -15.0), 1) for _ in range(days)]

        temperature_dict[month_n] = temperatures

    return temperature_dict

def calculate_average_temperatures(temperature_dict):
    average_temperatures_dict = {}

    for month_called, temperatures in temperature_dict.items():
        average_temp = round(sum(temperatures) / len(temperatures), 1)
        average_temperatures_dict[month_called] = average_temp

    return average_temperatures_dict

temperature_data = generate_monthly_temperatures()
average_temperatures = calculate_average_temperatures(temperature_data)

print("Temperatures for each month:")

for month, temps in temperature_data.items():
    print(f"{month}: {temps}")

print("\nAverage temperature for each month:")

for month, avg_temp in average_temperatures.items():
    print(f"{month}: {avg_temp}")
