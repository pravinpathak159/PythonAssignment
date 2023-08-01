import requests

def get_weather_data(city):
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data. Please check your internet connection and try again.")
        return None

def get_weather_option():
    print("1. Get weather")
    print("2. Get Wind Speed")
    print("3. Get Pressure")
    print("0. Exit")
    return int(input("Enter your choice: "))

def get_date_from_user():
    return input("Enter the date in the format 'YYYY-MM-DD': ")

def get_temperature(city, date):
    data = get_weather_data(city)
    if data:
        for entry in data['list']:
            if entry['dt_txt'].startswith(date):
                return entry['main']['temp']
        print("Date not found in the forecast.")
        return None

def get_wind_speed(city, date):
    data = get_weather_data(city)
    if data:
        for entry in data['list']:
            if entry['dt_txt'].startswith(date):
                return entry['wind']['speed']
        print("Date not found in the forecast.")
        return None

def get_pressure(city, date):
    data = get_weather_data(city)
    if data:
        for entry in data['list']:
            if entry['dt_txt'].startswith(date):
                return entry['main']['pressure']
        print("Date not found in the forecast.")
        return None

if __name__ == "__main__":
    city = "London,us"
    
    while True:
        option = get_weather_option()
        if option == 1:
            date = get_date_from_user()
            temp = get_temperature(city, date)
            if temp is not None:
                print(f"Temperature on {date}: {temp} K")
        elif option == 2:
            date = get_date_from_user()
            wind_speed = get_wind_speed(city, date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
        elif option == 3:
            date = get_date_from_user()
            pressure = get_pressure(city, date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
        elif option == 0:
            print("Terminating the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")