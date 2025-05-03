import requests

weather_data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Lyon&appid=2d4fd4772f0b78f3d44b9623526adbdd").json()
print(weather_data)