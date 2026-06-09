import os
from .request import request
import json
def json_write(file_name, data):
    with open(os.path.abspath(os.path.join(__file__, "..", "..", "json", file_name)), 'w',encoding = "utf-8") as file:
        json.dump(data, file, indent=4,ensure_ascii= False)
