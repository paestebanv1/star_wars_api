from getpass import getpass
import requests

def create_token():
    auth_endpoint = "http://localhost:8000/api_star_wars/auth/"
    username = input("What is your username?\n")
    password = getpass("What is your password?\n")
    json = {'username': username, 'password': password}
    auth_response = requests.post(auth_endpoint, json)
    return auth_response
