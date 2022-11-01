import requests
from auth_helper import *

auth_response = create_token()
if auth_response.status_code == 200:
    headers = {"Authorization": f"token {auth_response.json()['token']}"}
    task_id = input("What is the planet id you want to delete? ")

    try:
        task_id = int(task_id)
    except:
        task_id = None
        print(f'{task_id} not a valid id')

    if task_id:
        endpoint = f"http://127.0.0.1:8000/api_star_wars/planets/{task_id}/delete"
        get_response = requests.delete(endpoint, headers=headers)
        print(get_response.status_code, get_response.status_code==204)
else:
    print("Please verify your credentials")
