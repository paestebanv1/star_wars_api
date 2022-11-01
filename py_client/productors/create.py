import requests
from auth_helper import *

auth_response = create_token()
if auth_response.status_code == 200:
    headers = {"Authorization": f"token {auth_response.json()['token']}"}
    endpoint = "http://127.0.0.1:8000/api_star_wars/productors/"

    list_productors = [["George", "Lucas", "65"],
                    ["Ana", "Sanz", "60"]]

    for productor in list_productors:
        data = {"first_name" : productor[0], "last_name":productor[1], "age":productor[2]}
        get_response = requests.post(endpoint, json=data, headers=headers)
        print(get_response.json())
else:
    print("Please verify your credentials")
