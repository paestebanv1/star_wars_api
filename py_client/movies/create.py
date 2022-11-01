import requests
from auth_helper import *

auth_response = create_token()
if auth_response.status_code == 200:
    headers = {"Authorization": f"token {auth_response.json()['token']}"}
    endpoint = "http://127.0.0.1:8000/api_star_wars/movies/"

    list_movies = [["Episode I – The Phantom Menace", "2022-09-30T12:00:00Z", 120, "USA", "Sony", "Turmoil has engulfed the Galactic Republic. The taxation of trade routes to outlying star system is in dispute. Hoping to resolve the matter with a blockade of deadly battleships, the greedy Trade Federation has stopped all shipping to the small planet of Naboo.", 2, 1, [16,17,18]],
    ["Episode II – Attack of the Clones", "2002-05-16T12:0:00Z", 120, "USA", "Sony", "Several thousand solar systems have declared their intentions to leave the Republic. This Separatist movement, under the leadership of the mysterious Count Dooku, has made it difficult for the limited number of Jedi Knights to maintain peace and order in the galaxy.", 3, 2, [16,17,18]],
    ["Episode III – Revenge of the Sith", "2005-05-19T12:00:00Z", 120, "USA", "Sony", "The Republic is crumbling under attacks by the ruthless Sith Lord, Count Dooku. There are heroes on both sides. Evil is everywhere. In a stunning move, the fiendish droid leader, General Grievous, has swept into the Republic capital and kidnapped Chancellor Palpatine, leader of the Galactic Senate.", 4, 1, [16,17,18]],
    ["Episode IV – A New Hope", "2022-09-30T12:00:00Z", 120, "USA", "Sony", "It is a period of civil war. Rebel spaceships, striking from a hidden base, have won their first victory against the evil Galactic Empire. During the battle, Rebel spies managed to steal secret plans to the Empire's ultimate weapon, the DEATH STAR, an armored space station with enough power to destroy an entire planet.", 5, 2, [16,17,18]],
    ["Episode V – The Empire Strikes Back", "2022-09-30T12:00:00Z", 120, "USA", "Sony", "It is a dark time for the Rebellion. Although the Death Star has been destroyed, Imperial troops have driven the Rebel forces from their hidden base and pursued them across the galaxy.", 6, 1, [16,17,18]],
    ["Episode VI – Return of the Jedi", "2022-09-30T12:00:00Z", 120, "USA", "Sony", "Luke Skywalker has returned to his home planet of Tatooine in an attempt to rescue his friend Han Solo from the clutches of the vile gangster Jabba the Hutt. Little does Luke know that the GALACTIC EMPIRE has secretly begun construction on a new armored space station even more powerful than the first dreaded Death Star.", 5, 2, [16,17,18]],
    ["Episode VII – The Force Awakens", "2022-09-30T12:00:00Z", 120, "USA", "Sony", "Luke Skywalker has vanished. In his absence, the sinister FIRST ORDER has risen from the ashes of the Empire and will not rest until Skywalker, the last Jedi, has been destroyed. With the support of the REPUBLIC, General Leia Organa leads a brave RESISTANCE. She is desperate to find her brother Luke and gain his help in restoring peace and justice to the galaxy.", 4, 1, [16,17,18]],
    ["Episode VIII – The Last Jedi", "2022-09-30T12:00:00Z", 120, "USA", "Sony", "The FIRST ORDER reigns. Having decimated the peaceful Republic, Supreme Leader Snoke now deploys his merciless legions to seize military control of the galaxy. Only General Leia Organa's band of RESISTANCE fighters stand against the rising tyranny, certain that Jedi Master Luke Skywalker will return and restore a spark of hope to the fight.", 3, 2, [16,17,18]],
    ["Episode IX – The Rise of Skywalker", "2022-09-30T12:00:00Z", 120, "USA", "Sony", "The dead speak! The galaxy has heard a mysterious broadcast, a threat of REVENGE in the sinister voice of the late EMPEROR PALPATINE. GENERAL LEIA ORGANA dispatches secret agents to gather intelligence, while REY, the last hope of the Jedi, trains for battle against the diabolical FIRST ORDER. ", 3, 2, [16,17,18]]]

    for movie in list_movies:
        data = {"title" : movie[0], "date_release":movie[1], "running_time":movie[2], "country":movie[3], "production_company":movie[4], "detail":movie[5], "director":movie[6], "productor":movie[7], "planets":movie[8]}
        get_response = requests.post(endpoint, json=data, headers=headers)
        print(get_response.json())
else:
    print("Please verify your credentials")
