import requests
from config import API_KEY

def request(city_name,api_request):
    if api_request == "current":
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric&lang=ua")
    elif api_request == "daily":
        response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}&units=metric&lang=ua")
    elif api_request == "cities":
        response = requests.get(f"https://countriesnow.space/api/v0.1/countries")
    elif api_request == "geocoding" :
        response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={API_KEY}")
    data = response.json()
    return data

