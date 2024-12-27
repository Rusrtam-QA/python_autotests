import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TRAINER_ID = '12682'

def test_status_code ():
    response = requests.get(url=f'{URL}/pokemons', params = {'trainer_id':TRAINER_ID})
    assert response.status_code == 200

def test_part_of_respones():
 response_get = requests.get(url=f'{URL}/pokemons', params={'trainer_id':TRAINER_ID})
 assert response_get.json()["data"][0]["name"] =='Второй'