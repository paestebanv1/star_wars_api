import requests
from auth_helper import *

auth_response = create_token()
if auth_response.status_code == 200:
    headers = {"Authorization": f"token {auth_response.json()['token']}"}
    endpoint = "http://127.0.0.1:8000/api_star_wars/characters/"

    list_characters = [["Padmé", "Amidala", "NA", 35, [1, 2]],
                    ["Jar Jar", "Binks","NA", 38, [1, 2, 3]],
                    ["C-", "3PO","NA", 0, [1, 2, 3, 4, 5, 6]],
                    ["Chewbacca", "","NA", 50, [1, 2, 3]],
                    ["Jango", "Fett","NA", 38, [4]],
                    ["Qui-Gon", "Jinn","NA", 38, [4, 5]],
                    ["Obi-Wan", "Kenobi","NA", 38, [5]],
                    ["Darth", "Maul","NA", 38, [6]],
                    ["Anakin", "Skywalker","NA", 38, [1, 6]],
                    ["Luke", "Skywalker","NA", 38, [2, 3]],
                    ["Jango", "Fett","NA", 38, [4]],
                    ["Han", "Solo","NA", 38, [5, 6]]]

    for character in list_characters:
        data = {"first_name" : character[0], "last_name":character[1], "place_of_born":character[2], "age":character[3], "movies":character[4]}
        get_response = requests.post(endpoint, json=data, headers=headers)
        print(get_response.json())
else:
    print("Please verify your credentials")
