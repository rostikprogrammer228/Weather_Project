import requests
from config import API_KEY

def request(city_name):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&lang=ua&appid={API_KEY}")
    data = response.json()
    return data
    
