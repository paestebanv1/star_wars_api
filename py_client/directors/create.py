import requests
from auth_helper import *

auth_response = create_token()
if auth_response.status_code == 200:
    headers = {"Authorization": f"token {auth_response.json()['token']}"}
    endpoint = "http://127.0.0.1:8000/api_star_wars/directors/"



    list_directors = [["George", "Lucas", "male", "65"],
                    ["Irvin", "Kershner", "male", "60"],
                    ["Richard", "Marquand", "male", "80"],
                    ["J.J.", "Abrams", "male", "50"],
                    ["Gareth", "Edwards", "male", "55"],
                    ["Rian", "Johnson", "male", "53"],
                    ["Ron", "Howard", "male", "58"]]

    for director in list_directors:
        data = {"first_name" : director[0], "last_name":director[1], "genre":director[2], "age":director[3]}
        get_response = requests.post(endpoint, json=data, headers=headers)
        print(get_response.json())
else:
    print("Please verify your credentials")
