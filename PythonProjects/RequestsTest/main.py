import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8f895f1e2bd16919617034cc761a79bb'
HEADER = {'trainer_token' : TOKEN}
body_create = {
    "name": "Первый",
    "photo_id": 808
}
body_new_name = {
    "pokemon_id":"168233",
    "name": "Второй",
    "photo_id": 808
}
body_add = {"pokemon_id":"168233"}

'''response = requests.post(url=f'{URL}/pokemons',headers = HEADER, json = body_create)
print(response.text)'''

'''response = requests.put(url=f'{URL}/pokemons',headers = HEADER, json = body_new_name)
print(response.text)'''

response = requests.post(url=f'{URL}/trainers/add_pokeball',headers = HEADER, json = body_add)
print(response.text)
