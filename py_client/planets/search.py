import requests
from auth_helper import *

auth_response = create_token()
if auth_response.status_code == 200:
    headers = {"Authorization": f"token {auth_response.json()['token']}"}
    params = {'q': 'Mustafar'}
    endpoint = "http://127.0.0.1:8000/api_star_wars/planets/search/"
    get_response = requests.get(endpoint, params=params, headers=headers)
    print(get_response.json())
else:
    print("Please verify your credentials")
