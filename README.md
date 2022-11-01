Star Wars API

Created by Pablo Andrés Esteban

Required tools

django >= 4.0.0
djangorestframework
pyyaml
requests
django-cors-headers


To start the server please open your console and go to 'backend' folder, then use this command "python3 manage.py runserver 8000"

You need to create a user to access to all endpoints, to do that use the next command "python manage.py createsuperuser" and follow the instructions.

There are a list of end point grouped in the next Objects:
Characters
Movies
Directors
Planets
Productors

Every object has a group of options:
Create
Delete
Detail
List
Search
Update

The base url is http://127.0.0.1:8000/api_star_wars/"object"/"option"
I.E for director if you want to list directors just rewrite the object and the option to list all the directors
http://127.0.0.1:8000/api_star_wars/directors/list

Here you can see an example of the full URL's list for Planet Objects
Create: http://127.0.0.1:8000/api_star_wars/planets/
List: http://127.0.0.1:8000/api_star_wars/planets/list/
Upadte: http://127.0.0.1:8000/api_star_wars/planets/<int:pk>/update
Delete: http://127.0.0.1:8000/api_star_wars/planets/<int:pk>/delete
Search: http://127.0.0.1:8000/api_star_wars/planets/search/
Update: http://127.0.0.1:8000/api_star_wars/planets/<int:pk>/

Every endpoint is protected so you need to use token authentication to perform any action over them. You can see examples for every endpoint in the file py_client.

The correct order to create the test data is:
1) Create a director, planet and productor.
2) Create a movie
3) Create a character
