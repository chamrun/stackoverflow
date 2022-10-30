import random

weather_list = ("Clear", "Rain", "Thunderstorm", "Snowing", "Blizzard", "Arid", "Drought", "Sandstorm")

current_weather = (random.choice(weather_list)).lower().strip()
while current_weather not in weather_list:
    current_weather = (random.choice(weather_list)).lower().strip()
    if current_weather == "clear":
        print("true")
        break
    elif current_weather == "rain":
        print("false")
        break
