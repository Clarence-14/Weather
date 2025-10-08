import requests

api_key = ''
base_url = 'http://api.openweathermap.org/data/2.5/weather?'

user_input = input('Enter city name: ')

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}&units=metric"
)

if weather_data.status_code != 200:
    print("City not found. Please check the city name and try again.")
    
else:
    weather = weather_data.json()['weather'][0]['main']
    temperature = weather_data.json()['main']['temp']
    humidity = weather_data.json()['main']['humidity']  
    wind_speed = weather_data.json()['wind']['speed']
    city = weather_data.json()['name']
    country = weather_data.json()['sys']['country']

print(f"Current weather in {city}, {country}:")
print(f"Weather: {weather}")
print(f"Temperature: {temperature}°C")
print(f"Humidity: {humidity}%")
print(f"Wind Speed: {wind_speed} m/s")
