import requests, sys, json

def switcher_exam():
    try:
        with open("on_off_weather.txt", "r+") as file:
            switcher = file.readline().strip()
            switcher2 = file.readline().strip()

            if switcher == switcher2 == '1':
                file.seek(0)
                file.truncate()

                file.write('1' + '\n' + '0')

                def_city_exam()
            elif switcher == '0' or (switcher == '1' and switcher2 == '0'):
                return
            else:
                file.seek(0)
                file.truncate()

                file.write('1' + '\n' + '0')

                def_city_exam()
    except FileNotFoundError:
        with open("on_off_weather.txt", "w") as file:
            file.write('1' + '\n' + '0')

        def_city_exam()

def def_city_exam():
    print("Weather for Default City:")

    try:
        with open("default_city.txt", "r+") as file:
            city = list(map(str, file.read().split()))

            if len(city) == 1:
                response(city[0])
            else:
                city = 'Moscow'
                file.write(city)

                response(city)

    except FileNotFoundError:
        with open("default_city.txt", "w") as file:
            city = 'Moscow'
            file.write(city)

            response(city)

def response(town):
    try:
        resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={town}&appid=3bf37ed54c2746982a330b90a899959b')
        data = resp.json()

        city_country = str(data['name'] + ' ' + data['sys']['country'])
        weather_desc = str(data['weather'][0]['main'] + ": " + data['weather'][0]['description'])
        temp = str(round((data['main']['temp'] - 273.15), 2))
        wind = str(data['wind']['speed'])

        full_weather = {
            'name': city_country,
            'description': weather_desc,
            'temp': temp,
            'wind': wind
        }

        try:
            with open("weather_history.json", "r+") as file:
                try:
                    w_history = json.load(file)
                except json.JSONDecodeError:
                    w_history = []

                w_history.append(full_weather)
                file.seek(0)
                json.dump(w_history, file, indent = 4)
                file.truncate()

        except FileNotFoundError:
            with open("weather_history.json", "w") as file:
                json.dump([full_weather], file, indent = 4)

        print(city_country + '\n')
        print(weather_desc)
        print("Temperature - " + temp + " C")
        print("Speed of Wind - " + wind + " m/s" + '\n')

    except:
        print("The Site is not Responding or You Entered a Non-existent City. Please Try Again\n")

def weather():
    city = input("Please Enter a City Name or Enter Nothing to Exit to Main Menu: ")

    if city == '':
        return

    print("Weather in " + city + ":" + '\n')

    response(city)

def default():
    city = input("Please Enter a City Name or Enter Nothing to Exit to Main Menu: ")

    if city == '':
        return

    with open ("default_city.txt", "w") as file:
        file.write(city)

    with open ("on_off_weather.txt", "w") as file:
        file.write('1' + '\n' + '1')

    print("Default City Changed Successfully\n")

def history():
    try:
        with open ("weather_history.json", "r+") as file:
            try:
                weather_history = json.load(file)
            except json.JSONDecodeError:
                print("Weather History is Empty\n")

                return

            if not weather_history:
                print("Weather History is Empty\n")

                return

            print("Weather History:\n")

            for i_weather in weather_history:
                print(i_weather['name'])
                print(i_weather['description'])
                print("Temperature - " + i_weather['temp'] + " C")
                print("Speed of Wind - " + i_weather['wind'] + " m/s\n" + '\n')

            print("Do You Want to Delete Weather History?")

            while True:
                answer = input("Yes or No: ")

                if answer == 'Yes' or answer == 'yes':
                    file.seek(0)
                    file.truncate()

                    print("Weather History Deleted Successfully\n")

                    return
                elif answer == 'No' or answer == 'no':
                    print()

                    return
                else:
                    print("Invalid value. Please Try Again\n")
    except FileNotFoundError:
        print("Weather History is empty\n")

def main():
    while True:
        print("Welcome to Weather App Main Menu")

        switcher_exam()

        print("Please Select an Action:")
        print("1 - View the Weather for the Entered City" + '\t' + "2 - Change Default City\t" + '\t' + "3 - On/Off Weather for Default City\t" + '\t' + "4 - View Weather History")
        print("0 - Close the App\n")

        while True:
            try:
                choose = int(input("Please Select an Action: "))

                if choose < 0 or choose > 4:
                    print("Invalid Value. Please Try Again")

                    continue

                break
            except ValueError:
                print("Invalid Value. Please Try Again")

        if choose == 1:
            weather()

        elif choose == 2:
            default()

        elif choose == 3:
            with open("on_off_weather.txt", "r+") as file:
                switcher = file.readline().strip()

                if switcher == '1':
                    file.seek(0)
                    file.truncate()

                    file.write('0')
                else:
                    file.seek(0)
                    file.truncate()

                    file.write('1' + '\n' + '1')

        elif choose == 4:
            history()

        else:
            with open("on_off_weather.txt" , 'r+') as file:
                switcher = file.readline().strip()

                if switcher == '1':
                    file.seek(0)
                    file.truncate()

                    file.write('1' + '\n' + '1')

            sys.exit()

if __name__ == "__main__":
    main()
