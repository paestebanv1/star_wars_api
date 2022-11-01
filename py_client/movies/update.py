import requests
from auth_helper import *

auth_response = create_token()
if auth_response.status_code == 200:
    headers = {"Authorization": f"token {auth_response.json()['token']}"}
    endpoint = "http://127.0.0.1:8000/api_star_wars/movies/2/update"

    data = {"title" : "movie", "date_release":"2022-09-30T12:00:00Z", "running_time":"130", "country":"UK", "production_company":"Sony", "detail":"Detail", "director":2, "productor":1, "planets":[16,17,18]}

    get_response = requests.put(endpoint, json=data, headers=headers)
    print(get_response.json())
else:
    print("Please verify your credentials")
