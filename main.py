from weather import get_weather

city = input("Enter city name: ")

data = get_weather(city)

if data:
    print("\nWeather Report")
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Weather:", data["weather"][0]["description"])
else:
    print("City not found or API error")