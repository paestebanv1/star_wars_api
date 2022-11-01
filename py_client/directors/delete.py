import requests
from auth_helper import *

auth_response = create_token()
if auth_response.status_code == 200:
    headers = {"Authorization": f"token {auth_response.json()['token']}"}
    id = input("What is the director id you want to delete? ")

    try:
        id = int(id)
    except:
        id = None
        print(f'{id} not a valid id')

    if id:
        endpoint = f"http://127.0.0.1:8000/api_star_wars/directors/{id}/delete"
        get_response = requests.delete(endpoint, headers=headers)
        print(get_response.status_code, get_response.status_code==204)
else:
    print("Please verify your credentials")
