import requests

api_key="00908d8dc89da89b6e509f5105347f7b"
user_input=input("Enter city:")
weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
weather=weather_data.json()['weather'][0]['main']
temp=weather_data.json()['main']['temp']
print(f"The weather in {user_input} is:{weather}")
print(f"The temperature in {user_input} is:{temp}F")
