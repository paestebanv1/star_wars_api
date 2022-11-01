import requests
from auth_helper import *

auth_response = create_token()
if auth_response.status_code == 200:
    headers = {"Authorization": f"token {auth_response.json()['token']}"}
    endpoint = "http://127.0.0.1:8000/api_star_wars/planets/"
    list_planets = ["Tatooine", "Hoth", "Endor", "Coruscant", "Dagobah", "Mustafar"]

    for planet in list_planets:
        data = {"name" : planet}
        get_response = requests.post(endpoint, json=data, headers=headers)
        print(get_response.json())
else:
    print("Please verify your credentials")
