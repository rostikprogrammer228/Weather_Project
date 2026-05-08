import requests
from config import API_KEY

def request(city_name):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}")
    data = response.json()
    print(data)
    return data
    
