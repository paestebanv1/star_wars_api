import requests
from auth_helper import *

auth_response = create_token()
if auth_response.status_code == 200:
    headers = {"Authorization": f"token {auth_response.json()['token']}"}
    endpoint = "http://127.0.0.1:8000/api_star_wars/characters/3"
    get_response = requests.get(endpoint, headers=headers)

    movies = []
    for movie in get_response.json()["movies"]:
        endpoint = f"http://127.0.0.1:8000/api_star_wars/movies/{movie}"
        get_response_movie = requests.get(endpoint, headers=headers)
        movies.append(get_response.json())

    print(get_response.json())
    print(movies)
else:
    print("Please verify your credentials")
