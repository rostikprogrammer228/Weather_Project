import requests
from config import API_KEY
# current_weather_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"
# hours_weather_api_link = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}"
def request(city_name,api_request):
    if api_request == "current":
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric&lang=ua")
    elif api_request == "daily":
        response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}&units=metric&lang=ua")
    elif api_request == "cities":
        response = requests.get(f"https://countriesnow.space/api/v0.1/countries")
    data = response.json()
    return data

list1 = (("Monday","Понеділок"),)