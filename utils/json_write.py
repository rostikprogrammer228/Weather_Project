import os
from .request import request

def json_write(file_name, data):
    with open(os.path.abspath(os.path.join(__file__, "..", "..", "json", file_name)), 'w') as file:
        file.write(data)
        
json_write(file_name= "json1.json", data = request(city_name= "Dnipro"))